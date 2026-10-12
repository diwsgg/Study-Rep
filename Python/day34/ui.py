import tkinter as tk
from pathlib import Path
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
folder_path = str(Path.cwd())+'/images'
CHECK_IMAGE_PATH = folder_path+'/true.png'
WRONG_IMAGE_PATH = folder_path+'/false.png'

class Quiz_interface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title('Quizzler')

        #UI
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #label
        self.label_entry = tk.Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white', font=("Arial", 15))
        self.label_entry.grid(column=1, row=0)

        #CANVA
        #canva object for logo
        self.canvas = tk.Canvas(width=300, height=250, bg='white')
                                        # x, y coordenates (center of canvas obj)
        self.canvas_txt = self.canvas.create_text(150,125, width=280, font=("Arial", 20,"italic"), text='', fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #BUTTONS
       
        #create the image for the buttons
        #1
        check_image = tk.PhotoImage(file=CHECK_IMAGE_PATH)
        self.button_check = tk.Button(image=check_image, command=self.right_button_press, highlightthickness=0)
        self.button_check.grid(column=1, row=2)

        #2
        wrong_image = tk.PhotoImage(file=WRONG_IMAGE_PATH)
        self.button_wrong = tk.Button(image=wrong_image, command=self.wrong_button_press, highlightthickness=0)
        self.button_wrong.grid(column=0, row=2)

        self.get_next_question()
        
        self.window.mainloop()


    #We need to create a method to change the question
    def get_next_question(self):
        #turn back to white color
        self.canvas.config(bg='white')
        #change the score
        self.label_entry.config(text=f'Score: {self.quiz.score}')
        if (self.quiz.still_has_questions()):
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_txt, text= q_text)
        else:
            #finish the program
            self.canvas.itemconfig(self.canvas_txt, text='No more questions')
            #we disable the button to not continue pressing them
            self.button_check.config(state='disabled')
            self.button_wrong.config(state='disabled')
            
    #Buttons assign
    def right_button_press(self):
        is_ok = self.quiz.check_answer('True')
        #instaed of passing here to the next question we are going to compare if is right or not
        self.feedback(is_ok)
            
    def wrong_button_press(self):
        is_ok= self.quiz.check_answer('False')
        self.feedback(is_ok)

    def feedback(self, check : bool):
        if check:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        
        #we change the question after that
        self.window.after(1000, self.get_next_question)




