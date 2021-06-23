import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class Application(tk.Frame):
    def __init__(self, master=None):
        print("Initializing application.")
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_frames()
        self.create_widgets()

        print("Congratulations! You've plotted?")
        # the figure that will contain the plot
        self.fig = Figure(figsize = (4, 4), dpi = 100)
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master = self.top_frame)  
        self.canvas.draw()
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack()

    def create_frames(self):
        self.top_frame = tk.Frame(master=self.master)
        self.bottom_frame = tk.Frame(master=self.master)
        self.left_frame = tk.Frame(master=self.master)

        self.top_label = tk.Label(master=self.top_frame)
        self.bottom_label = tk.Label(master=self.bottom_frame)
        self.left_label = tk.Label(master=self.left_frame)

        self.top_label.pack(fill=tk.X)
        self.bottom_label.pack(fill=tk.X)
        self.left_label.pack(fill=tk.Y)
        self.top_frame.pack(fill=tk.X)
        self.bottom_frame.pack(fill=tk.X)
        self.left_frame.pack(fill=tk.Y)

    def create_widgets(self):
        print("Creating widget buttons.")
        self.plot_button = tk.plot_button = tk.Button(master = self.bottom_frame, 
                     command = self.plot,
                     height = 2, 
                     width = 10,
                     text = "Plot")
        self.plot_button.pack()

        self.quit = tk.Button(master = self.bottom_frame, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack()

    def plot(self):
    
        # list of squares
        y = [i**2 for i in range(101)]
    
        # adding the subplot
        plot1 = self.fig.add_subplot(111)
    
        # plotting the graph
        plot1.plot(y)
    
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(self.canvas, self.top_frame)
        toolbar.update()
    
        # placing the toolbar on the Tkinter window
        self.canvas.get_tk_widget().pack()

root = tk.Tk()
root.geometry("600x600")
app = Application(master=root)
app.mainloop()