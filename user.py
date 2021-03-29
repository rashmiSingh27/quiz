from question import Question


class User(Question):
    d={}  # stores all user details with name as key

    def __init__(self):
        super().__init__()
        self.sc={}  # stores name with scores

    def createUser(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.marks = 0
        if name not in User.d:

            User.d[self.name]={
                "name": self.name,
                "age": self.age,
                "email": self.email,
                "phone": self.phone,
                "marks": self.marks
            }
            print("User Added")
        else:
            print("name already exists.")

    def deleteUser(self, name):
        if name in User.d:
            User.d.pop(name)  # delete user from the user dict
            self.sc.pop(name)  # delete user from the score dict as well
            print("user deleted")
            print(User.d)
        else:
            print("name not found ")

    def updateUserMarks(self, name, marks):
        if name in User.d:
            # marks=input("enter new marks")
            User.d[name]["marks"]=marks
            self.sc[name]=marks

            print('\n')
        else:
            print("name not found ")

    def viewAll(self):
        if User.d:
            for i, j in User.d.items():
                print(i)
        else:
            print("list is empty.add users")

    def viewUserDetails(self, name):
        for i, j in User.d[name].items():
            print(i + "- " + str(j))
        # print(User.d[name])
