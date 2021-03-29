
from question import  Question
from user import User


if __name__=="__main__":
    #choice = 1
    u1=User()
    q1=Question()
    super_user ={"r":"r"}
    while True:
        print ('\n=========WELCOME TO QUIZ MASTER==========')
        print ('-----------------------------------------')
        print ('1. login as admin')
        print ('2. login as quiz taker')
        choice = int (input ('ENTER YOUR CHOICE: '))
        if choice==1:
            user = input("Enter admin username:")
            password= input("Enter password:")
            if user in super_user and super_user[user] == password:
                print("Welcome Admin!!!!!!!!!!!!")
                #print("choose a function for operation:")
                while True:
                    print('\n=========ADMIN MENU=======================')
                    print("1.ADD QUESTIONS \n2.ADD USER \n3.DELETE USER \n4.UPDATE MARKS \n5.VIEW ALL USERS \n6.VIEW "
                          "USER DETAILS \n7.VIEW ALL QUESTIONS \n")
                    choose=int(input("Enter choice :"))
                    if choose == 1:
                        #print("adding quiz")
                        topic=input("Enter topic name:")
                        difficulty=input("Enter difficulty level:")
                        q1.addQuestion(topic,difficulty)

                    if choose ==2:
                        #print("creating user..")
                        name=input("Enter name:")
                        age= input("Enter age:")
                        email=input("Enter email:")
                        phone=input("Enter phone:")
                        u1.createUser(name,age,email,phone)
                    if choose ==3:
                        #print("adduser..")
                        name=input("Enter user name to be deleted")
                        u1.deleteUser(name)
                    if choose ==4:
                        #print("update marks of user..")
                        name=input("Enter username to be updated")
                        marks=input("Enter new marks:")
                        u1.updateUserMarks(name,marks)
                        print("Marks updated for ", name)
                    if choose == 5 :
                        print("List of  all users: ")
                        u1.viewAll()
                    if choose ==6:
                        #print("view a user")
                        name=input("Enter name of user to be viewed:")
                        u1.viewUserDetails(name)
                    if choose ==7:
                        q1.displayAllQuestions()


                    if choose ==0:
                        break


            else:
                print("______________wrong admin credentials.enter again_____________")
        elif choice==2:
            member_name = input("Enter you username:")
            if member_name in User.d:
                print("Welcome member!!!")

            while True :

                if member_name in User.d :

                    print("\n==============MEMBER MENU===============")
                    print("1.Take quiz \n2.Check your last score\n")
                    option = int(input("Enter your option:"))
                    #print("you option",option )
                    if option == 1:
                        #print("take quiz..")
                        score,name = q1.run_test(member_name)
                        u1.sc[name]=score
                        u1.updateUserMarks(name,score)

                    elif option ==2:
                        #print("show results..")
                        if u1.sc[member_name]:
                            print(u1.sc[member_name])
                        else:
                            print("__________No last score available!!!_____________")
                        #q1.checkscore()
                    elif option ==0:
                        break
                    else:
                        print("___________wrong input choice__________")
                        break

                else:
                    print("__________not authorized to take quiz.Ask Admin______________ ")
                    break
        else:
            break


