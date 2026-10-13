# Ek function analyze_employee_skills(company_skills, employee_skills) banao jo:
# 1. Har employee ke skills ko company skills ke saath compare kare.
# 2. intersection() se har employee ke common skills nikale.
# 3. difference() se company ke woh skills nikale jo employee ke paas nahi hain.
# 4. issubset() se check kare ki employee ke saare skills company skills mein hain ya nahi.
# 5. issuperset() se check kare ki company skills, employee ke skills ko cover karti hai ya nahi.
# 6. isdisjoint() se check kare ki employee aur company ke skills mein koi common skill nahi hai.
# 7. symmetric_difference() se dono sets ke different skills nikale.
# 8. Set comprehension se un employees ke naam nikale jinke paas "Python" skill hai.
# 9. Results ko dictionary mein return kare.
# Expected result ke kuch important checks:
# - Amit ke common skills: {"Python", "SQL", "Git"}
# - Neha ke missing company skills: {"SQL", "Git", "Linux", "Docker"}
# - "Python" skill wale employees: {"Amit", "Neha"}
company_skills = {"Python", "SQL", "Git", "Linux", "Docker"}

employee_skills = {
    "Amit": {"Python", "SQL", "Git"},
    "Neha": {"Python", "HTML", "CSS"},
    "Raj": {"Java", "Linux"},
    "Priya": {"Docker", "Git", "Linux"}
}


def analyze_employee_skills(company_skills, employee_skills):
    match_skills = {}
    missing_skills = {}
    issubsets = {}
    issupersets = {}
    disjoint = {}
    symmetric_difference = {}

    for employee, skills in employee_skills.items():
        match_skills[employee] = company_skills.intersection(skills)
        missing_skills[employee] = company_skills.difference(skills)
        issubsets[employee] = skills.issubset(company_skills)
        issupersets[employee] = company_skills.issuperset(skills)
        disjoint[employee] = company_skills.isdisjoint(skills)
        symmetric_difference[employee] = company_skills.symmetric_difference(skills)
    python_employees = {
        employee
        for employee, skills in employee_skills.items()
        if "Python" in skills
    }

    return {
        "match_skills": match_skills,
        "missing_skills": missing_skills,
        "issubsets": issubsets,
        "issupersets": issupersets,
        "disjoint": disjoint,
        "symmetric_difference": symmetric_difference,
        "python_employees": python_employees
    }


print(analyze_employee_skills(company_skills, employee_skills))