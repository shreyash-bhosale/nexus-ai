# NEXUS AI

> **AI That Understands Your Computer**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

NEXUS AI is an AI-powered desktop assistant that understands what is happening on your computer in real time.

Unlike traditional AI chatbots that only respond to typed prompts, NEXUS AI is designed to understand the user's current desktop context—with permission—by combining screen capture, computer vision, OCR, memory, and large language models.

The long-term vision is to build an intelligent desktop companion capable of seeing, understanding, remembering, and assisting users naturally while they work.

---

## ✨ Vision

Imagine pressing a single shortcut and asking:

> "Explain this."

NEXUS AI already knows what you're looking at.

Whether you're:

- 💻 Debugging code
- 📄 Reading a PDF
- 🎥 Watching a tutorial
- 📊 Reviewing a presentation
- 🛒 Comparing products online

NEXUS AI understands your current screen and provides contextual assistance.

---

## 🎯 Current Status

Current Version:

```text
v0.1.0
```

Completed:

- ✅ Project architecture
- ✅ Python package structure
- ✅ Logging system
- ✅ Configuration system
- ✅ Runtime path management
- ✅ Screen capture service

In Progress:

- 🚧 Image preprocessing pipeline

---

## 🏗 Architecture

```
                User
                  │
                  ▼
         Global Shortcut
                  │
                  ▼
        Screen Capture Service
                  │
                  ▼
         Image Processing
                  │
                  ▼
               OCR Engine
                  │
                  ▼
           Vision AI Model
                  │
                  ▼
          Context Builder
                  │
                  ▼
          Large Language Model
                  │
                  ▼
             Desktop UI
```

---

## 📂 Project Structure

```text
nexus-ai/

├── src/
│   └── nexus_ai/
│       ├── core/
│       ├── features/
│       ├── models/
│       ├── services/
│       ├── ui/
│       └── main.py
│
├── data/
├── docs/
├── assets/
├── tests/
│
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11 |
| UI | PySide6 *(planned)* |
| Screen Capture | MSS |
| OCR | EasyOCR *(planned)* |
| Computer Vision | OpenCV *(planned)* |
| AI | OpenAI Vision API *(planned)* |
| Memory | ChromaDB *(planned)* |
| Automation | PyAutoGUI *(planned)* |

---

## 🗺 Roadmap

### Phase 0
- [x] Project foundation
- [x] Repository setup
- [x] Architecture

### Phase 1
- [x] Screen capture
- [ ] Image preprocessing
- [ ] OCR
- [ ] Vision AI
- [ ] Context builder

### Phase 2
- [ ] Floating desktop assistant

### Phase 3
- [ ] Voice interaction

### Phase 4
- [ ] Long-term memory

### Phase 5
- [ ] Desktop automation

### Phase 6
- [ ] AI coding assistant

### Phase 7
- [ ] Research assistant

### Phase 8
- [ ] Multi-agent system

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/shreyash-bhosale/nexus-ai.git
```

Enter the project:

```bash
cd nexus-ai
```

Create a virtual environment:

```bash
python3.11 -m venv .venv
```

Activate it:

macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python -m nexus_ai.main
```

---

## 📸 Demo

Coming soon.

---

## 🤝 Contributing

Contributions will be welcome once the first stable MVP is completed.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shreyash Bhosale**

Building NEXUS AI one production-quality phase at a time.