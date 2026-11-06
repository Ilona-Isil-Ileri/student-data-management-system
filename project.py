# --- Importing necessary modules and files ---
from datetime import datetime, timedelta

courses_file = "courses.txt"
students_file = "students.txt"
passed_file = "passed.txt"




# --- FUNCTIONS ---
def add_student():
    # 1. Generate next available student ID
    def generate_next_id():
        max_id = 0
        f = open(students_file, "r")

        for line in f:
            parts = line.strip().split(",")
            student_id = int(parts[0])
            if student_id > max_id:
                max_id = student_id

        f.close()
        return max_id + 1

    st_nr = generate_next_id()

    # 2. Ask for user input (names, major) and validate
    # ---- Ask names ----
    # -- First name --
    while True:
        first_name = input("Enter the first name of the student:\n").strip()

        # letters only AND starts with uppercase
        if first_name.isalpha() and first_name[0].isupper():
            break  # valid → exit loop
        print("Names should contain only letters and start with capital letters.")

    
    # -- Last name --
    while True:
        last_name = input("Enter the last name of the student:\n").strip()
        
        if last_name.isalpha() and last_name[0].isupper():
            break
        print("Names should contain only letters and start with capital letters.")


    # -- Middle name --
    while True:
        middle_name = input("Enter the middle name "
                            "(just press enter and leave it blank if no middle name) "
                            "of the student:\n").strip()

        if middle_name == "" or (middle_name.isalpha() and middle_name[0].isupper()):
            break
        print("Names should contain only letters and start with capital letters.")
        

    
    # ---- Ask program/major ----
    programs = {"CE", "EE", "ET", "ME", "SE"}
    while True:
        major = input("""Select student's major:
                    CE: Computational Engineering
                    EE: Electrical Engineering
                    ET: Energy Technology
                    ME: Mechanical Engineering
                    SE: Software Engineering
                What is your selection? \n""").strip().upper()

        if major in programs:
            break
        print("Invalid program. Please choose one of CE, EE, ET, ME, or SE.")
    


    # ---- Student e-mail format: first.last@lut.fi (lowercase) ----
    email = f"{first_name.lower()}.{last_name.lower()}@lut.fi"
   
    # ---- Registration year ----
    year = str(datetime.now().year)
    

    
    # 3. Append to students.txt  
    f = open(students_file, "a")
    f.write(f"{st_nr},{last_name},{first_name},{middle_name},{email},{year},{major}\n")
    f.close()


    # 4. Print success message
    print()
    print("Student added successfully!")
    


    
def search_student():  
    # 1. Ask for user input (names)
    search_name = input("Give at least 3 characters of the students first, middle or last name:\n")
    if len(search_name) < 3:
        print("Please enter at least 3 characters.")
        print()
        return    

    # 2. Open the file and import the students names
    f = open(students_file, "r")

    s = search_name.lower() # user input converted to lowercase
    matches = []            # a list for matching students
    
    for line in f:
        parts = line.strip().split(",")

        student_id = int(parts[0])
        last_name = parts[1]
        first_name = parts[2]
        middle_name = parts[3]
        email = parts[4]
        registered_year = parts[5]
        major = parts[6]       
    

    # 3. Compare lowercase versions
        if (s in last_name.lower()) or (s in first_name.lower()) or (s in middle_name.lower()):
            match_info = f"ID: {student_id}, {last_name}, {first_name} {middle_name}, {email}, {major}"
            matches.append(match_info)
        
    f.close()


    # 4. Print the matching students
    if len(matches) == 0:
        print("No matching students.")
        print()

    else:
        print("Matching students:")
        for m in matches:
            print(m)




def search_course():
    # 1. Ask for user input (course or teacher names)
    search_course = input("Give at least 3 characters of the course name or the teacher:\n")
    if len(search_course) < 3:
        print("Please enter at least 3 characters.")
        print()
        return  

    # 2. Open the file, import the course and teacher names
    f = open(courses_file, "r")

    c = search_course.lower() # user input converted to lowercase
    matches = []              # a list for matching courses
        
    for line in f:
        parts = line.strip().split(",")

        course_id = parts[0]
        course_name = parts[1]
        ects_credit = parts[2]
        teacher_names = parts[3:]


    # 3. Compare lowercase versions
    # First check if the course name matches
        course_match = c in course_name.lower()

    # Then check each teacher manually
        teacher_match = False
        for teacher in teacher_names:
            if c in teacher.lower():
                teacher_match = True
                break   # stop looping if one teacher matches already

        if course_match or teacher_match:
            teacher_str = ""
            for teacher in teacher_names:
                if teacher_str != "":
                    teacher_str += ", "
                teacher_str += teacher

            match_info = f"ID:{course_id}, Name: {course_name}, ECTS: {ects_credit}, Teacher(s): {teacher_str}"
            matches.append(match_info)
        
    f.close()


    # 4. Print the matching courses
    if len(matches) == 0:
        print("No courses found.")
        print()

    else:
        print("Courses found:")
        for m in matches:
            print(m)


def add_course_completion():
    # 1. Getting user input and validating for the course and student ID
    while True:
        user_course_id = input("Give the course ID:\n").strip()

        found = False
        cour_file = open(courses_file, "r")

        for line in cour_file:
            parts = line.strip().split(",")
            course_id = parts[0]

            if course_id == user_course_id:
                found = True
                break  
        
        cour_file.close()

        if found:
            break   # valid → exit loop
        
        print("No courses found. Please try again with another course ID.")



    while True:    
        user_student_id_str = input("Give the student ID:\n").strip()

        if not user_student_id_str.isdigit():
            print("Student ID must be digits only.")
            continue

        user_student_id = int(user_student_id_str)

        found = False
        stud_file = open(students_file, "r")

        for line in stud_file:
            parts = line.strip().split(",")
            student_id = int(parts[0])

            if student_id == user_student_id:
                found = True
                break

        stud_file.close()

        if found:
            break
        
        print("Student not found. Please try again.")


    # 2. Getting user input for the exam date and grade
    # -- Exam Date --
    while True:
        exam_date_str = input("Enter a date(YYYY-MM-DD):\n").strip()
        
        try:
            # Convert from string to datetime object
            user_exam_date = datetime.strptime(exam_date_str, "%Y-%m-%d").date()

        except ValueError:
            print("Invalid date format. Please try again with YYYY-MM-DD. \n")
            continue     

        # Check if the date is in the future
        today = datetime.now().date()
        
        if user_exam_date > today:
            print("Input is later than today. Try again! \n")
            continue

        # Check if the date is older than 30 days
        days_gap = today - user_exam_date
        if days_gap > timedelta(days=30): 
            print("Input date is older than 30 days. Please contact 'opinto'.\n")
            continue

        # Passed all checks
        break


    # -- Grade -- 
    while True:
        user_grade = input("Give the grade:\n").strip()

        if not user_grade.isdigit() or not (int(user_grade) >= 1 and int(user_grade) <= 5):
            print("Grade is not correct. Please enter a number between 1 and 5.")
            continue

        # Passed all checks
        break

    user_grade = int(user_grade)

        
    # 3. Opening the passed.txt file
    rows = []
    pass_file = open(passed_file, "r")

    for line in pass_file:
        parts = line.strip().split(",")

        p_course_id = parts[0]
        p_student_id = int(parts[1])
        p_exam_date = parts[2]
        p_grade = int(parts[3])
        rows.append([p_course_id, p_student_id, p_exam_date, p_grade])

    pass_file.close()


    # 4. Overwriting the record (if students increased their grades)
    updated = False
    new_rows = []
    
    for record in rows:
        p_course_id, p_student_id, p_exam_date, p_grade = record

        if p_course_id == user_course_id and p_student_id == user_student_id:
            if not updated:
                if int(user_grade) < int(p_grade):  # Keep latest record when grade ties
                    new_rows.append(record)         # keep old better grade
                else:
                    new_rows.append([p_course_id, p_student_id, user_exam_date, user_grade])

            updated = True
            continue    # If updated is already True, skip additional duplicates silently

        new_rows.append(record) # Keep every unrelated row
        
    if not updated: # if no match was found, add the new record
        new_rows.append([user_course_id, user_student_id, user_exam_date, user_grade])

                
    # 5. Writing the passed.txt file
    pass_file = open(passed_file, "w")

    for p_course_id, p_student_id, p_exam_date, p_grade in new_rows:
        pass_file.write(f"{p_course_id},{p_student_id},{p_exam_date},{p_grade}\n")

    pass_file.close()

    # 6. Printing out the record addition
    print("Record added!")
    print()
    
    
 
def show_student_record():
    # Getting the input and matching with the IDs inside the files
    while True:
        user_student_id_str = input("Give the student ID:\n").strip()

        if not user_student_id_str.isdigit():
            print("Student ID must be digits only.")
            continue

        user_student_id = int(user_student_id_str)

    # scan students.txt for this ID
        found = False
        last_name = first_name = middle_name = email = registered_year = major = ""
    
        stud_file = open(students_file, "r")
        for line in stud_file:
            parts = line.strip().split(",")
            student_id = int(parts[0])

            if student_id == user_student_id:
                last_name = parts[1]
                first_name = parts[2]
                middle_name = parts[3]
                email = parts[4]
                registered_year = parts[5]
                major = parts[6]

                found = True
                break  
        
        stud_file.close()

        if found:
            break
        
        print("No student found. Please try again with another student ID.")


    # Clean Display
    if middle_name != "":
        full_name = f"{last_name}, {first_name} {middle_name}"
    else:
        full_name = f"{last_name}, {first_name}"

    print()
    print(f"Student ID: {user_student_id}")
    print(f"Name: {full_name}")
    print(f"Starting Year: {registered_year}")
    print(f"Major: {major}")
    print(f"Email: {email}")
    print()   
        
    passes = []
    pass_file = open(passed_file, "r")

    for line in pass_file:
        parts = line.strip().split(",")
        p_student_id = int(parts[1])

        if p_student_id == user_student_id:
            p_course_id = parts[0]
            p_exam_date = parts[2]
            p_grade = int(parts[3])
            passes.append([p_course_id, p_student_id, p_exam_date, p_grade])

    pass_file.close()


    total_ects = 0
    grade_sum = 0
    course_count = 0

    print(f"Passed Courses:")
    # Matching the variables in courses.txt and passed.txt files
    for p_course_id, p_sid, p_exam_date, p_grade in passes:
        # Later needed for calculations and organizing the output
        course_name = ""
        ects_credit = 0
        teacher_names = []
    
        cour_file = open(courses_file, "r")
        
        for line in cour_file:
            parts = line.strip().split(",")
            c_course_id = parts[0]

            if c_course_id == p_course_id:
                course_name = parts[1]
                ects_credit = int(parts[2])
                teacher_names = parts[3:]
                break

        cour_file.close()

        teacher_str = ""
        for t in teacher_names:
            if teacher_str != "":
                teacher_str += ", "
            teacher_str += t
        
        print(f"Course ID: {p_course_id}, Name: {course_name}, Credits: {ects_credit}")
        print(f"Date: {p_exam_date}, Teacher(s): {teacher_str}, Grade: {p_grade}")

    # Calculations
        total_ects += ects_credit
        grade_sum += p_grade
        course_count += 1

    if course_count > 0:
        average_grade = grade_sum / course_count
    else:
        average_grade = 0

    print()
    print(f"Total Credits: {total_ects}, Average Grade: {average_grade}")
    print()
    



# ---- MENU ----
def main():
    while True:
        print("You may select one of the following:\n")
        print("1) Add student")
        print("2) Search student")
        print("3) Search course")
        print("4) Add course completion")
        print("5) Show student's record")
        print("0) Exit\n")
        choice = input("What is your selection?\n").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            add_student()        

        elif choice == "2": 
            search_student()
            
        elif choice == "3":
            search_course()
            
        elif choice == "4":
            add_course_completion()
            
        elif choice == "5":
            show_student_record()

        else:
            print("Invalid choice, please enter a number between 0 and 5.\n")


if __name__ == "__main__":
    main()



