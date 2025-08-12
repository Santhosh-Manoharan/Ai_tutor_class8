# Ai_tutor_class8

## 🌟 Class 8 Science AI Tutor

This repository contains an AI-powered tutor designed to assist students in learning NCERT Class 8 Science curriculum topics. The tutor uses Retrieval-Augmented Generation (RAG) techniques to provide accurate and contextually relevant answers based on the official NCERT textbook.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files in the Repository](#files-in-the-repository)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview

The **Class 8 Science AI Tutor** is an educational tool that leverages advanced natural language processing techniques to answer questions related to the NCERT Class 8 Science curriculum. It uses a combination of semantic search and contextual understanding to provide precise and informative responses.

## Features

- **Retrieval-Augmented Generation (RAG):** Utilizes FAISS for efficient retrieval of relevant textbook content.
- **NCERT Curriculum Aligned:** Strictly adheres to the NCERT Class 8 Science textbook.
- **Interactive Web Interface:** Built using Streamlit for an intuitive user experience.
- **Source Transparency:** Displays chapter references for all answers.
- **Performance Metrics:** Includes BLEU and ROUGE-L scores for evaluation.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Santhosh-Manoharan/Ai_tutor_class8.git
   cd Ai_tutor_class8

2. **Set Up Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
    # or
    source .venv/bin/activate

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run the Application:**
    ```bash
    streamlit run app.py
This will start the web application at http://localhost:8501.


## Usage
Open your web browser and navigate to http://localhost:8501.
Enter your question in the input box and click "Get Answer."
The AI Tutor will retrieve relevant information from the NCERT Class 8 Science textbook and provide a response along with source citations.

## Files in the Repository
ai_tutor_class8.ipynb: Jupyter Notebook containing the implementation logic.
app.py: Streamlit application code for the web interface.
class8_science.jsonl: Processed textbook data used by the tutor.
report.md: Project report detailing methodology, results, and future work.
README.md: This file.
Other files: Supporting files like index files, configuration files, etc.

## Evaluation
The performance of the AI Tutor has been evaluated using BLEU and ROUGE-L metrics. Results are available in the evaluation.csv file.

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!

## Contact
For any questions or feedback, feel free to reach out:

Email: santhosh.manoharan107@gmail.com
GitHub: Santhosh-Manoharan
