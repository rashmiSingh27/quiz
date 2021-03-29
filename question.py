class Question:
    ques=[]
    options=[]
    answers=[]
    topic=[]
    difficulty=[]
    c1=1
    c2=1
    c3=1
    d_easy={}
    d_med={}
    d_hard={}

    def __init__(self):
        self.score=0

    def addQuestion(self, topic, difficulty):

        q=input("Enter question:")
        Question.ques.append(q)
        Question.topic.append(topic)
        Question.difficulty.append(difficulty)
        l1=[]
        for i in range(4):
            l1.append(input("enter option no." + chr(i + 65) + ":"))
        Question.options.append(l1)
        ans=input("correct ans is :")
        Question.answers.append(ans)
        #print(Question.ques)
        #print(Question.topic)
        #print(Question.options)
        #print(Question.answers)

        if difficulty == "easy":
            Question.d_easy[Question.c1]=[Question.ques[-1], Question.options[-1], Question.answers[-1],
                                          Question.topic[-1]]
            Question.c1+=1
        #print("d_Easy", Question.d_easy)
        if difficulty == "medium":
            Question.d_med[Question.c2]=[Question.ques[-1], Question.options[-1], Question.answers[-1],
                                         Question.topic[-1]]
            Question.c2+=1
        #print("d_meduim", Question.d_med)
        if difficulty == "hard":
            Question.d_hard[Question.c3]=[Question.ques[-1], Question.options[-1], Question.answers[-1],
                                          Question.topic[-1]]
            Question.c3+=1
        print("Question Added ")
        print('\n')


    def displayAllQuestions(self):
        for i in range(len(Question.ques)):
            print("Q." + str(i + 1)+"-" + Question.ques[i])
            for j in range(4):
                print(chr(j + 65) + ":" + str(Question.options[i][j]))
            print("ans:",Question.answers[i])
            print("\n")


    def viewTopics(self):
        a=set(Question.topic)
        print(a)


    def run_test(self, mem_name):
        self.score=0
        self.mem_name=mem_name
        p=input("Enter difficulty level:")
        # if Question.prompt:
        #   for statement in range(len(Question.d_)):
        #      p=input("enter difficulty level:")
        if p == "easy" and len(Question.d_easy) > 0:
            print("in easy")
            for i in range(len(Question.d_easy)):
                print(Question.d_easy[i + 1][0])
                for j in range(4):
                    print(chr(j + 65) + ": " + Question.d_easy[i + 1][1][j])
                a=input("ANSWER:")
                if a == Question.d_easy[i + 1][2]:
                    print("correct answer")
                    self.score+=1
                else:
                    print("Wrong answer !!!,correct=",Question.d_easy[i + 1][2])
        elif p == "hard" and len(Question.d_hard) > 0:
            # print(Question.d_hard)
            for i in range(len(Question.d_hard)):

                print(Question.d_hard[i + 1][0])
                for j in range(4):
                    print(chr(j + 65) + ": " + Question.d_hard[i + 1][1][j])
                a=input("ANSWER:")
                if a == Question.d_hard[i + 1][2]:
                    print("correct answer")
                    self.score+=1
                else:
                    print("Wrong answer!!!,correct=", Question.d_hard[i + 1][2])

        elif p == "medium" and len(Question.d_med) > 0:
            for i in range(len(Question.d_med)):
                print(Question.d_med[i + 1][0])
                for j in range(4):
                    print(chr(j + 65) + ": " + Question.d_med[i + 1][1][j])
                a=input("ANSWER:")
                if a == Question.d_med[i + 1][2]:
                    self.score+=1
                    print("correct answer")
                else:
                    print("Wrong answer!!!,correct=", Question.d_medium[i + 1][2])
        else:
            print("____________no questions added yet.Ask admin______________")
        # print("your score:",self.score)
        return self.score, self.mem_name

    def checkscore(self):
        print(self.score)
