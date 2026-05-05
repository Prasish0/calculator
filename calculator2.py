import tkinter

# Move the function definition to the top to avoid NameError
def button_clicked(value):
    current_text = label.cget("text")
    
    if value == "AC":
        label.config(text="0")
    elif value == "=":
        try:
            # Note: eval() is used here for simplicity in this example
            result = eval(current_text)
            label.config(text=str(result))
        except:
            label.config(text="Error")
    else:
        if current_text == "0":
            label.config(text=value)
        else:
            label.config(text=current_text + value)

button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

# Main container frame
frame = tkinter.Frame(window, bg=color_black)
frame.pack()

# Label Setup - span across all columns using columnspan
label = tkinter.Label(frame, text='0', font=("Arial", 45), anchor="e",
                      background=color_black, foreground=color_white, 
                      width=10, height=2)
label.grid(row=0, column=0, columnspan=4) 

# Grid Loop
for row in range(len(button_values)):
    for column in range(len(button_values[0])):
        value = button_values[row][column]
        
        # Determine button color based on your symbol lists
        bg_color = color_dark_gray
        fg_color = color_white
        
        if value in ["/", "*", "-", "+", "="]:
            bg_color = color_orange
        elif value in ["AC", "+/-", "%"]:
            bg_color = color_light_gray
            fg_color = color_black

        button = tkinter.Button(frame, text=value, font=("Arial", 25), 
                                width=4, height=1, 
                                bg=bg_color, fg=fg_color,
                                command=lambda v=value: button_clicked(v))
        button.grid(row=row+1, column=column, sticky="nsew", padx=1, pady=1)

window.mainloop()