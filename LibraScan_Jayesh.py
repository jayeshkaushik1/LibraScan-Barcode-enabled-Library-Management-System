#Modules Used in Program :tkinter,tkinter.messagebox,random,time,datetime,pyzbar,opencv-python,numpy,python-mysql-connector
#Modules Imported
from tkinter import*
import tkinter.messagebox
import mysql.connector as msc
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import random
import time
from datetime import date

#***************************Main Page***************************
def Main_Page():

    root = Tk()
    root.geometry("800x530+50+50")
    root.title("Library Management System")
    #If Background image not in directory then message will appear that "The image for the program not in the Directory"
    try:
        Pic=PhotoImage(file="C:\\Users\jayesh\Documents\Library Management System Background\Lib Background.png")
        background=Label(root,image=Pic)
        background.place(x=0,y=0)
    except:
        print("The image for the program not in the Directory")

    #TIME
    localtime=time.asctime()
    #INFO TOP
    tkinter.messagebox.showinfo('Access Granted','Welcome to 221B')
    lblinfo=Label(root,font=('aria',30,'bold'),text="Welcome to 221B",fg="steel blue",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)
    lblinfo=Label(root,font=('aria',20,'bold'),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=0)
    #Destroying The Main Page Frame and open Required Frame by calling Required function
    def AddBooks():
        root.destroy()
        AddBook()
    def IssueBooks():
        root.destroy()
        IssueBook()
    def SearchBooks():
        root.destroy()
        SearchBook()
    def ReturnBooks():
        root.destroy()
        ReturnBook()
    def DeleteBooks():
        root.destroy()
        DeleteBook()
    def PendingReturns():
        root.destroy()
        PendingReturn()
    def sexit():
        root.destroy()
        

    #Buttons
    AddbookBtn=Button(root,padx=16,pady=8,bd=15,fg="black",font=('ariel',14,'bold'),width=13,text="Add Book Details",bg="powder blue",command=AddBooks)
    AddbookBtn.grid(row=3,column=0)

    IssueBookBtn=Button(root,padx=16,pady=8,bd=15,fg="black",font=('ariel',16,'bold'),width=10,text="Issue Book",bg="powder blue",command=IssueBooks)
    IssueBookBtn.grid(row=4,column=0)

    SearchBookBtn=Button(root,padx=16,pady=8,bd=15,fg="black",font=('ariel',16,'bold'),width=10,text="Search Book",bg="powder blue",command=SearchBooks)
    SearchBookBtn.grid(row=5,column=0)

    ReturnBookBtn=Button(root,padx=16,pady=8,bd=15,fg="black",font=('ariel',16,'bold'),width=10,text="Return Book",bg="powder blue",command=ReturnBooks)
    ReturnBookBtn.grid(row=6,column=0)

    DeleteBookBtn=Button(root,padx=16,pady=8,bd=15,fg="black",font=('ariel',16,'bold'),width=10,text="Delete Book",bg="powder blue",command=DeleteBooks)
    DeleteBookBtn.grid(row=7,column=0)

    PendingBtn=Button(root,padx=16,pady=8,bd=15,fg="black",font=('ariel',16,'bold'),width=10,text="Pending Return",bg="powder blue",command=PendingReturns)
    PendingBtn.grid(row=6,column=1)

    btnexit=Button(root,padx=16,pady=8,bd=20,fg="black",font=('ariel',16,'bold'),width=10,text="EXIT",bg="powder blue",command=sexit)
    btnexit.grid(row=7,column=1)



    root.mainloop()

#***************************Add Book Data***************************

def AddBook():

    root=Tk()

    root.geometry("1000x900+0+0")
    root.title("Library Management System")
    try:
        Pic=PhotoImage(file="C:\\Users\jayesh\Documents\Library Management System Background\Lib Background4.png")
        background=Label(root,image=Pic)
        background.place(x=0,y=0)
    except:
        print("The image for the program not in the Directory")


    #TIME
    localtime=time.asctime()
    #INFO TOP
    lblinfo = Label(root, font=('aria',30,'bold'),text="ADD BOOKS DATA",bd=10,anchor='w')
    lblinfo.grid(row=0,column=1)
    lblinfo = Label(root, font=('aria' ,20),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=1)
    def Sub():
        Isbn=txtIsbn.get()
        Scan=txtBarcode.get()
        Title=txtTitle.get()
        Author=txtAuthor.get()
        Pub=txtPub.get()
        Stat="Avail"
        try:
            import mysql.connector as msc
            mydb=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
            mycursor=mydb.cursor()
            INSERT=("insert into AddBooks(Isbn_No,Book_Id,Title,Author,Publication,Status)""values (%s,%s,%s,%s,%s,%s)")
            DATA=(Isbn,Scan,Title,Author,Pub,Stat)
            mycursor.execute(INSERT,DATA)
            mydb.commit()

        except:
            import mysql.connector as msc
            mydb0=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
            mycursor1=mydb0.cursor()
            Create=("create table AddBooks(Isbn_No varchar(30),Book_Id varchar(40) ,Title varchar(100) ,Author varchar(100),Publication varchar(100),Status varchar(7))")
            mycursor1.execute(Create)
            mydb0.commit()
            tkinter.messagebox.showinfo('Re Submit','Re Submit Last Record')
            

    def Scanner():
        import cv2
        import numpy as np
        import pyzbar.pyzbar as pyzbar

        cap=cv2.VideoCapture(0)
        while True:
            _,frame=cap.read()
            decodeobjs=pyzbar.decode(frame)
            for obj in decodeobjs:
                Scaning=obj.data
            cv2.imshow("Frame",frame)
            key=cv2.waitKey(1)
            if decodeobjs !=[]:
                break
        cap.release()
        cv2.destroyAllWindows()
        Scan.set(Scaning)

    def sexit():
        root.destroy()
    def sback():
        root.destroy()
        Main_Page()
        

    def reset():
        Isbn.set("")
        Scan.set("")
        Title.set("")
        Author.set("")
        Pub.set("")

    Scan=StringVar()
    Title=StringVar()
    Isbn=StringVar()
    Author=StringVar()
    Pub=StringVar()

    lblIsbn=Label(root,font=( 'aria',16,'bold'),text="ISBN No.",fg="steel blue",bd=10,anchor='w')
    lblIsbn.grid(row=3,column=0)
    txtIsbn=Entry(root,font=('ariel',16,'bold'),textvariable=Isbn,bd=6,bg="powder blue" ,justify='right')
    txtIsbn.grid(row=3,column=1)

    btnBarcode=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=16, text="Barcode Scan", bg="powder blue",command=Scanner)
    btnBarcode.grid(row=4, column=0)
    txtBarcode=Entry(root,font=('ariel' ,16,'bold'),textvariable=Scan,bd=6,bg="powder blue" ,justify='right')
    txtBarcode.grid(row=4,column=1)

    lblTitle=Label(root, font=( 'aria' ,16, 'bold' ),text="Title",fg="steel blue",bd=10,anchor='w')
    lblTitle.grid(row=5,column=0)
    txtTitle=Entry(root,font=('ariel' ,16,'bold'),textvariable=Title,bd=6,bg="powder blue" ,justify='right')
    txtTitle.grid(row=5,column=1)

    lblAuthor=Label(root, font=( 'aria' ,16, 'bold'),text="Author",fg="steel blue",bd=10,anchor='w')
    lblAuthor.grid(row=6,column=0)
    txtAuthor=Entry(root,font=('ariel' ,16,'bold'),textvariable=Author,bd=6,bg="powder blue" ,justify='right')
    txtAuthor.grid(row=6,column=1)

    lblPub=Label(root, font=( 'aria',16, 'bold'),text="Publisher",fg="steel blue",bd=10,anchor='w')
    lblPub.grid(row=7,column=0)
    txtPub=Entry(root,font=('ariel',16,'bold'),textvariable=Pub,bd=6,bg="powder blue" ,justify='right')
    txtPub.grid(row=7,column=1)

    #buttons
    btnback=Button(root,padx=16,pady=8,bd=20,fg="black",font=('ariel',16,'bold'),width=6,text="Back",bg="powder blue",command=sback)
    btnback.grid(row=8,column=0)

    btnreset=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="RESET", bg="powder blue",command=reset)
    btnreset.grid(row=8,column=1)

    btnsub=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="SUBMIT", bg="powder blue",command=Sub)
    btnsub.grid(row=8,column=2)

    btnexit=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="EXIT", bg="powder blue",command=sexit)
    btnexit.grid(row=8,column=3)

    root.mainloop()
#***************************Issue Book***************************

def IssueBook():
    root=Tk()

    root.geometry("1000x900+0+0")
    root.title("Library Management System")
    try:
        Pic=PhotoImage(file="C:\\Users\jayesh\Documents\Library Management System Background\Lib Background4.png")
        background=Label(root,image=Pic)
        background.place(x=0,y=0)
    except:
        print("The image for the program not in the Directory")

    #TIME
    localtime=time.asctime()
    #INFO TOP
    lblinfo = Label(root, font=('aria',30,'bold'),text="Issue Book",bd=10,anchor='w')
    lblinfo.grid(row=0,column=1)
    lblinfo = Label(root, font=('aria' ,20),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=1)

    import mysql.connector as msc
    mydb=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
    mycursor=mydb.cursor()
    INSERT=("select Isbn_No,Title from AddBooks")
    mycursor.execute(INSERT)
    for i in mycursor:
        #S=show
        Isbn=i[0]
        Title=i[1]

    def Sub():
        Sname=txtSname.get()
        Sadmn=txtSAdmn.get()
        Scls=txtScls.get()
        SBId=txtSBId.get()
        SDOI=date.today()
        Return=txtReturn.get()
        try:
        
            import mysql.connector as msc
            mydb=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
            mycursor=mydb.cursor()
            INSERT=("insert into IssueBooks(SName,Admn_No,Class,Book_Id,DOI,Isbn_No,Title,Return_Date)""values (%s,%s,%s,%s,%s,%s,%s,%s)")
            DATA=(Sname,Sadmn,Scls,SBId,SDOI,Isbn,Title,Return)
            mycursor.execute(INSERT,DATA)
            mydb.commit()

            def Sub1():
                mydb1=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
                mycursor1=mydb1.cursor()
                k="update AddBooks Set Status='Issued' where Book_Id="+"'"+SBId+"'"
                mycursor1.execute(k)
                mydb1.commit()
                tkinter.messagebox.showinfo('Book Issued','Book Succesfully Issued')
            Sub1()
        except:
            import mysql.connector as msc
            mydb0=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
            mycursor1=mydb0.cursor()
            Create=("create table IssueBooks(SName varchar(100),Admn_No varchar(11),Class varchar(7),Book_Id varchar(40),DOI varchar(12),Isbn_No varchar(30),Title varchar(100),Return_Date varchar(12))")
            mycursor1.execute(Create)
            mydb0.commit()
            tkinter.messagebox.showinfo('Re Submit','Re Submit Last Record')
        
            

    
    #Scaning of Barcode/Qr Code
    def Scanner():
        #Modules Imported
        import cv2
        import numpy as np
        import pyzbar.pyzbar as pyzbar

        cap=cv2.VideoCapture(0)
        while True:
            _,frame=cap.read()
            decodeobjs=pyzbar.decode(frame)
            for obj in decodeobjs:
                Scaning=obj.data
            cv2.imshow("Frame",frame)
            key=cv2.waitKey(1)
            if decodeobjs !=[]:
                break
        cap.release()
        cv2.destroyAllWindows()
        Scan.set(Scaning)

    def sexit():
        root.destroy()
    def sback():
        root.destroy()
        Main_Page()

    def reset():
        Sname.set("")
        SAdmn.set("")
        Scls.set("")
        Srno.set("")
        Scan.set("")
        Return.set("")

    Sname=StringVar()    
    SAdmn=StringVar()
    Scls=StringVar()
    Srno=StringVar()
    Scan=StringVar()
    Return=StringVar()

    lblSname=Label(root,font=( 'aria',16,'bold'),text="Student Name:",fg="steel blue",bd=10,anchor='w')
    lblSname.grid(row=3,column=0)
    txtSname=Entry(root,font=('ariel',16,'bold'),textvariable=Sname,bd=6,bg="powder blue" ,justify='right')
    txtSname.grid(row=3,column=1)

    lblSAdmn=Label(root,font=('aria',16,'bold'),text="Admission No.:",fg="steel blue",bd=10,anchor='w')
    lblSAdmn.grid(row=4,column=0)
    txtSAdmn=Entry(root,font=('ariel',16,'bold'),textvariable=SAdmn,bd=6,bg="powder blue" ,justify='right')
    txtSAdmn.grid(row=4,column=1)

    lblScls=Label(root, font=( 'aria' ,16, 'bold' ),text="Class:",fg="steel blue",bd=10,anchor='w')
    lblScls.grid(row=5,column=0)
    txtScls=Entry(root,font=('ariel' ,16,'bold'),textvariable=Scls,bd=6,bg="powder blue" ,justify='right')
    txtScls.grid(row=5,column=1)


    lblSrno=Label(root, font=( 'aria' ,16, 'bold'),text="Roll No.:",fg="steel blue",bd=10,anchor='w')
    lblSrno.grid(row=6,column=0)
    txtSrno=Entry(root,font=('ariel' ,16,'bold'),textvariable=Srno,bd=6,bg="powder blue" ,justify='right')
    txtSrno.grid(row=6,column=1)

    btnSBId=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=5, text="Book Id:", bg="powder blue",command=Scanner)
    btnSBId.grid(row=7, column=0)
    txtSBId=Entry(root,font=('ariel' ,16,'bold'),textvariable=Scan,bd=6,bg="powder blue" ,justify='right')
    txtSBId.grid(row=7,column=1)

    lblReturn=Label(root, font=( 'aria' ,16, 'bold'),text="Return Date(YYYY-MM-DD):",fg="steel blue",bd=10,anchor='w')
    lblReturn.grid(row=8,column=0)
    txtReturn=Entry(root,font=('ariel' ,16,'bold'),textvariable=Return,bd=6,bg="powder blue" ,justify='right')
    txtReturn.grid(row=8,column=1)



    #buttons

    btnback=Button(root,padx=16,pady=8,bd=20,fg="black",font=('ariel',16,'bold'),width=6,text="Back",bg="powder blue",command=sback)
    btnback.grid(row=9,column=0)

    btnsub=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="SUBMIT", bg="powder blue",command=Sub)
    btnsub.grid(row=9,column=2)

    btnreset=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="RESET", bg="powder blue",command=reset)
    btnreset.grid(row=9,column=1)

    btnexit=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="EXIT", bg="powder blue",command=sexit)
    btnexit.grid(row=9,column=3)

    root.mainloop()

#***************************Search Book***************************
    
def SearchBook():

    root=Tk()

    root.geometry("1450x1100+0+0")
    root.title("Library Management System")
    try:
        Pic=PhotoImage(file="C:\\Users\jayesh\Documents\Library Management System Background\Lib Background2.png")
        background=Label(root,image=Pic)
        background.place(x=0,y=0)
    except:
        print("The image for the program not in the Directory")

    #TIME
    localtime=time.asctime()
    #INFO TOP
    lblinfo = Label(root, font=('aria',30,'bold'),text="Search Book",bd=10,anchor='w')
    lblinfo.grid(row=0,column=1)
    lblinfo = Label(root, font=('aria',20),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=1)

    def Sub():
        Book=txtBName.get()
        BId=txtBId.get()

        import mysql.connector as msc
        mydb=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
        mycursor=mydb.cursor()
        mycursor.execute("Select Isbn_No,Book_Id,Title,Status from AddBooks where Book_Id="+"'"+BId+"'"+"Or Title="+"'"+Book+"'")


        #Header
        lblHIsbn=Label(root, font=('aria' ,16, 'bold'),text="ISBN NO.",fg="steel blue",bd=10,anchor='w')
        lblHIsbn.grid(row=6,column=0)

        lblHBId=Label(root, font=('aria' ,16, 'bold'),text="BOOK ID",fg="steel blue",bd=10,anchor='w')
        lblHBId.grid(row=6,column=1)

        lblHTitle=Label(root, font=('aria' ,16, 'bold'),text="TITLE",fg="steel blue",bd=10,anchor='w')
        lblHTitle.grid(row=6,column=2)

        lblHStat=Label(root,font=('aria',16,'bold'),text="Status",fg="steel blue",bd=10,anchor='w')
        lblHStat.grid(row=6,column=3)

        
        lblEx=Label(root, font=('aria',16, 'bold'),text="------------------------------------------------",fg="steel blue",bd=10,anchor='w')
        lblEx.grid(row=7,column=0)


        lblEx1=Label(root, font=('aria',16, 'bold'),text="------------------------------------------------",fg="steel blue",bd=10,anchor='w')
        lblEx1.grid(row=7,column=1)

        lblEx2=Label(root, font=('aria',16, 'bold'),text="------------------------------------------------",fg="steel blue",bd=10,anchor='w')
        lblEx2.grid(row=7,column=2)

        lblEx3=Label(root, font=('aria',16, 'bold'),text="------------------------------------------------",fg="steel blue",bd=10,anchor='w')
        lblEx3.grid(row=7,column=3)

        R=8

        for i in mycursor:
            lblS1Isbn=Label(root,font=('aria',16,'bold'),text=i[0],fg="steel blue",bd=10,anchor='w')
            lblS1Isbn.grid(row=R,column=0)

            lblS1BId=Label(root,font=('aria',16,'bold'),text=i[1],fg="steel blue",bd=10,anchor='w')
            lblS1BId.grid(row=R,column=1)

            lblS1Title=Label(root,font=('aria',16,'bold'),text=i[2],fg="steel blue",bd=10,anchor='w')
            lblS1Title.grid(row=R,column=2)

            lblS1Stat=Label(root,font=('aria',16,'bold'),text=i[3],fg="steel blue",bd=10,anchor='w')
            lblS1Stat.grid(row=R,column=3)
            R=R+1

    def sexit():
        root.destroy()

    def sback():
         root.destroy()
         Main_Page()

    def reset():
        Book.set("")
        BId.set("")
        
    Book=StringVar()
    BId=StringVar()


    lblBName=Label(root,font=('aria',16,'bold'),text="Book Name:",fg="steel blue",bd=10,anchor='w')
    lblBName.grid(row=3,column=0)
    txtBName=Entry(root,font=('ariel',16,'bold'),textvariable=Book,bd=6,bg="powder blue" ,justify='right')
    txtBName.grid(row=3,column=1)
    
    lblBId=Label(root,font=('aria',16,'bold'),text="Book Id:",fg="steel blue",bd=10,anchor='w')
    lblBId.grid(row=4,column=0)
    txtBId=Entry(root,font=('ariel',16,'bold'),textvariable=BId,bd=6,bg="powder blue" ,justify='right')
    txtBId.grid(row=4,column=1)




    #buttons
    btnback=Button(root,padx=16,pady=8,bd=20,fg="black",font=('ariel',16,'bold'),width=6,text="Back",bg="powder blue",command=sback)
    btnback.grid(row=5,column=0)


    btnsub=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="SUBMIT", bg="powder blue",command=Sub)
    btnsub.grid(row=5,column=2)

    btnreset=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="RESET", bg="powder blue",command=reset)
    btnreset.grid(row=5,column=1)

    btnexit=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="EXIT", bg="powder blue",command=sexit)
    btnexit.grid(row=5,column=3)

    root.mainloop()

#***************************Return Book***************************
    
def ReturnBook():
    root=Tk()

    root.geometry("800x500+0+0")
    root.title("Library Management System")
    try:
        Pic=PhotoImage(file="C:\\Users\jayesh\Documents\Library Management System Background\Lib Background.png")
        background=Label(root,image=Pic)
        background.place(x=0,y=0)
    except:
        print("The image for the program not in the Directory")

    #TIME
    localtime=time.asctime()
    #INFO TOP
    lblinfo = Label(root, font=('aria',30,'bold'),text="Return Book",bd=10,anchor='w')
    lblinfo.grid(row=0,column=1)
    lblinfo = Label(root, font=('aria' ,20),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=1)
    def Sub():
        def Sub0():
            SBId=txtSBId.get()
            import mysql.connector as msc
            mydb=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
            mycursor=mydb.cursor()
            mycursor.execute("Delete from issuebooks where Book_Id="+"'"+SBId+"'")
            mydb.commit()

        Sub0()
        def Sub1():
            SBId=txtSBId.get()
            import mysql.connector as msc
            mydb=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
            mycursor=mydb.cursor()
            mycursor.execute("Update addbooks Set status='Avail' where Book_Id="+"'"+SBId+"'")
            mydb.commit()
        Sub1()
            
        

        tkinter.messagebox.showinfo('Book Returned','Book Succesfully Returned')
    #Scaning of Barcode/Qr Code
    def Scanner():
        #Modules Imported
        import cv2
        import numpy as np
        import pyzbar.pyzbar as pyzbar

        cap=cv2.VideoCapture(0)
        while True:
            _,frame=cap.read()
            decodeobjs=pyzbar.decode(frame)
            for obj in decodeobjs:
                Scaning=obj.data
            cv2.imshow("Frame",frame)
            key=cv2.waitKey(1)
            if decodeobjs !=[]:
                break
        cap.release()
        cv2.destroyAllWindows()
        Scan.set(Scaning)

    def sexit():
        root.destroy()
    def sback():
        root.destroy()
        Main_Page()

    def reset():
        SBId.set("")

    Scan=StringVar()

    btnSBId=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=5, text="Book Id:", bg="powder blue",command=Scanner)
    btnSBId.grid(row=3, column=0)
    txtSBId=Entry(root,font=('ariel' ,16,'bold'),textvariable=Scan,bd=6,bg="powder blue" ,justify='right')
    txtSBId.grid(row=3,column=1)


    #buttons
    btnback=Button(root,padx=16,pady=8,bd=20,fg="black",font=('ariel',16,'bold'),width=6,text="Back",bg="powder blue",command=sback)
    btnback.grid(row=8,column=0)


    btnsub=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="SUBMIT", bg="powder blue",command=Sub)
    btnsub.grid(row=8,column=2)

    btnreset=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="RESET", bg="powder blue",command=reset)
    btnreset.grid(row=8,column=1)

    btnexit=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="EXIT", bg="powder blue",command=sexit)
    btnexit.grid(row=8,column=3)

    root.mainloop()

#***************************Delete Book***************************

def DeleteBook():
    root = Tk()

    root.geometry("800x500+0+0")
    root.title("Library Management System")
    try:
        Pic=PhotoImage(file="C:\\Users\jayesh\Documents\Library Management System Background\Lib Background.png")
        background=Label(root,image=Pic)
        background.place(x=0,y=0)
    except:
        print("The image for the program not in the Directory")

    #TIME
    localtime=time.asctime()
    #INFO TOP
    lblinfo = Label(root,font=('aria',30,'bold'),text="DELETE BOOK DATA",bd=10,anchor='w')
    lblinfo.grid(row=0,column=1)
    lblinfo = Label(root,font=('aria',20),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=1)
    def Sub():
        try:
            Scan=Scan.get()
        except:
            Scan=txtIsOrBId.get()
        import mysql.connector as msc
        mydb=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
        mycursor=mydb.cursor()
        mycursor.execute("delete from addbooks where Book_Id="+"'"+Scan+"'"+" or Isbn_No="+"'"+Scan+"'")
        
        mydb.commit()
      
    #Scaning of Barcode/Qr Code
    def Scanner():
        import cv2
        import numpy as np
        import pyzbar.pyzbar as pyzbar

        cap=cv2.VideoCapture(0)
        while True:
            _,frame=cap.read()
            decodeobjs=pyzbar.decode(frame)
            for obj in decodeobjs:
                Scaning=obj.data
            cv2.imshow("Frame",frame)
            key=cv2.waitKey(1)
            if decodeobjs !=[]:
                break
        cap.release()
        cv2.destroyAllWindows()
        Scan.set(Scaning)

    def sexit():
        root.destroy()
    def sback():
        root.destroy()
        Main_Page()

    def reset():
        root.destroy()
        import AddBook
    Scan=StringVar()

    btnIsOrBId=Button(root,padx=8,pady=5,bd=10,fg="black",font=('ariel',16,'bold'),width=15,text="Isbn No. or Book Id",bg="powder blue",command=Scanner)
    btnIsOrBId.grid(row=9,column=0)
    txtIsOrBId=Entry(root,font=('ariel',16,'bold'),textvariable=Scan,bd=6,bg="powder blue",justify='right')
    txtIsOrBId.grid(row=9,column=1)

    #buttons
    btnback=Button(root,padx=16,pady=8,bd=20,fg="black",font=('ariel',16,'bold'),width=6,text="Back",bg="powder blue",command=sback)
    btnback.grid(row=11,column=0)


    btnsub=Button(root,padx=16,pady=8,bd=10,fg="black",font=('ariel',16,'bold'),width=6,text="SUBMIT",bg="powder blue",command=Sub)
    btnsub.grid(row=11,column=2)

    btnreset=Button(root,padx=16,pady=8,bd=10,fg="black",font=('ariel',16,'bold'),width=6,text="RESET",bg="powder blue",command=reset)
    btnreset.grid(row=11,column=1)

    btnexit=Button(root,padx=16,pady=8,bd=10,fg="black",font=('ariel',16,'bold'),width=6,text="EXIT",bg="powder blue",command=sexit)
    btnexit.grid(row=11,column=3)

    root.mainloop()

#***************************Pending Book Return***************************

    
def PendingReturn():
    root=Tk()

    root.geometry("1450x1100+0+0")
    root.title("Library Management System")
    try:
        Pic=PhotoImage(file="C:\\Users\jayesh\Documents\Library Management System Background\Lib Background2.png")
        background=Label(root,image=Pic)
        background.place(x=0,y=0)
    except:
        print("The image for the program not in the Directory")

    #TIME
    localtime=time.asctime()
    #Today's Date
    Date=str(date.today())
    #INFO TOP
    lblinfo = Label(root, font=('aria',30,'bold'),text="Pending Return",bd=10,anchor='w')
    lblinfo.grid(row=0,column=1)
    lblinfo = Label(root, font=('aria' ,20),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=1)

    import mysql.connector as msc
    mydb=msc.connect(host="localhost",user="root",passwd="insane",database="221B")#connects the database by checking passwd,username
    mycursor=mydb.cursor()
    INSERT=("select * from IssueBooks where Return_Date<"+"'"+Date+"'")
    mycursor.execute(INSERT)

    #Header Labeling
    lblSName=Label(root, font=('aria',12, 'bold'),text="SName",fg="steel blue",bd=10)
    lblSName.grid(row=2,column=0)

    lblAdmn=Label(root, font=('aria',12, 'bold'),text="Admn_No.",fg="steel blue",bd=10)
    lblAdmn.grid(row=2,column=1)

    lblCls=Label(root, font=('aria',12, 'bold'),text="Class",fg="steel blue",bd=10)
    lblCls.grid(row=2,column=2)

    lblDOI=Label(root, font=('aria',12, 'bold'),text="DOI",fg="steel blue",bd=10)
    lblDOI.grid(row=2,column=3)

    lblBId=Label(root, font=('aria',12, 'bold'),text="Book_Id",fg="steel blue",bd=10)
    lblBId.grid(row=2,column=4)

    lblTitle=Label(root, font=('aria',12, 'bold'),text="Title",fg="steel blue",bd=10)
    lblTitle.grid(row=2,column=5)

    lblAdmn=Label(root, font=('aria',12, 'bold'),text="Return_Date",fg="steel blue",bd=10)
    lblAdmn.grid(row=2,column=6)

    #Extra
    lblEx=Label(root, font=('aria',12, 'bold'),text="-----------------",fg="steel blue",bd=10)
    lblEx.grid(row=3,column=0)

    lblEx1=Label(root, font=('aria',12, 'bold'),text="-----------------",fg="steel blue",bd=10)
    lblEx1.grid(row=3,column=1)

    lblEx2=Label(root, font=('aria',12, 'bold'),text="-----------------",fg="steel blue",bd=10)
    lblEx2.grid(row=3,column=2)

    lblEx3=Label(root, font=('aria',12, 'bold'),text="-----------------",fg="steel blue",bd=10)
    lblEx3.grid(row=3,column=3)

    lblEx4=Label(root, font=('aria',12, 'bold'),text="-----------------",fg="steel blue",bd=10)
    lblEx4.grid(row=3,column=4)

    lblEx5=Label(root, font=('aria',12, 'bold'),text="-----------------",fg="steel blue",bd=10)
    lblEx5.grid(row=3,column=5)

    lblEx6=Label(root, font=('aria',12, 'bold'),text="-----------------",fg="steel blue",bd=10)
    lblEx6.grid(row=3,column=6)

    R=4  #Initial ror=4

    for i in mycursor:
        #P=Pending
        lblPname=Label(root,font=('aria',12,'bold'),text=i[0],bd=10,anchor='w')
        lblPname.grid(row=R,column=0)

        lblPAdmn=Label(root,font=('aria',12,'bold'),text=i[1],bd=10,anchor='w')
        lblPAdmn.grid(row=R,column=1)

        lblPCls=Label(root,font=('aria',12,'bold'),text=i[2],bd=10,anchor='w')
        lblPCls.grid(row=R,column=2)

        lblPBId=Label(root,font=('aria',12,'bold'),text=i[3],bd=10,anchor='w')
        lblPBId.grid(row=R,column=4)
        
        lblPDOI=Label(root,font=('aria',12,'bold'),text=i[4],bd=10,anchor='w')
        lblPDOI.grid(row=R,column=3)

        lblPTitle=Label(root,font=('aria',12,'bold'),text=i[6],bd=10,anchor='w')
        lblPTitle.grid(row=R,column=5)

        lblPReturn=Label(root,font=('aria',12,'bold'),text=i[7],bd=10,anchor='w')
        lblPReturn.grid(row=R,column=6)

        R=R+1

    def sexit():
        root.destroy()
    def sback():
        root.destroy()
        Main_Page()


    #buttons
    btnback=Button(root,padx=12,pady=8,bd=20,fg="black",font=('ariel',16,'bold'),width=6,text="Back",bg="powder blue",command=sback)
    btnback.grid(row=R+1,column=1)

    btnexit=Button(root,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=6, text="EXIT", bg="powder blue",command=sexit)
    btnexit.grid(row=R+1,column=2)

    root.mainloop()

#***************************Login Page***************************

root1=Tk()
root1.geometry("500x500+0+0")
root1.title("Sign In")
try:
    Pic= PhotoImage(file="C:\\Users\jayesh\Documents\Library Management System Background\Lib 1Background.png")
    background=Label(root1,image=Pic)
    background.place(x=0,y=0,relwidth=1,relheight=1)
except:
    print("The image for the program not in the Directory")

name=StringVar()
password=StringVar()
captcha=StringVar()
j=chr(random.randint(45,99))
k=chr(random.randint(45,99))
i=chr(random.randint(45,99))
CAPTCHA=str(random.randint(10,99))+i+k+str(random.randint(1,9))+j
def enter():
    if name.get()=="Library" and password.get()=="1234" :
        if CAPTCHA==captcha.get():
            root1.destroy()
            Main_Page()   #Function Calling (Main Page)
        else:
            tkinter.messagebox.showinfo('Error','Authentication Failed')
            name.set("")
            password.set("")
            
    else:
        tkinter.messagebox.showinfo('Error','Authentication Failed')
        name.set("")
        password.set("")	

def destroy():
    root1.destroy()	


label = Label(root1,font = ("arial",30,"bold"),text="Sign In",fg="Steel Blue",bd=10)
label.grid(row=0,column=2)

label1=Label(root1,text="Name:")
label2=Label(root1,text="Password:")
label3=Label(root1,text="CAPTCHA:")
label4=Label(root1,text=CAPTCHA)
label5=Label(root1,text="ENTER CAPTCHA:")
        
entry1=Entry(root1,textvariable=name)
entry2=Entry(root1,textvariable=password)
entry5=Entry(root1,textvariable=captcha)

label1.grid(row=1,column=1)        
label2.grid(row=2,column=1)
label3.grid(row=3,column=1)
label4.grid(row=3,column=2)
label5.grid(row=4,column=1
            )
entry1.grid(row=1,column=2)
entry2.grid(row=2,column=2)
entry5.grid(row=4,column=2)

enterbtn=Button(root1,text="Enter",command= enter)
enterbtn.grid(row=5,column=2)

exitbtn=Button(root1,padx= 12,text="Exit",command= destroy)
exitbtn.grid(row=5,column=1)

root1.mainloop()




