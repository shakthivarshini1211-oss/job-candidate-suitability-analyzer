# AI-Based Job Candidate Suitability Analyzer Using Fuzzy Logic

## 1. Introduction

The AI-Based Job Candidate Suitability Analyzer is a web-based application
that analyzes a candidate's natural-language profile and estimates their
suitability for a selected job role.

The system combines Large Language Models (LLMs), LangChain, and fuzzy
logic to process candidate information and produce a suitability score.

## 2. Problem Statement

Recruiters and students may find it difficult to compare a candidate's
skills, education, experience, and projects with the requirements of a
job role.

This project provides an automated way to analyze these factors and
produce an interpretable suitability score.

## 3. Objectives

- Extract candidate information from natural language.
- Identify job requirements.
- Calculate skill and education matching.
- Apply fuzzy logic to handle uncertain or partial information.
- Produce a suitability score between 0 and 100.
- Provide a simple web interface using Streamlit.

## 4. Technologies Used

- Python
- LangChain
- Google Gemini
- scikit-fuzzy
- Streamlit
- NumPy
- Pydantic
- GitHub

## 5. AI Component

The project uses LangChain with Google Gemini.

The LLM extracts structured information from the candidate's natural
language profile.

For example, the candidate may write:

"I know Python and SQL and have completed two projects."

The LLM extracts information such as:

- Python
- SQL
- 2 projects

The LLM is also used to identify requirements when the user enters
a custom job role.

## 6. Fuzzy Logic Component

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

The system evaluates fuzzy rules and performs defuzzification to
produce a numerical suitability score.

## 7. System Flow

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
Skill/Education/Project Matching
        ↓
Fuzzy Inference System
        ↓
Suitability Score
        ↓
Result Display

## 8. Job Selection

The application supports two methods:

1. Selecting a job from the built-in job database.
2. Entering a custom job role.

For a custom job, the LLM identifies relevant skills and educational
backgrounds.

## 9. Future Scope

Possible future improvements include:

- Resume PDF upload.
- More detailed experience analysis.
- Additional job roles.
- Improved fuzzy rules.
- Interview recommendation features.
- Candidate comparison.

## 10. Conclusion

The project demonstrates how LLM-based natural-language processing can
be combined with a fuzzy inference system to analyze job candidate
suitability.

The LLM handles language understanding while fuzzy logic handles
uncertainty and produces the final suitability score.