# 🎤 Voice → 🎨 Image Generator

> Instantly convert recorded speech into an AI-generated image using Streamlit, Google STT, and DeepAI.

---

## 🚀 Key Features

| Feature | Description |
| :--- | :--- |
| 🎙️ Voice Recording | `audio_recorder_streamlit` captures microphone input directly in the browser. |
| 🧠 Speech-to-Text | Google STT via `speech_recognition.recognize_google`. |
| 🎨 Image Generation | `requests.post` to DeepAI `text2img` API. |
| ✨ UI | Built entirely with Streamlit. |

---

## ⚙️ Tech Stack

| Component | Technology / Service |
| :--- | :--- |
| UI | Streamlit |
| Audio Capture | audio-recorder-streamlit |
| STT Engine | SpeechRecognition (Google STT) |
| Image Gen | DeepAI Text2Img API |
| Language | Python |

---
## [Demo Version](https://project2.ai-softdev.com)
## 📦 Installation & Run

### Clone the repository

```
git clone https://github.com/kametshi/speech_to_image.git
cd speech_to_image
```

### Install dependencies

```
pip install -r requirements.txt
```

### API Key Configuration (config.py)

```
# config.py
class Settings:
    DEEPAI_KEY = "YOUR_DEEPAI_API_KEY_HERE"

settings = Settings()
```


### Launch the app

```
streamlit run app.py
```

### 🛠 Key Functions (app.py)

```
# transcribe_google

def transcribe_google(audio_bytes: bytes, lang="en-US"):
    try:
        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:
            audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data, language=lang)
    except:
        return "(speech recognition failed)"
```

```
# generate_image

def generate_image(prompt: str) -> Image.Image:
    url = "[https://api.deepai.org/api/text2img](https://api.deepai.org/api/text2img)"
    response = requests.post(
        url,
        data={"text": prompt},
        headers={"Api-Key": settings.DEEPAI_KEY}
    )
    return Image.open(io.BytesIO(img_bytes)).convert("RGB")
```

### Main Streamlit Logic

```
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
```

## Supported Audio Inputs

- 🎤 Recorded speech
- 🗣 Any spoken description





