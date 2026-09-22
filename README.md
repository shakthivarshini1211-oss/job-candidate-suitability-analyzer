**AI-Based Job Candidate Suitability Analyzer Using Fuzzy Logic**

**Student Information**

Student Name: Shakthi Varshini Murugan

Roll Number: 19050

**1. Introduction**

The AI-Based Job Candidate Suitability Analyzer is a web-based application that analyzes a candidate's natural-language profile and estimates their suitability for a selected job role.

The system combines Large Language Models (LLMs), LangChain, Google Gemini, and fuzzy logic to process candidate information and produce a suitability score.

The LLM understands the candidate's natural-language profile and extracts structured information, while the fuzzy inference system evaluates the candidate's suitability using fuzzy membership functions and rules.

**2. Problem Statement**

Recruiters and students may find it difficult to compare a candidate's skills, education, experience, and projects with the requirements of a job role.
This project provides an automated way to analyze these factors and produce an interpretable suitability score.

**3. Objectives**

- Extract candidate information from natural language.
- Identify job requirements.
- Calculate skill and education matching.
- Apply fuzzy logic to handle uncertain or partial information.
- Produce a suitability score between 0 and 100.
- Provide a simple web interface using Streamlit.

**4. Main Features**

- Natural Language Candidate Analysis : 
  Users can enter candidate information in normal natural language.

- AI-Based Information Extraction :
  Google Gemini extracts skills, education, experience, projects, internships, and career interest from the candidate profile.

- Predefined Job Database :
  The application provides multiple predefined job roles such as Data Analyst, Python Developer, Web Developer, Cloud Engineer, Data Scientist, AI Engineer, and others.

- Custom Job Role Analysis :
  Users can enter a custom job role. The LLM identifies relevant skills and educational backgrounds for the entered role.

- Fuzzy Logic-Based Suitability Analysis :
  The system uses a genuine fuzzy inference system with membership functions, fuzzy rules, and defuzzification.

- Suitability Score :
  The system produces a numerical suitability score between 0 and 100.

- Streamlit Web Interface :
  The project provides a simple and user-friendly browser-based interface.

- AI + Fuzzy Logic Integration :
  The LLM performs natural-language understanding and information extraction, while fuzzy logic performs the suitability evaluation.

**5. Technologies Used**
   
- Python
- LangChain
- Google Gemini
- scikit-fuzzy
- Streamlit
- NumPy
- Pydantic
- python-dotenv
- Git
- GitHub
- Streamlit Community Cloud

**6. AI Component**
   
The project uses LangChain with Google Gemini.The LLM extracts structured information from the candidate's natural-language profile.
For example, the candidate may write:I know Python and SQL and have completed two projects.
The LLM extracts information such as:
- Python
- SQL
- 2 projects

The LLM is also used to identify requirements when the user enters a custom job role.
The AI component therefore performs actual language understanding and information extraction.

**7. Fuzzy Logic Component**
   
The fuzzy inference system uses the following inputs:

- Skill Match
- Experience
- Education Match
- Project Experience

The output is:
- Suitability Score
Each input is represented using membership functions such as:

- Low
- Medium
- High

The suitability output contains:

- Poor
- Average
- Good
- Excellent

The fuzzy system performs:

1. Fuzzification
2. Fuzzy rule evaluation
3. Aggregation
4. Defuzzification

The final defuzzified value is used to produce the numerical suitability score.

**8. System Flow**

Candidate Profile
        ↓
Streamlit Interface
        ↓
LangChain + Gemini
        ↓
Structured Candidate Information
        ↓
Job Requirements
        ↓
Skill / Education / Project Matching
        ↓
Fuzzy Inference System
        ↓
Suitability Score
        ↓
Result Display

**9. Job Selection**

The application supports two methods of selecting a job.

Option 1: Select from Job Database
The user can select a job role from the predefined job database.
The application loads the corresponding skills and educational requirements.

Option 2: Enter Custom Job
The user can enter a custom job role.
The LLM analyzes the job role and identifies relevant skills and educational backgrounds.

**10. Installation and Setup**

Prerequisites

- Python 3.10 or later
- Git
- Google Gemini API key

Install and Run
Clone the repository:

git clone https://github.com/shakthivarshini1211-oss/job-candidate-suitability-analyzer.git
cd job-candidate-suitability-analyzer

Create and activate a virtual environment:
python -m venv venv

For Windows PowerShell:
.\venv\Scripts\Activate.ps1

Install the required packages:
pip install -r requirements.txt

**11. How to Run the Project**

After activating the virtual environment, run:
streamlit run app.py

The application will open in the browser, usually at:
http://localhost:8501

**12. How to Use the Project**

Step 1: Select or Enter a Job
Choose either:

- Select from Job Database
- Enter Custom Job

Step 2: Enter Candidate Profile
Enter the candidate's information in natural language.

Example:

I am a Computer Science graduate with 2 years of experience
in Python and SQL. I have completed 4 projects and one
internship. I am interested in becoming a Data Analyst.

Step 3: AI Extraction
The Gemini LLM analyzes the candidate profile and extracts structured information such as:

- Skills
- Education
- Experience
- Projects
- Internships
- Career interest

Step 4: Job Requirement Analysis
For a predefined job, the application uses the stored job requirements.
For a custom job, the LLM identifies the relevant skills and educational backgrounds.

Step 5: Fuzzy Evaluation
The extracted information is passed to the fuzzy inference system.
The system performs fuzzification, fuzzy rule evaluation, aggregation, and defuzzification.

Step 6: View the Result
The application displays the candidate's suitability result and suitability score.

**13. Project Structure**
job-candidate-suitability-analyzer/
│
├── app.py
├── fuzzy_logic.py
├── llm_extractor.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    └── output.png

  14. Screenshots
      


**14. Live Deployment**

Live Application:
https://shakthivarshini1211-oss-job-candidate-suitability-an-app-nufox1.streamlit.app/

**15. GitHub Repository**

GitHub Repository:
https://github.com/shakthivarshini1211-oss/job-candidate-suitability-analyzer
