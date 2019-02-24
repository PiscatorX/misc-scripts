#!/usr/bin/python
import tkinter as tk

class CountWords(object):

    def __init__(self, master):

        self.master = master
        master.title("Count words")
        self.frame1 = tk.Frame(master,
                               width=100,
                               height=100, bd= 10)
        self.frame1.pack()
        self.wc_input =  tk.Text(self.frame1)
        self.master.bind("<Key>", self.wc)
        self.wc_input.pack()
        self.text_label = tk.Label(master, text= "0 Words.")
        self.text_label.pack()
        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()
 
    def wc(self, event):
        word = self.wc_input.get('1.0','end')
        wc = len(word.split())
        self.text_label.config(text=" ".join([str(wc),'Words']))
        

if __name__ == '__main__':
    root = tk.Tk()
    window = CountWords(root)
    root.mainloop()
