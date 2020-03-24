import tkinter as tk
import numpy as np
from random_word import RandomWords

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def drawLimb():
    print('Bad choice. :(')

def checkLetter(index):
    matches = []
    for i,letter in enumerate(word):
        if letter == letters[index]:
            matches.append(i)
    if len(matches) == 0:
        drawLimb()

def clickLetter(index):
    checkLetter(index)
    buttons[index].config(state="disabled")



# Create main window as master, 'm'.
m = tk.Tk(screenName='Hangman')
m.title('Hangman Game')
# Gets the requested values of the height and widht.
windowWidth = m.winfo_reqwidth()
windowHeight = m.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(m.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(m.winfo_screenheight()/2 - windowHeight/2)
#m.geometry("+{}+{}".format(positionRight, positionDown))
m.geometry("500x600")


# Create a canvas on which to draw image of hangman.
c = tk.Canvas(m, width=400, height=400)
# Pack up the canvas (organizes in blocks)
c.grid()

top_frame = tk.Frame(m)
top_frame.grid()
bottom_frame = tk.Frame(m)
bottom_frame.grid()

#empty row spacers
spacer1 = tk.Label(top_frame, text = "")
spacer1.grid(row = 4)
spacer2= tk.Label(top_frame, text = "")
spacer2.grid(row = 5)

#f = tk.Frame()
#f.grid(row=0, column=0, rowspan=3, columnspan=10)

#a = tk.Text()
#a.grid(c,row=0, column=0, rowspan=3, columnspan=10)

# Generate random words and draw one.
rw = RandomWords()
x = 200
y= x + 10
word = rw.get_random_word().upper()
print(word)

for i in range(len(word)):
    c.create_line(x,250,y,250)
    x+=15
    y+=15

size = 1
buttons = []
for index in range(len(letters)):
    letter = letters[index]
    button = tk.Button(bottom_frame, text=letter, command=lambda index=index, n=letter: clickLetter(index), height=size, width=size)
    button.grid(padx=3,pady=1, row=int(np.floor(index/10)+3), column=index%10)
    buttons.append(button)

stop = tk.Button(m, text='Stop', height=size, width=25, command=m.destroy)
stop.grid(row=3,column=0, columnspan = 10)







m.mainloop()

