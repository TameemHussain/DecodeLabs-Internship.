# Multi-Project Showcase: AI, ML, and Rule-Based Systems

Welcome to my central projects repository. This repository features three production-ready Python applications demonstrating core software engineering principles, machine learning pipelines, and recommendation systems.

---

## 🛠️ Project Portfolio

| # | Project Name | Tech Stack | Core Concept |
|---|---|---|---|
| 1 | [Simple Rule-Based Chatbot](#1-simple-rule-based-chatbot) | Python (Standard Library) | Control Flow, String Cleaning, Loops |
| 2 | [Simple Classification Model using AI](#2-simple-classification-model-using-ai) | Python, Pandas, Scikit-Learn | Supervised ML, Feature Scaling, KNN Classifier |
| 3 | [Content-Based Movie Recommendation System](#3-content-based-movie-recommendation-system) | Python (Standard Library) | Weighted Similarity Vectoring, Progress UI |

---

## 1. Simple Rule-Based Chatbot

A lightweight, interactive Python chatbot designed to showcase clean code architecture, deterministic state routing, and robust error/stream handling.

### Core Features
- **Interactive Loop:** A resilient `while True` main execution loop.
- **Case-Insensitive Input Processing:** `.strip().lower()` input sanitization to filter out whitespace and casing discrepancies.
- **Randomized System Responses:** Utilizes `random.choice()` variations to dynamicize greeting sequences.
- **Graceful Termination:** Intercepts system interrupts (`KeyboardInterrupt`, `EOFError`) and exit phrases to kill execution cleanly.

### How to Run
```bash
python chatbot.py

