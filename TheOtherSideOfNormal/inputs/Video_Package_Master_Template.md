# Video Package Master Template

**Revizyon:** 2026-09-09 — hareketli açılış, video genelinde görsel tekrar yasağı ve gerçek görüntü odaklı kurgu.

Bu dosya, kanaldan ve konudan bağımsız **üretim ve teslim sözleşmesidir**. Araştırmanın nasıl doğrulanacağını, telif ve kaynak kayıtlarının nasıl tutulacağını, varlıkların nasıl kodlanacağını, birebir seslendirme/edit map eşleşmesini, rough-cut bütünlüğünü ve zorunlu video-package çıktı yapısını belirler.

Her yeni videoda bu dosya, ilgili kanal profil dosyası ve konuya özel prompt birlikte uygulanmalıdır. Kanal profili videonun **ne söyleyeceğini ve nasıl hissettireceğini**; bu master template ise seçilen videonun **nasıl araştırılıp doğrulanacağını, paketleneceğini ve rough-cut’a dönüştürüleceğini** belirler.

Bu dosya kanal kimliği, varsayılan süre, anlatım tonu, WPM, hook’un yaratıcı yapısı, retention kadansı, hareketli görüntü/grafik oranı, grafik adedi, müzik estetiği veya başlık/thumbnail dilini kendi başına belirlemez. Bu yaratıcı değerler ilgili kanal profilinden; video özelindeki değişiklikler konu promptundan alınır. Master ayrıca kanal kimliğinden bağımsız editoryal kalite kontrollerini tanımlar: vaat–içerik uyumu, anlaşılabilirlik, kanıta dayalı ilerleme ve tatmin edici cevap. Bunlar tek tip dramatik yapı veya sürekli hızlı anlatım zorunluluğu değildir. Kullanıcının kesin görsel sınırları ayrıca uygulanır: ilk 40 saniyede sabit görsel yok; Bölüm 9 kapsamındaki açılışta en fazla iki hareketli G kullanımı; aynı veya görsel olarak eşdeğer video kesiti bütün videoda yalnızca bir kez. Kanal profili bu sınırlar içinde yaratıcı yönü belirler.

**Master standard:** evidence verification, rights-safe sourcing, exact source-time inspection, asset sufficiency, deterministic asset coding, verbatim voice-over continuity, complete edit-map coverage, repetition audit, fixed A–O output structure and rough-cut-ready delivery.

---

# Ana üretim talimatları

## 1. Talimat önceliği

Bu dosya ile kanal profili aynı hiyerarşide yarışmaz; farklı karar alanlarının sahibidir.

| Karar alanı | Asıl sahibi |
| --- | --- |
| Kanal vaadi, hedef kitle, konu sınırı, editoryal tez, anlatım tonu, enerji, varsayılan süre/WPM, hook ve retention karakteri, yaratıcı görsel oranı, grafik aileleri, müzik hissi, başlık ve thumbnail yaklaşımı | İlgili **Channel Profile** |
| Video konusu, hedef süre, ana soru, özellikle anlatılacaklar, video özelindeki coğrafya/ton/görsel oranı ve istisnalar | **Konuya özel prompt** |
| Araştırma kanıt standardı, claim doğrulama yöntemi, telif/lisans kaydı, kaynak zaman kodu incelemesi, asset kodları, seslendirme dosyaları, edit map, tekrar auditi, rough-cut teknik bütünlüğü, dosya adlandırma ve zorunlu A–O çıktı yapısı | **Video Package Master Template** |

Yeni video için verilen **konuya özel prompt**, açıkça belirttiği yaratıcı ve içerik kararlarında kanal profilinin varsayımlarını geçersiz kılabilir. Ancak kullanıcı özellikle yapısal bir değişiklik istemedikçe prompt; bu master template’in zorunlu A–O çıktı şemasını, edit-map sütunlarını, kaynak doğrulamasını, telif kayıtlarını veya rough-cut bütünlük kurallarını sessizce kaldıramaz.

Öncelik sırası:

1. Güvenlik, telif ve platform kuralları
2. Kullanıcının konuya özel ekstra promptundaki açık talimatları
3. Editoryal ve yaratıcı kararlarda ilgili kanal profili
4. Teknik üretim, doğrulama, rough-cut ve çıktı yapısında bu master template
5. Araştırma sırasında verilmesi gereken editoryal kararlar

Görünen bir çelişkide önce kararın alanı sınıflandırılır. Kanal kimliği ve yaratıcı anlatım kararıysa profil; teknik üretim ve teslim kararıysa master uygulanır. Bölüm 8’deki kullanıcıya ait tek-plan süre üst sınırları ile Bölüm 9 ve 10’daki kesin görsel sınırlar kanal profilinin varsayımlarından üstündür. Diğer alanlarda bir dosya diğerinin alanındaki kararı ezemez. Prompt belirsizse kanal profili yaratıcı varsayılanı verir; master bu kararın eksiksiz uygulanmasını sağlar.

### 1.0. Kural türleri ve tek karar kaydı

- **Kesin kapı:** doğruluk, kabul edilen kaynak/hak koşulları, Bölüm 8’deki tek-plan süre üst sınırları, hook için Bölüm 9'daki ilk 40 saniye sabit görsel yasağı ve en fazla iki motion G sınırı, tekrar sınırları, dosya/kod eşleşmesi ve teslim şeması. Bunlar yalnızca açık kullanıcı talimatıyla ilgili kapsamda değişir; kanal profili bunları sessizce değiştiremez.
- **Editoryal kontrol:** izleyicinin vaadi anlaması, erken gerçek değer alması, açıklamayı takip edebilmesi ve sonunda cevabı alması. Bunların işlevi zorunludur; yaratıcı biçimi profilden gelir.
- **Esnek başlangıç değeri:** konuşma/ilerleme süreleri, bölüm sayıları ve önerilen ritimler. Bunlar YouTube algoritma kuralları veya başarı garantisi değildir. Profil/prompt önceliklidir; değerler aynı anda uygulanıp toplanmaz. Ancak Bölüm 8’deki kullanıcıya ait fotoğraf/görsel, G ve video tek-plan maksimumları esnek başlangıç değeri değil, kesin üst sınırdır.
- Yaratıcı sayısal kararlar A, C, E ve J'de birbiriyle tutarlı kaydedilir. Profil verilmemişse okunmuş gibi davranılmaz; geçici varsayımlar A'da açıkça belirtilir.
- Editoryal değerlendirmeyi yalnızca saniye/adet tutturmaya indirgeme. Bir süreç anlaşılır biçimde gelişiyorsa süre doldu diye yeni soru, isim, efekt veya kesme ekleme.

### 1.1. Template yapısını koruma — hard lock

- Final video paketi bu ana template içinde tanımlanan çıktı yapısını **birebir** uygulamalıdır. Template dışında yeni bölüm, alt bölüm, tablo, sütun, satır türü, alan, ek, alternatif format veya serbest açıklama eklenemez; zorunlu hiçbir öğe çıkarılamaz.
- Başlıkların adı ve sırası, tabloların sütun adları ve sütun sırası, zorunlu alanların içeriği ve yazım biçimi değiştirilemez. Benzer anlamlı başka başlık veya sütun adı kullanmak da yapı değişikliği sayılır.
- Özellikle `G. Exact voice-over and edit map` tablosu yalnızca şu altı sütundan ve bu sıradan oluşmalıdır: `Time`, `Chapter`, `Voice file`, `Exact voice-over`, `Picture and edit instruction`, `Claim ID`. `Edit intent`, `SFX`, `Notes`, `Source`, `Transition` veya başka bir sütun eklenemez; hiçbir sütun birleştirilemez veya çıkarılamaz.
- Edit map içinde her veri satırı tek bir ana görsel planını temsil eder ve bütün hücreleri bu template’in kurallarına göre doldurulur. Template veya konuya özel prompt kesin satır sayısı ya da belirli satır içeriği veriyorsa bunlar birebir korunur; satır eklenemez, çıkarılamaz, birleştirilemez veya yapay biçimde bölünemez.
- Edit map için önceden kesin toplam satır sayısı verilmemişse gerekli satır sayısını yalnızca 0:00’dan video sonuna kadar boşluksuz ilerleyen gerçek plan değişimleri belirler. Tabloya açıklama, ara başlık, özet, alternatif kurgu veya tablo dışı edit satırı eklenemez.
- Konuya özel ekstra prompt içerik kararlarında öncelikli olabilir; ancak kullanıcı açıkça template’in yapısını değiştirmeyi istemedikçe bu bölümdeki format kilidini geçersiz kılamaz.

## 2. Kanal, hedef kitle ve format

Kanalın adı, vaadi, hedef kitlesi, varsayılan coğrafi yönü, konu alanı, üslubu, görsel yaklaşımı ve editoryal odağı ilgili kanal profilinden alınmalıdır.

- **Dil:** İngilizce
- **Format:** 16:9, yüz göstermeyen YouTube uzun-form video; kesin tür ve anlatım karakteri kanal profilinden alınır
- **Varsayılan çözünürlük:** 1920×1080
- **Hedef süre:** Önce konu promptundan, orada yoksa kanal profilinden alınır. Bu master template evrensel dakika aralığı koymaz. Seçilen süre, ana soruyu kanıt ve yeterli görselle tamamlayamadığı ya da yalnızca dolgu ile sağlanabildiği durumda zorlanmaz; açı daraltılır veya gerekçeli süre revizyonu yazılır.
- **İdeal ilk hedef:** Her dakika izleyicinin anlayışını, merakını veya konuya bağını ilerletmelidir. Daha fazla bilgi yığmak kalite ölçütü değildir; bir mekanizmayı anlaşılır kılan örnek ve gerekli sindirme süresi değerlidir. Sırf hedef süreye ulaşmak için tarihçe, ek neden, tekrar, sessizlik veya B-roll eklenemez.
- **Anlatım hızı ve enerji eğrisi:** İlgili kanal profilinden alınır; konu promptu farklı bir hız veriyorsa o uygulanır. Master yalnızca seçilen hızın süre/kelime hesabına, VO dosyalarına ve edit map’e tutarlı biçimde yansımasını zorunlu kılar.
- **Tahmini seslendirme uzunluğu:** Final süre ve arşiv sesi/görsel nefes miktarına göre hesaplanmalıdır. Sabit kelime kotası yoktur; metin yalnızca merkezi hikâyenin gerektirdiği kadar uzun olmalıdır. Süreyi doldurmak için kesintisiz konuşma yazılmaz.
- **Kurgu temposu:** Kanal profilindeki anlatım ve retention motorundan alınır. Master, bu yaratıcı ritmin gerçek plan değişimleri, kaynak varlıkları ve kesintisiz timeline ile uygulanabilir olmasını denetler.

## 3. Editoryal yaklaşım

### 3.1. Ana tez

Her video tek bir açık ana soruya, tek bir görünür hikâye taşıyıcısına ve kanıtlanabilir bir teze sahip olmalıdır. Hikâye taşıyıcısının konu alanına uygun türleri ve kanalın tercih ettiği somut çatışmalar ilgili kanal profilinden alınmalıdır.

Ana tez:

- Bir cümlede yazılabilmeli
- Kanıtın desteklediği açıklamayı vermeli; bir baskın mekanizma yeterliyse yapay ek neden üretmemeli
- Başlığın iddiasına doğrudan cevap vermeli
- “Everything changed”, “the world was never the same” gibi kanıtsız genellemelerden kaçınmalı

### 3.2. Başlık iddiasının doğruluk sınırı

Başlık güçlü olabilir; fakat senaryo başlığın neyi tam olarak iddia ettiğini erken açıklamalıdır. Başlıkta `lost`, `failed`, `disappeared`, `destroyed`, `saved`, `changed the war`, `ahead of its time`, `never recovered` gibi kelimeler kullanılıyorsa bunların ölçülebilir anlamı tanımlanmalıdır.

Videoda erken aşamada şu ayrım yapılmalıdır: başlıktaki güçlü fiilin neyi kapsadığı ve neyi kapsamadığı açıkça söylenmelidir.

Paket hazırlanırken:

- Başlık iddiasını destekleyen ölçüt belirlenir.
- Uymayan istisnalar saklanmaz.
- Gerekli niteleme, Bölüm 7.6’ya göre ilk yanıltıcı çıkarım oluşmadan kısa biçimde verilir.
- Başlığın literal olarak yanlış olduğu fark edilirse başlık değiştirilir; senaryo zorlanmaz.

### 3.3. Nedensel yeterlilik; zorunlu neden kotası yok

Bir yükseliş, başarı, başarısızlık, gerileme, kayıp veya dönüşüm genellikle tek nedene indirgenemez. Araştırma; teknik kapasite, maliyet, yönetim, insan, altyapı, rakipler, zamanlama, politika, çevre ve kanıtların güvenilirliği gibi konuya uygun etkenleri ayrı ayrı değerlendirmelidir. Alana özgü neden kontrol listesi ilgili kanal profilinden alınmalıdır.

Bir neden güçlü kanıt olmadan “asıl suçlu” veya “tek belirleyici” ilan edilmemelidir. Basit ve politik olarak çekici anlatılar, daha güçlü kanıtların yerini alamaz. Araştırmanın kapsamı senaryonun kapsamı değildir: yalnızca cevabı değiştiren etkenler anlatılır. Bir mekanizma yeterliyse bir; birkaç neden gerekiyorsa önemleri ve ilişkileri açık biçimde kullanılır. Her videoya teknik, ekonomik, politik ve insani nedenler ekleme zorunluluğu yoktur.

### 3.4. İnsan ölçeği

Makro, teknik veya stratejik anlatı gerçek insanların yaşadığı somut koşullarla bağlanmalıdır. Uygun insan ölçeği girişleri ve kontrol soruları ilgili kanal profilinde tanımlanır.

Tek bir tanıklık, inceleme, hatırat veya kişisel hikâye bütün grubu temsil ediyormuş gibi sunulmamalıdır. Bu kaynaklar değerli fakat öznel ve çoğu zaman eksiktir.

### 3.5. Eleştirel mesafe

- Geçmiş, teknoloji, sanayi veya savaş yalnızca nostalji, teknik hayranlık ya da kahramanlık üzerinden romantikleştirilmemelidir.
- Zarar, güvenlik, mahremiyet, ayrımcılık, çevre, sivil etki veya başka önemli bedeller anlatının parçasıysa saklanmamalıdır.
- Dönem reklamları, tanıtım filmleri, propaganda, resmî açıklamalar ve zafer raporları tarafsız gerçek kayıt gibi sunulmamalıdır.
- Sonucun kaçınılmaz olduğu da, tek bir karar veya kişiyle kolayca değişeceği de kanıtsız biçimde iddia edilmemelidir.

### 3.6. Günümüz bağlantısı

Günümüz bağlantısı, başlık vaadini tamamlıyor veya sonucun anlamını değiştiriyorsa kullanılır. Her videoya ayrı bir “bugün” bölümü eklenmez. Olayın gerçek sonucu ana soruyu tatmin edici biçimde kapatıyorsa video orada bitebilir. Kanala özgü kapanış işlevi profilden alınır; gereksiz miras listesi ve ikinci kapanış yazılmaz.

### 3.7. Hikâye motoru ve ilerleme

- Önce bir cümleyle yaz: **izleyicinin merak ettiği somut soru → bunu çözmeye yarayan kanıt/mekanizma → ulaşılan cevap**. Yanlış inanış veya ters köşe gerçekten yoksa uydurma.
- Her chapter yeni bir nedensel aşama, kanıt, deneyim veya sonuç getirmelidir. Yalnızca yeni tarih/isim ilerleme değildir.
- Rakip açıklamalar konu gerçekten nedensel bir tartışma içeriyorsa araştırılır; sayı tamamlamak için iki yapay teori üretilemez. Sonucu değiştiren karşı kanıt saklanamaz.
- Başlıktaki özne ve vaat açılışta görünür olmalı; bir ilk somut cevap hook içinde, daha derin açıklama gövdede verilmelidir. Zamanlama için tek başvuru Bölüm 7.6'dır.
- Kronoloji, açıklama veya karşılaştırma yapısından konuya uygun olanı seç. Sonucu baştan söylemek bazen merakı azaltmaz: devamı “nasıl” ve “hangi bedelle” sorularını cevaplayabilir.
- Her bölüm geçişinde sonraki bölümün neden gerekli olduğu anlaşılmalı. “Sonra şu oldu” zinciri yerine mümkünse karar → sonuç → yeni kısıt ilişkisi kur.
- İnsan ölçeği gerçek bir kişi gerektirmez; kullanıcının yapabildiği bir işlem, askerin taşıdığı yük veya evdeki somut bir davranış olabilir. Kanıtsız tanıklık, diyalog veya duygu uydurma.
- Bir veya birkaç güçlü, hatırlanabilir an planla; sabit üçlü kota yoktur. Bu anları C, F ve G içinde somut kanıt ve görsel işleve bağla.
- Yan ayrıntıyı çıkarma testi: çıkarınca doğruluk, anlama, duygusal bağ veya sonuç zayıflamıyorsa VO'dan çıkar. Yalnızca araştırılmış olması anlatılması için yeterli değildir.

### 3.8. Senaryodan önce izleyici vaadi

B bölümünün mevcut alanlarını kullan; yeni teslim tablosu açma:

- Ana soru: Konuyu bilmeyen biri neden bunu merak etsin? Somut farkı, gerilimi veya sonucu yaz.
- Temel fikir: İzleyici sonunda neyi açıklayabilecek veya farklı görecek?
- Kısa cevap: Araştırmanın gerçek cevabını başlık yazmadan saklamadan belirt.
- Başlık doğruluğu: L'deki üç başlık–thumbnail eşleşmesinin aynı final senaryo tarafından karşılandığını kontrol et. Alternatif paketleme, videoda bulunmayan farklı bir cevap vaat edemez.
- Kullanılan konu yapısı: yalnızca bu videonun ana sorusunu taşıyan kapsamı ve dışarıda bırakılan yan konuları kısa biçimde belirt.

Bu beş karar anlamlı değilse ayrıntılı edit map yazmaya geçmeden açıyı düzelt. Teknik açıdan dolu bir paket, zayıf izleyici vaadini telafi etmez.

## 4. Araştırma standardı

### 4.1. Temel kurallar

1. Tarihsel, ekonomik, teknik, ticari, kurumsal, taktik, stratejik veya insan deneyimine dair iddiaları araştırmadan yazma.
2. Önemli iddialarda mümkün olduğunca birincil, akademik ve kurumsal kaynaklara öncelik ver.
3. Wikipedia araştırmaya başlangıç noktası olabilir; önemli iddiaların tek veya nihai kaynağı olamaz.
4. Ana tezi taşıyan her kritik iddiayı mümkünse birbirinden bağımsız en az iki güvenilir kaynakla kontrol et.
5. Kaynaklar çelişiyorsa tek bir rakamı kesin gerçek gibi verme; farkı açıkla veya güvenilir aralık kullan.
6. Ana sonucu taşıyan tarihler, sayılar, adlar, sınıflandırmalar ve ölçüler özellikle doğrulanmalıdır. Kanala özgü yüksek riskli ölçüler ilgili profilde listelenir.
7. Nominal para değerleri kullanılıyorsa dönem ve para birimi açık olmalıdır. Modern karşılık veriliyorsa kullanılan dönüşüm yöntemi belirtilmelidir.
8. Benzer görünen fakat farklı olay, aşama, statü ve ölçüler birbirine karıştırılmamalıdır. Kanala özgü ayrımlar ilgili profilden alınmalıdır.
9. Geniş sonuç ifadelerinde kullanılan farklı ölçüler ayrı ayrı ele alınmalıdır.
10. Geniş bir ülke, dönem, sektör, taraf veya pazar ile tek bir şirket, ürün, birlik, kişi, bölge ya da olayın sonucu birbirinin yerine kullanılmamalıdır.
11. Korelasyon nedensellik gibi sunulmamalıdır. Aynı dönemde gerçekleşen iki olay arasında mekanizma gösterilmelidir.
12. Araştırmada kullanılan bütün kaynaklar doğrudan bağlantıları ve destekledikleri iddialarla listelenmelidir.

### 4.2. Tercih edilen araştırma kaynakları

Kanala özgü birincil, kurumsal, akademik ve arşiv kaynaklarının öncelik sırası ilgili kanal profilinden alınmalıdır. Kaynak seçimi konuya göre yapılmalı; dönem reklamı, propaganda, şirket anlatısı, kullanıcı tanıklığı veya hatırat kendi taraflılığı ve sınırlılığı belirtilmeden bağımsız doğrulama gibi kullanılmamalıdır.

### 4.3. Claim ledger

Senaryo yazılmadan önce ana iddialar için bir kanıt tablosu hazırlanmalıdır. Bu tablo final pakette görünür olmalıdır.

| Claim ID | Planned claim            | Importance  | Primary / institutional support | Independent support | Caveat or wording limit | Status   |
| -------- | ------------------------ | ----------- | ------------------------------- | ------------------- | ----------------------- | -------- |
| C01      | Videonun ana tez iddiası | Core thesis | Doğrudan kaynak                 | İkinci kaynak       | Kapsam ve ölçüm sınırı  | VERIFIED |

Kurallar:

- `VERIFIED`, `DISPUTED`, `CONTEXT ONLY`, `REMOVE` durumlarından biri kullanılmalıdır.
- `Core thesis` iddia `VERIFIED` değilse senaryo kesinleştirilemez.
- `DISPUTED` iddia kesin dille yazılamaz.
- Claim ID’ler kurgu tablosunda kullanılmalıdır.
- Kaynak yalnızca ana sayfaya değil, ilgili belgeye veya veri sayfasına gitmelidir.

## 5. Telif ve kaynaklandırma

Bu template kapsamında bir görsel veya videonun `kullanımı ücretsiz` sayılması için, **gelir elde edilen ticari bir YouTube videosunda** ücretsiz kullanılabilmesi ve kurgu içinde kesme, kırpma, yeniden boyutlandırma, renk düzenleme ve ses kapatma gibi gerekli değişikliklere izin vermesi gerekir. Kullanım için ücret ödeme, lisans satın alma, kuruma/hak sahibine başvurma, e-posta ile izin isteme, özel onay alma veya sonradan kullanım raporu gönderme zorunluluğu bulunamaz.

Kabul edilen hak durumları yalnızca şunlardır:

- Doğrulanmış `Public Domain` / kamu malı
- `CC0`
- Ticari kullanıma ve uyarlamaya izin veren `CC BY` lisansları; gerekli atıf paket içinde eksiksiz yazılmak şartıyla
- Pexels, Pixabay veya benzeri bir kaynağın, ilgili tekil varlık için ticari kullanıma ve düzenlemeye açıkça izin veren; ücret veya ayrıca izin gerektirmeyen ücretsiz platform lisansı
- Yukarıdakiler kadar açık biçimde ticari kullanıma ve düzenlemeye izin veren başka bir ücretsiz lisans; koşulları tekil varlık sayfasında doğrulanmak şartıyla

`CC BY-SA`, `CC BY-NC`, `CC BY-ND`, `editorial use only`, `research only`, `personal use only`, `educational use only` ve benzeri ek paylaşım, kullanım alanı veya değişiklik kısıtı getiren lisanslar bu üretim akışında kabul edilmez. Yalnızca atıf yazma zorunluluğu, ayrıca lisans veya izin istemek anlamına gelmez; ancak atıf metni teslim paketinde hazır verilmelidir.

### 5.1. Tercih edilen görsel kaynaklar

- U.S. federal kurumları ve arşivleri; yalnızca kamu malı durumu öğe bazında doğrulandığında
- Wikimedia Commons; yalnızca tekil dosya sayfasındaki lisans yukarıdaki kabul edilen kategorilerden biriyse
- Library of Congress ve benzeri ulusal kütüphaneler; yalnızca tekil öğe açıkça kamu malıysa veya yukarıdaki kabul edilen ücretsiz lisanslardan birini taşıyorsa
- Internet Archive; yalnızca tekil öğe açıkça kamu malıysa veya gerçek hak sahibi tarafından yukarıdaki kabul edilen ücretsiz lisanslardan biriyle yayımlanmışsa
- Imperial War Museums, BFI, Historic England, Historic Environment Scotland ve benzeri kurumların yalnızca ticari kullanımı ve düzenlemeyi ücretsiz, başvurusuz ve öğe bazında açıkça izinli kılan varlıkları
- Europeana üzerindeki hak etiketi yukarıdaki kabul edilen ücretsiz kategorilerden birine açıkça karşılık gelen kayıtlar
- Smithsonian ve benzeri müzelerin yalnızca `Open Access`, `CC0`, kamu malı veya yukarıdaki ölçütleri karşılayan açık koleksiyon öğeleri
- Kurum veya üretici tarafından ticari kullanıma ve düzenlemeye izin veren ücretsiz lisansla yayımlanmış tarihsel tanıtım, eğitim veya test filmleri
- Pexels ve Pixabay; yalnızca tekil varlığın ücretsiz ticari kullanım ve düzenleme hakkı doğrulandığında, gerçek arşiv bulunamadığında ve modern bağlamı doğrudan desteklediğinde
- Kullanıcının bizzat sahibi olduğu veya yukarıdaki ücretsiz ticari kullanım ölçütlerini karşıladığı doğrulanmış varlıklar

### 5.2. Kullanılmayacak kaynaklar

- Başka YouTube kanallarının videoları
- **YouTube için mutlak yasak:** YouTube üzerinde barındırılan hiçbir video veya video kesiti, `Public Domain`, `CC0`, `CC BY`, Creative Commons, açık ticari lisans veya başka herhangi bir lisans kapsamında ticari kullanım ve düzenlemeye açık görünse dahi **hiçbir koşulda kullanılamaz**. YouTube videosu asset library’ye, hook’a, thumbnail’e, edit map’e veya final kurguya alınamaz; lisans uygunluğu bu yasağı geçersiz kılamaz.
- Televizyon belgesellerinden veya ticari filmlerden alınmış kesitler
- Lisansı açıkça belirtilmemiş sosyal medya yüklemeleri
- Uploader logosu veya filigranı taşıyan görüntüler
- Pinterest ve benzeri kaynağı belirsiz görsel toplayıcıları
- Arama motoru önizleme görselleri
- Sahibi veya orijinal kaynağı bulunamayan reklam, propaganda ve arşiv derlemeleri
- Ücretli lisans, abonelik, kurum/hak sahibi onayı, yazılı izin, başvuru, e-posta veya özel kullanım sözleşmesi gerektiren varlıklar
- `Contact us for licensing`, `permission required`, `rights-managed`, `licence on request` veya benzeri ifade taşıyan varlıklar
- `CC BY-SA`, `CC BY-NC`, `CC BY-ND`, `editorial use only`, `research only`, `personal use only`, `educational use only` veya ticari kullanımı/düzenlemeyi sınırlayan varlıklar
- Hak durumu yalnızca koleksiyon veya kurum düzeyinde açıklanan fakat tekil öğe için doğrulanamayan varlıklar

`Fair use` varsayımı kullanılmaz. Pakete yalnızca yukarıda kabul edilen, ücretsiz ticari kullanımı ve gerekli düzenlemeleri açıkça mümkün kılan varlıklar alınır. Uygun varlık bulunamazsa ücretli veya izin gerektiren bir kaynak önerilmez; başka ücretsiz kaynak aranır, anlatım mevcut görsellere göre yeniden yazılır veya ilgili bölüm çıkarılır.

### 5.3. Birleşik Krallık ve Avrupa arşivleri için özel uyarı

Bir kurumun kamuya açık olması, koleksiyonundaki dosyaların serbestçe yeniden kullanılabildiği anlamına gelmez.

- Kurumun ana sayfası değil, tekil öğenin hak bildirimi kontrol edilmelidir.
- `Available online`, `research use`, `personal use`, `educational use` veya `viewable` ifadeleri ticari YouTube kullanım izni sayılmaz.
- Lisans açık değilse veya ayrıca izin/lisans başvurusu gerekiyorsa dosya hiçbir şekilde asset library’ye ya da edit map’e alınmamalıdır. `İzin alınabilir` veya `lisans satın alınmalı` şeklinde alternatif sunulmamalıdır.
- Gerekli üretici, fotoğrafçı, kurum ve koleksiyon kredileri eksiksiz yazılmalıdır.

### 5.4. Her varlık için zorunlu bilgiler

Her video, fotoğraf, belge, harita veya ses kaydı için:

- Varlık kodu
- Açık ve kısa içerik açıklaması
- Görüntünün tarihi veya yaklaşık dönemi
- Konuya uygun yer, kişi, kurum, ürün, araç, sistem veya olay bağlamı
- Doğrudan kaynak sayfası
- Kesin lisans veya kamu malı durumu; yalnızca `Public Domain`, `CC0`, kabul edilen `CC BY` ya da koşulları açık ücretsiz ticari platform lisansı
- Ücret, ayrıca izin, başvuru veya özel onay gerekmediğinin doğrulanması
- Gerekli üretici, fotoğrafçı, kurum veya koleksiyon kredisi
- Video için doğrulanmış kullanılabilir kaynak zaman aralıkları
- Görüntünün gerçek olay mı, tanıtım/eğitim/propaganda mı, haber filmi mi, reenactment mı veya bağlamsal görüntü mü olduğu

## 6. Uzun video hikâye yapısı

Konuya özel prompt belirli bir yapı veriyorsa o yapı kullanılır. Aksi hâlde ilgili kanal profilindeki varsayılan hikâye omurgalarından konuya en uygun olanı seçilir. Hedef süre prompttan; orada yoksa kanal profilindeki varsayılan süreden alınır. Profildeki bölüm zamanları bu hedefe göre ölçeklenen **oransal hikâye yönüdür**; hiçbir bölüm sırf takvimdeki yerine ulaşmak için uzatılmaz. Bu yapılar eksiksiz kronoloji değil, tek bir merkezi hikâyenin ilerleme planıdır.

## 7. İzleyici tutma ve anlatım ritmi

Amaç, izleyicinin videoyu seçtiği soruya anlaşılır ve tatmin edici biçimde ilerlemektir. **Konuşma hızı, yeni bilgi yükü ve görsel değişim sıklığı ayrı değişkenlerdir.** Hızlı kesilmiş bir video yavaş ilerleyebilir; sakin bir açıklama yüksek merak taşıyabilir. Enerji ve ritim profilden gelir. Aşağıdaki süreler aksi belirtilmedikçe profil/prompt boşluğunda kullanılan editoryal başlangıç değerleridir; algoritma eşiği değildir. Bölüm 8’de açıkça maksimum olarak tanımlanan tek-plan süreleri bu esnekliğin dışındadır.

### 7.1. Anlamlı ilerleme ve reset

- Her anlatı bloğu bir şeyi göstermeli, açıklamalı, kanıtlamalı veya önceki bilginin sonucunu hissettirmelidir. Önce izlenebilir somut sahne/eylem, ardından onu açıklayan kısa VO ve görünür sonuç planla; yalnızca metni bitirip altına genel B-roll döşeme.
- Her sekansın sonunda izleyicinin başlangıca göre neyi farklı anladığını C’deki mevcut soru/kanıt/reset alanlarıyla kontrol et. Aynı soru, aynı makine hareketi veya aynı sonuç farklı cümlelerle dönüyorsa sekansı kısalt.
- Yaklaşık 60–90 saniyelik yoğun açıklamadan sonra yeni terim eklemeyen kısa bir uygulama, karşılaştırma veya insan sonucu düşün. Bu bir zorunlu duraklama değildir; yaklaşık 5–15 saniyelik örnek çoğu durumda yeterli başlangıçtır. Ritmi korumak için sırf nefes adına uzun hareketsiz bekleme ekleme.
- Profil sayı vermiyorsa gövdede yaklaşık 30–60 saniyede bir “izleyici ne öğrendi veya ne değişti?” kontrolü yap. Bu kontrol yeni bir bilgi ekleme veya kesme kotası değildir; gelişen bir sürecin ara sonucu yeterlidir.
- Reset; yeni kısıt, karşılaştırma, karar, kanıt veya sonuçla yapılır. Sırf süre geçti diye müzik yükseltme, efekt veya “but everything changed” ekleme.
- Gerekli bağlam soruya bağlandığı yerde verilir. Kesintisiz genel bağlam yaklaşık 30–45 saniyeyi buluyorsa gerekliliğini kontrol et; anlaşılmakta olan bir mekanizmayı yalnızca kronometre yüzünden bölme.
- Bir reset anlaşılmamış bilgiyi bırakıp başka konuya kaçış olamaz.

### 7.2. Chapter ve merak döngüleri

- Chapter bir nedensel aşama veya anlamlı soru etrafında kurulur; sayısı konu ve süreye göre belirlenir.
- Her chapter aynı soru–açıklama–cevap kalıbını tekrarlamaz. Olay, eylem, sonuç veya karşılaştırmayla da başlayabilir.
- Ana video sorusuna ek olarak aynı anda tercihen en fazla bir önemli yan soru açık tutulur. Yan soruya mümkünse aynı sekans/bölümde cevap ver; uzun gecikme gerekiyorsa anlamlı ara cevap sun.
- “Birazdan göreceğiz” cümlesi yerine izleyiciye şimdi değer ver. Cevabı yalnızca sona saklamak için doğal anlatı sırasını bozma.
- Önceki sonucu kısa hatırlatma, yeni karşılaştırmayı anlamak için gerekliyse kullanılabilir. Aynı açıklamayı ikinci kez anlatmak veya her chapter'da özetlemek dolgu sayılır.

### 7.3. Bilgi yoğunluğu ve anlaşılabilirlik

- Bir cümle/ekran odağı mümkün olduğunca bir yeni ilişki taşısın. Bir kavramı kurmadan ikinci kavramı açıklamaya geçme.
- İsim, tarih, sayı ve kısaltmaları hatırlatma zorunluluğu yaratmadan seç. Dakika başına tek özel isim gibi mekanik kota yoktur; karşılaştırmanın iki tarafını aynı anda tanıtmak gerekebilir.
- Teknik terimi ilk kullanımda gündelik dille açıkla. Sayıya birim, kapsam ve anlaşılır bir referans ver; benzetme gerçek ölçüyü çarpıtmasın.
- Tercih edilen açıklama sırası: somut örnek/eylem → nasıl çalıştığı → sonucu. Her bölümün önemi bağlamdan anlaşılabiliyorsa ayrıca “this matters because” cümlesi ekleme.
- VO yeni bir sayı anlatırken ekranda bağımsız, uzun bir metin okutma. Grafik üzerinde dikkatin nereye gitmesi gerektiği belli olsun.
- Zor bir bölümü hızlandırarak çözme. Önce gereksiz terimleri ve yan nedenleri çıkar; sonra görsel aşamaları sadeleştir; gerekiyorsa anlatımı yavaşlat.
- Üretim öncesi, konuya yabancı izleyici açısından kontrol et: “Bu kim/ne?”, “Ne değişti?”, “Neden oldu?”, “Sonucu ne?” sorularının o an gerekli olanları cevaplanıyor mu?

### 7.4. Seslendirme boşlukları ve görsel nefes

- Nefes alanı yalnızca tam sessizlik değildir. Aynı fikri gösteren somut örnek, yeni terim eklemeyen kısa sonuç cümlesi veya izlenebilir bir eylem de zihinsel yükü azaltır.
- Gerçek görüntü, okunması gereken grafik veya anlamlı doğal ses gerektiriyorsa anlatıcı geri çekilir. Yaklaşık 1–4 saniyelik duraklamalar başlangıç noktasıdır; güçlü bir süreç/ses daha uzun alan gerektirebilir.
- Toplam nefes saniyesi, nefesler arasında 90 saniye veya tüm video için 10–35 saniye kotası yoktur. Süre, görüntü ve anlaşılabilirliğe göre seçilir; boşlukla hedef süre doldurulmaz. Görsel plan sınırları Bölüm 8'de ayrıca uygulanır.
- Grafik sonucunu söyledikten sonra gerekirse yaklaşık 2–3 saniye temiz okuma alanı bırak; bu sırada bağımsız yeni bilgi ekleme. Grafik ilk gösteriminden itibaren okunacak kadar uzun kalmalıdır.
- **2.0 saniyeye kadar kısa duraklamalar** I bölümüne göre ElevenLabs v4 duraklama etiketiyle (`[short pause]`, `[pause]`, `[long pause]`) yazılabilir. **2.0 saniyeden uzun** görsel nefesler ve doğal/arşiv sesi alanları ilgili `Picture and edit instruction` hücresinde `NARRATION ENDS AT [timeline]; NATURAL SOUND / VISUAL HOLD UNTIL [timeline]` biçiminde kesin zamanlanır. VO dosyasında korunur; otomatik silence trimming uygulanmaz.

### 7.5. Konuşma dili ve hız hesabı

- Kısa vurgu, orta uzunlukta açıklama ve gerektiğinde daha uzun neden–sonuç cümlelerini doğal biçimde karıştır. Sürekli kesik cümle veya sürekli yan cümle kullanma.
- Her paragraf bir ana fikir taşısın. Aktör ve eylem açık olsun; çeviri kokan, soyut ve dolambaçlı ifadeler yeniden yazılsın.
- WPM ve enerji profilden/prompttan alınır. Hiç değer verilmemişse İngilizce açıklayıcı VO için yaklaşık **140–160 konuşulan kelime/dakika** geçici üretim varsayımı kullanılabilir; bunu optimum YouTube hızı olarak sunma. Karmaşık bölüm için önce daha az bilgi, sonra gerekirse daha yavaş okuma seç.
- A ve J'de konuşulan bölüm WPM'i ile tüm timeline üzerinden ortalama WPM'i karıştırma. `Tahmini süre = Σ(bölümün konuşulan kelimesi / bölüm WPM'i × 60) + ayrıca zamanlanmış konuşmasız alanlar`. Duraklama etiketlerini kelime sayma; aynı sessizliği iki kez ekleme.
- Kayıt öncesi zamanlar tahminidir. Gerçek VO varsa ölçülen süre ve hizalamayla G/I zamanlarını güncelle; gerçek ses ölçülmeden kare hassasiyetinde eşleşme doğrulandığını iddia etme.
- Metin sığmıyorsa önce tekrar ve yan ayrıntıları çıkar; yalnızca sığdırmak için konuşma hızını artırma.
- Sessiz görüntü incelemesi ve yalnız ses okuması yap: görsel anlaşılır mı, VO görüntü olmadan ana nedensel bağı kuruyor mu? Bu kontroller izleyici testi veya performans kanıtı diye sunulmaz.

### 7.6. Açılış, ilk cevap ve kapanış

- Selamlama, logo animasyonu, bölüm listesi ve genel “in this video” girişi kullanma.
- İlk plan başlık–thumbnail vaadini somutlaştırır. İlk cümle konuya özgü olay, çelişki, eylem veya sonuçla başlar. Başlıktaki ilginç sayı/teknik özellik doğrudan vaadin kendisiyse ilk cümlede kullanılabilir; kuru özellik kataloğu yazma.
- Profil/prompt zamanlama vermiyorsa başlangıç hedefi: **ilk 5 saniyede özne/vaat görsel olarak tanınır; ilk 15 saniyede temel gerilim anlaşılır; ilk 30 saniyede bir somut kanıt veya kısmi cevap gelir; ilk 30–60 saniyede ana mekanizma/olay açıklanmaya başlar.** Bunlar dört ayrı kart veya zorunlu dört cümle değildir; aynı an birkaç işlev taşıyabilir.
- Hook'un 60 saniye sürmesi ilk cevabı 60. saniyeye ertelemek anlamına gelmez. Daha uzun hook, aynı sorunun tekrarına dönüşemez.
- Ana cevabın yönünü erken söylemek serbesttir. Devamında mekanizma, kanıt, gerçek sınır veya sonuç derinleşir; sahte sır yaratılmaz.
- Başlık yanlışsa açılışa uzun savunma eklemek yerine başlığı düzelt. Gerekli kapsam nitelemesini ilk yanıltıcı çıkarım oluşmadan kısa ve doğal biçimde ver.
- Hook sonrası yeni bir giriş başlatma; açılışta görülen olayın nedenine veya sonucuna geç. İlk 40 saniyeyi kurarken uygulanabilir başlangıç akışı: 0–5s somut özne/eylem; 5–15s görünür fark ve neden önem taşıdığı; 15–30s gerçek kanıt veya küçük bir cevap; 30–40s bu cevabın açıklanacak mekanizmasına geçiş. Bunlar zorunlu kesme noktaları değildir; anlatı profille uyarlanır, sabit görsel yasağı uyarlanmaz.
- Açılıştaki en güçlü kanıtı uzun tarihçenin arkasına saklama. Gövdede bu görüntüyü yeniden oynatmak yerine farklı işlem, ayrıntı veya sonuçla açıklamayı derinleştir. Açılış ön izlemesi de video tekrar yasağına tabidir.
- Kapanış ana soruyu açıkça cevaplar ve mümkünse açılıştaki somut nesne/karara yeni anlam kazandırır. Genellikle kısa bir sonuç sekansı yeterlidir; bütün videoyu özetleme, yeni büyük konu açma veya uzun vedayla bitirme.
- Doğal sonraki video bağlantısı varsa cevaptan sonra tek cümleyle kurulabilir. Zorunlu “like and subscribe” ve merakı kapatmadan yönlendirme yoktur.

### 7.7. Yayın sonrası öğrenme; sonuç uydurma yok

- Gerçek Studio verisi yoksa düşük izlenmenin sebebini bu template'ten kesin teşhis etme; değişiklikleri test edilecek editoryal hipotezler olarak sun.
- Veri sağlanırsa benzer süre/konu ve trafik kaynaklarını karşılaştır. CTR'ı gösterim hacmi ve Browse/Search/Suggested dağılımıyla; izlenme süresini ilk 30 saniye, düşüş/yükseliş noktaları ve ortalama izlenen yüzdeyle birlikte değerlendir. Reklam trafiğini organik trafikle karıştırma.
- Düşüş otomatik olarak “yavaş anlatım” değildir: vaat uyumsuzluğu, anlaşılmayan terim, tekrar veya konu geçişi olabilir. Yükseliş de otomatik başarı değildir; anlaşılmadığı için tekrar izleme olabilir.
- Tek videodan evrensel CTR/retention eşiği veya kanal kapatma sonucu çıkarma. Az veri varsa belirsizliği yaz.
- Sonraki üretimde tek bir temel hipotezi önceliklendir: örneğin ilk mekanizmayı erkene almak veya bir teknik bölümü sadeleştirmek. N'de varsa önceki bulguyu ve denenmekte olan değişikliği kısa kaydet; yayınlanmamış videoya performans sonucu yazma.

## 8. Görsel ve kurgu kuralları

Bu bölümdeki tekrar sınırları ve tek-plan süre üst sınırları teslimi durduran zorunlu kurallardır. Konuya özel prompt açıkça farklı sınır vermedikçe uygulanır.

### 8.1. Görsel karışımın uygulanması

1. Hedef hareketli görüntü, özgün grafik, lisanslı fotoğraf ve belge oranları konu promptundan; orada yoksa kanal profilinden alınır. Master gövde için evrensel bir oran koymaz; ilk 40 saniye ve hook için Bölüm 9 kesindir. Gerçek video ile gerçek fotoğraf/belge birlikte görsel anlatının temelini oluşturur; üretilmiş grafik varsayılan dolgu değildir.
   - Her ana bölüm için video adaylarıyla birlikte doğru özneye ait gerçek fotoğraf/belge de araştır. İlk 40 saniye sonrasında güçlü gerçek fotoğrafları aktif olarak kullan; yalnızca hareket oranını yükseltmek için bunları zayıf videoyla veya temsili G sahnesiyle değiştirme.
   - V, P, gerçek belge/harita G ve üretilmiş G sürelerini mevcut A/E açıklamalarında ayır; fotoğrafa pan/zoom eklemek onu V yapmaz, fotogerçekçi G gerçek fotoğraf sayılmaz. G içinde gömülü fotoğraf varsa süreyi iki kez sayma.
   - Seçilen oran A ve E bölümlerinde sayısal olarak yazılmalı; asset library ve edit map üzerinde fiilen karşılanmalıdır.
   - Yeterli sayıda anlamlı ve farklı varlık bulunamazsa oran veya hedef süre yalnızca gerekçeli biçimde revize edilir. İlgisiz, zayıf bağlantılı, tekrarlı ya da gereksiz kesitlerle kota doldurulamaz.
2. **Doğru, konuya doğrudan bağlı ve görsel değer taşıyan gerçek video varsa kurgu olabildiğince onu kullanmalıdır.** Kaynak dosya sayısı belirleyici değildir; tek videodaki birbirinden farklı, anlamlı ve doğrulanmış eylemler de güçlü hareketli kurgu sağlayabilir. Aynı anlatım anını hem doğru bir V hem statik bir seçenek taşıyabiliyorsa ve V gerçekten kanıt, mekanizma, ölçek, insan sonucu veya anlamlı eylem gösteriyorsa öncelik V’dedir. Uygun ve doğru hareketli sahneler varken sırf grafik/fotoğraf oranı veya üretim kolaylığı için uzun statik bölümler kurulamaz. İlgisiz, gevşek bağlantılı veya yalnızca ekranda hareket olsun diye seçilmiş video bu önceliği karşılamaz. Gerçek fotoğraf ve belgeler kendi güçlü kanıt/ayrıntı işlevleri için kısa ve seçici kullanılır. Video birkaç arşiv klibi döndürülerek veya uzun kaynaklar sırf süre kazanmak için parçalanarak doldurulamaz. Her ana bölüm için yeterli sayıda **anlamlı ve farklı** sahne bulunmalıdır.
3. Hook içinde aynı orijinal video kaynağından en fazla **iki farklı kesit** kullanılabilir. Bu teknik tekrar sınırı master’a aittir. Hook dâhil bütün videoda aynı kaynaktan seçilen kesitler hem çakışmamalı hem görsel olarak yeni bilgi/eylem göstermelidir; yalnızca kamera açısının veya zaman kodunun değişmesi yeterli değildir (Bölüm 10.3).
4. Hareketli görüntü sırf hareket var diye seçilmez; anlatılan olay, kişi, kurum, ürün, araç, dönem, yer veya işlemle anlamlı bağlantısı olmalıdır.
   - Görüntü doğru konuya ait olsa bile **seçilen saniyeler** anlatılan cümleye görsel değer sağlamıyorsa kullanılmaz. Kaynak doğruluğu tek başına yeterli değildir.
   - Kaynak sesi kullanılmıyorsa yalnızca konuşan bir insanı gösteren talking-head kesiti varsayılan olarak reddedilir. Kişinin kimliği, mimikleri, gösterdiği nesne/eylem veya bulunduğu tarihsel an görsel olarak başlı başına önemliyse istisna yapılabilir.
   - Bir kesitin VO ile birlikte kullanılabilmesi için en az bir işlevi olmalıdır: kanıt göstermek, mekanizmayı açıklamak, ölçek/yer/zaman kurmak, insan sonucunu göstermek, merkezi özneyi tanıtmak veya bir geçişi anlamlı biçimde taşımak. Bu işlevlerden hiçbiri yoksa kesit kaldırılır.
5. Gerçek kullanım, üretim, hareket veya insan etkileşimi anlatılırken bunu gerçekten gösteren video tercih edilir. Kimlik, tasarım farkı, tarihsel an, belge veya fiziksel ayrıntı anlatılırken ilk 40 saniye sonrasında doğru gerçek fotoğraf/belge doğrudan seçilebilir; fotoğraf son çare değildir.
6. Gerçek dönem/olay videosu yoksa sırasıyla doğru öznenin açık lisanslı demo, eğitim, test, müze, miras veya modern kullanım görüntüsü; gövdede bu adaylarla birlikte doğru gerçek fotoğraf/belge değerlendirilir; açıklama gerektiriyorsa plan/harita veya özgün grafik kullanılır.
7. Modern görüntü tarihsel görüntü gibi renklendirilip sunulamaz.
8. Başka ülke, şirket, model, taraf, birlik, cephe veya tarihteki benzer görüntü yalnızca mekanizmayı doğru açıklıyorsa kullanılmalı ve `context footage` olarak açıkça belirtilmelidir.
9. Video kesitleri kesinlikle yavaşlatılamaz, yapay biçimde uzatılamaz, freeze-frame ile süre dolduramaz veya aynı kareler tekrar edilerek uzun gösterilemez. Kurgu, kaynağın gerçek oynatma hızı ve kullanılabilir doğal süresi üzerinden planlanmalıdır.
10. Hızlandırma gerçek hareketi, tepki süresini, kullanım kolaylığını, üretim sürecini veya operasyonu yanıltacak biçimde kullanılamaz. Her video kesitinin edit map’teki ekran süresi, kaynak zaman aralığının doğal oynatma süresiyle birebir uyumlu olmalıdır.

### 8.2. Fotoğraf, belge, harita ve grafik kullanımı

1. Fotoğraflar gerçek kişi, doğru özne/model, yer, belge, önemli olay veya sonucu göstermenin gerekli olduğu yerlerde kullanılmalıdır.
2. Hook dışında tek bir fotoğraf/görsel planı için normal hedef **12–15 saniyedir** ve kesin üst sınır **15 saniyedir**. Görsel işlevini daha kısa sürede tamamlıyorsa yalnızca 12 saniyeyi doldurmak için yapay biçimde bekletilmez; ancak hiçbir tek fotoğraf/görsel planı 15 saniyeyi aşamaz.
3. Bölüm 9’un korunan açılış aralığı dışında tek bir `G` varlığının — sabit veya motion; harita, belge, plan, veri grafiği, timeline, açıklayıcı şema, teknik görselleştirme ya da temsili sahne — kesintisiz ekran süresi en fazla **10 saniyedir**. Normal hedef okunabilirlik ve anlatım işlevine göre yaklaşık **5–10 saniyedir**. Daha fazla okuma veya açıklama süresi gerektiren içerik sadeleştirilir ya da araya konuya doğrudan bağlı gerçek V planı girerek anlamlı aşamalara bölünür. Aynı veya görsel olarak eşdeğer G’yi satırlara, katmanlara veya motion aşamalarına bölmek 10 saniyelik üst sınırı sıfırlamaz. Bölüm 9’daki hook G sınırı daha sıkıdır ve ayrıca uygulanır.
4. Hook dışında arka arkaya üç sıradan fotoğraf planı kullanılamaz.
5. **Birleşik statik sekans sınırı:** fotoğraf, sabit grafik, belge, harita ve diğer hareketsiz görseller ardışık kullanıldığında süreleri birlikte toplanır. Kesin üst sınır **15 saniyedir**; bu süre dolmadan konuya anlamlı biçimde bağlı hareketli görüntüye geçilmelidir. P → G → belge → başka fotoğraf geçişi veya G kodunu değiştirmek sayacı sıfırlamaz. Uygun video varken statik sekans gereksiz yere uzatılamaz. Uzun metin veya grafik okuma ihtiyacı istisna değildir; içerik sadeleştirilir veya anlamlı video planlarıyla bölünür. Uygun video bulunamaması da 15 saniyelik birleşik statik üst sınırı aşma izni vermez; gerekirse anlatım mevcut varlıklara göre kısaltılır veya yeniden kurulur.
6. Harita, belge ve sabit grafikler **birleşik statik sekans sayacına dâhildir**; tek değişmeyen durum için ayrıca madde 3 uygulanır. Parlama, shimmer, titreşim, yazı hareketi, otomatik pan/zoom veya fotoğraf değiştirme hareketli görüntüye dönüş sayılmaz. Sayacı sonlandıran plan, izleyiciye anlamlı eylem, işlem veya gelişme izleten gerçek V ya da gerçekten açıklayıcı içerik hareketi taşıyan motion G olmalıdır; uygun gerçek V varsa öncelik V’dedir. Sırf sayacı sıfırlamak için 1 saniyelik alakasız video sıkıştırılamaz; hareketli plan kendi anlamlı eylemini göstermeli ve Bölüm 8.3.1 ritmine uymalıdır.
7. Fotoğrafa zoom veya pan yalnızca ayrıntıyı okumayı kolaylaştırıyorsa uygulanmalıdır. Otomatik sürekli zoom varsayılan kurgu stili değildir.
8. Tarih, yer, kurum/ürün/birim adı ve önemli sayı için kısa statik ekran yazısı kullanılabilir.
9. Karmaşık veri görseli yerine izleyicinin bir bakışta anlayabileceği tek karşılaştırma tercih edilmelidir.
10. Grafikteki her sayı ve eksen araştırma kaynağına dayanmalıdır.
11. `G` varlıkları yalnızca istatistik, sayı, eksen veya veri karşılaştırması gereken anlarla sınırlandırılmamalıdır. Arşiv görüntüsü tek başına bir olayı, fiziksel ilişkiyi, süreci, karar anını, insan etkileşimini, mekânsal düzeni veya neden-sonuç bağını gözde canlandırmaya yetmiyorsa açıklayıcı ya da temsili bir görsel hazırlanabilir.
12. Her chapter için önce gerçek video ve gerçek fotoğraf/belgeyle nelerin gösterilebildiğini belirle. `G` yalnızca bu malzemelerin açıklayamadığı ilişki, veri veya mekanizmayı görünür kılıyorsa seçilir. Chapter başına grafik adayı veya grafik adedi zorunluluğu yoktur; gerçek malzemeyi yeniden üretmek için temsili sahne eklenemez.
13. İstatistik dışı bir `G` varlığında içerik fişi; sahnede bulunacak kişi, araç, nesne ve çevreyi; bunların konumunu, eylemini, birbirleriyle ilişkisini ve görünmesi gereken fiziksel ayrıntıları açıkça tarif etmelidir. Örneğin yalnızca `people beside a car` yazılamaz; doğruysa aracın nerede durduğu, kapısının açık olup olmadığı, kaç kişinin bulunduğu, ne yaptığı, arka planda hangi yapının görüldüğü ve sahnenin hangi anı açıklamak için kullanıldığı belirtilmelidir.
14. Kaynakların birebir doğrulamadığı tarihsel bir an görselleştiriliyorsa bu varlık gerçek arşiv fotoğrafı veya doğrudan kanıt gibi sunulamaz. İçerik fişinde `illustrative reconstruction` veya `explanatory visualization` olarak işaretlenmeli; doğrulanmamış yüz, kimlik, logo, üniforma, model, mekân veya olay ayrıntısı uydurulmamalıdır.
15. `G` varlıklarında ekran metni varsayılan olarak **bir kısa ana başlık ve en fazla bir kısa açıklama cümlesiyle** sınırlandırılmalıdır. Ana başlık çoğunlukla **2–7 kelime**, açıklama çoğunlukla **6–16 kelime** olmalı; grafik başlık veya açıklama olmadan açıkça anlaşılabiliyorsa bu alanlar kota doldurmak için eklenmemelidir.
16. Eksen adları, ölçü birimleri, kategori/seri adları, doğrudan veri etiketleri, zorunlu tarih ve yer adları, kısa kaynak satırı ve gerekli doğruluk açıklaması ana başlık/açıklama sınırına dâhil değildir; ancak yalnızca grafiği doğru okumak için zorunlu olan minimum sayıda kullanılmalıdır. Ayrıntılı veri tablosu, formül ve kaynak dokümantasyonu üretim girdisidir; ekranda paragraf, madde listesi veya veri dökümü olarak gösterilemez.
17. İkinci başlık, birden fazla bölüm etiketi veya ek açıklama yalnızca karşılaştırmanın taraflarını ayırmak, zaman çizelgesinin farklı evrelerini göstermek, haritadaki birden fazla durum/rota arasındaki farkı açıklamak ya da belge üzerindeki zorunlu ayrımı kurmak için kullanılabilir. Bu metinler kısa olmalı, birbirini veya seslendirmeyi tekrar etmemeli ve görsel kodlamayla anlatılabilen bilgi metne çevrilmemelidir.
18. `Main takeaway`, `Exact matching VO`, production note, detailed visual specification, accuracy note, `must not show` talimatı ve tam kaynak açıklamaları hiçbir koşulda kendiliğinden ekran metnine dönüştürülemez. Ekranda görünmesine açıkça karar verilmeyen her açıklama `production note only — do not place on screen` kabul edilmelidir.
19. Grafik; metin kutularının çevresine yerleştirilmiş dekoratif bir arka plan gibi değil, bilgiyi kompozisyon, ölçek, konum, şekil, çizgi, rota, nesne ilişkisi ve veri işaretleriyle anlatan gerçek bir görsel olarak kurulmalıdır. Bir bilgi görsel olarak anlatılabiliyorsa ayrıca uzun metinle açıklanmamalıdır.
20. Grafikler modern, temiz, yüksek kaliteli ve konu uygunsa sinematik bir görsel etkiye sahip olmalıdır; güçlü ana özne, derinlik, ışık, ölçek ve belirgin görsel hiyerarşi kullanılabilir. Ancak doğruluk, okunabilirlik ve açıklayıcı işlev korunmalı; sonuç salt dekoratif poster, konsept sanat veya konudan kopuk `visual art` görünümüne dönüşmemelidir.
21. Metin, ana özneyi veya veri görselleştirmesini küçültüyor; kompozisyonu kalabalıklaştırıyor; mobil/televizyon izleme boyutunda okunamıyor ya da grafiğin ana odağının ilk bakışta seçilmesini engelliyorsa içerik sadeleştirilmeli, gereksiz metin kaldırılmalı veya gerekçeli biçimde ayrı bir `G` varlığına bölünmelidir.

### 8.3. Görsel çeşitlilik

Kurgu yalnızca dosya sayısında değil, görsel işlevde de çeşitlenmelidir. Mümkün olduğunda şu plan tipleri arasında ritim kurulmalıdır:

- Geniş çevre, tesis, kullanım alanı, şehir veya olay alanı planı
- İnsan ve gerçek deneyim/etkileşim
- Üretim, mekanik, arayüz, araç, sistem veya eylem hareketi
- Merkezi özne ve teknik/fiziksel ayrıntı
- Harita, rota, ağ veya konum
- Belge, kayıt, kılavuz, ilan, reklam veya gazete
- Veri, zaman çizelgesi, karşılaştırma grafiği, açıklayıcı şema veya temsili sahne görselleştirmesi
- Konuya uygun kişi, uzman, kullanıcı, çalışan, asker veya tanık
- Sonuç, kapanış, kalıntı, modern karşılık veya bugünkü durum

Aynı öznenin aynı açıdan çekilmiş çok benzer fotoğrafları farklı dosya olsa bile `visual family` olarak değerlendirilir ve art arda kullanılmaz. Videoda görsel olarak eşdeğer sahne/eylem, farklı kaynak veya zaman kodundan gelse de bütün timeline boyunca bir kez kullanılabilir (Bölüm 10.3). Yeni açı yalnızca önce görünmeyen anlamlı ayrıntıyı gösteriyorsa farklı görsel değer taşır.

### 8.3.1. Plan ritmi ve görsel sekans

Bu alt bölümdeki ritim aralıkları profil/prompt boşluğunda kullanılan başlangıç değerleridir; ancak Bölüm 8.2’deki fotoğraf/görsel için **15 saniye**, G için **10 saniye** ve bu bölümdeki video için **20 saniye** tek-plan üst sınırları kesindir. Bölüm 10’daki tekrar kuralları ayrıca uygulanır.

- Kurgu metronom gibi her cümlede kesmemelidir. Plan değişimi yeni bilgi, yeni odak, hareketin tamamlanması veya duygusal vurgu tarafından gerekçelendirilmelidir.
- İlk 60–90 saniyede video planları çoğunlukla **2.5–6 saniye** sürer; fotoğraf/görsel ve G planları için Bölüm 8.2’deki süreler uygulanır. Gövdede sıradan açıklayıcı video planları çoğunlukla **3–8 saniye**; içinde gözle görülür gelişme, eylem veya süreç bulunan güçlü planlar **8–15 saniye** sürebilir. Kendi içinde gerçekten gelişen istisnai süreç planları doğal sesiyle **15–20 saniye** kullanılabilir; hiçbir tek video planı veya kesintisiz aynı görsel video bloğu **20 saniyeyi aşamaz**.
- Uzun plan yalnızca görüntü içinde izlenebilir bir gelişme varsa korunmalıdır. Tekrarlanan makine hareketi veya anlamsız bekleme uzun plan gerekçesi değildir.
- Mümkün olduğunda tekil stok/arşiv görüntüleri yerine **10–25 saniyelik** anlamlı mini-sekanslar kurulmalıdır: geniş bağlam → insan/özne → işleyiş ayrıntısı → ortaya çıkan sonuç gibi. Her plan yine edit map’te ayrı satır olarak yazılır. Mini-sekans içinde bile aynı görsel işlev 8–10 saniyeden uzun sürmemelidir; sekansın içinde gözle görülür ilerleme olmalıdır.
- VO ve görüntü birebir kelime eşleştirmesine zorlanmamalıdır. Görüntü aynı düşünceyi tamamlayan bir sahne kurabilir; ancak başka özneyi, tarafı, dönemi, coğrafyayı veya nedeni ima edecek kadar kopuk olamaz.
- Büyük grafik, harita, belge veya merkezi özne değişiminden önce/sonra kısa bir görsel köprü kullanılabilir. Sürekli aynı dissolve veya sürekli aynı hareketli zoom kullanılmaz.

### 8.4. Yapay zekâ ve canlandırma

- Yapay zekâ üretimi tarihsel fotoğraf veya video varsayılan olarak kullanılmaz.
- Modern reenactment, bilgisayar oyunu veya dramatizasyon gerçek arşiv görüntüsü gibi sunulamaz.
- Konuya özel prompt açıkça isterse bu materyal ayrı etiketlenir.
- Veri grafiği, sade harita ve açıklayıcı şema oluşturmak mümkündür; bunlar tarihsel kanıt yerine geçmez.
- Olayı veya fiziksel durumu zihinde canlandırmak için yapay zekâyla hazırlanmış bir `G` görseli kullanılabilir; ancak içerik fişinde `illustrative reconstruction` veya `explanatory visualization` olarak açıkça tanımlanmalı, gerçek arşiv görüntüsü izlenimi vermemeli ve doğrulanmış bilgilerin ötesine geçen ayrıntılar içermemelidir.
- Üretilemeyen gerçek görüntü, sahte “arşiv görüntüsü” ile tamamlanmaz.

### 8.5. Arşiv sesi

- Konuya uygun anlamlı gerçek mekanik, araç, ortam, insan, arşiv veya kullanım sesi kısa süre korunabilir.
- Kaynağın telif ve ses kullanım durumu ayrıca kontrol edilir.
- Tanıtım, propaganda, eğitim veya haber filmi anlatıcısının sesi kullanılacaksa bunun dönemsel ve taraflı niteliği belirtilmelidir.
- Arşiv anlatıcısı çoğunlukla kapatılır; yalnızca güçlü, kısa ve bağlamı açıklanmış anlar korunur.
- En az bir doğal sesli an kullanmak zorunlu değildir; fakat uygun haklara sahip güçlü ses bulunursa müzik ve anlatım kısa süre geri çekilerek sesin kendisine alan verilmelidir.
- Arşiv sesi VO altına anlaşılmaz biçimde bindirilmemelidir. Önce anlatıcı bağlamı kurar, sonra ses tek başına duyulur veya çok kısa bir sound bridge ile sonraki plana taşınır.
- Sesin korunacağı kesin süre, edit map’te görselin kaynak zamanıyla birlikte belirtilmelidir.

### 8.6. Geçişler

- Ana geçiş biçimi düz kesmedir.
- Cross-dissolve yalnızca dönem, mekân veya bugüne geçişte gerekliyse kullanılabilir.
- Geçiş estetiği kanal profilinden alınır. Hangi stil seçilirse seçilsin geçiş, yeni bölüm/yer/zaman/özne işlevi taşımadan yalnızca hareket üretmek için kullanılamaz.
- Chapter kartları zorunlu değildir. Kullanılırsa 1–2 saniyeyi geçmemeli ve arka plandaki hareketli görüntüyü durdurmamalıdır.

## 9. Hook için zorunlu kurallar

Hook’un yaratıcı süresi, cümle ritmi, WPM’i ve anlatısal işlev dizisi profilden/prompttan alınır; ilk değer zamanlaması Bölüm 7.6 ile çözülür. Görsel tercihler aşağıdaki zorunlu hook standardını karşılamalıdır. Minimum plan sayısı yalnızca profil/prompt tanımlıyorsa kullanılır; sayıyı doldurmak için anlamsız plan eklenmez.

### Hook görsel önceliği ve hareketlilik hard gate’i

Bu hard gate, **0:00–0:40 aralığı ile tanımlı hook’un birleşimine** uygulanır. Hook 25 saniyede bitse de koruma 40. saniyeye kadar sürer; hook 60 saniyeyse hook’un tamamına uygulanır. Böylece chapter adını veya hook süresini değiştirerek kural aşılamaz.

- Bu aralıkta **sabit fotoğraf, sabit G, sabit belge/harita, slayt, freeze-frame ve tek kare video kesinlikle yoktur**. Eski “bir fotoğraf / üç saniye” istisnası kaldırılmıştır. P’ye pan/zoom, paralaks, titreşim veya parıltı eklemek yasağı kaldırmaz. Gerçek videonun üzerinde kısa ve okunur etiket olabilir; etiket ana görüntünün yerine geçemez.
- İlk tercih, kesin kaynak zamanı incelenmiş, konuya doğrudan bağlı ve anlamlı eylem/değişim gösteren **gerçek V**’dir. Korunan aralığın süresinin **en az %70’i gerçek V** olmalıdır; motion G bunun dışında sayılır. Aynı hareketin döngüsü bu oranı doldurmak için kullanılamaz.
- Korunan aralıkta **en fazla iki G gösterimi** olabilir; sıfır veya bir de uygundur. İki farklı kod vermek, aynı G’yi yeniden getirmek, katmanları veya satırları bölmek bu bütçeyi artırmaz. Her kesintisiz G planı tek gösterimdir; her biri en fazla **6 saniye** sürer ve gerçek içerik hareketi taşır. İki G üst sınırdır, üretim hedefi değildir. %70 gerçek V koşulu ayrıca sağlanır.
- Her açılış G’sinin mevcut kurgu hücresinde `MOTION GRAPHIC REQUIRED` ve zamanlı, anlamlı hareket açıklaması bulunur. Yalnızca “sonradan animasyon yapılabilir” demek yeterli değildir. Nesne/işleyiş/ilişki hareketi gerekir; yalnızca shimmer, yazı titreşimi veya kamera zoom’u yeterli sayılmaz. Mevcut yazılar sürekli görünür ve okunur kalır; yeni öğe/iddia eklenmez.
- G için `G01.jpg` temel görseli ve mevcut fiş şeması korunur. Gerçek animasyon henüz yoksa mevcut yeterlilik tablosunun `Main gaps` / `Decision` açıklamasında üretim bağımlılığı belirtilir; JPG rough-cut’a sabit yerleştirilerek bu kural sağlanmış sayılamaz. Animasyon üretilmeden ilgili açılış planı final kurguya hazır ilan edilmez; gerekirse doğrulanmış benzersiz V ile değiştirilir.
- Yeterli benzersiz V yoksa araştırmayı genişlet veya hook’un anlattığı örneği/eylemi mevcut güçlü gerçek görüntüye göre yeniden kur. Eksikliği üçüncü G, sabit P, benzer makine kesitleri veya ilgisiz stokla kapatma. Çözülemeyen görsel boşluk varken paket eksiksiz ilan edilmez. Açılış sonrasında gerçek fotoğraflar Bölüm 8.2’ye göre serbesttir ve aktif biçimde değerlendirilir.

1. Hook’un kesin timeline aralığı, hedef görsel karışımı, plan sayısı ve gerekiyorsa kaynak çeşitliliği A, C ve E bölümlerinde açıkça çözülmelidir.
2. İlk plan başlık ve thumbnail vaadine doğrudan hizmet etmeli; profil özgün grafikle açılışa izin veriyorsa doğrulanmış/temsili rolü doğru etiketlenmiş ve Bölüm 9’daki gerçek motion koşulunu sağlayan güçlü bir G varlığı kullanılabilir.
3. Logo, siyah ekran, uzun başlık kartı, boş atmosfer veya yalnızca hareket var diye seçilmiş alakasız görüntü açılış planı olamaz.
4. Hook plan süreleri seçilen kanal ritmine göre belirlenir; bir plan iç gelişme, kanıt veya okunması gereken bilgi taşımıyorsa sırf süre kazanmak için uzatılamaz.
5. Hook içinde aynı orijinal video kaynağından en fazla **iki ayrı kesit** kullanılabilir. Bir uzun kesiti yapay olarak bölmek, farklı dosya adı vermek veya araya başka plan koymak bu sınırı sıfırlamaz.
6. İlk cümle konuya özgü ve başlık vaadine bağlı olmalıdır; kuru özellik/tarih kataloğu veya sözlük tanımıyla başlamamalıdır. Vaadin kendisi olan çarpıcı sayı/özellik kullanılabilir (Bölüm 7.6).
7. Hook metni, kullanılacak gerçek görüntüler ve/veya G varlıklarının üretilebilirliği görülmeden kesinleştirilmemelidir.
8. İlgisiz hareketli görüntü yalnızca ekranı dinamik tutmak için kullanılamaz.
9. Hook’taki gerçek video kesitlerinin kaynak zamanları izlenerek veya karelerle incelenerek doğrulanmalı; G varlıklarının rolü ve kanıt sınırı doğru etiketlenmelidir.
10. H tablosunda hook ve non-hook sayıları ayrı sütunlarda tutulur; ancak video tekrar kontrolünde toplanır. Hook’ta kullanılan aynı veya görsel olarak eşdeğer video kesiti gövdede tekrar kullanılamaz.
11. Hook videosu doğal hızında kullanılmalı; tempo için yavaşlatılamaz, freeze-frame ile uzatılamaz veya sahte hareket üretilemez.
12. Hook rastgele “en iyi görüntüler” montajı değildir. Profilde tanımlanan işlev dizisini yerine getirmeli; en azından vaadin kanıtını, merkezi merakı ve ilk gerçek değer/payoff’u taşımalıdır.
13. Hook kelime sayısı ve WPM’i profilden alınır ve gerçek hook süresiyle hesaplanır. Güçlü görüntü, grafik okuması veya doğal ses çalışıyorsa kelime kotası doldurmak için metin eklenmez.
14. Hook yalnızca aynı soruyu farklı cümlelerle tekrar edemez; doğrulanmış bir ayrıntı, mekanizma, sonuç veya beklenmedik karşıtlık vermelidir.
15. Başlık/thumbnail’de öne çıkarılan öznenin görünme ve sözlü olarak kurulma zamanı profildeki açılış kuralına göre edit map’te kesinleştirilmelidir.
16. Hook sonrası retention bridge’in süresi ve enerji karakteri profilden alınır. Bu köprü uzun kanal tanıtımına, bölüm listesine veya değersiz bağlam bloğuna düşemez.
17. Hook sonunda izleyici videonun yalnızca soru sormadığını, cevabı vermeye başladığını açıkça hissetmelidir.

## 10. Görsel tekrarların sayılması

### 10.1. Genel sayım

1. Tamamı hook içinde kalan gösterimler H’de Hook uses sütununa yazılır; video için kullanım hakkı hook ve non-hook toplamında bir defadır. Sütunların ayrı tutulması yeniden kullanım hakkı vermez.
2. Hook’tan sonra başlayan veya hook sınırını aşan her gösterim non-hook kullanımıdır.
3. Bir varlığın ekrandan çıkıp başka bir varlıktan sonra yeniden görünmesi yeni kullanım sayılır.
4. Aynı fotoğrafın kırpılmış, yakınlaştırılmış, aynalanmış, renklendirilmiş, restore edilmiş, yazı eklenmiş veya farklı çözünürlükteki sürümü aynı fotoğraftır.
5. Aynı orijinal videonun yeniden kodlanmış, kesilmiş veya farklı adla kaydedilmiş kopyası aynı video kaynağıdır ve aynı `V` kodunu kullanır.
6. Farklı video kesiti için çakışmayan kaynak zamanı ve izleyicinin fark edebileceği yeni eylem, işlem aşaması, anlamlı ayrıntı veya sonuç birlikte gerekir. Görsel eşdeğerlik Bölüm 10.3’e göre kaynaklar arasında da incelenir.
7. Kaynak zamanları aynıysa, çakışıyorsa veya birkaç saniye kaydırılmasına rağmen aynı kamera planını gösteriyorsa aynı video kesitidir.
8. Koda yeni numara vermek tekrar sayacını sıfırlamaz.
9. Aynı `G` varlığının kırpılmış, yakınlaştırılmış, yeniden renklendirilmiş, farklı metin yerleşimli, farklı çözünürlüklü, farklı motion uygulanmış veya başka `G` koduyla yeniden üretilmiş sürümü; izleyiciye yeni ve anlamlı görsel bilgi getirmiyorsa aynı grafik kabul edilir.
10. Bir `G` varlığının tek kesintisiz gösterimi teknik nedenlerle birden fazla edit-map satırına bölünmüşse bu tek kullanım sayılır. Grafik ekrandan çıktıktan sonra yeniden görünmesi yeni kullanım sayılır ve Bölüm 10.4’e tabidir.

### 10.2. Fotoğraf tekrar sınırı

1. Hook dışında her benzersiz fotoğrafın varsayılan kullanım hakkı **bir defadır**.
2. İkinci kullanım yalnızca tarihsel veya kanıtsal olarak vazgeçilmezse yapılabilir.
3. Aynı fotoğrafın üçüncü non-hook kullanımı yasaktır.
4. İkinci kullanım için koşulların tamamı:
   - Farklı chapter’da olmalı
   - İlk kullanımın bitişi ile ikinci kullanımın başlangıcı arasında en az **90 saniye** olmalı
   - Arada en az **sekiz farklı görsel plan** bulunmalı
   - İkinci kullanım farklı somut bir ayrıntı veya karşılaştırma göstermeli
   - İki non-hook kullanımın toplam ekran süresi **18 saniyeyi** aşmamalı
   - Kurgu hücresinde `FORCED REUSE 2/2 — reason: ...` yazmalı
5. Bitişik tekrar ve `A–B–A` düzeni yasaktır.

### 10.3. Video kesiti tekrar sınırı

1. **Aynı, çakışan veya görsel olarak eşdeğer video kesiti hook + gövde + kapanış toplamında yalnızca bir kez kullanılabilir.** İkinci kullanım için anlatısal/kanıtsal istisna yoktur. `FORCED REUSE 2/2`, `INTENTIONAL REPLAY` veya farklı chapter kullanmak bu yasağı kaldırmaz; ikinci kullanım izni yalnızca Bölüm 10.2’deki fotoğraf koşullarında kalır.
2. Aynı kaynak videodan birden fazla kesit seçilebilir. Hook içinde kaynak başına en fazla iki kesit sınırı korunur; gövdede adet kotası yoktur. Ancak her kesit çakışmayan kaynak aralığına ve **görünür yeni içeriğe** sahip olmalıdır. Farklı zaman kodu veya dosya adı tek başına farklı içerik değildir.
3. **Görsel eşdeğerlik testi:** seçilen aralıkları normal hızda ve sessiz izle; özne, eylem/işlem aşaması, görünen ayrıntı ve sonuç bakımından karşılaştır. “İzleyici burada önce görmediği neyi görüyor?” sorusuna görüntüye dayalı somut cevap yoksa aynı görsel içerik kabul et. VO’nun farklı şey anlatması yeni görsel bilgi oluşturmaz.
4. **Çamaşır makinesi örneği:** 00:10–00:16, 01:20–01:26 ve 04:00–04:06 boyunca aynı tambur aynı biçimde dönüyorsa bütün video için yalnızca biri seçilir. Döngünün başka turu, çamaşırın farklı konumu, küçük açı/ışık değişimi veya farklı crop yeni kesit değildir. Buna karşılık çamaşır yükleme, farklı bir mekanizmanın çalışması, kontrol seçimi, tahliye ve bitmiş çamaşırın çıkarılması gerçekten görünüyorsa ayrı işlem aşamaları olabilir.
5. Aynı testi farklı V kodlarına ve farklı kaynaklardaki benzer planlara da uygula. Aynı işlevi gören neredeyse aynı döngü görüntülerini art arda veya uzak chapter’larda kullanma. Aynı özne tekrar görünebilir; açık yeni mekanizma, ayrıntı, ölçülebilir fark veya sonuç göstermelidir. Karşılaştırmanın iki tarafı gerçekten görünür fark sunuyorsa ayrı içeriktir.
6. F’deki mevcut `Footage` açıklamasında kullanılan her aralığın somut eylemini/ayrıntısını belirt. H’deki mevcut `Reuse / distinction note` içinde diğer kesitlerden farkını ve varsa görsel eşdeğerini yaz; yeni sütun, kod ailesi veya zorunlu hücre anahtarı ekleme. Farkı doğrulanamayan kesit seçilmez; görsel inceleme yapılmadan `PASS` yazılmaz.
7. Aynı uzun planı bölmek, zamanını kaydırmak, aynalamak, kırpmak, renklendirmek, hızını değiştirmek veya yeniden kodlamak yeni içerik oluşturmaz. Kaynak normal hızında kesintisiz ilerliyorsa teknik VO satır sınırı yeni kullanım değildir; gerçek blok toplamı plan süresi ve ilerleme kurallarına uyar. Görüntü ekrandan çıktıktan sonra eşdeğer içerikle geri dönemez.
8. Kesitler doğal oynatma hızında kullanılmalıdır. Slow motion, optical flow, frame interpolation, freeze-frame veya kare tekrarıyla ekran süresi uzatılamaz. Benzersiz içerik yetmiyorsa yeni görsel araştırılır, 40. saniye ve hook sonrasında gerçek fotoğraf/belge seçilir veya anlatım kısaltılır.

### 10.4. `G` grafik, harita ve belge tekrar sınırı

1. **Her benzersiz `G` varlığının hook + gövde + kapanış toplamında kullanım hakkı bir defadır.** Aynı `G` ekrandan çıktıktan sonra videonun ilerleyen bir noktasında yeniden gösterilemez; ikinci kullanım için anlatısal, kanıtsal veya estetik istisna yoktur.
2. Aynı `G` varlığını kırpmak, yakınlaştırmak, yeniden renklendirmek, metnini yeniden yerleştirmek, farklı motion uygulamak, farklı çözünürlükte dışa aktarmak veya yeni bir `G` koduyla yeniden üretmek yeni varlık oluşturmaz.
3. **Görsel eşdeğerlik testi:** iki `G` varlığını başlık/metinlerinden bağımsız değerlendir. Ana özne, veri/harita düzeni, mekanizma, nesne ilişkisi, gösterilen işlem aşaması ve izleyicinin öğrendiği görsel sonuç bakımından “İzleyici burada önce görmediği hangi yeni bilgiyi görüyor?” sorusuna somut cevap yoksa bunlar aynı/eşdeğer grafik kabul edilir ve yalnızca biri kullanılabilir.
4. Aynı özne veya veri ailesi yeniden gösterilebilir ancak yeni `G`; önceki grafiğin varyasyonu değil, açıkça yeni bir mekanizma, işlem aşaması, karşılaştırma, ölçülebilir fark, rota, belge ayrıntısı veya sonuç göstermelidir. Yalnızca farklı VO, farklı chapter, farklı metin, farklı renk veya farklı kompozisyon yeni görsel bilgi sayılmaz.
5. Tek bir `G` varlığının kendi içinde aşamalı motion, durum değişimi veya A→B→C açıklaması bulunabilir. Grafik ekrandan hiç çıkmadan kesintisiz ilerliyorsa bu tek kullanım sayılır; motion içindeki aşamalar ayrı kullanım değildir.
6. Aynı veya görsel olarak eşdeğer `G` ikinci kez gerekiyormuş gibi görünüyorsa önce yeni bilgi taşıyan farklı bir görsel çözüm hazırlanır. Yeni bilgi yoksa ikinci grafik oluşturulmaz; VO sadeleştirilir, gerçek V/P/belge kullanılır veya ilgili anlatım kısaltılır.
7. F’deki grafik içerik fişi ve H’deki `Reuse / distinction note`, benzer `G` varlıklarının neden gerçekten farklı olduğunu somut görsel bilgi üzerinden açıklamalıdır. Fark doğrulanamıyorsa ikinci `G` seçilemez ve `PASS` verilemez.

### 10.5. Görsel yetersizliğinde hard stop

1. Yeterli benzersiz varlık yoksa araştırmaya devam edilir.
2. Aynı fotoğraf, video kesiti, `G` grafiği/haritası/belgesi veya bunların görsel olarak eşdeğer sürümü döndürülerek herhangi bir hedef süre doldurulamaz.
3. Güvenli görseli bulunamayan önemsiz anlatım kısaltılır veya çıkarılır.
4. Ana tezi taşıyan bölüm görsel olarak desteklenemiyorsa anlatım açısı değiştirilir.
5. Konu prompt/profil hedefini anlamlı ve doğru biçimde desteklemiyorsa dolgu yapılmaz; açı daraltılır veya gerekçeli daha kısa süre seçilir. Evrensel 15/20 dakika varsayımı yoktur.
6. Tekrar auditinde tek bir `FAIL` varsa paket teslime hazır değildir.

**Araştırmayı sürdürme kuralı:** Bir video adayının dosyasına erişilememesi, oynatıcısının açılmaması veya seçilen kesitin henüz doğrulanamaması tek başına araştırmayı bitirme ya da `TOPIC NOT VISUALLY VIABLE` kararı verme nedeni değildir. Önce aynı varlığın hak durumu doğrulanabilir erişilebilir özgün dosyasını veya aynı anlatım işlevini karşılayan başka uygun kaynakları araştır; erişilebilir videoları incele. Bu sırada bağımsız ilerleyebilen iddia doğrulamasını ve doğru fotoğraf/belge/grafik araştırmasını sürdür. Görsel bulunursa ilgili bölümü yeniden kur veya gerekçeli biçimde kısalt. Erişim engelini kesin zaman kodu uydurarak, doğrulanmamış adayı `V` sayarak veya tekrar kurallarını esneterek aşma. Alternatif kaynak ve anlatım yolları somut olarak denendiği hâlde ana soru desteklenemiyorsa ancak o zaman eksikliği belirt; incelenen adayları, her biri için erişim/doğrulama engelini, denenen alternatifleri, tamamlanan bağımsız çalışmayı ve kalan işleri açıkça kaydet. Tek kaynak hatası veya kısa bir ilk arama, görevi tek paragraflık `yapamıyorum` sonucuyla kapatmaz.

## 11. Birebir seslendirme metni

1. İngilizce seslendirme metni tamamen yazılmalıdır.
2. Kurgu tablosundaki `Exact voice-over` sütunu kaydedilecek son metindir.
3. Metin daha sonra VO dosyalarına ayrılmış hâlde ikinci kez verilmelidir.
4. Kurgu tablosundaki cümlelerle VO kayıt bölümündeki cümleler birebir aynı olmalıdır.
5. İngilizce doğal, konuşulur ve uluslararası izleyici için anlaşılır olmalıdır.
6. Metin akademik makale veya doğrudan çeviri gibi duyulmamalıdır.
7. Ton yavaş olabilir fakat cümleler gereksiz uzun ve dolambaçlı olmamalıdır.
8. Her cümle ayrılan zaman içinde doğal biçimde okunabilecek uzunlukta olmalıdır.
9. Toplam kelime sayısı ve gerçek hedef konuşma hızı hesaplanmalıdır.
10. Arşiv sesi veya bilinçli sessiz anlar varsa kelime hedefi buna göre azaltılmalıdır.
11. Yer, kurum, kişi, ürün, model, araç, sistem ve diğer özel adların doğru yazımı korunmalıdır.
12. Gerekli isimler için kısa telaffuz notu eklenmelidir.
13. Aynı iddia farklı chapter’larda yeniden açıklanmamalıdır. Yeni karşılaştırma veya sonucun anlaşılması için kısa hatırlatma yapılabilir; yeni işlevi açık olmalıdır.
14. Yalnızca süreyi uzatmak için genel tarih, tekrar veya önemsiz isim eklenmemelidir.
15. Metin yazıldıktan sonra `spoken-language pass` yapılmalıdır: yüksek sesle doğal okunmayan, tek nefeste bitmeyen, çeviri kokan veya art arda benzer ritim taşıyan cümleler yeniden yazılmalıdır.
16. İlk taslak hedef sürenin üzerindeyse önce zayıf bağlam, tekrar, isim ve tarih listeleri kesilir; anlatım hızı artırılarak metin sıkıştırılmaz.
17. Her 45–90 saniyelik anlatı bloğunda yalnızca bir ana takeaway bulunmalıdır. Aynı blokta birden fazla teknik mekanizma zorunluysa görsel veya grafikle bölünmelidir.
18. **2.0 saniyeye kadar olan kısa duraklamalar ve ton etiketleri** Bölüm I’deki ElevenLabs v4 kurallarıyla `Recording text` içine köşeli parantezli etiket olarak yazılır ve karşılık gelen `Exact voice-over` metniyle birebir eşleşir. **2.0 saniyeden uzun** görsel nefesler ile doğal/arşiv sesi alanları konuşulacak metin veya kısa duraklama etiketi sayılmaz; ilgili kurgu hücresinde zamanlanır.
19. Seslendirme, izleyicinin sektörü önceden bildiğini varsaymamalıdır. Teknik veya kurumsal terim yalnızca ana hikâye için zorunluysa kullanılmalı ve gündelik İngilizceyle hemen açıklanmalıdır.
20. Doğal soru cümleleri bölüm geçişlerinde kullanılabilir; ancak arka arkaya soru sorulup cevap geciktirilemez. Her soru sonrasında izleyiciye yeni kanıt veya kısmi cevap verilmelidir.
21. “There were many reasons”, “things began to change” ve “the rest is history” gibi belirsiz geçişler yerine somut aktör, karar veya mekanizma yazılmalıdır.

## 12. Zorunlu çıktı formatı

Yeni video paketi aşağıdaki başlıkları aynı sırada içermelidir.

### A. Production target

Bu bölümün alanları master tarafından doldurulmaz; konu promptu ve kanal profilinden çözülen değerler burada kayıt altına alınır. Master yalnızca bütün alanların eksiksiz ve paket boyunca tutarlı olmasını zorunlu kılar.

- Channel
- Working title
- Format and resolution
- Target duration
- Estimated word count
- Language
- Target audience
- Narration style
- Delivery speed
- Music approach
- Visual approach
- Target moving-footage ratio
- Geographic focus
- Historical period

### B. Editorial premise and title accuracy

- Videonun açılışta kuracağı ana soru
- Araştırmanın ulaştığı kısa cevap
- İzleyicinin videodan alacağı temel fikir
- Kullanılan konu yapısı
- Başlığın kelimesi kelimesine doğru olup olmadığı
- Gerekli niteleme veya açıklama
- Kaçınılacak basit/yanıltıcı açıklamalar
- Günümüz bağlantısı

### C. Narrative architecture and retention plan

Chapter omurgası, hook/payoff zamanlaması ve retention karakteri ilgili kanal profilinden alınır. Bu tablo, o yaratıcı yapıyı kesin timeline ve kanıt/görsel planına dönüştürür.

| Chapter | Timeline target | Core question  | Main evidence / event | Retention reset           | Visual character |
| ------- | --------------- | -------------- | --------------------- | ------------------------- | ---------------- |
| 1       | 0:00–1:30       | Bölümün sorusu | Ana kanıt             | Yeni soru veya güçlü sayı | Hareketli arşiv  |

Kurallar:

- Chapter sayısı süreyi doldurmak için belirlenmez. Çoğu orta uzunluktaki videoda **4–8 anlamlı chapter** yeterlidir; kısa ve tek kırılmalı hikâyelerde daha azı kullanılabilir.
- Chapter süreleri konu/profil gereğine göre seçilir; hook ve kapanış kısa olabilir. Bölüm, anlamlı bir nedensel aşama bittiğinde sona erer. İlerleme kontrolü Bölüm 7.1’e göre uygulanır; yeni bilgi kotası değildir.
- Her chapter yeni bir soruya veya nedensel aşamaya geçmelidir.
- `Retention reset` hücresi gerçek içeriği belirtmeli; “keep it interesting” gibi belirsiz ifade kullanılamaz.
- Zaman hedefleri final kurgu haritasıyla uyumlu hâle getirilmelidir.
- İlk chapter’ın `Retention reset` hücresinde özne/vaat, ilk somut cevap ve hook sonrası mekanizma/olay geçişi, Bölüm 7.6’dan çözülen kesin zamanlarla yazılır. Her hook’a ayrıca paradoks veya ters köşe eklenmez.
- Chapter’lar kronolojik başlıklardan ibaret olmamalı; her `Core question` önceki bölümden daha ileri bir nedensel soruya geçmelidir.
- Aynı neden farklı chapter’larda tekrarlanıyorsa birleştirilmeli veya ikinci kullanım yeni kanıtla görüşü anlamlı biçimde değiştirmelidir.

### D. Claim ledger

| Claim ID | Planned claim | Importance | Primary / institutional support | Independent support | Caveat or wording limit | Status |
| -------- | ------------- | ---------- | ------------------------------- | ------------------- | ----------------------- | ------ |

Ana tezi, thumbnail sayısını ve bölüm dönüm noktalarını taşıyan iddialar zorunlu olarak listelenmelidir.

### E. Non-negotiable edit rules

Bu videoya özel çözülmüş kurallar kısa biçimde listelenmelidir. Yaratıcı değerler kanal profili/prompttan, teknik bütünlük değerleri bu master’dan alınır; çelişen iki ayrı değer birlikte yazılamaz.

Aşağıdaki değerler paketin kendi E bölümünde yeniden yazılmalıdır:

- Hook’un kesin başlangıç ve bitiş aralığı
- Hedef hareketli görüntü / özgün grafik / fotoğraf-belge oranı
- Hook’taki görsel karışım, minimum plan sayısı ve gerekiyorsa kaynak çeşitliliği; 0:00–0:40 ile hook birleşiminde sıfır sabit görsel, en az %70 gerçek V, en fazla iki motion G gösterimi ve G başına en fazla 6 saniye
- Hook’ta aynı orijinal videodan en fazla iki farklı kesit; yalnızca açık kullanıcı istisnası varsa o değer
- Fotoğraf planlarının normal ve istisnai maksimum süreleri
- Fotoğraf + sabit G + belge + haritanın birlikte sayıldığı statik sekans için normal 10 saniye / maksimum 15 saniye sınırı; uygun anlamlı video araştırılmasına rağmen bulunamadıysa kullanılan son çare istisnasının kesin süresi ve gerekçesi
- Hook dışındaki fotoğrafların varsayılan bir, zorunlu durumda en fazla iki kullanım sınırı
- Aynı orijinal videodan en fazla iki farklı kesit sınırının yalnızca Hook için geçerli olduğu; Hook dışında çakışmayan ve görünür yeni içerik taşıyan kesit sayısının sınırlı olmadığı
- Aynı, çakışan veya görsel olarak eşdeğer video kesitinin hook + gövde + kapanış toplamında yalnızca bir kullanım sınırı
- Her benzersiz `G` grafiği/haritası/belgesinin hook + gövde + kapanış toplamında yalnızca bir kesintisiz kullanım sınırı; ekrandan çıktıktan sonra ikinci gösterim yasaktır
- Kırpma, zoom, yeniden renklendirme, metin/motion değişikliği veya yeni `G` kodunun tekrar sayacını sıfırlamadığı; görsel olarak eşdeğer `G` varlıklarının birlikte denetlendiği
- Yalnızca fotoğraftaki izinli ikinci kullanım için en az 90 saniye, en az sekiz farklı ara plan ve farklı chapter koşulu
- Tekrar edilen fotoğraf için 18 saniye toplam non-hook süre sınırı; video kesitinde ikinci kullanım ve eski 24 saniyelik tekrar istisnasının kaldırılmış olduğu
- Üçüncü kullanımın, bitişik tekrarın ve `A–B–A` tekrarının yasak olduğu
- Videoların doğal hızında kullanılacağı; yavaşlatma, freeze-frame, optical flow, frame interpolation veya kare tekrarıyla uzatmanın yasak olduğu
- Template’in bölüm, tablo, sütun, satır türü ve edit map yapısına hiçbir ekleme veya çıkarma yapılamayacağı
- Profil/prompttan alınan ilk somut payoff zamanı ve retention bridge aralığı
- Bu videoda gerçekten kullanılacak bilinçli nefes anları varsa yaklaşık yerleri ve toplam süresi; sayısal kota yoktur, güçlü varlık yoksa `No forced breathing moments` yazılması
- Nefes anlarının yalnızca güçlü görüntü, grafik okuma veya anlamlı arşiv sesi için kullanılacağı; her cümle sonuna dağıtılmayacağı
- Profilde tanımlanan hook işlevleri, çözülmüş hook kelime hedefi ve WPM aralığı

Bu maddeler template’e atıfla geçilemez; pakette görünür olmalıdır.

### F. Asset library

Üç ayrı tablo hazırlanmalıdır.

#### Moving footage

| Code | Footage                 | Relevant source time     | Date / context | Footage type       | Licence / attribution | Source     |
| ---- | ----------------------- | ------------------------ | -------------- | ------------------ | --------------------- | ---------- |
| V01  | Açık görüntü açıklaması | 04:12–04:26; 09:10–09:28 | Exact context  | Archive / context  | Exact licence         | Direct URL |

#### Still photographs

| Code | Photograph               | Date / context | Visual family        | Licence / attribution | Source     |
| ---- | ------------------------ | -------------- | -------------------- | --------------------- | ---------- |
| P01  | Açık fotoğraf açıklaması | Exact date     | Related-photo set    | Exact licence         | Direct URL |

#### Maps, documents and data graphics

| Code | Required content | Date / data period | Direct data / document source | Licence / attribution |
| ---- | ---------------- | ------------------ | ----------------------------- | --------------------- |
| G01  | Açık ve kısa bilgi/görsel açıklaması | Exact period | Direct research URL | Data or document citation |

Bu başlıktaki `G` varlıkları yalnızca veri grafikleriyle sınırlı değildir. Harita, belge, zaman çizelgesi ve sayısal karşılaştırmalara ek olarak; bir mekanizmayı açıklayan şema, fiziksel ilişkiyi gösteren teknik görsel, bir süreci aşamalara ayıran açıklayıcı görsel veya kaynaklarla desteklenen bir anı gözde canlandıran temsili sahne de `G` kodu alabilir.

Bu tablo yalnızca `G` envanterinin kısa özetidir. Kullanıcı tarafından üretilecek her `G` varlığı için tablonun hemen ardından ayrı bir **grafik içerik fişi** hazırlanmalıdır. Fiş, görseli hazırlayacak kişinin yeniden araştırma yapmasına gerek bırakmadan hangi doğru bilgilerin, verilerin, kaynakların, birebir ekran metinlerinin ve — istatistik dışı görsellerde — hangi kişi, araç, nesne, çevre, eylem ve fiziksel ilişkilerin görünmesi gerektiğini vermelidir.

Grafik fişlerinde renk, palet, font, tipografi, estetik stil, doku, efekt, ikon dili, animasyon veya geçiş gibi **sanat yönetimi** talimatları yazılmamalıdır. Buna karşılık içeriğin doğru kurulması için gereken sahne kompozisyonu ve ilişkiler — örneğin öznenin nerede durduğu, aracın hangi parçasının açık olduğu, iki kişinin ne yaptığı, arka planda hangi yapının bulunduğu veya hangi nesnelerin aynı karede görünmesi gerektiği — açık ve ayrıntılı biçimde yazılmalıdır. Buradaki amaç tasarım stili belirlemek değil, görselin anlatacağı olayı ve doğrulanabilir içeriği kesinleştirmektir.

Grafiğin yaratıcı yoğunluğu, görsel ailesi ve kanal estetiği ilgili profilden gelir. Ancak bu içerik fişi yalnızca doğrulanabilir üretim içeriğini taşır; profilin sanat yönünü tekrar ederek ikinci bir tasarım promptuna dönüşmez.

##### Her `G` varlığı için zorunlu içerik

1. **Kimlik ve kurgu eşleşmesi**
   - Grafik kodu ve kısa İngilizce adı
   - Exact voice-over and edit map içindeki kesin kullanım zamanı
   - Eşleştiği chapter ve voice file
   - Grafiğin eşlik ettiği birebir İngilizce VO cümlesi veya cümleleri
   - Ekranda kalacağı kesin süre
   - İlgili Claim ID

2. **Verilecek bilgi ve birebir ekran metni**
   - İzleyicinin bu varlıktan öğrenmesi gereken ana sonuç bir cümleyle yazılmalı ve `production note only — do not place on screen` olarak işaretlenmelidir.
   - Varsayılan ekran metni en fazla bir kısa ana başlık ve bir kısa açıklamadır. Ana başlık çoğunlukla 2–7, açıklama çoğunlukla 6–16 kelime olmalı; zorunlu değillerse kullanılmamalıdır.
   - Tarih/yıl, ad, kategori, veri etiketi, düğüm, ok ilişkisi, legend ve kaynak dipnotu yalnızca doğru okuma için gerekiyorsa **İngilizce ve birebir** verilmelidir. İstatistik ayrıntıları eksiksiz üretim verisi olarak yazılmalı; ekranda ise mümkün olduğunca grafik, eksen, ölçek, konum, çizgi, şekil ve kısa veri etiketleriyle anlatılmalıdır.
   - İkinci başlık, birden fazla bölüm etiketi veya ek açıklama yalnızca karşılaştırma tarafları, timeline evreleri, harita durumları/rotaları ya da belge içindeki zorunlu ayrımlar birbirinden ayrılamıyorsa kullanılabilir. Her ek metnin neden zorunlu olduğu production note içinde açıklanmalıdır.
   - Haritada gösterilmesi gereken ülke, şehir, tesis, rota, sınır, konum, işaretçi ve tarih tek tek belirtilmelidir.
   - Belge kullanılacaksa belgenin tam adı, tarihi, sayfası, alınacak bölüm ve gerekiyorsa vurgulanacak kısa kelime/cümle belirtilmelidir. Uzun telifli metinler ekrana taşınmamalıdır.
   - VO cümleleri, main takeaway, ayrıntılı açıklamalar, kaynak dokümantasyonu ve üretim talimatları ekrana taşınmamalıdır. Ekranda gösterileceği açıkça yazılmayan bütün açıklamalar `production note only — do not place on screen` kabul edilmelidir.

3. **Ayrıntılı görsel içerik tarifi**
   - Her `G` varlığı `data graphic`, `map`, `document`, `timeline`, `explanatory diagram`, `technical visualization` veya `illustrative reconstruction` türlerinden uygun olanıyla işaretlenmelidir.
   - İstatistik dışı bir görselde sahnenin neyi açıkladığı ve izleyicinin tek bakışta ne anlaması gerektiği yazılmalıdır.
   - Görünmesi zorunlu kişi, araç, ürün, nesne, yapı, belge, çevre ve arka plan öğeleri tek tek belirtilmelidir.
   - Öznenin konumu, yönü, eylemi, duruşu; nesnelerin açık/kapalı, dolu/boş, hasarlı/sağlam veya hareketli/durağan durumu; kişiler ve nesneler arasındaki mekânsal ya da nedensel ilişki açıkça tarif edilmelidir.
   - Doğrulanabilen dönem, yer, model, kıyafet, işaret, hava/ışık koşulu veya çevresel ayrıntılar belirtilmeli; doğrulanamayan ayrıntılar zorunluymuş gibi yazılmamalıdır.
   - Görsel gerçek bir tarihsel ana ait fotoğraf değilse `illustrative reconstruction — not archival evidence` ifadesi production note olarak eklenmelidir.
   - Yanlış çağrışım yaratabilecek kişi, logo, model, üniforma, bina, coğrafya, tarih veya olay ayrıntıları `must not show` altında açıkça yasaklanmalıdır.

4. **Kesin veri tablosu**
   - Veri kullanılan her `G` varlığında gösterilecek değerler dosyanın içinde tablo hâlinde verilmelidir.
   - Her satırda en az `year/category`, `exact source value`, `display value`, `unit`, `scope`, `series definition` ve `source reference` bulunmalıdır.
   - Birbirinden farklı ölçüler, kapsamlar ve dönem tanımları karıştırılmamalıdır.
   - Değer hesaplanmışsa formül ve ham değerler; yuvarlanmışsa kaynak değeri ile ekranda gösterilecek değer birlikte yazılmalıdır.
   - Farklı kaynaklardan seri birleştiriliyorsa yöntem veya kapsam kırılması açıkça işaretlenmelidir.
   - Görsel bir veri iddiası taşıyorsa kesin veri bulunamadığında tahmin uydurulmamalı; ilgili veri gösterimi kaldırılmalı veya yalnızca kaynakların desteklediği bilgilerle sınırlandırılmalıdır.
   - Bu tablo grafik üreticisi için eksiksiz ve doğrulanabilir üretim girdisidir. Tablo satırları, formüller, kapsam açıklamaları ve kaynak referansları ekrana metin bloğu olarak kopyalanamaz; değerler uygun grafik türü ve minimum zorunlu etiketlerle görselleştirilmelidir.

   - Sayısal veri kullanılmayan açıklayıcı veya temsili `G` varlığında tablo uydurulmamalı; şablondaki alan `Not applicable — non-data explanatory/illustrative graphic` olarak doldurulmalıdır.

5. **Kaynak paketi**
   - Yalnızca kurum veya kaynak kategorisi yazmak yasaktır.
   - Her veri, ilişki, harita bilgisi veya belge için doğrudan açılan kaynak bağlantısı verilmelidir.
   - Her kaynakta belgenin/veri setinin tam adı, yayıncı veya kurum, yayın tarihi, doğrudan URL, ilgili sayfa/tablo/figure/section ve erişim tarihi yazılmalıdır.
   - PDF için PDF sayfası ve mümkünse basılı sayfa numarası; veri dosyası için sheet/tablo/seri kodu ve filtreler belirtilmelidir.
   - Kaynağın hangi değeri, metni veya ilişkiyi desteklediği bir cümleyle açıklanmalıdır.
   - Ana sonucu taşıyan bilgi mümkün olduğunda ikinci güvenilir kaynakla çapraz kontrol edilmelidir.
   - Belge, harita tabanı, logo veya fotoğraf görselin içinde doğrudan kullanılacaksa lisans, hak sahibi ve gerekli atıf ayrıca belirtilmelidir.

6. **Doğruluk sınırı**
   - Kaynakların desteklemediği sonuçlar açıkça yazılmalıdır.
   - Konuya özgü ölçüm, kapsam, tarih, ad, mülkiyet, konum veya nedensellik karışıklığı riskleri belirtilmelidir.
   - Eksik veri, tartışmalı sayı veya belirsiz ilişki kesin gerçek gibi sunulmamalıdır.
   - Kaynakta bulunmayan sayı, etiket, logo, belge, ilişki veya veri noktası uydurulmamalıdır.

7. **Teslim ve eşleşme**
   - Çıkış dosyasının kesin adı yazılmalıdır: `G01.jpg`.
   - Varsayılan çıktı 1920×1080, 16:9’dur.
   - Son görselde kullanılan her sayı, tarih, isim, ilişki ve kaynak satırı içerik fişiyle karşılaştırılmalıdır.
   - Grafik kodu, asset library özeti ve Exact voice-over and edit map kullanımı birebir eşleşmelidir.

##### Zorunlu yazım şablonu

```markdown
##### G01 — [Exact English graphic name]

- **Timeline / chapter / voice file:**
- **Exact matching VO:** “...”
- **Screen duration:**
- **Claim ID:**
- **Output:** `G01.jpg` — 1920×1080

**Required information and exact on-screen text**
- Main takeaway — production note only; do not place on screen:
- Primary title — optional; normally 2–7 words; maximum one:
- Short explanation — optional; normally 6–16 words; maximum one:
- Additional heading / section labels — exceptional only; state why each is necessary:
- Required dates / names / data labels / axes / units / nodes / legend — minimum needed for correct reading:
- Exact source footer — only if needed; otherwise `Not needed`:
- Production notes not shown on screen:

**Detailed visual content specification**
- Graphic type:
- Visual purpose / what the viewer must understand:
- Exact scene or explanatory content:
- Required people / vehicles / objects / environment:
- Required actions, positions, object states and relationships:
- Verified period / location / model details:
- Must not show / uncertainty limits:
- Reconstruction disclosure, if required:

**Exact data to use**
| Year / category | Exact source value | Display value | Unit, scope and series definition | Source ref |
| --------------- | -----------------: | ------------: | --------------------------------- | ---------- |

The table above is production input, not an on-screen text layout. Visualize the values through an appropriate chart, scale, position, line, shape or concise direct label; do not reproduce the table, formulas or source documentation as paragraphs or bullet lists on screen.

If no numerical data is used: `Not applicable — non-data explanatory/illustrative graphic.`

**Reference documents or assets actually used**
| Item | Direct file/page URL | Licence / owner | Information taken from it |
| ---- | -------------------- | --------------- | ------------------------- |

**Full source documentation**
1. Full document title — publisher — date  
   Direct URL:  
   Relevant page/table/section:  
   Supports:  
   Accessed:

**Accuracy notes / unsupported claims**
- ...

**Final QA**
- [ ] Every number, date, name and relationship matches the cited source
- [ ] Every required English on-screen text is written exactly
- [ ] Default text budget is respected: no more than one short primary title and one short explanation unless a documented exception is necessary
- [ ] Exact VO, main takeaway, production notes, full source documentation and detailed scene instructions are not rendered on screen
- [ ] Statistical detail is encoded visually rather than copied as prose, bullets or a table dump
- [ ] Non-data graphic, if used, has a complete scene/content specification
- [ ] Any illustrative reconstruction is clearly identified and does not imitate archival evidence
- [ ] Code and timeline use match the edit map
- [ ] No invented logo, document, relationship or data point
```

##### Grafik bölümü teslim kapısı

- [ ] Asset library özet tablosundaki her `G` kodunun içerik fişi var
- [ ] Edit haritasında kullanılan her `G` kodu aynı içerik ve aynı amaçla tanımlanmış
- [ ] Her veri noktası dosya içinde açıkça yazılmış; grafik üreticisinin linklerden sayı çıkarması gerekmiyor
- [ ] Her chapter için gerçek V/P/belge adayları değerlendirildi; G yalnızca bunların açıklayamadığı bilgi için seçildi, chapter başına G kotası yok
- [ ] İstatistik dışı her `G` fişinde kişi, araç, nesne, çevre, eylem, konum, fiziksel durum ve ilişkiler üretime yetecek ayrıntıda tarif edildi
- [ ] Temsili canlandırmalar gerçek arşiv kanıtı gibi sunulmadı ve doğrulanmamış ayrıntılar uydurulmadı
- [ ] Kurum adı yerine doğrudan belge/veri bağlantıları, sayfa ve tablo numaraları verilmiş
- [ ] Ekranda gösterilecek bütün İngilizce metinler birebir hazırlanmış
- [ ] Varsayılan bir kısa başlık + bir kısa açıklama sınırı uygulanmış; ek başlık/etiket/açıklamaların her biri zorunlu bir karşılaştırma, timeline, harita veya belge işleviyle gerekçelendirilmiş
- [ ] Exact VO, main takeaway, production note, ayrıntılı sahne tarifi ve tam kaynak dokümantasyonu ekrana taşınmamış
- [ ] İstatistik ayrıntıları metin yığını veya tablo kopyası olarak değil, uygun grafik ve minimum zorunlu veri etiketleriyle görselleştirilmiş
- [ ] Metin ana özneyi/veriyi küçültmüyor; grafik modern, yüksek kaliteli, okunabilir ve açıklayıcı işlevini koruyacak ölçüde görsel olarak güçlü
- [ ] Kaynak dipnotu gerekiyorsa birebir yazılmış
- [ ] Yanıltıcı kapsam karışıklığı veya kanıtsız neden-sonuç ilişkisi yok
- [ ] G01–Gxx dosya adları, asset library ve edit map arasında kod uyumsuzluğu yok
- [ ] Renk, font, estetik stil, doku, efekt, ikon dili, animasyon veya geçiş promptu eklenmemiş; yalnızca doğru içeriği kurmak için gereken sahne ilişkileri tarif edilmiş

Bu kapıdaki maddelerden biri sağlanmıyorsa grafik bölümü tamamlanmış kabul edilmez ve paket `eksiksiz` olarak teslim edilemez.

Kodlar sıralı olmalıdır:

- Video: `V01`, `V02`, `V03`
- Fotoğraf: `P01`, `P02`, `P03`
- Harita, belge ve grafik: `G01`, `G02`, `G03`

#### Varlık kodlarının tekilliği

- Her benzersiz video dosyasına yalnızca bir `V` kodu verilir.
- Aynı videonun bütün kullanılan zaman aralıkları aynı kod altında listelenir.
- Aynı video kaynağının farklı kesitleri kurgu tablosunda aynı kod ve farklı kesin zamanlarla yazılır.
- Hook satırlarında aynı `V` kodu altında en fazla iki farklı kaynak zaman aralığı bulunabilir. Hook dışındaki satırlarda aynı `V` kodu için hem çakışmayan hem görünür yeni içerik gösteren aralıkların sayısı sınırlı değildir; görsel eşdeğer aralıklar farklı kesit sayılamaz.
- Aynı orijinal videonun farklı çözünürlük, kırpma veya yeniden kodlanmış kopyası yeni kod alamaz.
- Her benzersiz fotoğraf yalnızca bir `P` kodu alır.
- Aynı fotoğrafın restore edilmiş, kırpılmış, renklendirilmiş veya başka sitedeki kopyası yeni kod alamaz.
- Çok benzer seri kareler aynı `visual family` ile işaretlenir.
- Kullanıcı tarafından üretilecek grafik ve haritalar `G` kodu alır; veri kaynakları ayrıca yazılır.
- Her benzersiz `G` varlığı yalnızca bir `G` kodu alır. Aynı grafiğin kırpılmış, yakınlaştırılmış, yeniden renklendirilmiş, farklı metin/motion uygulanmış veya farklı çözünürlükteki sürümü yeni kod alamaz.
- Farklı `G` kodları ancak izleyiciye somut olarak yeni mekanizma, işlem aşaması, karşılaştırma, veri ilişkisi, rota, belge ayrıntısı veya sonuç gösteriyorsa ayrı varlık sayılır; görsel olarak eşdeğer `G` varlıkları ayrı kodlarla tekrar kullanılamaz.
- Asset library’de bulunmayan kod kurgu tablosunda kullanılamaz.

### G. Exact voice-over and edit map

| Time      | Chapter | Voice file | Exact voice-over                     | Picture and edit instruction | Claim ID |
| --------- | ------- | ---------- | ------------------------------------ | ---------------------------- | -------- |
| 0:00–0:08 | Hook    | VO01       | Kaydedilecek birebir İngilizce metin | V01 — 04:12–04:20            | C01      |

Bu tablonun altı sütunu, sütun sırası ve satır içeriği formatı değiştirilemez. Ek sütun, alternatif edit map, tablo dışı kurgu satırı veya hücre içinde template’in istemediği yeni veri alanı eklenemez. Konuya özel prompt veya template kesin satır sayısı veriyorsa edit map tam olarak o sayıda veri satırına sahip olmalıdır. Kesin sayı verilmemişse her gerçek ana plan için bir satır yazılır; satır sayısı yalnızca boşluksuz final timeline tarafından belirlenir.

#### Picture and edit instruction yazım kuralı

- Hücre doğrudan varlık koduyla başlamalıdır.
- Koddan sonra `—` işareti gelmelidir.
- Video için kesin kaynak zamanı yazılmalıdır: `V03 — 12:44–12:57`.
- Video kesitinin timeline süresi, kaynak zaman aralığının doğal hızdaki süresiyle aynı olmalıdır; kesit yavaşlatılarak, dondurularak veya kare tekrarıyla satıra uydurulamaz.
- Fotoğraf için gösterim süresi ve odak yazılmalıdır: `P07 — 12 seconds; exact relevant subject/detail visible`.
- `G` varlığı için ekran süresi ve gösterilecek içerik yazılmalıdır: `G02 — 10 seconds; show the source-backed values and exact labels listed in G02`.
- Ekran yazısı varsa birebir metni verilmelidir.
- `Use archive video`, `similar image`, `war footage`, `factory footage` veya `retro technology footage` gibi belirsiz ifadeler yasaktır.
- Her satır tek bir ana görsel planını temsil etmelidir.
- Zaman çizelgesi 0:00’dan sona kadar boşluk veya çakışma olmadan ilerlemelidir.
- Görüntü bağlamsalsa hücrede açıkça yazılmalıdır.
- Yalnızca izinli ikinci non-hook fotoğraf kullanımında `FORCED REUSE 2/2 — reason: ...` bulunmalıdır. Video kesitinde ve `G` varlığında ikinci kullanım yasaktır. Aynı `G` kesintisiz biçimde birden fazla teknik VO satırına yayılıyorsa bu tek kullanım sayılır; ekrandan çıktıktan sonra aynı veya görsel olarak eşdeğer `G` geri getirilemez.
- Ana iddia taşıyan satır ilgili `Claim ID` ile eşleştirilmelidir.
- Sadece atmosfer sağlayan satırlarda Claim ID `N/A` olabilir.
- `Recording text` içinde kullanılan her ElevenLabs v4 köşeli parantezli etiket (ton veya `[short pause]`/`[pause]`/`[long pause]`) karşılık gelen `Exact voice-over` hücresinde de aynı yerde birebir bulunmalıdır; rough-cut aracı hizalamada bu etiketleri yok sayar. `2.0s` değerini aşan görsel nefesler ile doğal/arşiv sesi alanları etikete çevrilmez; kurgu hücresinde kesin timeline zamanlarıyla `NARRATION ENDS AT 06:14; NATURAL SOUND / VISUAL HOLD UNTIL 06:18` biçiminde yazılır.
- Doğal arşiv sesi korunuyorsa `PRESERVE SOURCE AUDIO [source start–end]; NO MUSIC; NO VO` ifadesi ve kesin aralık yazılmalıdır.
- Bir mini-sekans ardışık planlardan oluşuyorsa her plan ayrı satırda kalmalı; hücre sonunda aynı `SEQUENCE A/B/C...` kimliğiyle işaretlenmelidir.
- Hook G için `MOTION GRAPHIC REQUIRED` ve zamanlı içerik hareketi bu hücrede yazılır; F içerik fişine animasyon promptu eklenmez. Örnek: `G02 — 5 seconds; MOTION GRAPHIC REQUIRED; 0–3s show the existing object moving along the verified route; 3–5s continue the verified action to its outcome; keep existing text continuously visible; do not add objects`. Hareket yalnızca kaynaklı içeriği açıklamalıdır.
- Tek JPG teslimi hareketli grafik teslimi değildir. Paket G01.jpg temel görselini tarif edebilir; gerçek animasyonun üretilmesi ve kontrolü ayrıca gerekir. Bu gerçekleşmediyse “motion rendered/verified” yazılamaz.
- Kesin sayılar, eksenler, metinler, rota ve fiziksel ilişkiler animasyon boyunca korunmalıdır. Mevcut yazı kaybolup yeniden beliremez; okunurluğu bozan harf hareketi veya fade uygulanmaz. Dekoratif ışıma tek başına anlamlı motion sayılmaz.
- Konuşmasız satırda `Exact voice-over` boş bırakılır; sessizlik açıklaması yalnızca kurgu hücresindedir. Bir cümle görsel kesmeyi aşıyorsa kelimeler ilgili satırlara bölünebilir; yeni cümle veya duraklama eklenmez. I’de birleştirildiğinde birebir metin elde edilmelidir.

#### Kesintisiz video devamlılığı

- Aynı video görüntüsü ardışık satırlarda kesintisiz ilerliyorsa tek bir sürekli blok olarak planlanmalıdır.
- Her satırda kesin kaynak başlangıç ve bitiş zamanı yazılmalıdır.
- Sonraki kaynak başlangıcı önceki kaynak bitişiyle birebir aynı olmalıdır.
- Zaman kodu elle yuvarlanmamalıdır.
- Gerekirse milisaniyeli zaman kodu kullanılmalıdır.
- Aynı blok bütün satırlarda aynı kimlikle işaretlenmelidir.
- Kesintisiz bloğun kaynak süresi timeline süresinden kısa olamaz. Görüntü doğal hızında yetmiyorsa blok kısaltılmalı veya başka bir video planına geçilmelidir; hız düşürülerek ya da son kare dondurularak uzatılamaz. Aynı kesintisiz görsel video bloğu, edit map’te birden fazla satıra veya VO cümlesine bölünmüş olsa bile toplamda **20 saniyeyi aşamaz**; süreyi sıfırlamak için yapay satır bölme kullanılamaz.

Doğru:

`V01 — 00:05.000–00:15.000; CONTINUOUS BLOCK A`  
`V01 — 00:15.000–00:25.000; CONTINUE BLOCK A`

Yanlış:

`V01 — 00:05–00:15`  
`V01 — 00:14–00:25; DEVAM`

- Kaynakta ileriye yapılan anlamlı atlama varsa mevcut `INTENTIONAL JUMP CUT` etiketiyle gerekçelendirilir; yeni plan yine görsel olarak farklı içerik taşımalıdır. `INTENTIONAL REPLAY` ve `INTENTIONAL OVERLAP` etiketleri bu sürümde video tekrarı için kullanılamaz; Bölüm 10.3 kesindir.
- Son kontrolde her sürekli blokta önceki kaynak bitişi ile sonraki kaynak başlangıcı eşit olmalıdır.

### H. Mandatory visual repetition audit

Hook kullanımları mevcut sütunlarda ayrı gösterilir. Videolarda kabul kontrolü `Hook uses + Non-hook uses` toplamına ve görsel eşdeğer kesitlerin toplam kullanımına göre yapılır; toplam en fazla birdir. Fotoğraflar kod başına, videolar kesin kaynak kesiti başına, `G` varlıkları kod başına listelenir. Görsel olarak eşdeğer video kesitleri ve `G` varlıkları farklı satırlarda veya farklı kodlarda kalsa da mevcut not hücresinde birbirleriyle ilişkilendirilir ve birlikte denetlenir. `G` için `Source range` alanı `N/A` yazılabilir.

| Asset / clip | Type       | Source range | Hook uses | Non-hook uses | Non-hook timeline ranges | Total non-hook time | Smallest gap | Reuse / distinction note | Status |
| ------------ | ---------- | ------------ | --------: | ------------: | ------------------------ | ------------------: | -----------: | ------------------------ | ------ |
| V01 clip A   | Video clip | 01:05–01:15  |         0 |             1 | 05:12–05:22              |                10 s |          N/A | Single use; visually distinct action verified | PASS   |

Audit kuralları:

1. Fotoğrafın non-hook kullanımı 2’yi aşarsa `FAIL`.
2. Aynı, çakışan veya görsel olarak eşdeğer video içeriğinin Hook uses + Non-hook uses toplamı 1’i aşarsa `FAIL`; farklı V kodları ve farklı zaman aralıkları birlikte kontrol edilir.
3. Aynı videodan alınan hem çakışmayan hem yeni görsel içerik taşıyan kesitler ayrı kesit olarak denetlenir. Aynı orijinal video kaynağı altında ikiden fazla farklı kesit bulunması yalnızca Hook içinde `FAIL` nedenidir; Hook dışındaki farklı ve çakışmayan kesitler için adet sınırı yoktur.
4. Aynı `G` kodunun Hook uses + Non-hook uses toplamı 1’i aşarsa `FAIL`. Tek kesintisiz gösterimin teknik olarak birden fazla edit-map satırına bölünmesi ayrı kullanım sayılmaz.
5. Farklı `G` kodları görsel olarak eşdeğerse ve izleyiciye somut yeni mekanizma, işlem aşaması, karşılaştırma, veri ilişkisi, rota, belge ayrıntısı veya sonuç göstermiyorsa ikinci ve sonraki eşdeğer `G` kullanımları `FAIL`.
6. Aynı `G` varlığının crop, zoom, renk, metin yerleşimi, motion, çözünürlük veya kod numarası değiştirilmiş sürümü yeni varlık sayılmaz; yeniden gösterimi `FAIL`.
7. Tekrar edilen fotoğraf 18 saniyeyi aşarsa `FAIL`.
8. Video kesitinin ikinci gösterimi süresinden bağımsız `FAIL`; 24 saniyelik eski tekrar izni uygulanmaz.
9. İzinli fotoğraf tekrarları arasındaki boşluk 90 saniyeden azsa `FAIL`.
10. Fotoğrafın ikinci kullanımı aynı chapter’daysa veya arada sekiz farklı plan yoksa `FAIL`.
11. Fotoğrafın ikinci kullanımında `FORCED REUSE 2/2` gerekçesi yoksa `FAIL`; bu etiket video veya `G` tekrarına izin vermez.
12. Bitişik veya `A–B–A` tekrar varsa `FAIL`; bu kontrol `G` varlıkları için de uygulanır.
13. Audit değerleri kurgu tablosundan hesaplanmalıdır.
14. Tek bir `FAIL` bulunan paket teslim edilemez.

### I. Voice recording files

| File                        | Timeline  | Chapter / purpose | Recording text          |
| --------------------------- | --------- | ----------------- | ----------------------- |
| `VO01_Hook_and_Promise.wav` | 0:00–1:30 | Hook              | Birebir İngilizce metin |

Kurallar:

- VO dosyası sayısı video süresine değil doğal chapter ve anlatı alt bölümlerine göre belirlenmelidir. Çoğu orta uzunluktaki videoda **5–10 ayrı VO dosyası** yeterlidir; sırf adet tamamlamak için dosya bölünmez.
- Dosyalar doğal chapter veya anlatı alt bölümlerinden ayrılmalıdır.
- VO dosyası doğal kayıt birimine göre ayrılır; kısa hook ve kapanış dosyaları olabilir. 1:15–3:00 bir zorunlu süre değildir. Dosya bölmek için metin uzatılmaz.
- 48 kHz/24-bit WAV önerilir.
- Dosya başında ve sonunda yaklaşık 200 ms sessizlik bırakılabilir.
- Teknik baş/son sessizliği kurgu süresine dâhil edilmez. Buna karşılık edit map’te zamanlanmış bilinçli anlatım boşlukları VO dosyasında korunur ve timeline süresine dâhil edilir.
- VO metni ana kurgu tablosuyla birebir aynı olmalıdır.
- VO üretim veya temizleme aşamasında otomatik `remove silence` uygulanacaksa edit map’te işaretli bilinçli boşluklar bu işlemden korunmalıdır.
- **Seslendirme motoru ElevenLabs v4'tür (model `eleven_v4`, ses `David - Documentary`).** v4, SSML `<break>` etiketini değil köşeli parantez içindeki **audio tag**'leri kullanır. Bu nedenle `Recording text` içinde `<break time="..." />` veya `&lt;break ... /&gt;` **kesinlikle kullanılmaz.**
- **Ton etiketi (zorunlu):** Her `Recording text` hücresi, Bölüm J'deki o chapter tonunu karşılayan tek bir ton etiketiyle başlar. Bölüm içinde ton belirgin biçimde değişiyorsa (ör. açıklamadan ağır bir sonuca geçiş) yalnızca o noktaya ikinci bir ton etiketi eklenebilir. Bir hücrede en fazla 3 ton etiketi olur.
- İzin verilen ton etiketleri (küçük harf, İngilizce): `[serious]`, `[curious]`, `[thoughtful]`, `[calm]`, `[firm]`, `[measured]`, `[somber]`, `[intrigued]`, `[matter-of-fact]`, `[warm]`, `[reflective]`, `[emphatic]`. Kanal profili ve Bölüm J'deki "yapay drama yok" kuralı geçerlidir: `[whispers]`, `[shouting]`, `[excited]`, `[laughs]`, `[sighs]`, ses efekti (`[explosion]` vb.) ve aksan etiketleri kullanılamaz.
- **Duraklama etiketleri:** Kısa sessizlik gereken yerde yalnızca şu üç etiket kullanılır: `[short pause]` ≈ 0.5 s (kısa vurgu), `[pause]` ≈ 1.0 s (doğal duraklama, güçlü fotoğraf veya belgeyi inceletme), `[long pause]` ≈ 1.5–2.0 s (ağır bir sonucu sindirme, kısa görsel bakış). 2.0 saniyeden uzun görsel nefes veya doğal/arşiv sesi alanı gerekiyorsa etiket kullanılmaz; süre `Picture and edit instruction` hücresinde `NARRATION ENDS AT [timeline]; NATURAL SOUND / VISUAL HOLD UNTIL [timeline]` biçiminde zamanlanır ve VO dosyasında gerçek sessizlik olarak korunur.
- Her `Recording text` yazılırken yalnızca konuşulacak cümleler değil, o chapter'ın görsel akışı da birlikte değerlendirilmelidir. Önemli bir video anını kısa süre izletmek, güçlü bir fotoğrafı inceletmek, belge/harita/grafiği kavratmak ya da ağır bir sonucu sindirmek için kısa sessizlik gereken yere duraklama etiketi doğrudan **Recording text içine** eklenmelidir. Duraklama her cümleye, paragraf sonuna veya chapter geçişine otomatik eklenemez; hedef süreyi doldurmak veya yapay dramatizasyon için kullanılamaz.
- **Yazım:** Etiketler köşeli parantez içinde düz metin olarak yazılır; Markdown kaçışı gerekmez, backtick veya kod bloğu kullanılmaz, etiket içinde `|` bulunmaz. Etiket, ait olduğu cümlenin hemen önüne yazılır. Örnek: `[serious] But nobody reported the ship missing. [pause] [somber] And that mistake would cost hundreds of lives.`
- Etiketler sayılar, birimler ve özel isimler için telaffuz talimatı olarak kullanılmaz; okunuş Bölüm J'de verilir. Recording text'e etiket dışında hiçbir meta talimat (`(pause)`, `intentional silence`, `hold until...`) yazılamaz.
- `Recording text` ile karşılık gelen `Exact voice-over` alanı rough-cut ve timeline uyumu için birebir aynı kalmalıdır; ton ve duraklama etiketleri iki alanda aynı yerde ve aynı yazımla bulunur.
- Her duraklama etiketinin yaklaşık süresi (`[short pause]` 0.5 s, `[pause]` 1.0 s, `[long pause]` 1.5–2.0 s) timeline ve WPM hesabına dâhil edilmelidir. Son kontrolde bütün `Recording text` ve `Exact voice-over` alanları taranmalı; `<break` veya `&lt;break` kalmadığı, her hücrenin bir ton etiketiyle başladığı ve yalnızca izin verilen etiketlerin kullanıldığı doğrulanmalıdır.

### J. Narration direction

- Önerilen aksan
- Gerçek konuşma hızı
- Ton ve enerji
- Hook ile gövde arasındaki enerji farkı
- Vurgulanacak kelimeler
- Cümleler arasındaki yaklaşık duraklama
- Sayıların nasıl okunacağı
- Telaffuz notları
- Kaçınılacak yapay dramatizasyon
- Hook, açıklama, insan hikâyesi ve kapanış için ayrı yaklaşık hız/enerji yönlendirmesi
- Bilinçli nefes anlarının hangi VO dosyalarında ve hangi timeline zamanlarında korunacağı

Varsayılan yaklaşım:

- Ses karakteri, aksan, ton, enerji eğrisi ve bölüm bazlı WPM aralıkları ilgili kanal profilinden alınır; konu promptu farklı bir yön verirse o uygulanır.
- Bu bölüm genel sıfatlarla geçilemez. Profildeki yaratıcı yön; hook, gövde, teknik açıklama/insan hikâyesi ve kapanış için kaydedilebilir somut talimatlara çevrilmelidir.
- Gerçek konuşma hızı, toplam kelime sayısı ve timeline süresiyle uyumlu olmalı; bütün video tekdüze okunmamalıdır.

### K. Music and sound

Müzik türü, dönem hissi ve dramatik yoğunluk kanal profilinden alınır. Bu bölüm, seçilen yönün timeline üzerindeki teknik uygulamasını ve hakları güvenli ses kullanımını kaydeder.

- Müzik türü ve dönem hissi
- Seslendirmeye göre yaklaşık seviye
- Chapter değişimlerindeki müzik yaklaşımı
- Korunacak gerçek arşiv sesleri
- Kullanılacak doğal efektler
- Kaçınılacak abartılı efektler
- Kapanıştaki ses yaklaşımı
- Müzik ve VO’nun tamamen geri çekileceği planlı doğal ses anları
- Kullanılacaksa chapter’lar arası kısa sound bridge noktaları

Varsayılan:

- Düşük seviyeli, kanal profiline uygun ağırbaşlı veya merak uyandıran ambient
- Sürekli epik veya aşırı dramatik müzik yok
- Konuya uygun doğal mekanik, araç, ortam veya arayüz sesleri yalnızca telifçe güvenli ve görselle uyumluysa
- Whoosh ve impact sesleri sınırlı
- İnsan kaybı, sivil etki, kullanıcı hayal kırıklığı, ürün sonu veya kapanış anında melodramatik yükselişten kaçın

### L. Upload package

Başlık, thumbnail ve açıklamanın yaratıcı dili kanal profilinden alınır; master yalnızca seçeneklerin eksiksiz, araştırmayla uyumlu, yanıltıcı olmayan ve teslim edilebilir biçimde hazırlanmasını zorunlu kılar.

#### 1. Final title options

- Bir ana başlık
- İki güçlü alternatif
- Her başlık için kısa doğruluk ve merak değerlendirmesi
- Önerilen başlığın neden seçildiği

Başlıklar yalnızca tarihsel konuyu adlandırmamalı; kayıp, karar, yanlış inanış, beklenmedik neden veya bugün kalan sonuç üzerinden açık bir merak boşluğu kurmalıdır. Üç seçenek küçük kelime değişiklikleri değil, en az iki farklı izleyici vaadini test etmelidir. Başlıkta cevabın tamamı verilmemeli; fakat izleyicinin videoda tam olarak ne öğreneceği belirsiz de bırakılmamalıdır.

Varsayılan olarak geniş ve ansiklopedik başlık kalıbı yerine tek bir hikâye taşıyıcısı ve somut gerilim tercih edilmelidir: belirli kişi, ürün, araç, şirket, kurum, karar, görev, tarih, yanlış inanış veya kritik kırılma anı. Geniş konu adı başlıkta kullanılacaksa thumbnail ve senaryo yine somut bir taşıyıcıya dayanmalıdır. Başlık, araştırma tamamlandıktan sonra pakete eklenen bir etiket değil; senaryonun hangi soruyu cevaplayacağını belirleyen üretim kısıtıdır.

#### 2. Thumbnail concepts

En az üç farklı A/B konsepti:

| Concept | Main image | Contrast / composition | Exact text | Why it works | Accuracy risk |
| ------- | ---------- | ---------------------- | ---------- | ------------ | ------------- |

Kurallar:

- Metin tercihen 2–5 kelime
- Küçük ekranda okunabilir
- Başlığın aynısını tekrarlamak zorunda değil
- Tek bir güçlü kişi, nesne, ürün, tesis, araç, arayüz, harita anı veya sonuç odak noktası olmalı
- Önce/sonra kompozisyonu yalnızca iki görüntü gerçekten karşılaştırılabiliyorsa
- Yanlış özne, model, tesis, araç, üniforma, arayüz veya AI üretimi ‘tarihsel kanıt’ kullanılamaz
- Sayısal iddia claim ledger ile uyumlu olmalı
- Üç konsept yalnızca renk veya metin değişikliği olmamalı; en az iki farklı tıklama hipotezini test etmelidir: örneğin `lost icon`, `scale of decline`, `surprising cause` veya `then vs now`.
- Thumbnail metni mümkünse **2–4 kelime** olmalı ve video başlığını aynen tekrar etmemelidir. Metin, görselin tek başına veremediği yeni bir gerilim veya soru eklemelidir.
- Ana kişi, nesne veya olay küçük ekranda tek bakışta tanınmalı; gereksiz logo/amblem, küçük yüzler, çok sayıda nesne, uzun veri ve dekoratif ikon kullanılmamalıdır.
- Tek bir net odak noktası ve belirgin tonal/renk kontrastı bulunmalıdır. İki ana görsel kullanılıyorsa aralarındaki ilişki bir saniyeden kısa sürede anlaşılmalıdır.
- Konsept, mobil thumbnail boyutuna küçültüldüğünde test edilmeli; metin, nesne ve temel çelişki hâlâ anlaşılmıyorsa sadeleştirilmelidir.
- Title ve thumbnail birlikte tek bir vaat oluşturmalıdır: biri bağlamı, diğeri merakı taşımalı; ikisi aynı cümleyi iki kez söylememelidir.
- Seçilen thumbnail vaadinin açılışta karşılanma zamanı Bölüm 7.6’dan çözülür; C/E/G aynı zamanları kullanır.

Her konsept için görüntü üretim veya tasarım aracına doğrudan verilebilecek kısa İngilizce prompt da yazılmalıdır.

#### 3. YouTube description

- İlk iki satırda videonun ana vaadi
- 1–2 kısa açıklama paragrafı
- `00:00` ile başlayan final chapters
- Yalnızca **final kurguda gerçekten kullanılan ve lisansı/hak bildirimi atıf zorunluluğu getiren** görsel, video, belge, harita, ses ve müzikler için tek bir toplu `Visual and Media Credits` bölümü
- `Public Domain`, `CC0` veya Pexels/Pixabay/benzeri ücretsiz platform lisansı açıkça atıf istemiyorsa varlık YouTube açıklamasında tek tek listelenmemelidir. İstenirse yalnızca kısa ve genel bir kaynak teşekkür satırı eklenebilir; bu satır zorunlu kredi gibi sunulmamalıdır.
- Wikimedia Commons bir kaynak deposudur ve site genelinde bütün dosyalara uygulanan tek bir kullanım lisansı yoktur. Bu nedenle yalnızca `Wikimedia Commons` ana sayfasını veya genel izin sayfasını vermek, atıf zorunlu bir dosya için yeterli değildir. Wikimedia’daki `CC BY` veya başka bir kabul edilmiş atıf zorunlu varlık; eser/varlık adı ya da açık tanımı, üretici/hak sahibi, tekil dosya sayfası, kesin lisans ve gerekiyorsa yapılan değişiklik bilgisiyle kredilendirilmelidir.
- Aynı üretici, kurum ve lisans altındaki birden fazla varlık tek bir grup altında birleştirilebilir; ortak lisans bağlantısı bir kez verilebilir. Ancak atıf zorunlu her varlık kendi tekil kaynak bağlantısıyla açıkça tanımlanmalı ve hangi kredinin hangi varlığa ait olduğu belirsiz bırakılmamalıdır.
- `CC BY` kredisi en azından `varlık/eser adı veya açık tanım — üretici/hak sahibi — tekil kaynak bağlantısı — lisans adı ve lisans bağlantısı` öğelerini içermelidir. Varlık kırpıldı, renklendirildi, düzenlendi veya başka biçimde değiştirildiyse kısa biçimde `cropped`, `colour-adjusted` veya uygun değişiklik notu eklenmelidir.
- Kurum veya tekil varlık sayfası belirli bir kredi satırını zorunlu kılıyorsa bu metin korunmalıdır. Atıf zorunluluğu olmayan varlıklar sırf kaynak kaydı bulunsun diye açıklamaya eklenmemeli; bunların doğrudan URL ve lisans kayıtları asset library içinde tutulmaya devam etmelidir.
- YouTube açıklamasındaki kredi bölümü asset library’nin tamamını değil, yalnızca final kurguda kullanılan atıf zorunlu varlıkları içermelidir. Bir varlığa yalnızca kaynak linki vermek lisans şartlarını karşılamıyorsa üretici ve lisans bilgileri çıkarılamaz; buna karşılık kaynak göstermek telifli veya kullanımı yasak bir varlığı kullanılabilir hâle getirmez.
- Araştırma kaynakları için kısa bölüm
- Gerekiyorsa bağlamsal görüntü notu
- Doğal anahtar kelimeler; keyword stuffing yok

#### 4. Additional metadata

- Yalnızca yararlı konu/ad/yazım varyantları için alakalı tags; adet kotası yok. Etiketler ana büyüme stratejisi olarak sunulmaz
- En fazla 3 hashtag
- Kısa pinned-comment önerisi
- Kanal içindeki bir sonraki konuya doğal bağlantı önerisi

### M. Research sources

Araştırmada kullanılan güvenilir kaynaklar doğrudan bağlantılarıyla listelenmelidir. Her kaynak için:

- Kurum veya yazar
- Belge veya sayfa başlığı
- Yayın tarihi
- Doğrudan URL
- Desteklediği ana iddia
- Birincil, kurumsal, akademik veya ikincil kaynak türü

### N. Research notes and uncertainties

- Tartışmalı sayılar
- Çelişen tarihsel anlatılar
- Kurum, kişi, ürün, model, sürüm, birlik, operasyon, yer veya araç adlarındaki değişiklikler
- Kesin doğrulanamayan ayrıntılar
- Enflasyon veya para dönüşümü yöntemi
- Senaryoda kullanılan temkinli ifadeler
- Gerçek olaya ait olmayan bağlamsal görüntüler

Belirsizlik yoksa `No material unresolved issues` yazılabilir.

### O. Final copyright check

Her kullanılan varlık için:

- [ ] Doğrudan kaynak sayfası açıldı
- [ ] Lisans öğe bazında doğrulandı
- [ ] Ticari YouTube kullanımına izin veriyor
- [ ] Ticari kullanım ve gerekli düzenlemeler tamamen ücretsiz; ücretli lisans, abonelik, yazılı izin, başvuru veya özel onay gerekmiyor
- [ ] `CC BY-SA`, `CC BY-NC`, `CC BY-ND`, `editorial/research/personal/educational use only` veya benzeri ek kısıt yok
- [ ] Gerekli atıf eksiksiz yazıldı
- [ ] Uploader ile gerçek hak sahibi karıştırılmadı
- [ ] Video zaman aralığı gerçekten incelendi
- [ ] Filigran veya üçüncü taraf logo yok
- [ ] Modern görüntü dönem görüntüsü gibi sunulmuyor
- [ ] Tanıtım, reklam, propaganda, eğitim filmi veya taraflı haber filmi doğru bağlamlandı
- [ ] Kullanılan müzik ve arşiv sesinin hakkı ayrıca kontrol edildi

## 13. Görsel araştırma sırası

Hook için Bölüm 9’daki gerçek V önceliği, sabit görsel yasağı ve iki motion G üst sınırı uygulanır. Gövdede gerçek video adaylarıyla doğru fotoğraf/belge adayları birlikte araştırılır; ancak mekanizma/karşılaştırmayı özgün bir G daha iyi açıklıyorsa onu son çareye bırakma. Doğru belge/fotoğraf merkezi kanıtsa doğrudan seçilebilir. Aşağıdaki sıra araştırma başlangıcıdır, zayıf video kullanma zorunluluğu değildir:

1. Anlatılan gerçek özne, kurum, ürün, proje, yer veya olaya ait açık lisanslı dönem videosu
2. Anlatılan gerçek kişi, sistem, ürün, birlik, araç veya sürece ait dönem/kullanım videosu
3. Doğru modelin, makinenin, aracın, sistemin veya yöntemin açık lisanslı üretim, eğitim, test, teknik, müze ya da çalışma videosu
4. Aynı yer, taraf, kullanıcı eylemi ve döneme ait açık lisanslı bağlamsal video
5. Gerçek öznenin, tesisin, alanın, ürünün veya aracın açık lisanslı modern kullanım/restorasyon videosu
6. Doğru kişi, ürün, araç, sistem, yer, belge veya olay fotoğrafı
7. Doğru harita, teknik plan, resmî kayıt, yıllık rapor, kılavuz, emir, reklam veya dönem incelemesi
8. Güvenilir veriden hazırlanmış sade grafik
9. Anlatılan kavramı doğrudan destekleyen lisanslı modern stok
10. Son seçenek olarak doğru ad, yer ve tarih içeren statik görsel

Sadece ekranı doldurmak için alakasız stok, arşiv, tesis, teknoloji, araç, patlama veya şehir görüntüsü kullanılmamalıdır.

### Asset sufficiency gate

Exact voice-over yazılmadan önce bölüm bazında görsel yeterlilik kontrolü yapılmalıdır:

| Chapter | Needed screen time | Verified moving footage | Verified still/document coverage | Main gaps | Decision |
| ------- | -----------------: | ----------------------: | -------------------------------: | --------- | -------- |

Karar seçenekleri:

- `READY`
- `RESEARCH MORE`
- `REWRITE FOR AVAILABLE VISUALS`
- `REMOVE SECTION`
- `TOPIC NOT VISUALLY VIABLE`

Bu tablo F bölümünün sonunda yer alır; A–O dışında yeni ana bölüm açılmaz. Ana chapter’lardan biri `RESEARCH MORE` veya daha kötü durumda bırakılarak final script kesinleştirilemez. Araştırmaya yön veren taslak yazılabilir; doğrulanmış final diye teslim edilemez.

`Verified moving footage` yalnızca Bölüm 10.3 kontrolünden geçen, tüm videoda yeniden kullanılmayacak benzersiz görsel içerik taşıyan ve gerçekten incelenmiş V saniyelerini içerir; aynı tambur döngüsünün farklı dakikaları ayrı kapasite gibi toplanamaz. Bu hücreye yalnızca seçilen kullanılabilir süre yazılır; kaynak dosyanın toplam uzunluğu yazılmaz. G motion, fotoğraf pan/zoom ve planlanan üretimler bu sayıya katılmaz. `Verified still/document coverage` hücresinde mevcut P/G süreleri ve henüz üretilecek G kodları ayrı etiketlenir; üretilmemiş G için `PLANNED G — content/spec verified; render pending` yazılır. `READY`, içerik planının üretilebilir olduğunu belirtir; bitmiş video veya animasyon dosyası var demek değildir. Hook motion uygulaması ayrıca teslim aşamasında kontrol edilir.

Görsel yeterlilik yalnızca toplam saniye hesabı değildir. `READY` kararı verilebilmesi için o chapter’ın ana iddialarını gerçekten taşıyan, sessiz izlendiğinde de anlamlı, görsel olarak kullanılabilir ve kesin kaynak zamanları doğrulanmış kesitler bulunmalıdır. Yalnızca talking-head, boş bekleme, tekrarlı hareket veya gevşek bağlamsal görüntüyle süre tamamlanıyorsa chapter `READY` sayılamaz.

## 14. Arşiv videosu inceleme standardı

1. Video yalnızca başlığı, açıklaması, thumbnail’i veya arama sonucundaki kısa önizlemesi uygun göründüğü için asset library’ye eklenemez.
2. Finalde kullanılacak **her kaynak video**, kullanılabilir planları kaçırmayacak biçimde baştan sona izlenmeli veya tüm süreyi kapsayan düzenli sahne/kare örnekleriyle taranmalıdır. Seçilen her kesin kaynak aralığı ayrıca normal hızda doğrudan izlenmeli; plan başlangıcı, plan sonu ve aradaki hareket kare/shot düzeyinde kontrol edilmelidir. Arama sonucu, thumbnail veya seyrek örnek kareler seçilen kesitin normal hızda doğrudan incelenmesinin yerine geçmez. Kaynağın web oynatıcısı incelemeyi engelliyorsa hakları ve erişimi doğrulanabilir özgün medya dosyasıyla bu kontrolü yapmayı dene; bu da mümkün değilse aynı anlatım işlevini karşılayan başka erişilebilir ve uygun lisanslı video ara. İncelenemeyen adayı kesin kesit zamanı verilmiş `V` olarak kaydetme.
3. Başlangıç ve bitiş zamanları gerçek plan sınırlarına göre verilmelidir. Kesitin ilk veya son saniyelerinde anlamsız bekleme, kameranın oturması, konuşmaya hazırlık, boş kadraj veya konu dışı hareket varsa kesilmelidir.
4. Konuya uygun özne, kişi, kurum, model, sürüm, yer, araç, sistem, kullanım biçimi ve dönem mümkün olduğunca teşhis edilmelidir.
5. Teşhis kesin değilse görüntü genel bağlam olarak işaretlenmelidir. Görsel bağlam belirsizliği merkezi iddiayı etkiliyorsa kesit kullanılmamalıdır.
6. Tanıtım, propaganda veya eğitim filmi bağımsız ve tarafsız haber/olay görüntüsü gibi sunulmamalıdır.
7. Görsel doğruluk ve görsel ilgi ayrı ayrı kontrol edilmelidir. Kesit tarihsel olarak doğru olsa bile ekranda anlamlı bir eylem, nesne, süreç, ölçek, çevre, sonuç veya insan tepkisi göstermiyorsa yalnızca süre doldurmak için kullanılamaz.
8. **Kaynak sesi kapalıyken yalnızca konuşan bir insanı gösteren kesit varsayılan olarak kullanılmamalıdır.** Konuşanın kimliği bizzat hikâyenin konusuysa, konuşurken fiziksel olarak önemli bir şey gösteriyorsa veya görüntünün tarihsel değeri sözlerden bağımsızsa kullanılabilir. Aksi hâlde ilgili eylem, nesne, belge, tesis, araç, kullanıcı veya süreç görüntüsü aranmalıdır.
9. Aynı arşiv videosundan en fazla iki farklı kesit alma sınırı yalnızca Hook için geçerlidir. Hook dışında aynı kaynaktan alınan kesitler çakışmamalı, farklı plan veya hareket göstermeli ve görsel olarak farklı bilgi sağlamalıdır; kesit sayısı sınırlı değildir.
10. Aynı, çakışan veya görsel olarak eşdeğer kesit yeniden kullanılamaz; kaynaklar arası anlamsal/görsel kontrol Bölüm 10.3’e göre yapılır.
11. Kaynak videosundaki tabela, yazı, üniforma, model, arayüz, coğrafya veya görünür bağlam senaryodaki iddiayla çelişiyorsa görüntü kullanılamaz.
12. Kaynağın sesini koruma veya kapatma kararı kurgu hücresinde yalnızca gerektiğinde belirtilmelidir. Ses kapatılacaksa kesitin görsel olarak tek başına neden anlamlı olduğu kontrol edilmelidir.
13. Seçilen kaynak aralığı videonun gerçek toplam süresini aşamaz. `Timeline süresi = kaynak bitiş − kaynak başlangıç` olmalıdır; görüntü yetmiyorsa plan kısaltılmalı veya başka video seçilmelidir.
14. Final edit map’e girmeden önce her kesit için son kontrol sorusu şudur: **“Bu görüntü çıkarılsa izleyici anlatılan şeyi daha az mı anlar, daha az mı hisseder veya daha az mı görsel kanıt alır?”** Cevap hayırsa daha güçlü bir kesit aranmalı veya görsel plan sadeleştirilmelidir.

## 15. Veri grafiği, belge ve harita içerik standardı

1. `G` varlığı yalnızca sözlü anlatımı veya mevcut arşiv/fotoğraf planını gerçekten daha anlaşılır ve görsel olarak daha güçlü yapıyorsa kullanılmalıdır. Kullanım alanı yalnızca istatistik değildir; veri, harita ve belgeye ek olarak mekanizma, süreç, fiziksel ilişki, insan etkileşimi, karar anı veya gözde canlandırılması zor bir sahne açıklayıcı ya da temsili görselleştirilebilir.
2. Kullanılan her sayı, tarih, ad, ilişki, rota ve konum doğrudan kaynaklara dayanmalıdır.
3. Ekseni keserek, ölçeği değiştirerek veya kapsamı gizleyerek sonuç dramatize edilemez.
4. Birbirinden farklı ölçüler ve kapsamlar birbirinin yerine kullanılamaz.
5. Para değerlerinde yıl ve para birimi görünmelidir.
6. Tahmin ile gerçekleşen veri açıkça ayrılmalıdır.
7. Harita tarihsel sınırları, gerçek tarihleri, yerleri ve gerekiyorsa ölçeği doğru göstermelidir.
8. Ekranda kullanılacak kısa kaynak satırı birebir; tam bağlantılar ayrıntılı kaynak paketinde verilmelidir.
9. Grafik içerik fişinde gerekli bilgi, kesin veri, kaynak, ekran metni, referans varlık ve doğruluk sınırına ek olarak; istatistik dışı görseller için üretime yetecek ayrıntıda kişi, araç, nesne, çevre, eylem, konum, fiziksel durum ve ilişki tarifi bulunmalıdır. Renk, font, estetik stil, doku, efekt, ikon dili, animasyon veya geçiş promptu bulunmamalıdır.
10. Temsili bir sahne, kaynakların doğruladığı sınırların ötesine taşmamalı ve `illustrative reconstruction — not archival evidence` olarak işaretlenmelidir.
11. Varsayılan ekran metni en fazla bir kısa ana başlık ve bir kısa açıklamadır; ikisi de gerekli değilse kullanılmaz. Eksen, birim, kategori, seri, tarih, yer, doğrudan veri etiketi, kısa kaynak satırı ve zorunlu doğruluk açıklaması yalnızca doğru okuma için gereken minimum düzeyde eklenir.
12. İkinci başlık, ek bölüm etiketi veya ek açıklama yalnızca karşılaştırma taraflarını, timeline evrelerini, harita durumlarını/rotalarını ya da belge üzerindeki zorunlu ayrımları göstermek için kullanılabilir; dekoratif veya tekrarlayıcı metin eklenemez.
13. Exact VO, main takeaway, production note, ayrıntılı sahne tarifi, accuracy note, `must not show` talimatı ve tam kaynak dokümantasyonu ekran metni değildir.
14. Veri tablosu ve kaynak ayrıntıları doğruluk için eksiksiz yazılır; final görselde ise bunlar paragraf, madde listesi veya tablo dökümü olarak değil, uygun grafik türü ve kısa doğrudan etiketlerle anlatılır.
15. VO’da açıkça söylenen bilgi, grafiğin anlaşılması için ayrıca gerekli değilse ekranda tam cümle olarak tekrarlanmaz.
16. Modern, temiz, yüksek kaliteli ve konu uygunsa sinematik kompozisyon hedeflenir; fakat grafik bilgi aktarma işlevini kaybederek salt dekoratif poster veya `visual art` hâline gelemez.
17. Metin yoğunluğu ana özneyi, veriyi veya görsel kaliteyi zayıflatıyorsa metin azaltılır; bilgi tek karede okunabilir biçimde sadeleştirilemiyorsa gerekçeli olarak ayrı görsel aşamalara bölünür.

## 16. Son doğrulama listesi

### Araştırma ve doğruluk

- [ ] Ekstra prompttaki bütün açık talimatlar uygulandı
- [ ] Video tek bir açık ana soruya sahip
- [ ] Başlık iddiasının doğruluk sınırı açıklandı
- [ ] Nedensel açıklama kanıta yeterli; ne yanıltıcı tek neden ne yapay çok neden kotası var
- [ ] Claim ledger’daki bütün core iddialar doğrulandı
- [ ] Kritik iddialar mümkünse iki güvenilir kaynakla kontrol edildi
- [ ] Konuya özgü temel tarih, sayı, ad, kapasite, fiyat, üretim, pazar, kuvvet, kayıp, menzil, konum veya kapanış ölçüleri doğrulandı
- [ ] Konuya özgü benzer fakat farklı olay, aşama, statü ve ölçüler birbirine karıştırılmadı
- [ ] Korelasyon nedensellik gibi sunulmadı
- [ ] Tartışmalı bilgiler temkinli dille yazıldı
- [ ] İnsan ölçeği ve önemli bedeller konuya uygun işlendi; günümüz bağlantısı yalnızca cevaba değer katıyorsa kullanıldı
- [ ] Geçmiş gereksiz biçimde romantikleştirilmedi
- [ ] Hiçbir kaynak bitiş zamanı video dosyasının gerçek toplam süresini aşmıyor

### Süre, yapı ve seslendirme

- [ ] Başlık–thumbnail–ilk cevap aynı izleyici vaadini taşıyor
- [ ] Gerçek VO ölçülmediyse zamanlar tahmin olarak belirtilmiş; ölçüm iddiası yok
- [ ] Grafik okuma yükü ile eşzamanlı VO birbirini boğmuyor
- [ ] Tempo sorunları yalnızca WPM veya kesme sıklığı artırılarak çözülmemiş

- [ ] Konu promptundaki hedef süre, orada yoksa kanal profilindeki varsayılan süre kullanıldı; yalnızca dolgu ile sağlanabilecek bir süre zorlanmadı
- [ ] Kelime sayısı gerçek konuşma hızı ve arşiv sesiyle uyumlu
- [ ] İngilizce doğal ve konuşulur
- [ ] Ana soru ve ilk gerçek değer/payoff kanal profilindeki açılış zamanlamasına göre kuruldu
- [ ] Gerekli başlık nitelemesi yanıltmayacak kadar erken verildi
- [ ] Her chapter yeni bir nedensel aşama veya soru taşıyor
- [ ] Kanal profilindeki retention/reset kadansı edit map’te gerçek kanıt, mekanizma, sonuç veya görsel ilerlemeyle karşılandı
- [ ] Kanal profilindeki ilk dakika/hook sonrası retention bridge şartları karşılandı
- [ ] Çok nedenli açıklama liste hâlinde değil; nedenlerin önemi, sırası ve birbirini nasıl güçlendirdiği açık
- [ ] İlk 1–3 dakika içinde konuya uygun insan, ürün, araç, karar, deneyim, belge, yer veya olay üzerinden somut bir giriş noktası var
- [ ] Merak döngüleri konuya hizmet ediyor; adet kotası, yapay teaser ve karşılıksız yan soru yok
- [ ] Seslendirme genel izleyicinin bilmediği terim, isim ve tarih yükünden arındırıldı
- [ ] Final senaryo yalnızca ana cevabı anlamlı biçimde değiştiren neden ve ayrıntıları içeriyor
- [ ] Seslendirme duvardan duvara değil; yalnızca güçlü varlığın desteklediği seçici nefes anları planlandı
- [ ] Bilinçli nefes anlarının kesin zamanları edit map’te yazılı ve VO dosyasında korunuyor
- [ ] Cümle uzunluğu ve enerji video boyunca tekdüze değil
- [ ] Gereksiz özet, tekrar veya süre doldurma yok
- [ ] Açılıştaki ana soruya kapanışta cevap verildi
- [ ] VO dosyaları kurgu tablosuyla birebir aynı
- [ ] Her `Recording text` alanı bir ElevenLabs v4 ton etiketiyle başlıyor; duraklama ihtiyacı görsel akışla birlikte değerlendirildi ve uygun yerlerde yalnızca `[short pause]`, `[pause]` veya `[long pause]` kullanıldı
- [ ] Hiçbir yerde `<break` veya `&lt;break` yok; bütün köşeli parantezli etiketler izin verilen listede ve `Recording text` ile `Exact voice-over` alanında birebir aynı

### Görsel ve kurgu

- [ ] Video, kanal profilinin izin verdiği gerçek görüntü veya doğruluk rolü açıkça etiketlenmiş ve gerçek içerik hareketi taşıyan G varlığıyla başlıyor; sabit G açılışı yok
- [ ] Hook’un yaratıcı ritmi profil/prompttan; 0:00–0:40 ile hook birleşiminde sıfır sabit görsel, en az %70 gerçek V, en fazla iki motion G (her biri en fazla 6 saniye) ve kaynak başına iki farklı kesit sınırı Bölüm 9’dan E’ye yazıldı ve uygulandı
- [ ] İlk plan title ve thumbnail vaadini karşılıyor
- [ ] Profil/prompttan alınan hareketli görüntü–grafik–fotoğraf/belge oranı sağlandı veya gerekçeli revizyon yazıldı
- [ ] Asset sufficiency gate bütün chapter’larda `READY`
- [ ] Zaman çizelgesi baştan sona kesintisiz
- [ ] Her edit satırı asset koduyla başlıyor
- [ ] Her kod asset library’de mevcut
- [ ] Video zamanları görüntü incelenerek doğrulandı
- [ ] Finalde kullanılan her kaynak video tüm süreyi kapsayacak biçimde tarandı; seçilen kesin kesitler normal hızda shot/kare düzeyinde yeniden kontrol edildi
- [ ] Kaynak sesi kapalı talking-head veya görsel işlevi olmayan insan konuşması kesitleri kullanılmadı; varsa istisnasının somut nedeni var
- [ ] Her video kesiti yalnızca konuya ait olduğu için değil, ilgili VO anına gerçek görsel kanıt/açıklama/ölçek/insan sonucu kattığı için seçildi
- [ ] Sürekli blokların kaynak zamanları tam devam ediyor
- [ ] Bütün video kesitleri doğal hızında; slow motion, optical flow, frame interpolation, freeze-frame veya kare tekrarıyla uzatma yok
- [ ] Her video kesitinin kaynak süresi edit map’teki timeline süresiyle uyumlu; hiçbir tek video planı veya satırlara bölünmüş kesintisiz aynı görsel video bloğu 20 saniyeyi aşmıyor
- [ ] Fotoğraf/görsel planları normalde 12–15 saniye ve hiçbir durumda 15 saniyeden uzun değil; her G gösterimi en fazla 10 saniye; hook G için daha sıkı 6 saniye sınırı uygulanıyor
- [ ] Arka arkaya üç sıradan fotoğraf yok; P/sabit G/belge/harita sekansları birlikte sayıldı ve birleşik statik sekans hiçbir durumda 15 saniyeyi aşmadı; G varlıkları en fazla 10 saniye tutuldu ve uygun/doğru V bulunduğunda statik plan yerine V önceliklendirildi (Bölüm 8.2)
- [ ] Bağlamsal görüntüler doğru etiketlendi
- [ ] Yanlış özne, kişi, kurum, ürün, model, araç, üniforma, arayüz, coğrafya veya dönem görüntüsü yok
- [ ] Modern görüntü tarihsel görüntü gibi sunulmuyor
- [ ] Veri grafikleri kaynaklı ve yanıltıcı olmayan ölçek kullanıyor
- [ ] Grafikler varsayılan bir kısa başlık + bir kısa açıklama metin bütçesine uyuyor; zorunlu veri/harita/belge etiketleri minimum düzeyde
- [ ] Veri ve istatistik ayrıntıları ekranda paragraf, madde listesi veya tablo dökümü olarak değil, uygun görsel kodlama ve kısa etiketlerle anlatılıyor
- [ ] Exact VO, main takeaway, production notes, ayrıntılı sahne tarifleri ve tam kaynak dokümantasyonu ekran metnine dönüşmemiş
- [ ] Grafikler modern, yüksek kaliteli ve görsel olarak güçlü; ancak okunabilirlik ve açıklayıcı işlev dekoratif sanat yaklaşımına kurban edilmemiş
- [ ] Her chapter’da gerçek V/P/belge değerlendirildi; G gerçek malzemeyi gereksiz yere ikame etmiyor ve grafik kotası uygulanmıyor
- [ ] İstatistik dışı her `G` varlığının içerik fişi, sahneyi üretmeye yetecek kişi/araç/nesne/çevre/eylem/konum/ilişki ayrıntısını içeriyor
- [ ] Temsili `G` görselleri gerçek arşiv kanıtı gibi sunulmuyor ve doğrulanmamış tarihsel ayrıntı uydurmuyor
- [ ] Plan değişimleri her cümlede otomatik yapılmıyor; yeni bilgi, odak veya hareketle gerekçeli
- [ ] Güçlü süreç görüntüleri gerektiğinde doğal sesiyle nefes alıyor
- [ ] Konunun gerektirdiği hatırlanabilir güçlü anlar C/F/G içinde somut; sabit üçlü kota için dolgu yok

### Tekrar auditi

- [ ] Hook ve non-hook sütunları korundu; video tekrar kontrolünde toplam kullanım ve kaynaklar arası görsel eşdeğerlik birlikte denetlendi
- [ ] Bütün kullanılan fotoğraf ve video kesitleri auditte mevcut
- [ ] Hiçbir fotoğraf hook dışında iki defadan fazla kullanılmıyor
- [ ] Hiçbir aynı/çakışan/görsel olarak eşdeğer video içeriği hook, gövde ve kapanış toplamında bir defadan fazla kullanılmıyor
- [ ] Farklı zaman kodları tek başına benzersizlik sayılmıyor; her kesit görünür yeni işlem, ayrıntı veya sonuç taşıyor
- [ ] Hook içinde hiçbir orijinal video kaynağından ikiden fazla farklı kesit alınmıyor; Hook dışındaki farklı ve çakışmayan kesitler yanlışlıkla bu sınıra tabi tutulmuyor
- [ ] Tekrar edilen fotoğraf toplam 18 saniyeyi aşmıyor
- [ ] Eski 24 saniye/ikinci video kullanımı istisnası uygulanmıyor; dönen makine gibi görsel olarak eşdeğer kesitler ayıklandı
- [ ] Yalnızca izinli fotoğraf ikinci kullanımları farklı chapter’da, en az 90 saniye ve sekiz plan sonra
- [ ] Fotoğraflardaki izinli ikinci kullanımlarda `FORCED REUSE 2/2` ve somut gerekçe var; video için uygulanmıyor
- [ ] Bitişik veya `A–B–A` tekrar yok
- [ ] Aynı varlık farklı kodla yeni varlık gibi gösterilmiyor
- [ ] Audit tablosunda hiçbir `FAIL` yok

### Template yapısı

- [ ] A–O başlıkları ve bütün zorunlu alt başlıklar template’teki ad ve sırayla korunuyor
- [ ] Hiçbir zorunlu tablo, alan, sütun veya satır türü çıkarılmadı; template dışı bölüm, tablo veya sütun eklenmedi
- [ ] Exact voice-over and edit map yalnızca altı zorunlu sütundan oluşuyor ve sütun sırası değişmedi
- [ ] Template veya konu promptu kesin satır sayısı/içeriği verdiyse birebir uygulandı
- [ ] Edit map’te her satır tek ana görsel planını temsil ediyor; açıklama, alternatif kurgu veya yapay bölünmüş satır yok

### Telif ve teslim

- [ ] Başka YouTube veya sosyal medya kanalından alınmış içerik yok
- [ ] Her varlığın doğrudan kaynak bağlantısı ve lisansı var
- [ ] Bütün varlıklar `Public Domain`, `CC0`, kabul edilen `CC BY` veya ücretsiz ticari platform lisansı kapsamında; ücret veya ayrıca izin gerektiren hiçbir varlık yok
- [ ] Ticari kullanımı, düzenlemeyi veya dağıtımı sınırlayan `SA`, `NC`, `ND`, `editorial/research/personal/educational use only` türü lisans yok
- [ ] Birleşik Krallık ve Avrupa arşiv hakları öğe bazında kontrol edildi
- [ ] Atıf gerektiren bütün üretici ve kurumlar listelendi
- [ ] YouTube description içindeki `Visual and Media Credits` yalnızca finalde kullanılan atıf zorunlu varlıkları içeriyor; `Public Domain`, `CC0` ve atıf istemeyen platform varlıkları gereksiz yere tek tek listelenmiyor
- [ ] Atıf zorunlu Wikimedia ve diğer kaynaklarda genel site bağlantısıyla yetinilmedi; her varlık üretici/hak sahibi, tekil kaynak, kesin lisans ve gerekiyorsa değişiklik notuyla eşleştirildi
- [ ] Tanıtım, reklam, propaganda, eğitim filmi, reenactment ve bağlamsal görüntü doğru etiketlendi
- [ ] Chapters, description, tags ve pinned comment hazır
- [ ] Üç title ve üç thumbnail konsepti hazır
- [ ] Thumbnail iddiaları claim ledger ile uyumlu
- [ ] Üç thumbnail yalnızca renk/metin varyasyonu değil; farklı tıklama hipotezlerini test ediyor
- [ ] Seçilen title-thumbnail vaadi Bölüm 7.6’dan çözülen açılış zamanlarında karşılanıyor
- [ ] Dosyada boş varlık kodu, sahte URL veya doğrulanmamış zaman kodu yok

## 17. Dosya adı standardı

Yeni paket şu biçimde adlandırılmalıdır:

`[Short_Topic_Name]_video_package.md`

Örnekler:

- `Short_Topic_Name_video_package.md`
- `Specific_Product_or_Company_video_package.md`
- `Specific_Event_or_Decision_video_package.md`
- `Specific_Person_or_Vehicle_video_package.md`
- `Specific_System_or_Industry_video_package.md`

## 18. Teslim yaklaşımı

Sonuç doğrudan uygulanabilir, eksiksiz bir üretim paketi olmalıdır.

- Taslakta boş varlık kodları bulunmamalıdır.
- Kaynağı bulunmamış görüntü gerçekmiş gibi listelenmemelidir.
- Doğrulanmamış video zaman kodları uydurulmamalıdır.
- Eksik görüntü varsa açıkça belirtilmeli ve yalnızca ücretsiz ticari kullanıma ve düzenlemeye açık alternatif önerilmelidir. Ücretli lisans veya ayrıca izin gerektiren kaynak önerilemez.
- Kullanıcı varlık sağladıysa önce onlar incelenmeli ve uygun olanlar asset library’ye eklenmelidir.
- Araştırma, claim ledger, senaryo ve kurgu birbirinden kopuk hazırlanmamalıdır.
- Ana tez, güçlü kaynak ve güçlü görsel olmadan kesinleştirilmemelidir.
- Exact voice-over and edit map tamamlandıktan sonra tekrar auditi hesaplanmalıdır.
- Audit ihlali not düşülerek bırakılamaz; yeni varlık bulunmalı veya anlatım yeniden yazılmalıdır.
- Aynı orijinal videonun hem çakışmayan hem anlamlı yeni içerik taşıyan sahnelerine hook dışında yapay adet sınırı konulmamalıdır; görsel olarak eşdeğer sahneler zamanları farklı diye yeni sayılmamalıdır.
- Final süre önceden doldurulacak bir hedef değildir; merkezi hikâye taşıyıcısı, güçlü kanıt, insan etkisi, işleyen mekanizma, karşılaştırma ve bugünkü/tarihsel miras ne kadar süre gerektiriyorsa video o kadar sürmelidir.
- Konu, prompt/profil hedefinden daha kısa sürede güçlü biçimde tamamlanıyorsa dolgu eklenmez. Daha uzun süre ancak merkezi soruya gerçekten yeni cevap sağlayan kanıt, olay, insan hikâyesi veya görsel sekansla kazanılabilir; bunlar yoksa açı daraltılır veya hedef süre gerekçeli biçimde revize edilir.
- Final dosya, araştırmacıdan seslendiriciye ve editöre kadar ek açıklama gerektirmeden uygulanabilir olmalıdır.


## 19. Bu revizyonun dayanağı ve kullanım sınırı

Bu bölüm template bakım notudur; üretilen video paketine ayrı bölüm olarak kopyalanmaz. A–O teslim şeması korunur.

2026-09-09 değişiklikleri: ilk 40 saniye ile hook birleşiminde sabit görsel istisnası kaldırıldı; en fazla iki motion G ve G başına 6 saniye sınırı getirildi; video kesitinin ikinci kullanımı hook/gövde ayrımı olmadan yasaklandı; farklı zaman kodlarındaki aynı sahne/eylem ile farklı kaynaklardaki görsel eşdeğerlik birlikte denetlenir hâle getirildi. Gerçek fotoğraf/belge araştırması gövdede etkinleştirildi; chapter başına G adayı zorunluluğu kaldırıldı. Açılış için somut eylem → fark → erken kanıt → mekanizma akışı ve görselle birlikte senaryo kurma yöntemi netleştirildi. A–O başlıkları, tablo sütunları, kodlar, dosya adları ve VO teknik sözleşmesi korunmuştur. Saniye sınırları kullanıcı tercihini uygulayan üretim kararlarıdır; garantili retention formülü değildir.

Önceki 2026-09-06 incelemesinde: zorunlu çok neden/üç güçlü an/döngü kotaları kaldırıldı; erken cevap zamanlaması tek yerde toplandı; tempo üç ayrı değişkene ayrıldı; nefes için mutlak toplam süre kaldırıldı; grafik durum süresi netleştirildi; JPG ile motion teslimi ayrıldı; profil–master yetkileri, kaynak sayacı ve son kontrol çelişkileri düzeltildi. YouTube kaynak yasağı, öğe bazlı lisans doğrulaması ve teknik tekrar sınırları korundu.

Aşağıdaki resmî açıklamalar metriklerin yorumlanmasına dayanak olur; bu dosyadaki önerilen saniye/WPM değerlerini YouTube zorunluluğu yapmaz:

- [YouTube — Measure key moments for audience retention](https://support.google.com/youtube/answer/9314415?hl=en): ilk 30 saniye, beklenti uyumu, güçlü anların erkene alınması ve düşüş/yükselişlerin yorumlanması. Yükseliş, tekrar izleme kadar anlaşılmayan bölümü de gösterebilir.
- [YouTube — Impressions and click-through rate FAQ](https://support.google.com/youtube/answer/7628154?hl=en): CTR trafik kaynağı ve izleyici bağlamıyla değerlendirilir; yetersiz veriden veya küçük değişimlerden kesin sonuç çıkarılmaz.
- [YouTube — Performance FAQ & Troubleshooting](https://support.google.com/youtube/answer/141805?hl=en): izleyiciyle ilgililik ve tatmin, doğru başlık/thumbnail ve etiketlerin sınırlı rolü.

Audience retention kaynağı yeniden kontrol tarihi: 2026-09-09; diğer iki bağlantının önceki kontrol tarihi: 2026-09-06. Bu revizyon bir template incelemesidir; belirli videoların performans analizi yapılmış sayılmaz. Değişikliklerin etkisi gerçek yayın verisiyle değerlendirilmelidir.
