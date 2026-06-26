#  AI Resume Analyzer using Flask & Google Gemini AI

An AI-powered web application that analyzes resumes and provides intelligent feedback using Google's Gemini AI. Users can paste their resume into the application, and the AI generates a structured analysis including strengths, weaknesses, missing skills, and suggestions for improvement.

---

#  Project Overview

The AI Resume Analyzer is a beginner-friendly Artificial Intelligence project built using Flask and the Google Gemini API.

The application accepts a resume as input, sends it to the Gemini AI model for analysis, and displays a detailed report on the website. This project demonstrates how Large Language Models (LLMs) can be integrated into web applications using Python and Flask.

---

# 🚀 Features

* 🤖 AI-powered Resume Analysis
* 📄 Resume Summary
* 💪 Strength Identification

# 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### AI Model

* Google Gemini API

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

# 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── templates/
│      └── index.html
│
├── static/
│      └── style.css
│
└── screenshots/
       ├── home.png
       └── analysis.png
```
# 🧠 How It Works

1. The user opens the website.
2. The user pastes their resume into the text area.
3. JavaScript sends the resume to the Flask backend using a POST request.
4. Flask receives the resume and creates a prompt for the Gemini AI model.
5. The backend sends the prompt to the Gemini API.
6. Gemini analyzes the resume.
7. The AI returns a structured response.
8. Flask sends the response back to the frontend.
9. The website displays the analysis instantly.

---

# 🔄 Application Workflow

```
User

   │

   ▼

Paste Resume

   │

   ▼

HTML + CSS + JavaScript

   │

   ▼

Flask Backend

   │

   ▼

Google Gemini API

   │

   ▼

AI Resume Analysis

   │

   ▼

JSON Response

   │

   ▼

Display Result on Website
```

---

# 📊 AI Analysis Includes

* Resume Summary
* Strengths
* Weaknesses
* Missing Skills
* Improvement Suggestions

---

# 📸 Screenshots

Add your screenshots inside the **screenshots** folder.

Example:

```
screenshots/

home.png

analysis.png
```
---

# 💻 Skills Demonstrated

This project demonstrates knowledge of:

* Python Programming
* Flask Web Framework
* REST API Concepts
* JSON Data Handling
* Prompt Engineering
* Google Gemini API Integration
* Frontend and Backend Communication
* Environment Variables (.env)
* Git & GitHub

---

# 👨‍💻 Author

**Aman Srivastava**

B.Tech Computer Science Engineering

Interested in Artificial Intelligence, Cybersecurity and Full Stack Development.

---

# ⭐ If you found this project useful, consider giving it a Star.
