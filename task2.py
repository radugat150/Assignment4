#heloo teachher
def get_successful_students(students_list, passing_score=60):
    successful={}
    for student in students_list:
        name= students_list["name"]
        scores= students_list["scores"]
        flag=1
        count=0
        tot=0
        for score in scores.value():
            if score<passing_score:
                flag=0
                break
            tot=tot+score
            count+=1
        if flag==1:
            successful[name]=tot/count
    return successful