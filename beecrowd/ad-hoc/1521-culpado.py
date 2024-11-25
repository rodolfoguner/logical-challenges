def guilty(student_index, students):
    if student_index == students[student_index-1]:
        return True
    
    return False


while True:
    inputs = int(input())
    if inputs == 0:
        break
    
    students = list(map(int, input().split()))
    student = int(input())
    
    while True:
        if guilty(student, students):
            print(student)
            break
        
        student = students[student-1]
    