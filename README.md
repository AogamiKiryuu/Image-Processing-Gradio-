
# 📸 Aplikasi Pemrosesan Gambar dengan Python

Selamat datang di proyek **Aplikasi Pemrosesan Gambar**! 🎉  
Aplikasi ini dibuat menggunakan Python dengan library seperti **Gradio**, **OpenCV**, **NumPy**, dan **PIL**.

Aplikasi ini memungkinkan pengguna untuk mengunggah gambar dan memodifikasinya dengan berbagai fitur seperti:
- Grayscale Blending
- Denoising
- Brightness/Contrast Adjustment
- Rotasi

---

## 🛠️ Fitur dan Alur Kerja

Aplikasi ini memiliki empat fitur utama yang memungkinkan pengguna untuk memproses gambar secara interaktif:

### 1. 🌫️ Grayscale Blending
Fitur ini memungkinkan pengguna untuk mengubah gambar menjadi grayscale secara bertahap menggunakan slider (0 hingga 1).

**Konsep**:
- Gambar dikonversi ke grayscale menggunakan `cv2.cvtColor`.
- Dicampur kembali dengan gambar asli menggunakan `cv2.addWeighted`.

**Alur Kerja**:
- Gambar RGB → Grayscale
- Grayscale → RGB (agar bisa dicampur dengan warna asli)
- Slider menentukan intensitas grayscale:  
  `0 = gambar asli`, `1 = full grayscale`

---

### 2. 🧹 Denoising dengan Mean Filter
Menghaluskan gambar dengan mengurangi noise tanpa mengubah warna.

**Konsep**:
- Gunakan `cv2.blur` untuk menerapkan mean filter berdasarkan ukuran kernel.

**Alur Kerja**:
- Nilai slider menentukan kernel size.
- Kernel selalu ganjil: `max(3, int(denoise) // 2 * 2 + 1)`
- Gambar diblur agar tampak lebih bersih.

---

### 3. ☀️ Brightness dan Contrast Adjustment
Mengatur tingkat kecerahan dan kontras gambar.

**Konsep**:
- Gunakan `cv2.convertScaleAbs`:
  - `alpha` → kontras
  - `beta` → brightness

**Alur Kerja**:
- Brightness: `-100` (gelap) hingga `+100` (terang)
- Contrast: `0.1` (datar) hingga `3.0` (tajam)
- Diterapkan setelah denoising.

---

### 4. 🔄 Rotasi Gambar
Memutar gambar sesuai nilai slider dari `-180` hingga `180` derajat.

**Konsep**:
- Menggunakan transformasi geometri (`cv2.getRotationMatrix2D` + `cv2.warpAffine`).

**Alur Kerja**:
- Titik tengah dihitung dari ukuran gambar.
- Matriks rotasi dibuat dan diterapkan.
- Gambar diputar tanpa dipotong.

---

## 📊 Struktur Kode

1. **Fungsi `process_image`**  
   Menangani semua proses: grayscale → denoise → brightness/contrast → rotasi.

2. **Gradio Interface**  
   UI berbasis web untuk mengatur semua parameter via slider.

---

## 🚀 Cara Menjalankan

1. Install dependensi:

```bash
pip install gradio opencv-python numpy pillow
```

2. Simpan kode ke file Python, misalnya dengan nama:

```bash
image_processing.py
```

3. Jalankan file Python:

```bash
python image_processing.py
```

4. Setelah itu, akan muncul link dari Gradio di terminal, misalnya:

```
Running on local URL:  http://127.0.0.1:7860
```

5. Buka link tersebut di browser, unggah gambar, dan mulai bereksperimen dengan slider 🎨

---

> 💡 Pastikan Python versi 3.x sudah terinstal.  
> Jika ada error `ModuleNotFoundError`, pastikan dependensi sudah terpasang dengan benar.

---

## 🙌 Closing
Nama saya Faqih Fathurrachman dengan NPM 065122103
Kurang lebihnya mohon maaf. sign out and peace~
