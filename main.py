from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles and Kilometers converter")
window_height = 120
window_width = 280
window.minsize(width=window_width, height=window_height)
window.config(padx=20, pady=20)
# Centering the window - tk build-in, but not working well
# window.eval('tk::PlaceWindow . center')
# Centering the window - manually
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Label
label_top = Label(text="     ")
# label.config(text="This is new text")
label_top.grid(column=0, row=0)
label_top_unit = Label(text="miles")
label_top_unit.grid(column=2, row=0)

label_bot = Label(text="is equal to")
label_bot.grid(column=0, row=1)
label_bot_unit = Label(text="km")
label_bot_unit.grid(column=2, row=1)

label_bot_answer = Label(text="0")
label_bot_answer.grid(column=1, row=1)

# Entry
entry_miles = Entry(width=10)
# Add some text to begin with
entry_miles.insert(END, string=" ")
# Gets text in entry
print(entry_miles.get())
# Display using grid
entry_miles.grid(column=1, row=0)


# Buttons
def action():
    miles = float(entry_miles.get())
    km = miles*1.60934
    label_bot_answer.config(text=f"{km}")

# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)





window.mainloop()
