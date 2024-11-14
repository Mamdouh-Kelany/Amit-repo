import datetime
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")  # Adjust height if necessary
        self.root.title("Amit-Diploma")
        self.root.configure(bg="light grey")

        # Title Label with an icon (icon path needed)
        self.icon_title = PhotoImage(file="E:\Amit\icon1.png")  # Add path to your image here
        title = Label(self.root, text="Amit- Machine Learning Diploma", image=self.icon_title, compound=CENTER,
                      font=("times new roman", 40, "bold"), bg="#010c00", fg="#3ADEA7", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Exit Button (previously Logout Button)
        btn_exit = Button(self.root, text="Exit", font=("times new roman", 15, "bold"), bg="orange", cursor="hand2", command=self.exit_program)
        btn_exit.place(x=1150, y=10, height=50, width=150)

        # Clock Label
        self.lbl_clock = Label(self.root, text="", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Call the clock update function
        self.update_clock()

        # Experience Input
        self.lbl_exp = Label(self.root, text="Experienced years:", font=("times new roman", 15), bg="light grey")
        self.lbl_exp.place(x=330, y=130)  # Adjusted position to reduce space

        self.entry_exp = Entry(self.root, font=("times new roman", 15))
        self.entry_exp.place(x=550, y=130, width=100)

        # Calculate Button
        btn_calculate = Button(self.root, text="Expected Salary", font=("times new roman", 15), bg="blue", fg="white",
                               cursor="hand2", command=self.calculate_y_hat)
        btn_calculate.place(x=690, y=125, height=30, width=150)  # Adjusted position to reduce space

        # Result Label for Y_hat
        self.lbl_result = Label(self.root, text="", font=("times new roman", 15), bg="light grey", fg="green")
        self.lbl_result.place(x=500, y=180)  # Adjusted position to reduce space

        # Contact Label (Ensure it's not hidden)
        self.lbl_contact = Label(self.root, text="Contact us : Mamdouh.Kelany84@mail.com    Facebook:AAA   Whatsup:01222324751",
                                 font=("times new roman", 15), bg="#4d636d", fg="yellow")
        self.lbl_contact.place(x=0, y=670, relwidth=1, height=30)  # Adjust this position if needed

        # Create a LabelFrame (acts as a Groupbox)
        groupbox = LabelFrame(self.root, text="Machine Learning", font=("Arial", 16), bg="#4d636d", fg="white", padx=10, pady=10)
        groupbox.place(x=0, y=250, width=200, height=400)  # Adjust position and size as needed

        # Add widgets inside the LabelFrame
        Label(groupbox, text="Calculating the Y_hat", borderwidth=1, relief="solid", font=("times new roman", 13, "bold"),
              bg="#ffffff", fg="black").place(x=0, y=0, width=180, height=40)
        Label(groupbox, text="Pending", borderwidth=1, relief="solid", font=("times new roman", 13, "bold"),
              bg="#ffffff", fg="black").place(x=0, y=100, width=180, height=40)
        Label(groupbox, text="Pending", borderwidth=1, relief="solid", font=("times new roman", 13, "bold"),
              bg="#ffffff", fg="black").place(x=0, y=200, width=180, height=40)
        Label(groupbox, text="Pending", borderwidth=1, relief="solid", font=("times new roman", 13, "bold"),
              bg="#ffffff", fg="black").place(x=0, y=300, width=180, height=40)
        Label(groupbox, text="Pending", borderwidth=1, relief="solid", font=("times new roman", 13, "bold"),
              bg="#ffffff", fg="black").place(x=0, y=400, width=180, height=40)

        # Information LabelFrame
        info_groupbox = LabelFrame(self.root, text="Information", font=("Arial", 16), bg="#F5FFFA", fg="black", padx=10, pady=10)
        info_groupbox.place(x=210, y=250, width=1120, height=400)  # Adjust position and size as needed

    def update_clock(self):
        now = datetime.datetime.now()
        current_time = now.strftime("Date: %d-%m-%Y\t\t Time: %H:%M:%S")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t {current_time}")
        self.lbl_clock.after(1000, self.update_clock)

    def calculate_y_hat(self):
        try:
            # Get the years of experience from the entry
            x = int(self.entry_exp.get())
            
            # Calculate Y_hat "Salary"
            Y_hat = 900 * x + 500
            
            # Display the result in lbl_result
            self.lbl_result.config(text=f"Salary: {Y_hat}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer for years of experience")

    def exit_program(self):
        # Display confirmation message before exiting
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            self.root.quit()  # This will close the application

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
