# Fuzzy Sleep Quality Recommendation

## Overview

This project is a fuzzy logic-based system that recommends personalized advice to improve sleep quality.  
It takes into account:

- Sleep Duration
- Screen Time Before Bed
- Stress Level
- Room Environment

It uses **Flask** (for the web app), **scikit-fuzzy** (for fuzzy logic), and **Matplotlib** (for visualizations).

---

## Features

- Input your current sleep-related habits.
- Get an estimated sleep quality (Poor, Fair, Good, Very Good, Excellent).
- Receive actionable recommendations tailored to your situation.
- Visualize fuzzy membership functions for all input and output variables.
- Clean and user-friendly interface with a responsive design.

---

## How to Run Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/fuzzy-sleep-quality.git
   cd fuzzy-sleep-quality
   ```

2. **(Optional but recommended) Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**

   ```bash
   python app.py
   ```

5. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

---

## Folder Structure

```
/static/visualisations/      # Saved plots of membership functions
/templates/                  # HTML templates (index.html, visualizations.html)
app.py                       # Flask application
fuzzy_system.py              # Fuzzy logic system definitions
rules.py                     # Fuzzy rules for sleep quality assessment
memberships.py               # Script to generate membership function visualizations
requirements.txt             # Python dependencies
README.md                    # Project description (this file)
```

---

## Requirements

- Python 3.x
- Flask
- numpy
- scikit-fuzzy
- matplotlib
- pandas
- scipy
- networkx

_(All dependencies are listed in `requirements.txt`.)_

---

## Notes

- **No database** is required.
- Designed for **local demonstrations and human evaluation**.
- In this study, the system was evaluated at **Bern Hauptbahnhof (Bern HB)**.
- Recommendations are based on fuzzy logic calculations and best sleep practices.
- Designed for clarity, usability, and scientific demonstration.

---

# 🚀 Enjoy helping people sleep better with science!
