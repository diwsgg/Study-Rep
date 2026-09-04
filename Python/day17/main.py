from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank=[]
#Create n obj for the n questions
for i in question_data:
    #AT the 'i' position we access the key "txt" and "answer"
    # We are creating a new obj with the two values
    newQuestion = Question(i["q"],i["s"])

    #IS the same that writing: 
    # question_text = i["text"]
    # question_answer = i["answer"]
    # new_Question = Question(question_text,question_answer)

    #WE append those obj in a list (question bank)
    question_bank.append(newQuestion)

print(question_bank[0].text)

#Initialize
quiz = QuizBrain(question_bank)

#We can call the method in two ways, once its initialize it 

#QuizBrain.next_question(quiz) #Class name pass the obj
quiz.next_question() #obj.method without pass the obj again

#Going to the end

while quiz.still_has_questions(): # we have questions.... 
    quiz.next_question()

