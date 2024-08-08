from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import nlpturk

app = FastAPI()

# Model ve Tokenizer'ı yükleme
tokenizer = DistilBertTokenizer.from_pretrained("balciberin/distilbert_turkish_sentiment_analysis2")
model = DistilBertForSequenceClassification.from_pretrained("Gulzd/distilBERTT")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Varlık Tanıma (nlpturk) ile metni analiz etme
def get_entities(text):
    try:
        doc = nlpturk(text)
        return [(token.text, token.idx) for token in doc if token.pos == 'PROPN']
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Varlık tanıma hatası: {e}")

# Tahmin Fonksiyonu
def make_new_prediction(text, model, tokenizer):
    tokenized_text = tokenizer(
        text,
        return_tensors='pt', 
        padding=True,
        truncation=True,
        max_length=65
    )
    
    input_ids = tokenized_text['input_ids'].to(device)
    attention_mask = tokenized_text['attention_mask'].to(device)
    
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
    
    predicted_class = torch.argmax(logits, dim=1).item()
    class_labels = {0: 'olumsuz', 1: 'olumlu', 2: 'nötr'}
    predicted_label = class_labels.get(predicted_class, 'bilinmiyor')

    return predicted_label

# Veri modeli
class Item(BaseModel):
    text: str = Field(..., example="""Fiber 100mb SuperOnline kullanıcısıyım yaklaşık 2 haftadır @Twitch @Kick_Turkey gibi canlı yayın platformlarında 360p yayın izlerken donmalar yaşıyoruz. Başka hiç bir operatörler bu sorunu yaşamazken ben parasını verip alamadığım hizmeti neden ödeyeyim ? @Turkcell """)

@app.post("/predict/", response_model=dict)
async def predict(item: Item):
    text = item.text

    # Varlık Tanıma
    entities_with_indices = get_entities(text)
    entities_list = [entity for entity, _ in entities_with_indices]
    
    if not entities_list:
        return {"entity_list": [], "results": []}

    # Varlıkların sıralı listesi ve segmentleri oluştur
    segments = []
    previous_index = 0
    for entity, index in entities_with_indices:
        if previous_index < index:
            segments.append(text[previous_index:index].strip())
        segments.append(entity)
        previous_index = index + len(entity)
    if previous_index < len(text):
        segments.append(text[previous_index:].strip())

    # Varlıkları ve segmentleri eşleştir
    results = []
    segment_index = 0
    for entity in entities_list:
        while segment_index < len(segments) and not segments[segment_index].startswith(entity):
            segment_index += 1
        if segment_index < len(segments):
            # Varlığın bulunduğu metin parçasını al
            segment = segments[segment_index]
            sentiment = make_new_prediction(segment, model, tokenizer)
            results.append({
                "entity": entity,
                "sentiment": sentiment
            })

    # JSON formatında çıktı
    output = {
        "entity_list": entities_list,
        "results": results
    }

    return output

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
