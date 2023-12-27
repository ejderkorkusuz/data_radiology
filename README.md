data klasörü reposu
git clone https://github.com/ejderkorkusuz/data_epikriz
mv data_epikriz data
    <----
    data_epikriz klasörü içinde olduğunda ismi data diye değiştirdim.
    data klasörü içinde graph için, language model (lm) mevcut. sanırım orada bir sıkıntı var 
    train ve text içindeki wav.scp içerisindeki wav linkleri değiştirlecek.
    wav klasörleri iki tanedir. ve google drive da yüklüdür.
    --->
https://drive.google.com/file/d/1a20oB4zqmTfoNne1jqFn5oqmadBQe2uB/view?usp=sharing
    <
    clips klasörü
    gdown ile de indirilebilir.
    pip install gdown
    gdown 1a20oB4zqmTfoNne1jqFn5oqmadBQe2uB
    >
https://drive.google.com/file/d/1ZRXXBooZ4klEpDvEWYA4EL7fgWogdtib/view?usp=share_link
    <
    recordings2 klaörü
    gdown 1ZRXXBooZ4klEpDvEWYA4EL7fgWogdtib
    >
https://drive.google.com/file/d/1AbP3eHy2olbhyBNL5JsbwCPBzGnravDt/view?usp=sharing
    <
    radiology klasörü
    gdown 1AbP3eHy2olbhyBNL5JsbwCPBzGnravDt
    >
SONUÇ: Modeli eğittim. herhangi bir sıkıntı çıkmadı. Klasör içeriklerini ayarladım. Mikrofona konuştuğumda bir yada iki kelimeyi yakalıyor sonrasında işlem yapmıyor. Bazen language model içindeki bir cümleyi söylediğimde birebir çeviriyor. Yalnız cümlenin önüne yada arkasına başka bir kelime eklersem hata verip kendini kapatıyor. 