import tkinter as tk



#1
app=tk.Tk()
app.title("My First Tkinter App")
app.geometry("300x200")
app.resizable(True,True)
label=tk.Label(app, text="Welcome to Tkinter!",font=("Arial",20))
label.pack(pady=20)
close_button=tk.Button(app,text="Close",font=("Arial",15),command=app.destroy)
close_button.pack()

app.mainloop()

#2
def get_message():
    message['text']=f"Hello {entry_field.get()}!"

app=tk.Tk()
app.geometry("300x200")
app.resizable(True,True)
label=tk.Label(app, text="Enter your name: ",font=("Arial",20))
label.pack(pady=20)
entry_field=tk.Entry(app)
entry_field.pack()
button=tk.Button(app,text="Greet Me!",command=get_message)
button.pack()
message=tk.Label(font=("Arial",20))
message.pack(pady='10')
app.mainloop()

#3
count=0
def increase():
    global count
    count+=1
    label["text"] = f"Counter: {count}"
def decrease():
    global count
    count-=1
    label["text"]=f"Counter: {count}"


app=tk.Tk()
app.geometry("300x200")
app.resizable(True,True)
label=tk.Label(app, text=f"Counter: {count}",font=("Arial",20))
label.pack()

button_decrease=tk.Button(app,text="Decrease",command=decrease)
button_increase=tk.Button(app,text="Increase",command=increase)
button_decrease.pack()
button_increase.pack()
app.mainloop()
#4


app=tk.Tk()
app.geometry("300x200")
app.resizable(True,True)
top_bar=tk.Frame(app,height=50,bg="red")
top_bar.pack(fill='x')
center=tk.Frame(app,bg="green")
center.pack(fill='both',expand=True)
blue_bottom=tk.Frame(app,height=50,bg='blue')
blue_bottom.pack(fill='x')
app.mainloop()


#5

val = ''

def update(t):
    global val
    val += t
    answer.config(text=val)

def clean():
    global val
    val = ''
    answer.config(text='0')

def result():
    global val
    try:
        val = str(eval(val))
    except Exception:
        val = 'Error'
    answer.config(text=val)

app = tk.Tk()
app.geometry("300x500")

answer = tk.Label(app, text="0", font=("Helvetica", 20),anchor='e', width=14)
answer.grid(sticky="nsew",columnspan=4)

for i in range(4):
    app.columnconfigure(i, weight=1)
for i in range(2, 6):
    app.rowconfigure(i, weight=1)

symbols = [['7','8','9','/'],['4','5','6','*'],['1','2','3','+'],['0','-']]
for i in range(4):
    for j in range(len(symbols[i])):
        t = symbols[i][j]
        tk.Button(app, text=t, font=("Helvetica", 20), command=lambda x=t: update(x)).grid(
            row=i+2, column=j, sticky="nsew", padx=5, pady=10
        )

tk.Button(app, text='C', font=("Helvetica", 20), command=clean).grid(row=5, column=2, sticky="nsew", padx=5, pady=10)
tk.Button(app, text='=', font=("Helvetica", 20), command=result).grid(row=5, column=3, sticky="nsew", padx=5, pady=10)

app.mainloop()