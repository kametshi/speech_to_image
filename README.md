# 🎤 Voice → 🧠 AI → 🎨 Image  
**Convert any voice recording into an AI-generated image using Whisper + LLM + Flux**

This project is a Streamlit application that takes an audio file, transcribes it into text, transforms the text into an image prompt using an LLM, and finally generates an image via Flux 1.1 Pro.

---

## 🚀 Features

- 🎙 Upload voice/audio files (`wav`, `mp3`, `m4a`, `ogg`)
- 🧠 Automatic speech-to-text transcription (Google STT)
- ✨ LLM prompt generation using **Hermes 3 – Llama 3.1 405B**
- 🎨 Image generation using **Flux 1.1 Pro**
- 📸 Clean UI built with Streamlit
- 💾 Full session state (transcript, prompt, result image)

---

## 🧩 Tech Stack

| Component | Model / Library |
|----------|-----------------|
| Speech-to-Text | Google SpeechRecognition |
| LLM | `nousresearch/hermes-3-llama-3.1-405b` |
| Image Gen | `black-forest-labs/flux-1.1-pro` |
| Backend API | OpenRouter |
| UI | Streamlit |
| Audio Processing | pydub |

---

## 📦 Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/yourname/voice2img.git
cd voice2img
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Set your OpenRouter API key
```
Create .env file or edit directly:
OPENROUTER_KEY="your_api_key_here"
```

### ▶️ Run the app
```
streamlit run app.py
```

### The app will open in your browser:
[URL](https://project1.ai-softdev.com/)

## 🛠 How It Works

### 1. Upload audio
```
Any of these formats: wav/mp3/m4a/ogg.
```

### 2. Transcription
```
transcribe_online(audio_bytes)
```

Uses Google SpeechRecognition to convert speech → text.

### 3. Build an image prompt
```
build_prompt(user_text)
```

LLM rewrites your text into a detailed image prompt:
- style
- mood
- environment
- details

### 4. Generate final image
```
generate_image(prompt)
```

Flux 1.1 Pro returns a 1024×1024 generated image.

## 📂 Project Structure Overview
```bash
app.py               # Main Streamlit app
```

## 🪄 Example Workflow

- Upload audio: "a peaceful forest with soft wind"
- Whisper → “a peaceful forest with soft wind”
- LLM → “A serene green forest, soft golden sunlight, light mist, high-detail cinematic style…”
- Flux → Final image rendered on screen.

## 🧪 Supported Audio Inputs

- 🎧 Voice messages
- 🎤 Recorded speech
- 📱 Phone voice notes
- 🗣 Any spoken description

## ⚠️ Notes & Limitations

- Google STT depends on audio clarity
- Long audio files may slow down transcription
- OpenRouter models require internet access
- Whisper (local) model placeholder (/not wired)

## ❤️ Credits

- Built using:
- Streamlit
- OpenRouter
- Hermes 3 (Llama 3.1 405B)
- Flux 1.1 Pro
- SpeechRecognition
- PIL
- pydub