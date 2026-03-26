import streamlit as st
import zipfile 
import io
from pathlib import Path
from logic import convert_heic_bytes_to_jpg

st.title("HEIC to JPG Converter")
st.write("Upload one or more HEIC files to convert them to JPG format.")
quality = st.slider("JPEG Quality", min_value=1, max_value=95, value=85)
uploaded_files = st.file_uploader(
    "Uploaded HEIC files",
    type=["heic", "HEIC"],
    accept_multiple_files=True
)
if uploaded_files:
    st.write(f"Found {len(uploaded_files)} ")
if len(uploaded_files) == 1:
    file = uploaded_files[0]
    converted = convert_heic_bytes_to_jpg(file.read(), quality)
    st.success(f"Converted: {file.name}")
    st.download_button(
        label="Download JPG",
        data=converted,
        file_name=Path(file.name).stem + ".jpg",
        mime="image/jpeg"
        )
else:
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for file in uploaded_files:
            converted = convert_heic_bytes_to_jpg(file.read(), quality)
            zip_file.writestr(Path(file.name).stem + ".jpg", converted.read())
            st.success(f"Converted: {file.name}")

    zip_buffer.seek(0)
    st.download_button(
        label="Download All as ZIP",
        data=zip_buffer,
        file_name="converted_images.zip",
        mime="application/zip"
        )