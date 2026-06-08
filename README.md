# AI-Chatbot

A simple rule-based Python chatbot that demonstrates core programming concepts: control flow, conditional logic, and interactive loops.

## Core Concepts Demonstrated

- **Interactive Loop:** A `while True` loop keeps the application active until an exit command is received.
- **Case-Insensitive Input Processing:** `.strip().lower()` cleans user input to handle inputs like "Hello", "HELLO", or "  hello  ".
- **Conditional Routing:** An `if-elif-else` control structure evaluates conditions to generate appropriate responses.
- **Randomized Responses:** The `random.choice()` function selects dynamic greetings from a list of variations.

## How to Run

1. Make sure Python 3 is installed.
2. Open your terminal or Command Prompt.
3. Run the script:
   ```bash
   python chatbot.py
   ```
4. Interact with the chatbot by typing `hello`, `hi`, or `exit`.

# Project 02 (Simple Classification Model using AI)
Description
This project implements a complete, end-to-end Machine Learning workflow using Python and scikit-learn to classify species from the classic Iris dataset. It handles data loading, splitting into training and testing sets, feature scaling via standardization, and trains a K-Nearest Neighbors (KNN) classifier. The project concludes by generating comprehensive evaluation metrics (Accuracy, Classification Report, and Confusion Matrix) and running a live inference test on a brand-new data sample.

Prerequisites: Make sure you have Python 3 and the required dependencies installed. You can install them via terminal:

Bash
pip install pandas scikit-learn

# Project 03 AI based Recommendation System

A content-based movie recommendation system written in Python that utilizes a weighted similarity matching algorithm to suggest films based on user-defined genres, moods, and rating preferences.

## Features

- **Weighted Matching Engine:** Calculates a normalized match score ($0.0$ to $1.0$) by giving distinct priorities to different categories (Genre match = 2 points, Mood match = 1.5 points)[cite: 4].
- **Dynamic Threshold Filtering:** Excludes movies that fall below a user-specified minimum IMDb rating[cite: 4].
- **Visual Terminal UI:** Displays recommendation match percentages using an elegant text-based progress bar (`████░░░░`)[cite: 4].
- **Dual-Mode Execution:** Operates as an interactive command-line interface by default, with an automated fallback demo mode if the input stream is interrupted[cite: 4].

## How to Run

1. **Prerequisites:** Make sure you have Python 3 installed on your system. No external libraries are required.
2. **Open Terminal:** Navigate to the folder containing the project files.
3. **Run the Project:** Execute the script by running the following command verbatim:
```bash
   python "Project 3(Recomendation System).py"


