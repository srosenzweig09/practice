import tkinter as tk
import numpy as np
from random_word import RandomWords

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

### Functions are defined here! ###
def drawLimb(count):
    """Makes a new limb appear if the user guesses an incorrect letter."""
    # Create hangman
    print(count)
    if count == 1:
        c.create_oval(180,150,220,190) # Head
    elif count == 2:
        c.create_line(200,190,200,250) # Torso
    elif count == 3:
        c.create_line(200,200,220,230) # Right arm
    elif count == 4:
        c.create_line(200,200,180,230) # Left arm
    elif count == 5:
        c.create_line(200,250,185,280) # Left leg
    elif count == 6:
        c.create_line(200,250,215,280) # Right leg
    

def checkLetter(index,count):
    """Checks the letter that the user guesses to see if it is correct."""
    buttons[index].config(state="disabled")
    f = True
    for i,letter in enumerate(word):
        if letter == letters[index]:
            word_buttons[i].config(text=letter)
            f = False
    if f:
        print("I should be drawing...")
        count+=1
        drawLimb(count)


# Create main window as master, 'm'.
m = tk.Tk(screenName='Hangman')
m.title('Hangman Game')
# Gets the requested values of the height and widht.
windowWidth = m.winfo_reqwidth()
windowHeight = m.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(m.winfo_screenwidth()/3 - windowWidth/2)
positionDown = int(m.winfo_screenheight()/3 - windowHeight/2)
#m.geometry("+{}+{}".format(positionRight, positionDown))
m.geometry("500x600+{}+{}".format(positionRight, positionDown))


# Create a canvas on which to draw image of hangman.
c = tk.Canvas(m, width=500, height=400)
# Pack up the canvas (organizes in blocks)
c.grid()

# Create two different frames. The top will contain the hangman drawing and the hidden word. The bottom frame will contain the keyboard.
top_frame = tk.Frame(m)
top_frame.grid()
bottom_frame = tk.Frame(m)
bottom_frame.grid()

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

word = generate_word()
print(word)
word_dic = {}

size = 1
word_buttons = []
for index in range(len(word)):
    word_dic[word[index]] = index
    letter = word[index]
    word_button = tk.Button(top_frame, height=size, width=size, highlightbackground='black')
    word_button.grid(padx=3,pady=1, row=0, column=index)
    #word_button.grid_forget()
    word_buttons.append(word_button)

# Create hangman's gallows.
c.create_line(300,300,400,300)
c.create_line(350,300,350,100)
c.create_line(350,100,200,100)
c.create_line(200,100,200,150)


# Create letter buttons
size = 1
buttons = []
dic = {}
count = 0
for index in range(len(letters)):
    letter = letters[index]
    dic[letters[index]] = index
    button = tk.Button(bottom_frame, text=letter, command=lambda index=index, n=letter: checkLetter(index,count), height=size, width=size)
    button.grid(padx=3,pady=1, row=int(np.floor(index/10)+3), column=index%10)
    buttons.append(button)

# Create End Game button
stop = tk.Button(m, text='End Game', height=size, width=25, command=m.destroy)
stop.grid(row=3,column=0, columnspan = 10)







m.mainloop()

