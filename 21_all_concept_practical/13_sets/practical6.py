# Function check_applicant(required_skills, applicant_skills) banao jo:
# 1. copy() se applicant skills ki copy banaye.
# 2. Copy mein update() se "Linux" aur "Docker" add kare.
# 3. Copy se "HTML" ko discard() kare.
# 4. Copy se ek item pop() kare aur removed item ko result mein save kare.
# 5. clear() ko ek separate temporary set par use kare, taaki original data safe rahe.
# 6. issubset() se check kare ki required skills applicant ke paas hain ya nahi.
# 7. issuperset() se check kare ki applicant ke paas required skills hain ya nahi.
# 8. isdisjoint() se check kare ki dono sets mein koi common skill nahi hai.
# 9. len() se original aur updated skills ki count nikale.
# 10. Saare results dictionary mein return kare.
# Important: Points 6 aur 7 mein required skills aur applicant skills ka order dhyan se rakhna. Dono checks ka result logically same ho sakta hai, lekin method kis set par call karte ho, ye important hai.

required_skills = {"Python", "SQL", "Git"}
applicant_skills = {"Python", "HTML", "Git"}

def check_applicant(required_skills, applicant_skills):
    copy_application_skills = applicant_skills.copy()
    copy_application_skills.update(["Linux", "Docker"])
    copy_application_skills.discard("HTML")
    removed_item = copy_application_skills.pop()
    copy_application_skills.clear()
    issubset = required_skills.issubset(applicant_skills)
    issuperset = applicant_skills.issuperset(required_skills)
    isdisjoint = required_skills.isdisjoint(applicant_skills)
    len_required = len(required_skills)
    len_applicant = len(applicant_skills)
    return {
        "copy_application_skills": copy_application_skills,
        "removed_item": removed_item,
        "issubset": issubset,
        "issuperset": issuperset,
        "isdisjoint": isdisjoint,
        "len_required": len_required,
        "len_applicant": len_applicant
    }

print(check_applicant(required_skills, applicant_skills))