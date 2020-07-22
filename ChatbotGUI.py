# GUI for chat bot

from tkinter import *

# GUI for Chat Bot
window = Tk()

window.title('Friday Bot')
window.geometry('530x500')
main_menu = Menu(window)

# Main Menu

# Sub Menu
file_menu = Menu(window)
file_menu.add_command(label='New...')
file_menu.add_command(label='Save As...')
file_menu.add_command(label='Exit')

# Menu Bar
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')

window.config(menu=main_menu)

# Chat Window

chatWindow = Text(window, bd=1, bg='#ABB2B9', width=50, height=8)
chatWindow.place(x=6, y=6, height=385, width=500)

# Type window
typeWindow = Text(window, bg='#85C1E9', width=30, height=4)
typeWindow.place(x=128, y=400, height=88, width=260)

#typeWindow.place(x=128, y=400, height=88, width=260)

# Button to send

def sendCommand():
    send = 'You: ' + typeWindow.get(END)
    chatWindow.insert(END, "\n" + send)


sendButton = Button(window, text='Send',command=sendCommand, bg='#7D3C98', activebackground='#D2B4DE', width=112,
                    height=5)
sendButton.place(x=6, y=400, height=88, width=120)

# Button to clear

clearButton = Button(window, text='Clear', bg='#7D3C98', activebackground='#D2B4DE', width=112, height=5)
clearButton.place(x=390, y=399, height=88, width=120)

# Scrollbar

scrollbar = Scrollbar(window, command= chatWindow.yview())
scrollbar.place(x=510, y=5, height=385)

window.mainloop()
