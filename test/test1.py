import tkinter as tk
import Person as person

counter = 0 
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()
 
#p = person.Person()
print("Created person successfully")
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25)
button.configure(command=root.destroy)
button.pack()
root.mainloop()