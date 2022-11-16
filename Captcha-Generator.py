from tkinter import*
import random
from tkinter import messagebox
# definig all the funtions:
'''Function for the outlining of the captcha canvas
and to design the captcha'''
code=" "
def outline():
  c.create_rectangle(80,10,240,70,fill='lightyellow')
  c.create_line(80,20,230,50)
  c.create_line(85,55,180,25)
  c.create_line(150,10,170,70)
  c.create_line(100,65,240,40)
# defining generating function
def generate():
  n=""
  for i in range(0,6):
    cap=random.randint(1,3)
    if(cap==1):
      value=random.randint(97,122)
      n+=chr(value)
    elif(cap==2):
      value=random.randint(65,90)
      n+=chr(value)
    else:
      value=random.randint(48,57)
      n+=chr(value)
  return n
#defining the refresh function
def refresh():
  ent_cap.delete(0,END)
  global code
  g=generate()
  code=g
  outline()
  c.create_text(160,40,text=code,font='calibri 28 bold')
  c.grid(row=3,column=10)
# defining check function
def check():
  chk=ent_cap.get()
  ent_cap.delete(0,END)
  global code
  Reg=Regno_ent.get()
  if(Reg.isdigit() and (len(Reg)==8 or len(Reg)==5)):
    temp=Regno_ent.get()
  else:
    messagebox.showerror("ERROR","Registration number not valid")
    Regno_ent.delete(0,END)
    g=generate()
    code=g
    outline()
    c.create_text(160,40,text=g,font='Calibri 28 bold')
    c.grid(row=3,column=10)
    return 0
  if(chk==code):
    messagebox.showinfo("SUCCESSFULL","Registration number %s is accessed successfully"%temp)
    Regno_ent.delete(0,END)
    g=generate()
    code=g
    outline()
    c.create_text(160,40,text=g,font='Calibri 28 bold')
    c.grid(row=3,column=10)
  else:
    messagebox.showerror("ERROR","Wrong Captcha entered, Try again")
    g=generate()
    code=g
    outline()
    c.create_text(160,40,text=g,font='Calibri 28 bold')
    c.grid(row=3,column=10)
    see=Label(root,text='re-enter',font='Times 10')
    see.grid(row=6,column=10)
def on_enter(e):
   sub_btn.config(background='lightblue', foreground= "red")
def on_leave(e):
   sub_btn.config(background= 'white', foreground= 'black')
# defining the geometry of parent window
root=Tk()
root.geometry('450x290')
root.title("Login")
# designing the registration box
code=generate()
Reg_no=Label(root,text='Reg. Number: ',font='calibri 15 bold')
Reg_no.grid(row=1,column=10,sticky=E)
Regno_ent=Entry(root)
Regno_ent.grid(row=1,column=11)
# adding field for captcha writing.
ent=Label(root,text='Enter the above Code: ',font='calibri 15 bold')
ent.grid(row=4,column=10)
ent_cap=Entry(root)
ent_cap.grid(row=4,column=11)
# adding buttons and images
sub_btn=Button(root,text='Login',relief=RIDGE,height=2,width=10,bg='Black',fg='white',activebackground='blue',activeforeground='black',font='Times 10 bold',command=check)
#to set the co ordinates
sub_btn.place(x=180, y=160)
sub_btn.bind('<Enter>', on_enter)
sub_btn.bind('<Leave>', on_leave)
img=PhotoImage(file="Reload.png")
signup_btn=Button(root,text='Signup',relief=RIDGE,height=2,width=10,bg='Black',fg='white',activebackground='blue',activeforeground='black',font='Times 10 bold')
signup_btn.place(x=280, y=160)
refresh=Button(root,text="Refresh",relief=RIDGE,height=30,width=40,bg='Black',image=img,activebackground='lightblue',command=refresh)
refresh.grid(row=3,column=11)
# adding canvas for captcha 
c=Canvas(root,height=80,width=240)
outline()
c.create_text(160,40,text=code,font='calibri 28 bold')
c.grid(row=3,column=10)
root.mainloop()

# end
