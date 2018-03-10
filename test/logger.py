import logging
import tkinter as tk
import MainGUI as mainGUI

class WidgetLogger(logging.Handler): 
    def __init__(self, widget): 
        logging.Handler.__init__(self) 
        self.setLevel(logging.INFO) 
        self.widget = widget 
        self.widget.configure(state='disabled')

    def emit(self, record): 
        self.widget.configure(state='normal')
        # Append message (record) to the widget 
        self.widget.insert(tk.END, record + '\n')
        self.widget.see(tk.END) # Scroll to the bottom 
        self.widget.configure(state='disabled')
        
newLogger = WidgetLogger(mainGUI.logText)
#mainGUI.createMainGUI()