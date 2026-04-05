#heloo teachher
def get_successful_students(students_list, passing_score=60):
    successful={}
    for student in students_list:
        name= student["name"]
        scores= student["scores"]
        flag=1
        count=0
        tot=0
        for score in scores.values():
            if score<passing_score:
                flag=0
                break
            tot=tot+score
            count+=1
        if flag==1:
            successful[name]=tot/count
    return successful

students_math_results = [
{"name": "Олександр", "scores": {"Calculus": 85, "Algebra": 90, "Discrete Math": 78}},
{"name": "Марія", "scores": {"Calculus": 65, "Algebra": 55, "Discrete Math": 70}},
{"name": "Іван", "scores": {"Calculus": 92, "Algebra": 88, "Discrete Math": 95}},
{"name": "Анна", "scores": {"Calculus": 45, "Algebra": 60, "Discrete Math": 50}}
]

print (get_successful_students(students_math_results))