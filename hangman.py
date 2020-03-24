import tkinter as tk
import numpy as np
from random_word import RandomWords

class Hangman(tk.Frame):

    def __init__(self):
        # Create main window as master, 'm'.
        super().__init__()
        self.initUI()
        self.test = 1
        
    def initUI(self):
        self.master.title('Hangman Game')
        self.grid()

        self.count = 0

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
        

        # Generate random words and draw one.
        def generate_word():
            rw = RandomWords()
            word = rw.get_random_word(hasDictionaryDef='true').upper()
            for i in word:
                if i == '-' or i == ' ':
                    generate_word()
            return word

        self.word = generate_word()
        print(self.word)
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
        size = 1
        buttons = []
        dic = {}
        for index in range(len(self.letters)):
            letter = self.letters[index]
            dic[self.letters[index]] = index
            button = tk.Button(bottom_frame, text=letter, command=lambda index=index, n=letter: self.checkLetter(index,self.count), height=size, width=size)
            button.grid(padx=3,pady=1, row=int(np.floor(index/10)+3), column=index%10)
            buttons.append(button)
        self.buttons = buttons

        # Create End Game button
        stop = tk.Button(self, text='End Game', height=size, width=25, command=self.destroy)
        stop.grid(row=3,column=0, columnspan = 10)

        return buttons

    def drawLimb(self, count):
        """Makes a new limb appear if the user guesses an incorrect letter."""
        # Create hangman
        if count == 1:
            self.c.create_oval(180,150,220,190) # Head
        elif count == 2:
            self.c.create_line(200,190,200,250) # Torso
        elif count == 3:
            self.c.create_line(200,200,220,230) # Right arm
        elif count == 4:
            self.c.create_line(200,200,180,230) # Left arm
        elif count == 5:
            self.c.create_line(200,250,185,280) # Left leg
        elif count == 6:
            self.c.create_line(200,250,215,280) # Right leg


    def checkLetter(self,index,count):
        """Checks the letter that the user guesses to see if it is correct."""
        self.buttons[index].config(state="disabled")
        f = True
        for i,letter in enumerate(self.word):
            if letter == self.letters[index]:
                self.word_buttons[i].config(text=letter)
                f = False
        if f:
            self.count+=1
            self.drawLimb(self.count)

def main():

    m = tk.Tk()
    # Gets the requested values of the height and width.
    app = Hangman()
    m.mainloop()

if __name__ == '__main__':
    main()