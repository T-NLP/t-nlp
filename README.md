# Entity Bazlı Duygu Analizi

## Yarışma Hakkında:

Bu yarışma, katılımcılardan geniş bir yelpazedeki firmalar veya kurumlar tarafından sağlanan müşteri geri bildirimlerini analiz etmelerini ve bu yorumlardaki duyguları belirli hizmet yönleri veya ürün özelliklerine göre sınıflandırmalarını istemektedir.

## Görev:
Katılımcılar, verilen müşteri yorumlarını öncelikle ilgili entity'e (varlık) göre sıralamalı, ardından bu entity'lerin sunduğu hizmetler veya ürünlerle ilgili yorumlardaki duyguları (olumlu, olumsuz veya nötr) belirlemelidir.


## Takım adı: T-NLP
Teknofest 2024 Türkçe Doğal Dil İşleme Yarışması için oluşturulmuştur.

## Takım üyeleri:
- Gülzade Evni  **Github:** [GülzadeEvni](https://github.com/GulzadeEvni)
- Zeynep Baydemir  **Github:** [zeynepbaydemir](https://github.com/zeynepbaydemir)
- Kübra Arslan **Github:** [kbrars](https://github.com/kbrars),

## Veri Setleri:
Çalışma boyunca toplam **50.845** veri çekilmiştir.

Bu çalışmada kullanılan veri setleri, farklı platformlardan toplanmıştır.

1. **Ekşi Sözlük Verileri**: Ekşi Sözlük’te yer alan çeşitli konular üzerine yapılan kullanıcı yorumları, belirtilen içerik başlıklarına göre ayrılarak toplanmıştır. Her başlık için belirli bir sayfa sayısındaki veriler çekilerek ayrı dosyalar halinde kaydedilmiştir.
    
2. **Twitter Verileri**: Twitter üzerinden belirlenen anahtar kelimeler ve tarih aralıklarına göre tweetler toplanmış ve her bir dosya belirli bir zaman dilimine ait tweetleri içermektedir.
    
3. **Şikayetvar Verisi**: Şikayetvar platformundan şikayetler toplanmıştır.


### Ekşi Sözlük Verileri

|İçerik|Text Sayısı|Sayfa|Dosya Adı|
|---|---|---|---|
|turkcell|8024|804|turkcell_eksi_sozluk|
|turkcell superonline|1378|138|superonline_eksi_sozluk|
|turkcell superonline fiber internet|1900|190|fiber_eksi_sozluk|
|turkcell tv+|1081|108|tvplus_eksi_sozluk|
|turkcell superbox|733|74|superbox_eksi_sozluk|
|turkcell platinum|336|34|platinum_eksi_sozluk|
|fizy|1901|190|fizy_eksi_sozluk|
|gnçtrkcll|331|33|gnctrkcll_eksi_sozluk|
|paycell|194|20|paycell_eksi_sozluk|
|turkcell müşteri hizmetleri|190|19|musteri_hizmetleri_eksi_sozluk|
|bip|146|15|bip_eksi_sozluk|
|lifebox|57|6|lifebox_eksi_sozluk|
|upcall|25|3|upcall_eksi_sozluk|

### Twitter Verileri

|Dosya Adı|Satır Sayısı|
|---|---|
|dataset_1|4061|
|dataset_2|1995|
|dataset_3|132|
|dataset_4|4511|
|dataset_5|6558|
|wordlist_ile_19Kasim_2023ekadar|4063|
|2subat2024_18Eylül_2023|5953|
|2_subata_kadar_2024|5976|

### Şikayetvar Verisi

|Dosya Adı|Satır Sayısı|
|---|---|
|turkcell_sikayetvar.xlsx|600|

## NLP Modelleri: BERT, DistilBERT ve Electra

Bu depo, BERT, DistilBERT ve Electra gibi popüler NLP modellerinin ince ayar (fine-tuning) ve değerlendirme süreçlerini içeren Jupyter Notebook dosyalarını içerir. Her bir notebook, ilgili modelin yüklenmesi, eğitimi ve değerlendirilmesi adımlarını göstermektedir.

## Notebooklar

### 1. BERT

- **Dosya Adı:** `bert.ipynb`
- **Açıklama:** Bu notebook, BERT modelinin bir metin sınıflandırma görevi için ince ayarının nasıl yapılacağını göstermektedir. Veri ön işleme, model eğitimi ve değerlendirme adımlarını içerir.
- **Model:** BERT (Bidirectional Encoder Representations from Transformers)

### 2. DistilBERT

- **Dosya Adı:** `distilbert.ipynb`
- **Açıklama:** Bu notebook, BERT'in daha hafif ve hızlı bir versiyonu olan DistilBERT modelinin ince ayar sürecini kapsar. Hesaplama verimliliğinin önemli olduğu durumlar için idealdir.
- **Model:** DistilBERT (BERT'in distile edilmiş versiyonu)

### 3. Electra

- **Dosya Adı:** `electra.ipynb`
- **Açıklama:** Bu notebook, Electra modelinin ince ayarının nasıl yapılacağını anlatır. Electra, özellikle kaynakların kısıtlı olduğu ortamlarda verimliliği ve performansıyla bilinir.
- **Model:** Electra (Efficiently Learning an Encoder that Classifies Token Replacements Accurately)


**Model için : **
* [distilBERT](https://huggingface.co/Gulzd/distilBERTT)
* [BERT](https://huggingface.co/Gulzd/Bert)
* [Electra](https://huggingface.co/Gulzd/electra)


## Gereksinimler 

Aşağıdaki Python paketlerini yükleyin: 

``` 
pip install fastapi
pip install uvicorn 
pip install transformers 
pip install torch 
pip install nlpturk 
```

## Uygulamayı Başlatma

FastAPI uygulamanızı başlatmak için aşağıdaki komutu çalıştırın:

`uvicorn main:app --reload`

Uygulamanız [http://0.0.0.0:8000](http://0.0.0.0:8000) adresinde çalışmaya başlayacaktır.

## Swagger UI

Swagger UI'ye erişmek için tarayıcınızda şu adresi ziyaret edin:

[http://localhost:8000/docs](http://localhost:8000/docs)

**FastAPI Kodları için:** [main3.py](https://github.com/T-NLP/t-nlp/blob/main/main3.py)

## Kullanım

1. Bu depoyu klonlayın:
    
    `git clone https://github.com/kullaniciadi/depo-adi.git`
    
2. Proje dizinine gidin:
    
    `cd depo-adi`
    
3. Jupyter Notebook'u açın:
     
    `jupyter notebook`
    
4. İstediğiniz notebook dosyasını (`bert.ipynb`, `distilbert.ipynb`, veya `electra.ipynb`) seçin ve çalıştırın.

## Modelin Çıktısı:

![hugging](https://github.com/user-attachments/assets/91416d35-043f-477e-a077-e2d6009f36f6)

## Lisans
Yarışma süresince geliştirilmiş kodlar, veri kümeleri ve diğer bileşenleri GitHub’da erişilebilir biçimde Açık Kaynak Apache lisansı ile [Lisans dosyası](https://github.com/T-NLP/t-nlp/blob/main/LICENSE) adı altında paylaşıyoruz. 
