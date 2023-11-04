#Lea Nicole Kerr
#M02 case study
#This app/program takes a student's GPA and determines whether they've made honor roll, dean's list, or neither

while True:
    name_last = input("Enter the last name of a student, or press zzz to quit!")
    
    if name_last == 'zzz':
        break #stops the program if ZZZ is typed

    name_first = input("Enter the first name of a student")
    student_gpa = float(input("Enter the GPA of the student"))
  
    
    if student_gpa >= 3.5:
        print("This student has made Dean's List!")
    elif student_gpa >= 3.25:
        print("This student has made Honor Roll!")
    else: 
        print("Sorry! But this student doesn't qualify for Honor Roll or Dean's List")    
    
    #The if loop above determines whether or not the student has made dean's list or honor roll based on the GPA entered