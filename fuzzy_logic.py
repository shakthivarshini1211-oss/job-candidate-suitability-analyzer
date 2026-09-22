import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def calculate_suitability(
    skill_match,
    experience,
    education_match,
    project_experience
):
    # -----------------------------
    # 1. Define fuzzy input variables
    # -----------------------------

    skill = ctrl.Antecedent(
        np.arange(0, 101, 1),
        "skill"
    )

    experience_var = ctrl.Antecedent(
        np.arange(0, 5.1, 0.1),
        "experience"
    )

    education = ctrl.Antecedent(
        np.arange(0, 101, 1),
        "education"
    )

    projects = ctrl.Antecedent(
        np.arange(0, 11, 1),
        "projects"
    )

    # -----------------------------
    # 2. Define fuzzy output
    # -----------------------------

    suitability = ctrl.Consequent(
        np.arange(0, 101, 1),
        "suitability"
    )

    # -----------------------------
    # 3. Membership functions
    # -----------------------------

    # Skill Match: 0-100
    skill["low"] = fuzz.trapmf(
        skill.universe,
        [0, 0, 25, 50]
    )

    skill["medium"] = fuzz.trimf(
        skill.universe,
        [25, 55, 85]
    )

    skill["high"] = fuzz.trapmf(
        skill.universe,
        [60, 80, 100, 100]
    )

    # Experience: 0-5 years
    experience_var["low"] = fuzz.trapmf(
        experience_var.universe,
        [0, 0, 0.5, 1.5]
    )

    experience_var["medium"] = fuzz.trimf(
        experience_var.universe,
        [0.5, 2, 4]
    )

    experience_var["high"] = fuzz.trapmf(
        experience_var.universe,
        [2.5, 4, 5, 5]
    )

    # Education Match: 0-100
    education["low"] = fuzz.trapmf(
        education.universe,
        [0, 0, 25, 50]
    )

    education["medium"] = fuzz.trimf(
        education.universe,
        [25, 55, 85]
    )

    education["high"] = fuzz.trapmf(
        education.universe,
        [60, 80, 100, 100]
    )

    # Project Experience: 0-10
    projects["low"] = fuzz.trapmf(
        projects.universe,
        [0, 0, 0, 2]
    )

    projects["medium"] = fuzz.trimf(
        projects.universe,
        [1, 3, 5]
    )

    projects["high"] = fuzz.trapmf(
        projects.universe,
        [4, 6, 10, 10]
    )

    # Suitability Output: 0-100
    suitability["poor"] = fuzz.trapmf(
        suitability.universe,
        [0, 0, 20, 40]
    )

    suitability["average"] = fuzz.trimf(
        suitability.universe,
        [25, 45, 65]
    )

    suitability["good"] = fuzz.trimf(
        suitability.universe,
        [55, 70, 85]
    )

    suitability["excellent"] = fuzz.trapmf(
        suitability.universe,
        [75, 90, 100, 100]
    )

    # -----------------------------
    # 4. Fuzzy Rules
    # -----------------------------

    # Strong candidate
    rule1 = ctrl.Rule(
        skill["high"] &
        experience_var["high"] &
        education["high"] &
        projects["high"],
        suitability["excellent"]
    )

    # Strong skills + medium experience + education
    rule2 = ctrl.Rule(
        skill["high"] &
        experience_var["medium"] &
        education["high"],
        suitability["good"]
    )

    # Medium skills + medium experience + education + projects
    rule3 = ctrl.Rule(
        skill["medium"] &
        experience_var["medium"] &
        education["high"] &
        projects["high"],
        suitability["good"]
    )

    # Strong skills + low experience + good education + projects
    rule4 = ctrl.Rule(
        skill["high"] &
        experience_var["low"] &
        education["high"] &
        projects["high"],
        suitability["good"]
    )

    # Strong skills + low experience + good education
    rule5 = ctrl.Rule(
        skill["high"] &
        experience_var["low"] &
        education["high"],
        suitability["good"]
    )

    # Medium skills + low experience + good education
    rule6 = ctrl.Rule(
        skill["medium"] &
        experience_var["low"] &
        education["high"],
        suitability["average"]
    )

    # Weak skills + low experience + few projects
    rule7 = ctrl.Rule(
        skill["low"] &
        experience_var["low"] &
        projects["low"],
        suitability["poor"]
    )

    # Weak skills + weak education
    rule8 = ctrl.Rule(
        skill["low"] &
        education["low"],
        suitability["poor"]
    )

    # Medium candidate
    rule9 = ctrl.Rule(
        skill["medium"] &
        education["medium"] &
        projects["medium"],
        suitability["average"]
    )

    # Strong skills + education but few projects
    rule10 = ctrl.Rule(
        skill["high"] &
        education["high"] &
        projects["low"],
        suitability["average"]
    )

    # Medium skills + high experience + good education
    rule11 = ctrl.Rule(
        skill["medium"] &
        experience_var["high"] &
        education["high"],
        suitability["good"]
    )

    # Low skills + high experience + good education
    rule12 = ctrl.Rule(
        skill["low"] &
        experience_var["high"] &
        education["high"],
        suitability["average"]
    )

    # Strong skills + medium education
    rule13 = ctrl.Rule(
        skill["high"] &
        experience_var["low"] &
        education["medium"],
        suitability["average"]
    )

    # Medium skills + high experience + medium education
    rule14 = ctrl.Rule(
        skill["medium"] &
        experience_var["high"] &
        education["medium"],
        suitability["good"]
    )

    # Strong skills + high experience + medium education
    rule15 = ctrl.Rule(
        skill["high"] &
        experience_var["high"] &
        education["medium"],
        suitability["good"]
    )

    # Medium skills + low experience + medium education
    rule16 = ctrl.Rule(
        skill["medium"] &
        experience_var["low"] &
        education["medium"],
        suitability["average"]
    )

    # Strong skills + medium experience + medium education
    rule17 = ctrl.Rule(
        skill["high"] &
        experience_var["medium"] &
        education["medium"],
        suitability["good"]
    )

    # -----------------------------
    # 5. General coverage rules
    # -----------------------------
    # These rules make sure that a valid
    # candidate always produces a fuzzy output.

    rule18 = ctrl.Rule(
        skill["high"],
        suitability["good"]
    )

    rule19 = ctrl.Rule(
        skill["medium"],
        suitability["average"]
    )

    rule20 = ctrl.Rule(
        skill["low"],
        suitability["poor"]
    )

    # -----------------------------
    # 6. Create fuzzy control system
    # -----------------------------

    system = ctrl.ControlSystem([
        rule1,
        rule2,
        rule3,
        rule4,
        rule5,
        rule6,
        rule7,
        rule8,
        rule9,
        rule10,
        rule11,
        rule12,
        rule13,
        rule14,
        rule15,
        rule16,
        rule17,
        rule18,
        rule19,
        rule20
    ])

    # -----------------------------
    # 7. Create simulation
    # -----------------------------

    simulation = ctrl.ControlSystemSimulation(system)

    # -----------------------------
    # 8. Provide crisp inputs
    # -----------------------------

    simulation.input["skill"] = skill_match
    simulation.input["experience"] = experience
    simulation.input["education"] = education_match
    simulation.input["projects"] = project_experience

    # -----------------------------
    # 9. Run fuzzy inference
    # -----------------------------

    simulation.compute()

    # -----------------------------
    # 10. Defuzzification
    # -----------------------------

    score = simulation.output["suitability"]

    return round(score, 2)