import streamlit as st
import cv2
import numpy as np
from PIL import Image
from deepface import DeepFace
import matplotlib.pyplot as plt
import io

st.set_page_config(
    page_title="Deteksi Umur & Gender",
    page_icon="🧠",  # atau ganti dengan emoji/logo path
    layout="centered"
)

st.title("🧠 Deteksi Umur & Gender")
st.markdown(
    "Unggah gambar yang berisi satu atau lebih wajah. "
    "Sistem akan menampilkan kotak, umur, gender, grafik gender, rata-rata umur, "
    "dan tombol unduh hasil gambar."
)

# Upload gambar
uploaded_file = st.file_uploader("Unggah gambar wajah", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Baca dan tampilkan gambar
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Gambar yang diunggah", use_column_width=True)

    # Convert ke format OpenCV
    img_np = np.array(image)
    if img_np.shape[2] == 4:  # Jika RGBA, ubah ke RGB
        img_np = cv2.cvtColor(img_np, cv2.COLOR_RGBA2RGB)

    # Tombol untuk deteksi
    if st.button("🔍 Deteksi Wajah, Umur & Gender"):
        try:
            # Gunakan detector retinaface untuk deteksi wajah yang lebih akurat
            results = DeepFace.analyze(
                img_path=img_np,
                actions=['age', 'gender'],
                detector_backend='retinaface',
                enforce_detection=False
            )

            # Bungkus ke list jika hanya satu wajah
            if not isinstance(results, list):
                results = [results]

            if len(results) == 0:
                st.warning("⚠️ Tidak ada wajah yang terdeteksi.")
            else:
                # Siapkan variabel
                img_result = img_np.copy()
                gender_count = {"Man": 0, "Woman": 0}
                total_age = 0
                jumlah_wajah = 0

                for result in results:
                    region = result.get('region', {})
                    x, y, w, h = region.get('x', 0), region.get('y', 0), region.get('w', 0), region.get('h', 0)
                    gender = result.get('dominant_gender', 'Unknown')
                    age = result.get('age', '?')

                    # Hitung usia dan jumlah wajah valid
                    if isinstance(age, (int, float)):
                        total_age += age
                        jumlah_wajah += 1

                    # Hitung jenis kelamin
                    if gender in gender_count:
                        gender_count[gender] += 1
                    else:
                        gender_count[gender] = 1

                    # Gambar kotak dan label
                    cv2.rectangle(img_result, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    label = f"{gender}, {age} th"
                    cv2.putText(img_result, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (0, 255, 0), 2)

                # Tampilkan hasil gambar
                st.image(img_result, channels="RGB", caption="📌 Hasil Deteksi", use_container_width=True)

                # Diagram batang gender
                st.subheader("📊 Distribusi Jenis Kelamin")
                fig, ax = plt.subplots()
                ax.bar(gender_count.keys(), gender_count.values(), color=["blue", "pink"])
                ax.set_ylabel("Jumlah")
                ax.set_title("Jumlah Wajah Berdasarkan Jenis Kelamin")
                st.pyplot(fig)

                # Rata-rata umur
                if jumlah_wajah > 0:
                    rata_rata_umur = round(total_age / jumlah_wajah, 1)
                    st.info(f"🎂 **Rata-rata umur dari {jumlah_wajah} wajah:** {rata_rata_umur} tahun")

                # Buat tombol download gambar hasil
                hasil_image = Image.fromarray(img_result)
                buffered = io.BytesIO()
                hasil_image.save(buffered, format="PNG")
                img_bytes = buffered.getvalue()

                st.download_button(
                    label="⬇️ Unduh Hasil Gambar",
                    data=img_bytes,
                    file_name="hasil_deteksi.png",
                    mime="image/png"
                )

        except Exception as e:
            st.error("❌ Terjadi kesalahan saat analisis.")
            st.exception(e)
