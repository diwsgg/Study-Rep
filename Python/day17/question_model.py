#could have attributes like

#Text, answer 

#Example

'''
new_q  = Question("2+3+5", "True")

we have this on data
''' 

class Question:
    #constructor, to initialize TEXT and answer
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
