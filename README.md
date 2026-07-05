Intelligent Code Reviewer & Explainer

This project was developed as part of the DecodeLabs Generative AI Internship (Week 4).

The main objective of this project is to review source code using Google's Gemini AI model. It analyzes the given code, explains what it does, identifies possible bugs, suggests improvements, estimates time complexity, and generates an optimized version of the code.

Project Features

- Reviews source code using Gemini AI
- Explains the functionality of the code in simple language
- Detects logical errors and potential bugs
- Suggests optimization and coding best practices
- Provides an approximate time complexity
- Generates an improved version of the code
- Saves the review report automatically

Technologies Used

- Python 3.12
- Google Gemini API
- google-genai
- Rich
- Markdown

Project Structure

```
Task 4 - Intelligent Code Reviewer & Explainer

app.py
reviewer.py
prompt.py
config.py
requirements.txt
README.md

sample_code/
reports/
screenshots/
```

Installation

Clone the repository

```bash
git clone https://github.com/Falgunn014/DecodeLabs-Internship.git
```

Go to the project folder

```bash
cd "Task 4 - Intelligent Code Reviewer & Explainer"
```

Install the required packages

```bash
pip install -r requirements.txt
```

Configuration

Open the `config.py` file and replace the placeholder with your own Gemini API key.

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

Running the Project

```bash
python app.py
```

Example

Input

```
Enter source code file path:
sample_code/sample.py
```

The application analyzes the file and displays a detailed review in the terminal. A copy of the review is also saved in the `reports` folder.

Learning Outcomes

During this project, I learned how to integrate the Gemini API into a Python application, design effective prompts for code analysis, read source code from files, generate AI-powered reviews, and organize a Python project with a clean folder structure.

Future Improvements

- Support for reviewing multiple files
- PDF report generation
- Web interface using Streamlit
- Code quality scoring
- GitHub repository analysis

Author

Falgun Nagpure

DecodeLabs Generative AI Internship – Week 4
