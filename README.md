# Computer Vision

**Nama Projek**: Pendeteksi Wajah untuk Menentukan Umur dan Jenis Kelamin

## Latar Belakang
Teknologi pengenalan wajah (face recognition) telah mengalami perkembangan pesat dan diterapkan dalam berbagai sektor, seperti keamanan, pemasaran, dan sistem kehadiran. Salah satu kemampuan penting dari teknologi ini adalah kemampuannya untuk mendeteksi atribut demografis, seperti jenis kelamin, dari wajah seseorang. Deteksi jenis kelamin berdasarkan wajah dapat digunakan untuk analisis pelanggan, otomatisasi data, dan pengembangan aplikasi berbasis kecerdasan buatan yang lebih personal.

Namun, sebagian besar sistem pengenalan wajah masih bergantung pada input dari kamera secara real-time. Hal ini tidak selalu ideal, terutama ketika pengguna ingin menganalisis gambar yang telah tersimpan sebelumnya. Oleh karena itu, diperlukan sebuah sistem yang dapat melakukan pendeteksian wajah dan klasifikasi jenis kelamin dari gambar statis yang diunggah oleh pengguna.
Proyek ini bertujuan untuk membangun sebuah sistem berbasis Python yang dapat mendeteksi wajah dan mengklasifikasikan jenis kelamin berdasarkan gambar yang diunggah. Sistem ini akan diintegrasikan ke dalam sebuah website, memungkinkan pengguna untuk mengunggah gambar dan mendapatkan hasil analisis wajah secara langsung melalui platform web.

## Perumusan Masalah
1) Bagaimana cara mengembangkan sistem deteksi wajah yang dapat mengidentifikasi wajah pada gambar statis yang diunggah oleh pengguna
2) Bagaimana cara mengimplementasikan algoritma untuk mengklasifikasikan jenis kelamin dari wajah yang terdeteksi dalam gambar statis
3) Bagaimana memastikan akurasi deteksi wajah dan klasifikasi jenis kelamin pada berbagai kondisi gambar, seperti pencahayaan yang berbeda dan sudut pandang wajah yang beragam
4) Bagaimana mengintegrasikan sistem deteksi wajah dan klasifikasi jenis kelamin ke dalam platform web agar pengguna dapat mengunggah gambar dan mendapatkan hasil analisis secara real-time

## Batasan Masalah
1) Hanya Mendeteksi Wajah dalam Gambar Statis
2) Keterbatasan Akurasi pada Kondisi Tertentu
3) Integrasi dengan Web
  
## Tujuan
1) Membangun sistem deteksi wajah yang dapat mendeteksi dan mengenali wajah dalam gambar statis yang diunggah oleh pengguna
2) Mengembangkan algoritma klasifikasi jenis kelamin berdasarkan wajah yang terdeteksi, sehingga sistem dapat mengidentifikasi jenis kelamin pengguna secara otomatis.
3) Meningkatkan akurasi deteksi wajah dan klasifikasi jenis kelamin dengan memperhatikan berbagai faktor seperti pencahayaan, sudut pandang wajah, dan kualitas gambar
4) Mengintegrasikan sistem deteksi wajah dan klasifikasi jenis kelamin ke dalam sebuah website sehingga pengguna dapat mengunggah gambar secara mudah dan mendapatkan hasil analisis secara langsung

## Manfaat
1) Dengan adanya sistem deteksi wajah dan klasifikasi jenis kelamin pada gambar yang diunggah, pengguna dapat dengan mudah mendapatkan informasi demografis dari gambar tanpa memerlukan kamera real-time
2) Proyek ini memungkinkan otomatisasi dalam proses analisis wajah dan jenis kelamin, mengurangi waktu dan usaha yang diperlukan untuk melakukan analisis secara manual, yang berguna untuk berbagai aplikasi seperti pemasaran dan analisis data pelanggan

## Target Sistem
- Deteksi Wajah
- Klasifikasi Jenis Kelamin
- Akurasi dan Kinerja
- Antarmuka sederhana untuk input dan output hasil
- Menggunakan dataset Roboflow

## Tools & Teknologi
- Python
- YoloV8s
- Dataset: [Roboflow https://universe.roboflow.com/bethaniaworkspace/motorcycledetection-plboa](https://universe.roboflow.com/henk-bert-n4r2o/age-gender-detection-tg8pr/browse)
