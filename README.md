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

**Open Terminal:** Navigate to the directory containing your script (e.g., `classification_model.py`).
3. **Execute:** Run the following command to execute the pipeline:
   ```bash
python classification_model.py

#Project 3 Recomendation System
Description
This project implements an interactive movie recommendation engine using a weighted, content-based similarity algorithm. The system evaluates user-selected genres and moods against a curated movie catalog, assigning custom weights to distinct feature types (e.g., genre matches are heavily weighted relative to mood alignment) to compute a standardized similarity score. It filters movies based on custom IMDb thresholds and features a visual, text-based progress bar to represent match percentages. A resilient fallback system switches to a multi-scenario demonstration mode if user input is interrupted.

#How to Run
Prerequisites: Ensure you have Python 3 installed. This script relies entirely on standard libraries and does not require any external package installations.

Open Terminal: Navigate to the folder containing your script (e.g., movie_recommender.py).

Execute: Run the command below to launch the system:

Bash
python movie_recommender.py
