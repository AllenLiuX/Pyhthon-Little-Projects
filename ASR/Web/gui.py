import tkinter as tk

class GUI:
    def __init__(self, master):
        self.master = master
        self.entry1 = tk.Entry(master, bd=2)
        self.entry1.place(x=50,y=50, width=250, anchor='nw')
        self.button1 = tk.Button(master, text='send', command=self.send)
        self.button1.place(x=320,y=55, anchor='nw')

        self.var = tk.StringVar()
        self.select = tk.Radiobutton(master, text='Url', variable = self.var, value = 'Url')
        self.select2 = tk.Radiobutton(master, text='Path', variable = self.var, value = 'Path')
        self.select.place(x=50,y=25)
        self.select2.place(x=150, y=25)
        self.select2.place()
        self.label = tk.Label(master, font='Helvetica', text='', wraplength = 200, justify = 'left')
        self.label.place(x=50, y=80)
    def send(self):
        txt = self.entry1.get()
        self.label['text'] = txt

def main():
    window = tk.Tk()
    window.title('ASR Platform')
    window.geometry('400x400')
    interface = GUI(window)
    window.mainloop()

main()