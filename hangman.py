import tkinter as tk
import numpy as np
from random_word import RandomWords
import sys
import os

class Hangman(tk.Frame):

    def __init__(self):
        # Create main window as master, 'm'.
        super().__init__()
        self.initUI()
        self.test = 1
        
    def initUI(self):
        self.master.title('Hangman Game')
        self.master.geometry("500x700")
        self.grid()

        self.doom_counter = 0
        self.success_counter = 0

        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # Create a canvas on which to draw image of hangman.
        c = tk.Canvas(self, width=500, height=400)
        # Pack up the canvas (organizes in blocks)
        c.grid()
        self.c = c

        # Create hangman's gallows.
        c.create_line(300,300,400,300)
        c.create_line(350,300,350,100)
        c.create_line(350,100,200,100)
        c.create_line(200,100,200,150)

        # Create two different frames. The top will contain the hangman drawing and the hidden word. The bottom frame will contain the keyboard.
        top_frame = tk.Frame(self)
        top_frame.grid()
        bottom_frame = tk.Frame(self)
        bottom_frame.grid()
        self.tf = top_frame
        self.bf = bottom_frame

        # Empty row spacers for aesthetic.
        spacer1 = tk.Label(top_frame, text = "")
        spacer1.grid(row = 4)
        spacer2= tk.Label(top_frame, text = "")
        spacer2.grid(row = 5)
        spacer3= tk.Label(bottom_frame, text = "")
        spacer3.grid(row = 6)
        

        # Generate random words and draw one.
        def generate_word():
            rw = RandomWords()
            word = rw.get_random_word(hasDictionaryDef='true').upper()
            for i in word:
                if i == '-' or i == ' ':
                    generate_word()
            return word

        self.word = generate_word()
        word_dic = {}

        size = 1
        word_buttons = []
        for index in range(len(self.word)):
            word_dic[self.word[index]] = index
            letter =self.word[index]
            word_button = tk.Button(top_frame, height=size, width=size, highlightbackground='black')
            word_button.grid(padx=3,pady=1, row=0, column=index)
            #word_button.grid_forget()
            word_buttons.append(word_button)

        self.word_buttons = word_buttons

        # Create letter buttons
        buttons = []
        dic = {}
        for index in range(len(self.letters)):
            letter = self.letters[index]
            dic[self.letters[index]] = index
            button = tk.Button(bottom_frame, text=letter, command=lambda index=index, n=letter: self.checkLetter(index,self.doom_counter), height=size, width=size)
            button.grid(padx=3,pady=1, row=int(np.floor(index/10)+3), column=index%10)
            buttons.append(button)
        self.buttons = buttons


        # Create End Game button
        stop = tk.Button(self, text='Restart Game', height=size, width=25, command=self.stopButton)
        stop.grid(row=3,column=0, columnspan = 10)

        return buttons

    def stopButton(self):
            self.destroy()
            self.__init__()

    def drawLimb(self, doom_counter):
        """Makes a new limb appear if the user guesses an incorrect letter."""
        # Create hangman
        if doom_counter == 1:
            self.c.create_oval(180,150,220,190) # Head
            self.left_eye = self.c.create_oval(194,164,196,166) # Left eye
            self.right_eye = self.c.create_oval(204,164,206,166) # Right eye
            self.mouth = self.c.create_line(192,177,208,177) # Mouth
        elif doom_counter == 2:
            self.c.create_line(200,190,200,250) # Torso
        elif doom_counter == 3:
            self.c.create_line(200,200,220,230) # Right arm
        elif doom_counter == 4:
            self.c.create_line(200,200,180,230) # Left arm
        elif doom_counter == 5:
            self.c.create_line(200,250,185,280) # Left leg
        elif doom_counter == 6:
            self.c.create_line(200,250,215,280) # Right leg
            self.c.create_text(250,50,text='You Lose!', font=("Purisa", 30), fill='red', anchor=tk.CENTER)
            self.c.delete(self.mouth)
            self.c.create_arc(190,175,210,190,start=0, extent=180)
            self.c.delete(self.left_eye)
            self.c.create_line(192,162,198,168)
            self.c.create_line(192,168,198,162)
            self.c.delete(self.right_eye)
            self.c.create_line(202,162,208,168)
            self.c.create_line(202,168,208,162)
            for i,letter in enumerate(self.word):
                self.word_buttons[i].config(text=letter)


    def checkLetter(self,index,doom_counter):
        """Checks the letter that the user guesses to see if it is correct."""
        self.buttons[index].config(state="disabled")
        f = True
        for i,letter in enumerate(self.word):
            if letter == self.letters[index]:
                self.word_buttons[i].config(text=letter)
                f = False
                self.success_counter += 1
                if self.success_counter == len(self.word):
                    self.c.create_text(250,50,text='You Win!', font=("Purisa", 30), fill='green', anchor=tk.CENTER)
                    self.c.delete(self.mouth)
                    self.c.create_arc(185,155,215,185,start=180, extent=180)
        if f:
            self.doom_counter+=1
            self.drawLimb(self.doom_counter)


def main():

    m = tk.Tk()
    # Gets the requested values of the height and width.
    app = Hangman()
    m.mainloop()

if __name__ == '__main__':
    main()