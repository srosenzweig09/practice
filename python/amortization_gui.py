import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_frame = tk.Frame(master=self.master)
        self.title_label = tk.Label(master=self.title_frame, text="Amortization Graph", font=("Arial", 20))
        empty_frame = tk.Frame(master = self.title_frame, height=25)
        empty_frame.pack(fill=tk.X, side='top')
        self.title_label.pack(fill=tk.X, side='top')
        self.title_frame.pack(fill=tk.X, side='top')

        self.body_frame = tk.Frame(master=self.master)
        self.body_label = tk.Label(master=self.body_frame)
        self.body_label.pack(fill=tk.X, side='top')
        self.body_frame.pack(fill=tk.X, side='top')

        self.menu_frame = tk.Frame(master=self.master)
        self.plot_frame = tk.Frame(master=self.master)
        self.top_frame = tk.Frame(master=self.menu_frame)
        self.bottom_frame = tk.Frame(master=self.menu_frame)

        self.menu_label = tk.Label(master=self.menu_frame)
        self.top_label = tk.Label(master=self.top_frame)
        self.bottom_label = tk.Label(master=self.bottom_frame)
        self.plot_label = tk.Label(master=self.plot_frame)

        self.menu_label.pack(fill=tk.Y, side='left')
        self.plot_label.pack(fill=tk.Y, side='right')
        self.menu_frame.pack(fill=tk.Y, side='left')
        self.plot_frame.pack(fill=tk.Y, side='right')
        
        self.top_label.pack(fill=tk.X, side='left')
        self.bottom_label.pack(fill=tk.X,side='bottom')
        self.top_frame.pack(fill=tk.X, side='left')
        self.bottom_frame.pack(fill=tk.X, side='bottom')

        empty_frame = tk.Frame(master = self.menu_frame, height=50)
        empty_frame.pack(fill=tk.Y, side='top')

        self.principal_label = tk.Label(master = self.menu_frame, text="Principal Amount")
        self.principal_label.pack(fill=tk.X, side='top', padx=50, pady=(50,0))

        self.principal_entry = tk.Entry(master = self.menu_frame)
        self.principal_entry.pack(fill=tk.X, side='top', padx=50)
        self.principal_entry.insert(tk.INSERT, "154000")

        self.interest_label = tk.Label(master = self.menu_frame, text="Interest Rate")
        self.interest_label.pack(fill=tk.X, side='top', padx=50, pady=(15,0))

        self.interest_entry = tk.Entry(master = self.menu_frame)
        self.interest_entry.pack(fill=tk.X, side='top', padx=50)
        self.interest_entry.insert(tk.INSERT, "0.02785")

        self.time_label = tk.Label(master = self.menu_frame, text="Length of Loan (Years)")
        self.time_label.pack(fill=tk.X, side='top', padx=50, pady=(15,0))

        self.time_entry = tk.Entry(master = self.menu_frame)
        self.time_entry.pack(fill=tk.X, side='top', padx=50)
        self.time_entry.insert(tk.INSERT, "30")

        self.additional_label = tk.Label(master = self.menu_frame, text="Additional Monthly")
        self.additional_label.pack(fill=tk.X, side='top', padx=50, pady=(15,0))

        self.additional_entry = tk.Entry(master = self.menu_frame)
        self.additional_entry.pack(fill=tk.X, side='top', padx=50)

        # the figure that will contain the plot
        self.fig = Figure(figsize = (4, 4), dpi = 100)
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master = self.plot_frame)  
        self.canvas.draw()
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack(fill=tk.X, padx=50, pady=50)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.plot_frame)

        self.quit = tk.Button(master = self.menu_frame, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(fill=tk.X, side='bottom', padx=25)

        self.plot_button = tk.Button(master = self.menu_frame, 
                     command = self.plot,
                     height = 2, 
                     width = 10,
                     text = "Plot")
        self.plot_button.pack(fill=tk.X, side='bottom', padx=25)

    def plot(self):
    
        principal, interest, time = self.calculate_amortization()
    
        # adding the subplot
        plot1 = self.fig.add_subplot(111)
    
        # plotting the graph
        plot1.plot(time, principal, label='Principal Amount')
        plot1.plot(time, interest, label='Interest Paid')
        plot1.legend()
        plt.tight_layout()
    
        # creating the Matplotlib toolbar
        self.toolbar.update()
    
        # placing the toolbar on the Tkinter window
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def calculate_amortization(self):
        loan_amount, interest_rate, additional_monthly, time = 0, 0, 0, 30

        try:
            loan_amount = float(self.principal_entry.get())
            interest_rate = float(self.interest_entry.get())
            additional_monthly = float(self.additional_entry.get())
            time = int(self.time_entry.get())
        except:
            pass

        assert loan_amount >= 0, print("ERROR: Loan amount amount must be positive.")
        assert interest_rate >= 0 and interest_rate <= 1, print("ERROR: Interest rate must be a decimal value between 0 and 1.")
        assert additional_monthly >= 0, print("ERROR: Additional monthly payment must be positive.")
        assert time >= 0, print("ERROR: Length of loan must be a positive number.")

        n = 12 # assumes a monthly payment
        monthly_payment = loan_amount * (interest_rate / n) / (1 - (1 + interest_rate / n)**(-n*time))

        principal_array = np.array((loan_amount), dtype=float)
        interest_array = np.array((), dtype=float)
        time_array = np.arange(time*n+1)

        principal = loan_amount
        total_interest_paid = 0

        while principal > 1e-3:
            interest_payment = principal * interest_rate / n
            principal_payment = monthly_payment - interest_payment
            principal -= principal_payment

            total_interest_paid += interest_payment
            principal_array = np.append(principal_array, principal)
            interest_array = np.append(interest_array, total_interest_paid)

        interest_array = np.append(interest_array, total_interest_paid)

        return principal_array, interest_array, time_array


root = tk.Tk()
root.geometry("800x600")
app = Application(master=root)
app.mainloop()