# TODO 1 ASKING THE QUESTIONS
# TODO 2 CHECKING IF THE ANSWER WAS CORRECT
# TODO 3 CHECKING IF WE'RE THE END OF THE QUIZ

class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    #methods

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"\n You complete the quiz\n Yout final Score wa: {self.score}/{self.question_number}")
            return False
        
        # #We can do this to simplify it
        # return self.question_number<len(self.question_list)
        # #this will return true every time the condition is correct
    
    def check_answer(self, answer, currentq):
        if answer == currentq:
            self.score +=1
            print("That's right")
        else:
            print("That's wrong")
        print(f"The right answer is: {currentq} ")
        print(f"Your current score is: {self.score}/{self.question_number}")
    
    def next_question(self):

    #Try 1 By myself    
        # if self.question_number == 0:
        #     print(self.question_list[self.question_number])
        # elif self.question_number == len(self.question_list)-1:
        #     print("No more questions")
        # else:
        #     self.question_number += 1
        #     print(self.question_list[self.question_number])

    #Professor
        # current_question = self.question_list[self.question_number]
        # self.question_number +=1 
        # input(f'Q.{self.question_number}: {current_question.text}: "TRUE/FALSE" ')

    #Improving my version with professor
    #We are comparing if we're end of the list of questions 

        # current_question = self.question_list[self.question_number]
        # self.question_number +=1 
        # if self.question_number == len(self.question_list)-1:
        #     print("NO more questions")
        # else:
        #     input(f'Q.{self.question_number}: {current_question.text}: "TRUE/FALSE" ')

    #Final version
        
        current_question = self.question_list[self.question_number]
        self.question_number +=1 
        get_answer = input(f'Q.{self.question_number}: {current_question.text}: "TRUE/FALSE" ').title() 
        #Just do the counter not returning nothing just updating the score of the obj
        self.check_answer(get_answer, current_question.answer)

