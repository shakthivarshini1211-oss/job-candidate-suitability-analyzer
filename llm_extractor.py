import os
from typing import List

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


# Candidate Profile
class CandidateProfile(BaseModel):
    skills: List[str] = Field(
        description="Technical and job-related skills mentioned by the candidate."
    )

    education: str = Field(
        description="Highest or most relevant educational qualification."
    )

    experience_years: float = Field(
        description="Number of years of professional work experience explicitly mentioned."
    )

    project_count: int = Field(
        description="Number of academic, personal, or professional projects explicitly mentioned."
    )

    internship_count: int = Field(
        description="Number of internships explicitly mentioned."
    )

    career_interest: str = Field(
        description="The job or career area the candidate is interested in."
    )


# Custom Job Requirements
class JobRequirements(BaseModel):
    job_title: str = Field(
        description="The standardized name of the job role."
    )

    skills: List[str] = Field(
        description="Important technical and job-related skills normally required for this job."
    )

    education: List[str] = Field(
        description="Relevant educational backgrounds for this job."
    )


# Get Gemini API Key
def get_api_key():
    api_key = os.getenv("GOOGLE_API_KEY")

    if api_key:
        return api_key

    try:
        import streamlit as st
        return st.secrets["GOOGLE_API_KEY"]
    except Exception:
        return None


# Create Gemini Model
def get_llm():
    api_key = get_api_key()

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY was not found. "
            "Please add your Gemini API key to the .env file."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=api_key,
        temperature=0
    )

    return llm


# Extract Candidate Profile
def extract_candidate_profile(candidate_text):
    llm = get_llm()

    structured_llm = llm.with_structured_output(
        CandidateProfile
    )

    prompt = f"""
    You are an information extraction assistant for a Job Candidate Suitability Analyzer.

    Read the Candidate's natural-language profile.

    Extract only information that is supported by the text.

    Do not invent skills, experience, projects, education, or internships.

    Normalize skill names where appropriate.

    If professional experience is not mentioned, use 0.

    If projects are not mentioned, use 0.

    If internships are not mentioned, use 0.

    Candidate profile:

    {candidate_text}
    """

    result = structured_llm.invoke(prompt)

    return result.model_dump()


# Analyze Custom Job
def analyze_custom_job(job_title):
    llm = get_llm()

    structured_llm = llm.with_structured_output(
        JobRequirements
    )

    prompt = f"""
    You are a job requirement analysis assistant.

    The user has entered the following job role:
    {job_title}

    Identify the important requirements for this job.

    Return:
    1. A standardized job title.
    2. Important technical and job-related skills.
    3. Relevant educational backgrounds.

    Keep the skill list focused on the most important skills for this job.

    Do not create unrelated skills.

    For education, include common relevant fields such as
    Computer Science, Information Technology, Engineering, Business,
    Design, Mathematics, Statistics, or other appropriate fields when relevant.

    Job role:
    {job_title}
    """

    result = structured_llm.invoke(prompt)

    return result.model_dump()