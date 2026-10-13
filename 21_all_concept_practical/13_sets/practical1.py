# Ek function analyze_skills(student1_skills, student2_skills) banao jo:
# 1. Dono students ke total unique skills nikale.
# 2. Dono ke common skills nikale.
# 3. Sirf student 1 ke skills nikale.
# 4. Sirf student 2 ke skills nikale.
# 5. Student 1 ke set mein "Git" add kare.
# 6. Student 2 ke set mein "React" aur "Docker" add kare.
# 7. Student 1 se "CSS" remove kare.
# 8. Student 2 se "Java" ko discard() kare. Skill na hone par bhi error nahi aana chahiye.
# 9. Check kare ki "Python" dono students ke paas hai ya nahi.
# 10. Saare results dictionary mein return kare.

student1_skills = {"Python", "HTML", "CSS"}
student2_skills = {"Python", "JavaScript", "SQL"}

total_unique = student1_skills.union(student2_skills)
total_unique_count = len(total_unique)
common_skills = student1_skills.intersection(student2_skills)
student1_only = student1_skills.difference(student2_skills)
student2_only = student2_skills.difference(student1_skills)
student1_skills.add("Git")
student2_skills.update(["React", "Docker"])
student1_skills.remove("CSS")
student2_skills.discard("Java")
python_in_both = "Python" in student1_skills and "Python" in student2_skills

results = {
    "total_unique_skills": total_unique,
    "total_unique_count": total_unique_count,
    "common_skills": common_skills,
    "student1_only": student1_only,
    "student2_only": student2_only,
    "updated_student1_skills": student1_skills,
    "updated_student2_skills": student2_skills,
    "python_in_both": python_in_both
}

print(results)