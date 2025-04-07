# Hatchkings Otomasyon Botu 🐣🎮

Bu Python projesi, **Hatchkings** oyununu daha verimli oynamanıza yardımcı olmak için geliştirildi. Oyundaki belirli durumları tespit ederek, kullanıcı etkileşimine ihtiyaç duymadan otomatik olarak aksiyon alır.

## 🔧 Ne İşe Yarar?

Bu bot, oyunda şu gibi işlemleri otomatikleştirir:

- **Seviye atlandığında** otomatik olarak devam etmenizi sağlar.
- **Yumurta açma ekranlarında** “Open” butonuna tıklar.
- **Eksik anahtar nedeniyle devam edilemeyen** durumlarda “Continue” veya “Got It” gibi uyarılarda otomatik geçiş yapar.
- Yüzlerce spin sırasında sürekli başında bekleme ihtiyacını ortadan kaldırır.

## 🖼️ Görsel Tanıma

Bot, ekran görüntüsündeki butonları tanımak için `PyAutoGUI` kütüphanesini kullanır. Varsayılan olarak aşağıdaki görselleri arar:

- `open_button.png`
- `continue_button.png`
- `gotit_button.png`

Eğer bot istediğiniz gibi çalışmıyorsa:
- Kendi bilgisayarınızda bu butonların ekran görüntülerini alın,
- Yukarıdaki adlarla `.png` formatında **bot.py ile aynı klasöre** kaydedin.

## 🧪 Kurulum

### 1. Gerekli kütüphaneleri yükleyin

```bash
pip install -r requirements.txt
