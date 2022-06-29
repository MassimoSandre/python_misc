# import csv

# file = open('words.csv', encoding="utf8")

# csvreader = csv.reader(file)

# header = []

# header = next(csvreader)

# content = []
# for row in csvreader:
#     content.append(row)

import csv
import tkinter as tk
from typing import Collection

window = tk.Tk()
window.geometry("225x400")
window.title("Hello TkInter!")
window.resizable(False, False)
# window.configure(background="white")


class App:
    def __init__(self, window) -> None:
        self.correct = 0
        self.wrong = 0

        self.question_number =  1
        self.question = tk.Label(text=str(self.question_number),font=('Helvatical bold',20))
        self.question.grid(row=1,column=6,pady=20)        
        self.text = tk.Label(text="prova", font=('Helvatical bold',20))
        self.text.grid(row=2,column=6,pady=20)        
        self.description = tk.Label(text="provaprovaprova",font=('Helvatical bold',20))
        self.description.grid(row=3,column=6,pady=20)        

        self.entry = tk.Entry()
        self.entry.grid(row=4,column=6,pady=20)        

        confirm_button = tk.Button(text="Inizia il test", command=self.check_answer)
        confirm_button.grid(row=5,column=6, pady=20)

        file = open('words.csv', encoding="utf8")

        csvreader = csv.reader(file)

        header = []
        header = next(csvreader)

        self.content = []
        for row in csvreader:
            self.content.append(row)

        self.content = self.content[:3]

        self.text.config(text=self.content[self.question_number-1][0])
        self.description.config(text="Traduci in italiano:")
        print("zuz")

    def __update_question(self):
        self.text.config(text=self.content[self.question_number-1][0])

    def check_answer(self):
        input = self.entry.get()
        if self.content[self.question_number-1][2] == input:
            self.correct = self.correct+1
            print("giusto")
        else:
            self.wrong = self.wrong+1
            print("sbagliato")

        self.question_number = self.question_number+1
        if self.question_number <= len(self.content):
            self.__update_question()



app = App(window)

if __name__ == "__main__":
    window.mainloop()