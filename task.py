from tkinter import *
import os
import sqlite3 as sq


''''DATABASE CREATION'''
conn = sq.connect('info.db')
c = conn.cursor()
#c.execute("CREATE TABLE IF NOT EXISTS information( nameTEXT, branch TEXT, reg_ID REAL")

conn.commit()
c.close()
conn.close()

'''ENTER LOGIN DETAIL '''

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


''''LOGIN VERIFICATION'''
def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)


    list_of_files = os.listdir()

    if username1 in list_of_files:

        file1 = open(username1, "r")
        verify = file1.read().splitlines()

        if password1 in verify:
            login_sucess()


    else:
            invalid()


''''LOGIN SUCESS'''
def login_sucess():
    screen1=Tk()
    screen1.geometry('300x250')
    screen1.title('INFO')
    global name1
    global branch1
    global  reg1
    name1=StringVar()
    branch1=StringVar()
    reg1=StringVar()
    global name
    global reg
    global  branch
    Label(screen1,text='NAME').pack()
    name = Entry(screen1,textvariable=name1)
    name.pack()
    Label(screen1, text='').pack()
    Label(screen1, text='BRANCH').pack()
    branch = Entry(screen1,textvariable=branch1)
    branch.pack()
    Label(screen1, text='').pack()
    Label(screen1, text='REG').pack()
    reg = Entry(screen1,textvariable=reg1)
    reg.pack()
    Button(screen1, text="Submit", width=10, height=1, command= submit ).pack()



'''INDORMATION SUBMISSION'''
def submit():
    conn = sq.connect('info.db')
    c = conn.cursor()
    c.execute("INSERT INTO information VALUES(:name,:branch,:reg)",
              {
                  'name': name.get(),
                  'branch': branch.get(),
                  'reg': reg.get()


              })
    conn.commit()
    c.close()
    conn.close()
    open_window()


''''SUBJECT BUTTONS AND MARK SUBMISSION'''
def open_window():
    tip = Toplevel()
    tip.title("SUBJECTS")
    tip.geometry("300x250")

    Label(tip, text="MARKS SUBMISSION").pack()

    Label(tip, text="Enter the marks :").pack()

    Button(tip, text="EMFT", width=10,  command=open_window_emft).pack()

    Button(tip, text="IDS", width=10,  command=open_window_ids).pack()
    Button(tip, text="FCT", width=10,  command=open_window_fct).pack()

    Button(tip, text="SUBMIT", width=10, command=open_window3).pack()


def open_window_fct():
    global fct_marks
    global fct_entry
    fct_marks = StringVar()

    fct = Toplevel()
    fct.title("FCT")
    fct.geometry("500x500")
    Label(fct, text="Enter the marks obtained :").pack()

    fct_entry = Entry(fct, textvariable=fct_marks)
    fct_entry.pack()

    Button(fct, text="Done", command=fct_submission).pack()


def fct_submission():
    fct1 = fct_marks.get()
    name1 = name.get()

    conn = sq.connect("info.db")
    with conn:
        cur = conn.cursor()
    #    addColumn = "ALTER TABLE DETAILS ADD COLUMN FCT varchar(32)"
    #    cur.execute(addColumn)
    cur.execute('''UPDATE information SET FCT == "%s" WHERE Name == "%s"''' % (fct1, name1))
    conn.commit()
    cur.close()
    conn.close()


def open_window_ids():
    global ids_marks
    global ids_entry
    ids_marks = StringVar()

    ids = Toplevel()
    ids.title("IDS")
    ids.geometry("500x500")
    Label(ids, text="Enter the marks obtained :").pack()

    ids_entry = Entry(ids, textvariable=ids_marks)
    ids_entry.pack()

    Button(ids, text="Done", command=ids_submission).pack()


def ids_submission():
    ids1 = ids_marks.get()
    name1 = name.get()

    conn = sq.connect("info.db")
    with conn:
        cur = conn.cursor()
    #    addColumn2 = "ALTER TABLE DETAILS ADD COLUMN IDS varchar(32)"
    #    cur.execute(addColumn2)
    cur.execute('''UPDATE information SET IDS == "%s" WHERE Name == "%s"''' % (ids1, name1))
    conn.commit()
    cur.close()
    conn.close()


def open_window_emft():
    global emft_marks
    global emft_entry
    emft_marks = StringVar()

    emft = Toplevel()
    emft.title("EMFT")
    emft.geometry("500x500")
    Label(emft, text="Enter the marks obtained :").pack()

    emft_entry = Entry(emft, textvariable=emft_marks)
    emft_entry.pack()

    Button(emft, text="Done", command=emft_submission).pack()


def emft_submission():
    emft1 = emft_marks.get()
    name1 = name.get()

    conn = sq.connect("info.db")
    with conn:
        cur = conn.cursor()
        #addColumn3 = "ALTER TABLE information ADD COLUMN EMFT varchar(32)"
        #cur.execute(addColumn3)
    cur.execute('''UPDATE information SET EMFT == "%s" WHERE Name == "%s"''' % (emft1, name1))
    conn.commit()
    cur.close()
    conn.close()


''''RESULT SCREEN'''


def open_window3():
    tom = Toplevel()
    tom.title("GUI 3")
    tom.geometry("500x500")
    tom.configure(bg="aquamarine")

    Label(tom, text="RESULTS").pack()

    Label(tom, text="Input options :").pack()

    Button(tom, text="CGPA", width=10, command=do1).pack()

    Button(tom, text="GRADE", width=10, command=do2).pack()
    Button(tom, text="NEW INPUT", width=10, command=new_input).pack()

    Button(tom, text="CLOSE", width=10,  command=close).pack()


'''close the main screen'''
def close():
    main_screen.destroy()



'''redirect to for new login'''
def new_input():
    login()

'''ggpa calculation'''
def cgpa_func():
    global cgpa
    fct1 = fct_marks.get()

    ids1 = ids_marks.get()

    emft1 = emft_marks.get()

    avg = 0
    tot = 0
    avg_per = 0
    cgpa = 0

    tot = fct1 + ids1 + emft1
    avg = tot / 300
    avg_per = avg * 100

    cgpa = (avg_per) / 9.5
    print("The cgpa is:", cgpa)

''''cgpa display'''
def display_cgpa():
    tuf = Toplevel()
    tuf.title("Displaying CGPA")
    tuf.geometry("300x300")
    Label(tuf, text="THE CGPA OBTAINED IS :", font=("arial", 9, "bold"), bg="yellow", fg="red").place(x=78, y=40)
    Label(tuf, text=float(cgpa), bg="cyan").place(x=88, y=90)


def do1():
    cgpa_func()
    display_cgpa()


'''   GRADE CALCULATION   '''


#       CGPA          GRADE
#     9 - 10.0          O
#     8 - 8.9           E
#     7 - 7.9           A
#     6 - 6.9           B
#     5 - 5.9           C
#     below 5           D


def grade_func():
    global grade

    if (cgpa < 5.0):
        grade = "D"
    elif (cgpa < 6.0):
        grade = "C"
    elif (cgpa < 7.0):
        grade = "B"
    elif (cgpa < 8.0):
        grade = "A"
    elif (cgpa < 9.0):
        grade = "E"
    elif (cgpa < 10.1):
        grade = "O"

    print("The grade obtained is:", grade)

'''GRADE DISPLAY'''
def display_grade():
    tub = Toplevel()
    tub.title("Displaying Grade")
    tub.geometry("300x300")

    Label(tub, text="THE GRADE OBTAINED IS :", font=("arial", 9, "bold"), bg="yellow", fg="red").place(x=78, y=40)
    Label(tub, text=str(grade), width=10, bg="cyan").place(x=96, y=90)


def do2():
    grade_func()
    display_grade()


''''IF PASSWORD OR ID INVALID'''
def invalid():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password or ID").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

''''MAIN SCREEN'''
def main_account_screen():


    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    main_screen.mainloop()
main_account_screen()
