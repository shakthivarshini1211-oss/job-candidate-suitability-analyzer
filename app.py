import os

import streamlit as st
from dotenv import load_dotenv

from llm_extractor import extract_candidate_profile,analyze_custom_job
from fuzzy_logic import calculate_suitability


load_dotenv()


# ----------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------

st.set_page_config(
    page_title="AI Job Candidate Suitability Analyzer",
    page_icon="💼",
    layout="wide"
)


# ----------------------------------------
# JOB DATA
# ----------------------------------------
JOB_ROLES = {

    "Data Analyst": {
        "skills": [
            "python",
            "sql",
            "excel",
            "power bi",
            "statistics"
        ],
        "education": [
            "b.sc",
            "bca",
            "b.sc it",
            "bsc it",
            "computer science",
            "information technology",
            "statistics",
            "mathematics"
        ]
    },

    "Web Developer": {
        "skills": [
            "html",
            "css",
            "javascript",
            "php",
            "mysql"
        ],
        "education": [
            "bca",
            "b.sc",
            "b.sc it",
            "bsc it",
            "computer science",
            "information technology"
        ]
    },

    "Python Developer": {
        "skills": [
            "python",
            "sql",
            "git",
            "apis",
            "object oriented programming"
        ],
        "education": [
            "bca",
            "b.sc",
            "b.sc it",
            "bsc it",
            "computer science",
            "information technology"
        ]
    },

    "Cybersecurity Analyst": {
        "skills": [
            "cybersecurity",
            "networking",
            "linux",
            "python",
            "security"
        ],
        "education": [
            "bca",
            "b.sc",
            "b.sc it",
            "bsc it",
            "computer science",
            "information technology",
            "cybersecurity"
        ]
    },

    "Java Developer": {
        "skills": [
            "java",
            "sql",
            "git",
            "spring",
            "apis"
        ],
        "education": [
            "bca",
            "b.sc",
            "b.sc it",
            "bsc it",
            "computer science",
            "information technology"
        ]
    },

    "Full Stack Developer": {
        "skills": [
            "html",
            "css",
            "javascript",
            "react",
            "node.js",
            "sql"
        ],
        "education": [
            "bca",
            "b.sc",
            "b.sc it",
            "bsc it",
            "computer science",
            "information technology"
        ]
    },

    "Cloud Engineer": {
        "skills": [
            "aws",
            "azure",
            "linux",
            "networking",
            "docker",
            "kubernetes",
            "python"
        ],
        "education": [
            "bca",
            "b.sc",
            "b.sc it",
            "bsc it",
            "computer science",
            "information technology"
        ]
    },

    "Database Administrator": {
        "skills": [
            "sql",
            "mysql",
            "oracle",
            "database",
            "linux"
        ],
        "education": [
            "bca",
            "b.sc",
            "b.sc it",
            "bsc it",
            "computer science",
            "information technology"
        ]
    },

    "Data Scientist": {
        "skills": [
            "python",
            "sql",
            "statistics",
            "machine learning",
            "pandas",
            "numpy"
        ],
        "education": [
            "computer science",
            "information technology",
            "data science",
            "statistics",
            "mathematics",
            "bca",
            "b.sc it"
        ]
    },

    "Machine Learning Engineer": {
        "skills": [
            "python",
            "machine learning",
            "statistics",
            "tensorflow",
            "pytorch",
            "sql"
        ],
        "education": [
            "computer science",
            "information technology",
            "data science",
            "artificial intelligence",
            "mathematics",
            "statistics"
        ]
    },

    "AI Engineer": {
        "skills": [
            "python",
            "machine learning",
            "deep learning",
            "artificial intelligence",
            "apis",
            "sql"
        ],
        "education": [
            "computer science",
            "information technology",
            "artificial intelligence",
            "data science",
            "bca",
            "b.sc it"
        ]
    },

    "System Administrator": {
        "skills": [
            "linux",
            "windows server",
            "networking",
            "system administration",
            "python"
        ],
        "education": [
            "computer science",
            "information technology",
            "bca",
            "b.sc it"
        ]
    },

    "Network Administrator": {
        "skills": [
            "networking",
            "linux",
            "cisco",
            "tcp/ip",
            "network security"
        ],
        "education": [
            "computer science",
            "information technology",
            "networking",
            "bca",
            "b.sc it"
        ]
    },

    "DevOps Engineer": {
        "skills": [
            "linux",
            "docker",
            "kubernetes",
            "git",
            "ci/cd",
            "aws"
        ],
        "education": [
            "computer science",
            "information technology",
            "bca",
            "b.sc it"
        ]
    },

    "Mobile App Developer": {
        "skills": [
            "android",
            "kotlin",
            "java",
            "flutter",
            "dart",
            "apis"
        ],
        "education": [
            "computer science",
            "information technology",
            "bca",
            "b.sc it"
        ]
    },

    "Business Analyst": {
        "skills": [
            "sql",
            "excel",
            "power bi",
            "data analysis",
            "communication"
        ],
        "education": [
            "business",
            "management",
            "computer science",
            "information technology",
            "bca",
            "b.sc it"
        ]
    },

    "QA Test Engineer": {
        "skills": [
            "software testing",
            "selenium",
            "python",
            "java",
            "sql",
            "test automation"
        ],
        "education": [
            "computer science",
            "information technology",
            "bca",
            "b.sc it"
        ]
    }
}


# ----------------------------------------
# FUNCTIONS
# ----------------------------------------

def calculate_skill_match(candidate_skills, required_skills):

    candidate_skills = [
        skill.lower().strip()
        for skill in candidate_skills
    ]

    matched = 0

    for required_skill in required_skills:

        if any(
            required_skill.lower() in candidate_skill
            or candidate_skill in required_skill.lower()
            for candidate_skill in candidate_skills
        ):
            matched += 1

    if len(required_skills) == 0:
        return 0

    return round(
        (matched / len(required_skills)) * 100,
        2
    )


def calculate_education_match(
    education,
    accepted_education
):

    education = education.lower()

    for item in accepted_education:

        if item.lower() in education:
            return 100

    related_keywords = [
        "engineering",
        "technology",
        "computer",
        "science",
        "information",
        "mathematics",
        "statistics"
    ]

    for keyword in related_keywords:

        if keyword in education:
            return 60

    return 20


def calculate_project_score(project_count):

    if project_count <= 0:
        return 0

    if project_count == 1:
        return 40

    if project_count == 2:
        return 70

    return 100


def get_result_label(score):

    if score < 40:
        return "Poor Suitability"

    elif score < 65:
        return "Average Suitability"

    elif score < 85:
        return "Good Suitability"

    else:
        return "Excellent Suitability"


def create_explanation(
    profile,
    job_role,
    skill_match,
    education_match,
    project_score,
    suitability
):

    if suitability >= 85:
        level = "excellent"

    elif suitability >= 65:
        level = "good"

    elif suitability >= 40:
        level = "average"

    else:
        level = "low"

    strongest = ", ".join(profile["skills"][:5])

    return f"""
The candidate shows {level} suitability for the
{job_role} role.

The candidate's extracted skills include:
{strongest}.

The skill match is {skill_match}%, the education
match is {education_match}%, and the project
experience score is {project_score}%.

The fuzzy inference system produced a final
suitability score of {suitability}/100.

The candidate can improve their profile by
developing additional role-specific skills,
practical projects, and relevant experience.
"""


# ----------------------------------------
# TITLE
# ----------------------------------------

st.title(
    "💼 AI-Based Job Candidate Suitability Analyzer"
)

st.write(
    "This application uses LangChain and an LLM "
    "to understand a candidate's profile and a "
    "fuzzy inference system to calculate job suitability."
)


# ----------------------------------------
# INPUT SECTION
# ----------------------------------------

st.subheader("1. Select or Enter Job")

job_input_type = st.radio(
    "How would you like to provide the job?",
    [
        "Select from Job Database",
        "Enter Custom Job"
    ]
)

if job_input_type == "Select from Job Database":

    job_role = st.selectbox(
        "Select the job role:",
        list(JOB_ROLES.keys())
    )

else:

    job_role = st.text_input(
        "Enter your desired job role:",
        placeholder="Example: Cloud Engineer"
    )

st.subheader("2. Enter Candidate Profile")

candidate_text = st.text_area(
    "Describe the candidate in your own words:",
    height=220,
    placeholder=(
        "Example: I am a B.Sc IT student. "
        "I know Python, SQL and Power BI. "
        "I completed two projects and one internship."
    )
)


analyze = st.button(
    "🔍 Analyze Candidate",
    type="primary"
)


# ----------------------------------------
# ANALYSIS
# ----------------------------------------

if analyze:

    if not candidate_text.strip():

        st.warning(
            "Please enter a candidate profile first."
        )

        st.stop()

    with st.spinner(
        "AI is understanding the candidate profile..."
    ):

        try:

            profile = extract_candidate_profile(
                candidate_text
            )

        except Exception as error:

            st.error(
                f"AI extraction failed: {error}"
            )

            st.stop()


    st.subheader(
        "3. AI Extracted Candidate Information"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.write("**Education**")
        st.write(profile["education"])

        st.write("**Skills**")
        st.write(
            ", ".join(profile["skills"])
        )

    with col2:

        st.write("**Experience**")
        st.write(
            f'{profile["experience_years"]} years'
        )

        st.write("**Internships**")
        st.write(
            profile["internship_count"]
        )

    with col3:

        st.write("**Projects**")
        st.write(
            profile["project_count"]
        )

        st.write("**Career Interest**")
        st.write(
            profile["career_interest"]
        )


    # ----------------------------------------
    # CALCULATE INPUTS FOR FUZZY SYSTEM
    # ----------------------------------------
        # ----------------------------------------
    # CALCULATE INPUTS FOR FUZZY SYSTEM
    # ----------------------------------------

    if job_input_type == "Select from Job Database":

        job = JOB_ROLES[job_role]

    else:

        if not job_role.strip():
            st.error("Please enter a job role.")
            st.stop()

        with st.spinner(
            "AI is analyzing the job requirements..."
        ):

            try:
                custom_job = analyze_custom_job(job_role)

            except Exception as error:
                st.error(
                    f"Job analysis failed: {error}"
                )
                st.stop()

        job_role = custom_job["job_title"]

        job = {
            "skills": custom_job["skills"],
            "education": custom_job["education"]
        }

        st.subheader("AI-Identified Job Requirements")

        st.write(
            "**Job Role:**",
            custom_job["job_title"]
        )

        st.write("**Required Skills:**")

        for skill in custom_job["skills"]:
            st.write(f"- {skill}")

        st.write("**Relevant Education:**")

        for education in custom_job["education"]:
            st.write(f"- {education}")


    # ----------------------------------------
    # CALCULATE MATCHING SCORES
    # ----------------------------------------

    skill_match = calculate_skill_match(
        profile["skills"],
        job["skills"]
    )

    education_match = calculate_education_match(
        profile["education"],
        job["education"]
    )

    project_score = calculate_project_score(
        profile["project_count"]
    )

    experience = min(
        float(profile["experience_years"]),
        5.0
    )


    # ----------------------------------------
    # FUZZY LOGIC
    # ----------------------------------------

    try:

        suitability = calculate_suitability(
            skill_match,
            experience,
            education_match,
            profile["project_count"]
        )

    except Exception as error:

        st.error(
            f"Fuzzy logic calculation failed: {error}"
        )

        st.stop()


    # ----------------------------------------
    # DISPLAY FUZZY INPUTS
    # ----------------------------------------

    st.subheader(
        "4. Fuzzy Logic Analysis"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Skill Match",
            f"{skill_match}%"
        )

    with c2:
        st.metric(
            "Experience",
            f"{experience} years"
        )

    with c3:
        st.metric(
            "Education Match",
            f"{education_match}%"
        )

    with c4:
        st.metric(
            "Project Score",
            f"{project_score}%"
        )


    # ----------------------------------------
    # FINAL SCORE
    # ----------------------------------------

    st.subheader(
        "5. Final Suitability Result"
    )

    st.progress(
        int(suitability)
    )

    st.metric(
        "Suitability Score",
        f"{suitability}/100"
    )

    st.success(
        get_result_label(suitability)
    )


    # ----------------------------------------
    # AI EXPLANATION
    # ----------------------------------------

    st.subheader(
        "6. AI Explanation"
    )

    explanation = create_explanation(
        profile,
        job_role,
        skill_match,
        education_match,
        project_score,
        suitability
    )

    st.info(explanation)
