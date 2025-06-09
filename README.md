
````markdown
# 🌿 Zephyre-Derma-AI

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](#tech-stack)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](#contributing)

**Zephyre** is a smart, AI-powered dermatological assistant that detects your skin type using computer vision and recommends weather-aware skincare routines. Built for personalization, powered by machine learning.

---

## 🚀 Live Demo

🌐 **Coming soon via Streamlit / Web Hosting**  
*(Contact contributors for access or local demo setup instructions below)*

---

## 📌 Features

- 🎥 **Live Webcam Skin Scanner**  
- 🧠 **CNN Model for Skin Type Classification (19 types)**  
- ☀️ **Weather API Integration** (city-based)  
- 🧴 **Personalized Derma Suggestions** (LLM + web scraping hybrid)  
- 🌫️ **Animated Glassmorphism UI** with real-time visuals  
- 🧾 **MongoDB Logging** for user prediction history  
- 🧊 **Modern Frontend**: Lottie animations, responsive layout, Flex/Grid

---

## 🏗️ Architecture Overview

```text
[User Image] → [Skin Type Classifier (CNN)] → [Predicted Skin Type]
                            ↓
                [Weather API (City)]
                            ↓
   → [LLM + Scraper] → Derma Suggestions
                            ↓
          [MongoDB Logs] & [Frontend Display]
````

---

## 🧪 Tech Stack

| Layer           | Technology                                     |
| --------------- | ---------------------------------------------- |
| **Frontend**    | HTML, CSS, JavaScript, Flask, Lottie, Tailwind |
| **Backend**     | Python, Flask, OpenCV, TensorFlow/Keras        |
| **AI Model**    | CNN for Skin Type Classification               |
| **Database**    | MongoDB                                        |
| **Weather API** | OpenWeatherMap                                 |
| **NLP**         | OpenAI API (for GenAI-based skincare tips)     |
| **Scraping**    | Selenium (for backup derma scraping)           |

---

## 🧠 ML Model Highlights

* Model: Custom Convolutional Neural Network
* Dataset: Curated + augmented dataset of diverse skin types
* Classes: 19 skin type categories (e.g., oily, dry, normal, combination, acne-prone)
* Accuracy: \~92% on validation data
* Framework: TensorFlow/Keras

---

## 📦 Installation (Local)

```bash
git clone https://github.com/zephyre-labs/Zephyre-Derma-AI.git
cd Zephyre-Derma-AI
pip install -r requirements.txt
python app.py
```

Make sure you:

* Have Python 3.8+
* Add your API keys to `config.py`
* Enable webcam access for live detection

---

## 🧬 Sample Prediction Output

```json
{
  "skin_type": "Oily and Acne-Prone",
  "confidence": 0.94,
  "weather": {
    "temperature": "35°C",
    "humidity": "64%",
    "condition": "Sunny"
  },
  "suggestion": "Use oil-free moisturizers with SPF 30+, gentle cleansers, avoid heavy makeup..."
}
```
---

## 🖼️ Screenshots

### 🔐 Login Page  
![Login Page](assets/screenshot_1.png)

### 📸 Camera Interface – Image Capture  
![Camera Capture](assets/screenshot_2.png)

### 🧴 AI-Powered Skincare Suggestions  
**Step 1 – Personalized Output**
![Skin Suggestion UI](assets/screenshot_3.png)

**Step 2 – Further Recommendations**
![Skin Suggestion Follow-up](assets/screenshot_4.png)

---

### 🧪 Raw Output Screens (Console + Backend Logs)

**Prediction Result – JSON Output**
![Raw Output 1](assets/Screenshot_5.png)

**Weather API Response**
![Raw Output 2](assets/screenshot_6.png)

**Combined Model Output**
![Raw Output 3](assets/screenshot_7.png)

<p align="center">
  <img src="assets/screenshot_3.png" width="600" />
  <br/>
  <i>Figure: AI-generated skincare suggestions based on live skin classification and weather input</i>
</p>

---

---

## 🤝 Contributing

We welcome PRs, suggestions, and issue reports.

```bash
git checkout -b feature/my-feature
git commit -m "Add: my feature"
git push origin feature/my-feature
```

Check out our [contributing guide](CONTRIBUTING.md) *(coming soon)*.

---

## 👥 Team Zephyre

* **Selcii Maria** – AI/ML, Full Stack, System Architecture
* **Maha Shan** – Frontend, Data Engineering, Integration

Special thanks to Healthline, OpenWeather, OpenAI & TensorFlow community.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧭 Roadmap

* [ ] Deploy on Streamlit / Vercel
* [ ] Add face detection to crop regions of interest
* [ ] Introduce multilingual support
* [ ] Build Android/iOS wrapper via Flutter
* [ ] Run A/B tests on derma suggestions

---

## 🌐 Useful Links

* [Skin Type Classification Dataset (if open)](link)
* [OpenWeatherMap API](https://openweathermap.org/)
* [Selenium Scraper Guide](docs/scraping.md)
* [LLM Prompt Engineering Notes](docs/llm.md)

---

> “Zephyre is not just a project — it’s your AI-powered skincare companion.”
> *Crafted with care by humans, powered by machines.*

```

