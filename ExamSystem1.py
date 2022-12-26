from tkinter import *
from PIL import ImageTk,Image
import pymongo
root = Tk()
root.iconbitmap("image.ico")
root.title('Online Examination System')
root.geometry('800x600')
image_0 = Image.open('C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\417644.webp')
bck_end=ImageTk.PhotoImage(image_0)
lbl = Label(root, image=bck_end)
lbl.place(x=0,y=0)
Label(root, text='Online Examination System',bg='LightSlateGrey',fg='black',font=('Cooper Black',40)).pack(pady=70)

def admin():

    # root.geometry('600x500')
    # t = Toplevel()

    def register():
        # t = Toplevel()
        def save():
            # t=Toplevel()

            a = t1.get()
            b = t2.get()
            c = t3.get()
            d = t4.get()

            con = pymongo.MongoClient("mongodb://localhost:27017/")
            db = con["admin"]
            tbl = db["student"]
            tbl.insert_one({"name": a, "mob": b, "dept": c, "password": d})
            print("save")

        t = Toplevel()
        t.iconbitmap("image.ico")
        t.geometry('450x300')

        l1 = Label(t, text="Name",font=('arial',20),bg='light cyan',fg='black')
        t1 = Entry(t,font=('arial',15),bg='moccasin')
        l2 = Label(t, text="Mob",font=('arial',20),bg='light cyan',fg='black')
        t2 = Entry(t,font=('arial',15),bg='moccasin')
        l3 = Label(t, text="Dept",font=('arial',20),bg='light cyan',fg='black')
        t3 = Entry(t,font=('arial',15),bg='moccasin')
        l4 = Label(t, text="Password",font=('arial',20),bg='light cyan',fg='black')
        t4 = Entry(t,font=('arial',15),bg='moccasin')

        b1 = Button(t, text="Save", command=save, bg='cyan',font=('arial',25),fg='black')

        l1.grid(row=3, column=4,pady=5)
        t1.grid(row=3, column=5,padx=10)
        l2.grid(row=4, column=4,pady=5)
        t2.grid(row=4, column=5,padx=10)
        l3.grid(row=5, column=4,pady=5)
        t3.grid(row=5, column=5,padx=10)
        l4.grid(row=6, column=4,pady=5)
        t4.grid(row=6, column=5,padx=10)
        b1.grid(row=7, column=5)

    def login():
        c = 0
        m = t1.get()
        p = t2.get()
        import pymongo
        con = pymongo.MongoClient("mongodb://localhost:27017/")
        db = con["admin"]
        tbl = db["student"]
        for row in tbl.find({"mob":m, "password":p}):
            c = c+1
        if c == 1:

            def addstud():
                 def savestu():
                    a = t11.get()
                    b = t1.get()
                    c = t2.get()
                    d = t3.get()
                    p = t4.get()
                    h = t5.get()
                    e = k.get()
                    f = y.get()


                    g = " "
                    if v.get() == 1:
                        g = r["text"]
                    else:
                        g = r1["text"]

                    con=pymongo.MongoClient("mongodb://localhost:27017/")
                    db=con["admin"]
                    tbl=db["student"]
                    tbl.insert_one({"rno":a, "name":b, "mob":c, "email":d, "parent name":p, "parent mob":h, "gender":g, "sem":e, "branch":f})
                    print("save")

                 t=Toplevel()
                 t.iconbitmap("image.ico")

                 l11=Label(t,text="Roll no",font=('arial',20),bg='light cyan',fg='black')
                 t11=Entry(t,font=('arial',15),bg='moccasin')
                 l1=Label(t,text="Name",font=('arial',20),bg='light cyan',fg='black')
                 t1=Entry(t,font=('arial',15),bg='moccasin')
                 l2=Label(t,text="Mob",font=('arial',20),bg='light cyan',fg='black')
                 t2=Entry(t,font=('arial',15),bg='moccasin')
                 l3=Label(t,text="Email",font=('arial',20),bg='light cyan',fg='black')
                 t3=Entry(t,font=('arial',15),bg='moccasin')
                 l4=Label(t,text="Parent name",font=('arial',20),bg='light cyan',fg='black')
                 t4=Entry(t,font=('arial',15),bg='moccasin')
                 l5=Label(t,text="Parent mob",font=('arial',20),bg='light cyan',fg='black')
                 t5=Entry(t,font=('arial',15),bg='moccasin')
                 b1=Button(t,text="Save", command=savestu,bg='cyan',font=('arial',25),fg='black')
                 l8=Label(t,text="Gender",font=('arial',20),bg='light cyan',fg='black')
                 v=StringVar()
                 r=Radiobutton(t,text="Male", variable=v,value=1,font=('arial',20),bg='light cyan',fg='black')
                 r1=Radiobutton(t,text="Female",variable=v,value=2,font=('arial',20),bg='light cyan',fg='black')
                 l6= ["1", "2", "3", "4", "5", "6", "7", "8"]
                 l10=Label(t,text="Sem",font=('arial',20),bg='light cyan',fg='black')
                 k= StringVar()
                 c2= OptionMenu(t, k, *l6)

                 l7 = ["CSE", "IT", "MECH", "CIVIL"]
                 l9 = Label(t, text="Branch",font=('arial',20),bg='light cyan',fg='black')
                 y = StringVar()
                 c1 = OptionMenu(t, y, *l7)


                 l11.grid(row=0, column=0,pady=5)
                 t11.grid(row=0, column=1)
                 l1.grid(row=0, column=2,pady=5)
                 t1.grid(row=0, column=3)
                 l2.grid(row=0, column=4,pady=5)
                 t2.grid(row=0, column=5)
                 l8.grid(row=2, column=0,pady=5)

                 r.grid(row=2, column=1)
                 r1.grid(row=2,column=2)

                 l9.grid(row=3, column=0,pady=5)
                 c1.grid(row=3,column=2)
                 l10.grid(row=4,column=0,pady=5)
                 c2.grid(row=4,column=2)

                 l3.grid(row=5,column=0,pady=5)
                 t3.grid(row=5,column=1)
                 l4.grid(row=6,column=0,pady=5)
                 t4.grid(row=6,column=1,padx=5)
                 l5.grid(row=6,column=3,pady=5)
                 t5.grid(row=6,column=4)
                 b1.grid(row=7, column=5,pady=10)

            def addques():
                t=Toplevel()
                t.iconbitmap("image.ico")

                def saveques():
                    a=t1.get()
                    b=t2.get()
                    c=t3.get()
                    d=t4.get()
                    e=t5.get()
                    f=t6.get()
                    g=t7.get()

                    con=pymongo.MongoClient("mongodb://localhost:27017/")
                    db=con["admin"]
                    tbl=db["question"]
                    tbl.insert_one({"qid":a, "question":b, "option-1":c, "option-2":d, "option-3":e, "option-4":f, "answer":g})
                    print("save")

                l1=Label(t,text="Qid",font=('arial',20),bg='light cyan',fg='black')
                t1=Entry(t,font=('arial',15),bg='moccasin')
                l2=Label(t,text="Question",font=('arial',20),bg='light cyan',fg='black')
                t2=Entry(t,font=('arial',15),bg='moccasin')
                l3=Label(t,text="Option-1",font=('arial',20),bg='light cyan',fg='black')
                t3=Entry(t,font=('arial',15),bg='moccasin')
                l4=Label(t,text="Option-2",font=('arial',20),bg='light cyan',fg='black')
                t4=Entry(t,font=('arial',15),bg='moccasin')
                l5=Label(t,text="Option-3",font=('arial',20),bg='light cyan',fg='black')
                t5=Entry(t,font=('arial',15),bg='moccasin')
                l6=Label(t,text="Option-4",font=('arial',20),bg='light cyan',fg='black')
                t6=Entry(t,font=('arial',15),bg='moccasin')
                l7=Label(t,text="answer",font=('arial',20),bg='light cyan',fg='black')
                t7=Entry(t,font=('arial',15),bg='moccasin')
                b1=Button(t,text="Save",command=saveques, bg='cyan',font=('arial',25),fg='black')

                l1.grid(row=0,column=0,pady=5)
                t1.grid(row=0,column=1)
                l2.grid(row=1,column=0,pady=5)
                t2.grid(row=1,column=1)
                l3.grid(row=2,column=0,pady=5)
                t3.grid(row=2,column=1)
                l4.grid(row=3,column=0,pady=5)
                t4.grid(row=3,column=1)
                l5.grid(row=4,column=0,pady=5)
                t5.grid(row=4,column=1)
                l6.grid(row=5,column=0,pady=5)
                t6.grid(row=5,column=1)
                l7.grid(row=6,column=0,pady=5)
                t7.grid(row=6,column=1)
                b1.grid(row=7,column=2,pady=10)

            t=Toplevel()
            t.iconbitmap("image.ico")
            t.geometry('400x350')
            Button(t, text="Add Student",bg='cyan',font=('arial',25),fg='black', command=addstud).pack(pady=20)
            Button(t, text="Add Question",bg='cyan',font=('arial',25),fg='black', command=addques).pack(pady=5)
        else:
            print("invalid")
    t=Toplevel()
    t.iconbitmap("image.ico")
    t.geometry('650x500')

    Label(t, text='Admin portal', font=('arial bold', 25), fg='black', bg='seashell3').grid(row=1, column=9, pady=50)
    l1 = Label(t, text="Mob ", fg='white', bg='steelblue', font=('Arial', 15))
    t1 = Entry(t, bg='seashell3', font=('Arial', 15), fg='black')
    l2 = Label(t, text="Password ",fg='white',bg='steelblue',font=('Arial', 15))
    t2 = Entry(t, bg='seashell3',show='*', font=('Arial', 15), fg='black')

    b1 = Button(t, text="Login", command=login, bg='moccasin', fg='blue', font=('Arial', 12))
    b2 = Button(t, text="Register", command=register,bg='moccasin',fg='blue',font=('Arial',12))

    l1.grid(row=2, column=8, pady=10, padx=10)
    t1.grid(row=2, column=9, pady=10)
    l2.grid(row=3, column=8, pady=5, padx=15)
    t2.grid(row=3, column=9, pady=5)
    b1.grid(row=4, column=9, pady=10)
    b2.grid(row=5, column=9)



def student():
    # t = Toplevel()

    def registeration():
        # t = Toplevel()

        def save():
            # t = Toplevel()

            a = t1.get()
            b = t2.get()
            c = t3.get()
            d = t4.get()
            e = t5.get()
            f = t6.get()
            g = t7.get()

            import pymongo
            con = pymongo.MongoClient("mongodb://localhost:27017/")
            db = con["admin"]
            tbl = db["student"]
            tbl.insert_one({"rno":a, "name":b, "mob":c, "dob":d, "sem":e, "branch":f, "password":g})
            print("save")

        t=Toplevel()
        t.iconbitmap("image.ico")
        t.geometry('500x350')

        l1 = Label(t, text="Roll no",font=('arial',20),bg='light cyan',fg='black')
        t1 = Entry(t,bg='seashell3', font=('Arial', 15), fg='black')
        l2 = Label(t, text="Name",font=('arial',20),bg='light cyan',fg='black')
        t2 = Entry(t,bg='seashell3', font=('Arial', 15), fg='black')
        l3 = Label(t, text="Mob ",font=('arial',20),bg='light cyan',fg='black')
        t3 = Entry(t,bg='seashell3', font=('Arial', 15), fg='black')
        l4 = Label(t, text="Dob ",font=('arial',20),bg='light cyan',fg='black')
        t4 = Entry(t,bg='seashell3', font=('Arial', 15), fg='black')
        l5 = Label(t, text="Sem",font=('arial',20),bg='light cyan',fg='black')
        t5 = Entry(t,bg='seashell3', font=('Arial', 15), fg='black')
        l6 = Label(t, text="Branch",font=('arial',20),bg='light cyan',fg='black')
        t6 = Entry(t,bg='seashell3', font=('Arial', 15), fg='black')
        l7 = Label(t, text="Password",font=('arial',20),bg='light cyan',fg='black')
        t7 = Entry(t,bg='seashell3', font=('Arial', 15), fg='black')

        b1 = Button(t, text="save", command=save, bg='cyan', fg='blue', font=('Arial', 25))


        l1.grid(row=0, column=0,pady=5)
        t1.grid(row=0, column=1)
        l2.grid(row=1, column=0,pady=5)
        t2.grid(row=1, column=1)
        l3.grid(row=2, column=0,pady=5)
        t3.grid(row=2, column=1)
        l4.grid(row=3, column=0,pady=5)
        t4.grid(row=3, column=1)
        l5.grid(row=4, column=0,pady=5)
        t5.grid(row=4, column=1)
        l6.grid(row=5, column=0,pady=5)
        t6.grid(row=5, column=1)
        l7.grid(row=6, column=0,pady=5)
        t7.grid(row=6, column=1)
        b1.grid(row=7, column=1,pady=10)

    def login():
        c = 0
        m = t1.get()
        p = t2.get()

        import pymongo
        con = pymongo.MongoClient("mongodb://localhost:27017/")
        db = con["admin"]
        tbl = db["student"]
        for row in tbl.find({"mob":m, "password":p}):
            c = c+1
        if c == 1:

            def showexam():

                # t=Toplevel()
                index = 0
                answer = 0
                count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                def showquestion(x):
                    con=pymongo.MongoClient("mongodb://localhost:27017/")
                    db=con["admin"]
                    tbl=db["question"]

                    for row in tbl.find({"qid": str(x)}):
                        l1.config(text=row["question"],font=('arial',15))
                        r1.config(text=row["option-1"],font=('arial',15))
                        r2.config(text=row["option-2"],font=('arial',15))
                        r3.config(text=row["option-3"],font=('arial',15))
                        r4.config(text=row["option-4"],font=('arial',15))
                        global answer, showquestion
                        answer = row["answer"]

                def show1():
                    global index
                    index = 1
                    showquestion("1")

                def show2():
                    global index
                    index = 2
                    showquestion("2")

                def show3():
                    global index
                    index = 3
                    showquestion("3")

                def show4():
                    global index
                    index = 4
                    showquestion("4")

                def show5():
                    global index
                    index = 5
                    showquestion("5")

                def show6():
                    global index
                    index = 6
                    showquestion("6")

                def show7():
                    global index
                    index = 7
                    showquestion("7")

                def show8():
                    global index
                    index = 8
                    showquestion("8")

                def show9():
                    global index
                    index = 9
                    showquestion("9")

                def show10():
                    global index
                    index = 10
                    showquestion("10")

                def shownext():
                    global index
                    index += 1
                    showquestion(index)
                    print(index)

                def showpre():
                    global index
                    index = index-1
                    showquestion(index)

                def submit():
                    global count
                    if v.get() == answer:
                        count = count + 1
                    #     count[index - 1] = 1
                    # else:
                    #     count[index - 1] = 0
                    print('submitted')

                def finish():
                    s = 0
                    for i in range(0,len(count)):
                        s = s + count[i]
                    print(s,"/10")

                t = Toplevel()
                t.geometry('550x450')
                t.iconbitmap("image.ico")

                b1 = Button(t, text="1", font=('arial',20),fg='black', command=show1, bg='snow3')
                b2 = Button(t, text="2", font=('arial',20),fg='black', command=show2, bg='snow3')
                b3 = Button(t, text="3", font=('arial',20),fg='black', command=show3, bg='snow3')
                b4 = Button(t, text="4", font=('arial',20),fg='black', command=show4, bg='snow3')
                b5 = Button(t, text="5", font=('arial',20),fg='black', command=show5, bg='snow3')
                b6 = Button(t, text="6", font=('arial',20),fg='black', command=show6, bg='snow3')
                b7 = Button(t, text="7", font=('arial',20),fg='black', command=show7, bg='snow3')
                b8 = Button(t, text="8", font=('arial',20),fg='black', command=show8, bg='snow3')
                b9 = Button(t, text="9", font=('arial',20),fg='black', command=show9, bg='snow3')
                b10 = Button(t, text="10", font=('arial',25),fg='black', command=show10, bg='snow3')

                b1.grid(row=0, column=0,padx=5)
                b2.grid(row=0, column=1,padx=5)
                b3.grid(row=0, column=2,padx=5)
                b4.grid(row=0, column=3,padx=5)
                b5.grid(row=0, column=4,padx=5)
                b6.grid(row=0, column=5,padx=5)
                b7.grid(row=0, column=6,padx=5)
                b8.grid(row=0, column=7,padx=5)
                b9.grid(row=0, column=8,padx=5)
                b10.grid(row=0, column=9,padx=5)


                v = IntVar(t)
                l1 = Label(t,text="")
                r1 = Radiobutton(t,text="", font=('arial',15), variable=v, value=1, bg='honeydew2')
                r2 = Radiobutton(t,text="", font=('arial',15), variable=v, value=2, bg='honeydew2')
                r3 = Radiobutton(t,text="", font=('arial',15), variable=v, value=3, bg='honeydew2')
                r4 = Radiobutton(t,text="", font=('arial',15), variable=v, value=4, bg='honeydew2')

                l1.grid(row=1, column=2)
                r1.grid(row=2, column=0,padx=6)
                r2.grid(row=2, column=1,padx=6)
                r3.grid(row=3, column=0,padx=6)
                r4.grid(row=3, column=1,padx=6)

                btnext = Button(t, text="Next", font=('arial',25),command=shownext, bg='deep sky blue')
                btpre = Button(t, text="Pre", font=('arial',25),command=showpre, bg='steel blue')
                btsub = Button(t, text="Submit", font=('arial',25),command=submit, bg='cornflower blue')
                btfinish = Button(t, text="Finish", font=('arial',25),command=finish, bg='PeachPuff2')

                btnext.grid(row=5, column=1,padx=5)
                btpre.grid(row=5, column=2,padx=5)
                btsub.grid(row=5, column=3,padx=5)
                btfinish.grid(row=5, column=4,padx=5)

            t=Toplevel()
            t.geometry('450x300')
            t.iconbitmap("image.ico")
            b1=Button(t,text="showexam",fg='black',bg='light blue',font=('arial',25), command=showexam)
            b1.pack(pady=10,ipadx=20,ipady=5)
        else:
            print("invalid")

    t=Toplevel()
    t.iconbitmap("image.ico")
    t.geometry('650x500')
    Label(t,text='Student portal',font=('arial bold',25),fg='black',bg='seashell3').grid(row=1,column=8,pady=50)
    l1 = Label(t, text="Mob ",fg='white',bg='steelblue',font=('Arial',15))
    t1 = Entry(t,bg='seashell3',font=('Arial',15),fg='black')
    l2 = Label(t, text="Password",fg='white',bg='steelblue',font=('Arial',15))
    t2 = Entry(t,bg='seashell3',show='*',font=('Arial',15),fg='black')


    b1 = Button(t, text="login", command=login, bg='moccasin', fg='blue', font=('Arial', 12))
    b2 = Button(t, text="register", command=registeration,bg='moccasin',fg='blue',font=('Arial',12))

    l1.grid(row=2,column=7,pady=10,padx=10)
    t1.grid(row=2,column=8,pady=10)
    l2.grid(row=3,column=7,pady=5,padx=15)
    t2.grid(row=3,column=8,pady=5)
    b1.grid(row=4,column=8,pady=10)
    b2.grid(row=5,column=8)


b1 = Button(text="Admin",fg='white',bg='#856ff8',font=('Arial',30), command=admin)
b2 = Button(text="Student",bg='green',fg='white',font=('Arial',30), command=student)
# b1.grid(row=1,column=3)
# b2.grid(row=2,column=3)
b1.pack(pady=10,ipadx=20,ipady=5)
b2.pack(pady=5,ipadx=20,ipady=5)
# b1.place(height=400, width=400)
# b2.place(height=600, width=600)

mainloop()
