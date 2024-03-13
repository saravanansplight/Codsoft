from tkinter import Tk, Button, Entry

def update_display(value):
    current_value = entry_display.get()

    if value == '=':
        try:
            result = eval(current_value)
            entry_display.delete(0, 'end')
            entry_display.insert(0, result)
        except Exception as e:
            entry_display.delete(0, 'end')
            entry_display.insert(0, "Invalid Expression")
    else:
        entry_display.delete(0, 'end')
        entry_display.insert(0, current_value + str(value))

def clear_display():
    entry_display.delete(0, 'end')

window = Tk()
window.title("Calculator")

window.geometry('300x300')
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

entry_display = Entry(window, width=30, justify='right')
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

numbers = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '+', '=']
]

for i in range(4):
    for j in range(4):
        button = Button(window, text=numbers[i][j], width=6, height=3, command=lambda x=numbers[i][j]: update_display(x))
        button.grid(row=i+1, column=j, padx=5, pady=5)

button_clear = Button(window, text='C', width=6, height=3, command=clear_display)
button_clear.grid(row=5, column=0, padx=5, pady=5)

window.mainloop()
