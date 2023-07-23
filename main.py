import tkinter as tk


# Create a function to handle button click events
def on_button_click(event):
    current_text = result_label["text"]
    button_text = event.widget["text"]

    if button_text == "=":
        try:
            result = eval(current_text)
            result_label["text"] = str(result)
        except:
            result_label["text"] = "Error"
    elif button_text == "C":
        result_label["text"] = ""
    else:
        result_label["text"] = current_text + button_text


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row = 1
col = 0

for button in buttons:
    btn = tk.Button(root, text=button, font=("Arial", 20), padx=20, pady=20)
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

    btn.bind("<Button-1>", on_button_click)

# Run the main event loop
root.mainloop()
