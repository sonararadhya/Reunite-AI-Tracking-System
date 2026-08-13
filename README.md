<div align="center">
  <img src="https://img.icons8.com/color/150/000000/artificial-intelligence.png" alt="AI Icon"/>
  <br/>
  
  <h1>🌟 ARADHYA SONAR - AI Tracking & Reunion System 🌟</h1>
  
  <p>
    <strong>An Innovative Computer Vision & AI Platform for Tracking and Reuniting Missing Individuals</strong>
  </p>
  
  [![Author](https://img.shields.io/badge/Author-Aradhya_Sonar-blue?style=for-the-badge&logo=github)](https://github.com/sonararadhya)
  [![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python)](https://www.python.org/)
  [![Django](https://img.shields.io/badge/Django-5.2-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
  [![OpenCV](https://img.shields.io/badge/OpenCV-AI-red?style=for-the-badge&logo=opencv)](https://opencv.org/)
  
  <p align="center">
    <a href="#overview">Overview</a> • 
    <a href="#key-features">Key Features</a> • 
    <a href="#technology-stack">Technology Stack</a> • 
    <a href="#project-architecture">Architecture</a> • 
    <a href="#getting-started">Installation</a>
  </p>
</div>

---

## 🚀 Overview

Welcome to the **AI Tracking & Reunion System**, crafted by **Aradhya Sonar**. This powerful platform acts as an intelligent safeguard, leveraging cutting-edge AI and advanced computer vision algorithms to significantly accelerate the process of locating missing persons and ensuring their safe return to their families.

By integrating real-time facial recognition, decentralized RTSP camera tracking, and a comprehensive centralized database, this system enhances modern security and law enforcement capabilities.

## ✨ Key Features

- **🧠 Advanced Facial Recognition**: Employs deep-learning ArcFace models to achieve unparalleled accuracy in face matching, even under challenging lighting conditions or angles.
- **📍 Live RTSP Camera Tracking**: Connects with global or local surveillance streams to autonomously analyze live video feeds.
- **🚨 Instant AI Alerts**: Sends real-time notifications to administrators and law enforcement personnel upon detecting a positive match.
- **🛡️ Secure Command Center**: A Django-powered centralized dashboard that enables law enforcement to manage cases, monitor sightings, and coordinate operations effectively.
- **⚡ Asynchronous Processing**: Utilizes Celery and Redis to handle intensive image processing tasks in the background without losing frames.
- **🌍 Geospatial Mapping**: Instantly calculates the nearest police stations upon a positive sighting to facilitate prompt assistance.

## 🛠 Technology Stack

This project integrates established frameworks with state-of-the-art machine learning tools.

| Category | Technology |
| :--- | :--- |
| **Backend Framework** | Django 5.2, Python |
| **Asynchronous Engine** | Celery, Redis |
| **Database** | SQLite3 / Django ORM |
| **AI & Computer Vision** | OpenCV, InsightFace (RetinaFace & ArcFace) |
| **Data Analytics** | NumPy, Scikit-Learn |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap |

## 📂 Project Architecture

```text
Reunite-AI-Tracking-System/
├── Reunite/                 # Core Django Configuration & Settings
│   ├── settings.py          # Environment, Security, and Application Configuration
│   ├── urls.py              # Root URL Routing
│   └── wsgi.py / asgi.py    # Server Gateway Interfaces
├── cases/                   # Missing Person AI Match Engine
│   ├── ai_processor.py      # Core InsightFace Model Logic
│   ├── models.py            # Case Data & Face Embeddings
│   ├── tasks.py             # Asynchronous Celery Processing
│   └── views.py             # Match Logic & Reporting
├── police/                  # Law Enforcement Dashboard
│   ├── models.py            # Officer Profiles
│   └── views.py             # Authentication & Case Handling
├── static/                  # Static Assets
│   ├── assets/              # Vendor Libraries (Bootstrap, AOS)
│   ├── img/                 # Application Imagery & Emblems
│   └── missing_persons/     # Pre-processed Headshots
├── templates/               # User Interface
│   ├── base.html            # Master Layout
│   └── index.html           # Command Center View
├── data/                    # Geospatial & Department Datasets
│   ├── locations.csv        
│   └── police_stations.csv  
├── docs/                    # Project Documentation & Diagrams
│   ├── images/              
│   ├── certificates/        # Achievements and Awards
│   └── Final_Year_Project_Report.pdf
├── scripts/                 # Standalone utilities
│   └── rtspCam.py           # 🎥 Live Surveillance Script
├── requirements.txt         # Dependencies
└── manage.py                # Django CLI
```

## 💻 Getting Started

### 1. Environment Setup

Clone the repository and establish your environment:
```bash
git clone https://github.com/sonararadhya/Reunite-AI-Tracking-System.git
cd Reunite-AI-Tracking-System
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Ensure that you have the necessary system-level dependencies for OpenCV and Redis installed).*

### 3. Initialize Services

**Start Redis Server (Linux):**
```bash
sudo service redis-server start
```

**Run Database Migrations:**
```bash
python manage.py migrate
```

### 4. Boot up the Ecosystem
You will need multiple terminal windows to run the complete setup:

**Terminal 1 (Web Dashboard):**
```bash
python manage.py runserver
```

**Terminal 2 (AI Background Worker):**
```bash
celery -A Reunite worker -l info -P solo
```

**Terminal 3 (Live Surveillance):**
```bash
python scripts/rtspCam.py
```

## 🏆 Certifications & Reports

- **Final Year Project Report:** [Access the comprehensive project report](./docs/Final_Year_Project_Report.pdf)
- **Project Certificate:** [View Certificate](./docs/certificates/PROJECT_CERTIFICATE.pdf)

**Project Competition Award:**
![Project Competition Award](./docs/certificates/Project_Competition.png)

---

## 👤 Author & Creator

**Developed and maintained by Aradhya Sonar.**

🔗 **GitHub:** [https://github.com/sonararadhya](https://github.com/sonararadhya)

> *"Empowering communities through artificial intelligence to reunite loved ones."*

---
*📝 Last maintained: August 13, 2026 at 03:08 UTC*
