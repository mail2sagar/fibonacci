from tkinter import *
root = Tk()

root.title("Fibonacci Number Series")
root.geometry("500x500")

label = Label(root,text="The numbers are: ")

def series():
    first_no = 0
    second_no = 1
    sum = 0
    numbers = 20
    i = 1
    total = 0
    while i<numbers:
        label["text"]+=str(sum)+" "
        i = i+1
        first_no = second_no
        second_no = sum
        sum = first_no+second_no
        total = total+sum

button = Button(root,text="Show Fibonacci Series", command=series)
label = Label(root,text="Total = ")

label["text"]+=str(label)

button.pack()
label.pack()

root.mainloop()