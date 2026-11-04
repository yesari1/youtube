# cinecode ile üretim — YouTube kanalları için uygulama kuralları

**Kural (Yunus, 04.11.2026):** "Bundan sonra videolarının, shortlarının, grafiklerinin hepsini bununla yap." + "kural olarak yaz hepsini". Warfront Archives, The Other Side of Normal (TOSON) ve diğer kanallarda **her Short, her uzun video ve her grafik/motion graphic** cinecode skill'i ile üretilir. Deneme amaçlı: amaç ne kadar işe yaradığını ve ne kadar ilgi çektiğini ölçmek (aşağıda §6).

## 1. Kurulum

| Yer | Nasıl |
|---|---|
| Bulut (rutinler, thread'ler) | Her oturumun başında: `bash /mnt/project-files/pipeline/cinecode_setup/cinecode_cloud_setup.sh` (≈10 sn). Kiti `~/.claude/skills/cinecode` altına koyar, GPU olmadığı için Chrome'u SwiftShader WebGL ile çalıştırır ve probe eder. `KIT=~/.claude/skills/cinecode`. |
| Repo (yesari1/youtube) | Vendor kopya `.claude/skills/cinecode/` (MIT, kaynak commit `VENDORED.md`'de). Repo klonlanan oturumda skill otomatik listelenir. |
| Yunus'un PC'si | `git clone https://github.com/sarpstar/cinecode.git %USERPROFILE%\.claude\skills\cinecode` (Claude Code'da "Install the cinecode skill from https://github.com/sarpstar/cinecode" demek yeterli). Tek yere kur. |
| claude.ai hesabı (isteğe bağlı) | Ayarlar > Capabilities > Skills > Upload skill: `cinecode.zip` (bu klasörde). Hesap skill'i olarak yüklenince guard hook'ları çalışmayabilir; bulutta yukarıdaki kurulum esas. |

Skill listede yoksa: kurulum betiğini çalıştır, sonra `Skill` aracıyla `cinecode`'u yükle (guard hook'ları ancak böyle devreye girer). Yüklenemiyorsa `$KIT/SKILL.md` + `references/quick-mode.md` okunur ve kitin araçları (`init_film.py`, `make.py`, `qc.py`) yine kullanılır.

## 2. Hangi mod, hangi akış

- **Short (Warfront + TOSON, günlük rutinler dahil):** cinecode **Quick mode**, amaç `cinematic` (açıklayıcı belgesel). Her Short tek `film.html`: `python3 $KIT/scripts/init_film.py <kisa-ad> --quick --films-folder <daily klasörü>/cinecode` ile kur, `make.py stills` → `make.py draft` → `make.py final`. Format satırı: `30-39 s, 9:16, 1080x1920, 60 fps` · Delivered to: YouTube Shorts.
- **Uzun video:** cinecode **Film mode**; her G-grafiği / motion graphic sahnesi ya Film mode'un shot'ı ya da kendi Quick film'i (16:9, 1920x1080 veya 3840x2160). Arşiv görüntülü bölümler `references/footage-edit.md` yolu ile.
- **Tek grafik / motion graphic:** Quick mode, sahne başına bir film; süre ve okunabilirlik kuralları aynı kalır (G grafikleri 15-25 sn, ~8-10 sn'de kurulmuş).
- **Otomatik rutin = "tam brief, teslim et ve dur":** Rutinde kullanıcı yok. Brief'i eksiksiz yaz (beat tablosu, VO metni, süre, format, müzik, ses) ve STATE.md'ye `Pace: through` yaz; cinecode'un soru kapılarını sorma, her seçimde ★ seçeneği al ve STATE.md'ye yaz (SKILL.md "A complete brief goes straight to work"). "Kullanıcıya göster/sor" adımları rutinde critic incelemesi ve thread'deki durum mesajı ile karşılanır. Thread'de Yunus varsa (manuel üretim) cinecode kapıları normal sorulur.

## 3. Çelişkide hangi kural geçerli

Kanal kuralları cinecode'un varsayılanlarından **önce gelir**:

| Konu | Geçerli kural |
|---|---|
| Ses efekti | **Yalnızca** `/mnt/project-files/SFX/` WAV'ları + `sfx_lib.Plan` QA (±0,035 sn). cinecode'un `sounds.py`/kodla sentez SFX'i kullanılmaz; WAV'lar `audio/mix.json` sfx bus'ına konur. `make.py`'nin "SOUND ALL CODE / SOUND THIN" uyarıları SFX kütüphanesiyle giderilir. |
| Seslendirme | ElevenLabs "David - Documentary", eleven_v4, sakin ton etiketleri (rutin trigger'ları). cinecode'un "sesi kullanıcı kulakla seçer" kuralı bu sesle karşılanmış sayılır. Ham TTS'e cinecode'un §4b ses işlemi yalnızca netliği bozmuyorsa uygulanır. |
| Ses netliği | **SES NETLİĞİ KURALI (04.11.2026) aynen:** `python3 -I /mnt/project-files/pipeline/vo_check.py vo.wav words.json --out qa/vo_check.txt` zorunlu, critic sesi inceler, tek kelime net değilse yayın yok. |
| Müzik | Kanal kuralı (Kevin MacLeod CC BY 4.0 / kanal müzik klasörü, açıklamada yalnızca kullanılan parça). Shorts'ta müzik VO'nun altında belirgin şekilde kısık. Kodla müzik yok (Yunus seçmedikçe). Rutinde müzik `STATE.md`'ye `Music: <dosya> (routine, kanal kuralı)` diye yazılır. |
| Loudness | -14 LUFS master (cinecode ile aynı). |
| Hook | Shorts_Hook_Playbook.md + `hook_check.py` + 30 puanlık hook critic (≥ 25) — cinecode'un "ilk 2 sn hareket" kuralı ek olarak geçerli. |
| Eleştirmen | **Critic incelemesi kalır:** genel critic ≥ 80, grafik-hiza critic'i, hook critic, ses/VO critic'i. cinecode'un Jury'si (`references/jury.md`) bunlara **ek**tir, yerine geçmez. |
| Ekranda yazı | Ekranda kaynak/kredi yok (açıklamada); başlık/etiketlerde sonda nokta yok; ortalanan her şey x=540'ta gerçekten ortalı; tire (—) yok (cinecode da yasaklıyor). |
| Shorts yapısı | <40 sn, tek fikir, katman katman kurulan okunabilir grafikler, hikâye (tuhaflık + insan/olay + şaşırtan cevap), sözlü CTA yok, sonda görsel uzun-video kartı (Warfront). |
| Gerçek görüntü | Kanal oranları (Shorts gerçek ≤ %35). cinecode'un `asset_search.py`'si arşiv aramada kullanılabilir; lisans satırı hem `LICENSES.csv` hem `licenses.md`. |
| Üretilmiş görsel | ChatGPT/Codex görselleri kanal kuralı gereği serbest (cinecode'un "yalnızca kullanıcı isterse" kuralını Yunus'un 28.10 izni karşılar). Higgsfield vb. kredi harcayan servis yok. |
| Yayın | Zernio adımları, thumbnail, log güncelleme aynen. Teslim dosyası `make.py final`'ın `<Title>.mp4`'ü; master MP4 scratchpad'de, önizleme ≤ 24 MB proje klasöründe. |

## 4. Kalite kapısı sırası (her render)

1. `make.py draft` → kitin kendi uyarıları (hook, karanlık, renk, ses) düzeltilir.
2. `make.py final` (1080x1920 60 fps veya uzun video çözünürlüğü).
3. Kanalın ölçümleri: `vo_check.py`, `hook_check.py`, `sfx_lib` QA, ortalama ölçümü, loudness.
4. Taze critic'ler: hook (≥ 25/30), genel (≥ 80), grafik-hiza, ses. 80 kuralı aynen.

## 5. Kayıt

Her Short/uzun videonun `brief.md`'sine `Üretim: cinecode <mod> (KIT commit <kısa sha>)` satırı ve STATE.md'nin kopyası (`cinecode/STATE.md`) konur. Daily_Routine_Run_History'ye "cinecode notu" sütunu/satırı: neyi iyi yaptı, nerede zorladı.

## 6. Deneme ölçümü ("bakalım ne kadar işe yarıyor")

cinecode ile çıkan ilk 7 gün/≥ 10 Short, önceki 10 Short ile karşılaştırılır: izlenme, viewed-vs-swiped, ort. izlenme süresi, critic puanları, üretim süresi. Sonuç `Shorts_Log.md` altına "cinecode karşılaştırması" olarak yazılır ve Yunus'a raporlanır.
