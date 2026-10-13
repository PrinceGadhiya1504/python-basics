# Function analyze_learning(morning, afternoon, completed) banao:
# 1. Agar koi bhi tuple empty ho, toh "Learning data is missing" return karo.
# 2. + se morning aur afternoon topics combine karo.
# 3. * se morning tuple ko 2 baar repeat karo.
# 4. Slicing se combined tuple ke pehle 3 topics nikalo.
# 5. in operator se check karo ki "Python" completed tuple mein hai ya nahi.
# 6. count() se "Python" kitni baar completed tuple mein aaya hai, nikalo.
# 7. any() se check karo ki completed topics mein "Statistics" hai ya nahi.
# 8. all() se check karo ki morning ke sabhi topics completed tuple mein hain ya nahi.
# 9. list() se completed tuple ko list mein convert karo.
# 10. Saare results dictionary mein return karo aur empty tuple bhi test karo.
# Expected output
# {
#     "all_topics": ("Python", "SQL", "Excel", "Power BI", "Statistics"),
#     "repeated_morning": (
#         "Python", "SQL", "Excel",
#         "Python", "SQL", "Excel"
#     ),
#     "first_three_topics": ("Python", "SQL", "Excel"),
#     "python_completed": True,
#     "python_count": 2,
#     "statistics_completed": False,
#     "all_morning_completed": True,
#     "completed_list": ["Python", "SQL", "Python", "Excel"]
# }
# Learning data is missing

morning = ("Python", "SQL", "Excel")
afternoon = ("Power BI", "Statistics")
completed = ("Python", "SQL", "Python", "Excel")

def analyze_learning(morning, afternoon, completed):
    if not morning or not afternoon or not completed:
        return "Learning data is missing"
    
    all_topics = morning + afternoon
    repeated_morning = morning * 2
    first_three_topics = all_topics[:3]
    is_python_completed = "Python" in completed
    python_count = completed.count("Python")
    statistics_completed = any(topic == "Statistics" for topic in completed)
    all_morning_completed = all(topic in completed for topic in morning)
    completed_list = list(completed)

    return {
        "all_topics": all_topics,
        "repeated_morning": repeated_morning,
        "first_three_topics": first_three_topics,
        "is_python_completed": is_python_completed,
        "python_count": python_count,
        "statistics_completed": statistics_completed,
        "all_morning_completed": all_morning_completed,
        "completed_list": completed_list
    }

print(analyze_learning(morning, afternoon, completed))
print(analyze_learning((), (), ()))
    