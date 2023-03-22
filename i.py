import tkinter
import tkinter.scrolledtext
    
def write():
    code = text_area.get('1.0', 'end')
    print(code )
    message = f"compiled successfully"
    output_area.config(state='normal')
    output_area.delete('1.0', 'end')
    output_area.insert('end', message)
    output_area.yview('end')
    output_area.config(state='disabled') 

def stop():
    exit(0)

def on_closing(event=None):
    win.quit()

win = tkinter.Tk()
win.title("Mini java compiler")
win.protocol("WM_DELETE_WINDOW", on_closing)
win.configure(bg="#021b39")

#progam code
program_label = tkinter.Label(win, text="Program :", bg="#021b39")
program_label.config(font=("Arial", 12), fg='white')
program_label.pack(padx= 20, pady= 5)

text_area = tkinter.scrolledtext.ScrolledText(win)
text_area.pack(padx=20, pady=5)
text_area.config(font=("Cascadia Code", 12) , height=20)


#compile button
compile_button = tkinter.Button(win, text="Compile", command=write)
compile_button.config(font=("Arial", 12))
compile_button.pack(padx= 20, pady= 5)

#compiler output
output_label = tkinter.Label(win, text="Output :", bg="#021b39")
output_label.config(font=("Arial", 12), fg='white')
output_label.pack(padx= 20, pady= 5)

output_area = tkinter.Text(win)
output_area.pack(padx= 10, pady= 10)
output_area.config(state="disabled", height=3)


gui_done = True

win.mainloop()
win.protocol("wM_DELETE_WINDOW", stop)