

class student:     #create a class of student

    def __init__(self,std_id,std_name,std_lastname):
        self.id = std_id
        self.name = std_name
        self.lastname = std_lastname
    def get_id(self):
        return (self.id)
    def idname(self):
        return "(self.id) , (self.name) , (self.lastname)"

std_list = [] #create student list
std_txt = open("student.txt","r",encoding="utf-8").readlines() #read student.txt
for i in std_txt:
    if i.split()[0].isdigit() and len(i.split()[0]) == 6:
        std_list.append(i.rstrip().split()) #add students to student list
    else:
        continue

student_list = [] #separate student informations
for i in range(len(std_list)):
    studentt = student(std_list[i][0],std_list[i][1],std_list[i][2])
    student_list.append(studentt)


uni_list = [] #create university list
uni_txt = open("university.txt","r",encoding="utf-8").readlines() #read universtiy.txt
for i in uni_txt:
    uni_list.append(i.rstrip().split(",")) #add universities to university list


book_type = open("key.txt","r").readlines() #read key.txt
book_a = book_type[0]
book_b = book_type[1]

answ_list = [] #create answers list
answ_txt = open("answers.txt","r",encoding="utf-8").readlines() #read answers.txt
for i in answ_txt:
    answ_list.append(i.rstrip().split()) #add answers to answers list

def first(student_id):
    for i in std_list:
        if i[0] == student_id:
            return i
        else:
            print:("Student was not found! Student ID must contain 6 digits! \n Try Again:")

def uni_name(uni_number):
    for i in uni_list:
        if i[0] == (uni_number):
            return i[1]
def uni_point(uni_name):
    for i in uni_list:
        if i[1] == (uni_name):
            return i[2]

def uni_capacity(uni_name):
    for i in uni_list:
        if i[1] == (uni_name):
            return i[3]


def bubble_sort(listt, indx):  # bubble sort function
    len_list = len(listt)
    for i in range(0, len_list):
        for j in range(0, len_list - i - 1):
            if float(listt[j][indx]) < float(listt[j + 1][indx]):
                tempo = listt[j]
                listt[j] = listt[j + 1]
                listt[j + 1] = tempo
    return listt


university_list = bubble_sort(uni_list, 2)

def list_universities():  # list universities
    print("University Name / Base Point")
    for i in university_list:
        print(i[1], "/" ,i[2])
    input()

students_points = []
def std_answ_point(): #calculate student points
    resulttxt = open("result.txt" , "w" ,encoding="utf-8")
    for i in answ_txt:
        answerss = i.split(" ")[2]
        k = 0
        correct = 0
        empty = 0
        incorrect = 0
        if i[1] == "A":
            keyanswerss = book_a
            while k < 40:
                if answerss[k] == keyanswerss[k]:
                    correct+=1
                elif answerss[k] == "*":
                    empty +=1
                else:
                    incorrect +=1
                k += 1
        else:
            keyanswerss = book_b
            while k < 40:
                if answerss[k] == keyanswerss[k]:
                    correct+=1
                elif answerss[k] == "*":
                    empty +=1
                else:
                    incorrect +=1
                k += 1

        std_points = (15 * (correct - (incorrect / 4)))



        students_points.append([first(i[0:6]),str(std_points)])

        """resulttxt.writelines(str(first(i[0]) + "," + str(i[1]) + "," + str(correct) + "," +
                            str(incorrect) + "," + str(empty) + "," + str(std_points/15) + "," +
                            (std_points) + "," + str(i[3]) + "," + str(i[4])))"""



def department_name():
    print("DEPARTMENTS:")
    departments = []
    for k in university_list:
        if "University" in k[1]:
            y = (k[1].split("niversity"))
        else:
            y = (k[1].split("niversitesi"))
        if (y[1]) not in  departments:
            departments.append(y[1])
    for i in departments:
        print("_______________________")
        print (i)
    print("_______________________")
while True:  # Main Menu
    print("*MAIN MENU*")
    print("(1)Searh for a student with given ID")
    print("(2)List the university/universities and departments")
    print("(3)Create results.txt")
    print("(4)List the student information")
    print("(5)List the students placed in every university/department")
    print("(6)List the students who were not be able to placed anywhere")
    print("(7)List all the departments")
    user_input = input("..:")
    if user_input == "1":
        std_id_input = input("Press 0 for cancel...\n Student ID:")
        if std_id_input == "0":
            print("Cancelled...")
            break
        else:
            print(*first(std_id_input))

    elif user_input == "2":
        list_universities()
    elif user_input == "3":
        std_answ_point()
    elif user_input == "4":
        std_answ_point()
        students_list = bubble_sort(students_points, 1)
        for item in students_list:
            print(*item)

    elif user_input == "5":
        break
    elif user_input == "6":
        break
    elif user_input == "7":
        department_name()
    else:
        print("Choose Again...")
        continue