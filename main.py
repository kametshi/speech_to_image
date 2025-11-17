import io
import requests
import streamlit as st
import speech_recognition as sr
from PIL import Image
from audio_recorder_streamlit import audio_recorder

from config import settings

recognizer = sr.Recognizer()

def transcribe_google(audio_bytes: bytes, lang="en-US"):
    try:
        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
            audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language=lang)
    except:
        return "(speech recognition failed)"


def generate_image(prompt: str) -> Image.Image:
    url = "https://api.deepai.org/api/text2img"

    response = requests.post(
        url,
        data={"text": prompt},
        headers={"Api-Key": settings.DEEPAI_KEY}
    )
    try:
        data = response.json()
    except:
        raise Exception(f"DEEPAI ERROR — NOT JSON:\n{response.text}")

    if "output_url" not in data:
        raise Exception(f"DEEPAI ERROR:\n{data}")

    img_bytes = requests.get(data["output_url"]).content
    return Image.open(io.BytesIO(img_bytes)).convert("RGB")

st.set_page_config(page_title="Voice → Image", layout="centered")

st.markdown("""
<style>
h1 {
    background: -webkit-linear-gradient(45deg, #6a5acd, #00bfff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3rem !important;
    font-weight: 800 !important;
}
.subtitle {
    color: #666;
    text-align:center;
    margin-top: -20px;
}
.record-box {
    padding: 20px;
    border-radius: 12px;
    background: #f8f9fc;
    border: 1px solid #eaecef;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    background: #f0fff4;
    border: 1px solid #c6f6d5;
}
button[kind="primary"] {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Voice → Text → Image</h1>", unsafe_allow_html=True)

st.divider()

st.markdown("### Voice Recorder")

with st.container():
    st.markdown('<div class="record-box">Click → Speak → Click again to stop recording</div>', unsafe_allow_html=True)

audio_bytes = audio_recorder(
    pause_threshold=9999,
    energy_threshold=None,
    sample_rate=44_100
)

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

st.divider()

if st.button("Generate Image", use_container_width=True):
    if not audio_bytes:
        st.error("Please record audio first.")
    else:
        with st.spinner("Transcribing Speech..."):
            text = transcribe_google(audio_bytes)

        st.markdown(f"""
        <div class="result-box">{text}</div>
        """, unsafe_allow_html=True)

        if text != "(speech recognition failed)":
            with st.spinner("🎨 Generating Image..."):
                img = generate_image(text)

            st.image(img, use_container_width=True)
            st.success("Done!")
