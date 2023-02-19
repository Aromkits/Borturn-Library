from tkinter import *
import csv

booklist = [num for num in range(1,31)]

bookborrow = []
bookreturn = []

def write(): #บันทึกข้อมูลการยืม
    filepath = 'borrow.csv'
    with open(filepath,"a",encoding='utf-8') as infile:
        writer = csv.writer(infile,lineterminator = "\n")
        writer.writerow(bookborrow)
        
def write1(): #บันทึกของมูลการคืน
    filepath = 'return.csv'
    with open(filepath,"a",encoding='utf-8') as infile:
        writer = csv.writer(infile,lineterminator = "\n")
        writer.writerow(bookreturn)

def namebook(): #แสดงชื่อหนังสือกับรหัสหนังสือทั้งหมด
    shownamebook1 = Tk()
    shownamebook1.title("Show All Book")
    shownamebook1.minsize(300,280)
    head = Label(shownamebook1,text = "All Name Book and Number of Book",font = "Arial 12 bold")
    head.grid(row=0,columnspan=4,pady=30)
    head.configure(bg='goldenrod1')
    book = Label(shownamebook1 ,text = " 1. Mademoiselle de Scuderi\n"
                 +" 2. Arsène Lupin versus Sherlock Holmes\n"
                 +" 3. The Storied Life of A. J. Fikry\n"
                 +" 4. A Study in Terror\n"
                 +" 5. Time We Walk Together\n"
                 +" 6. Pedro Paramo\n"
                 +" 7. The Glass Bead Game\n"
                 +" 8. Harry Potter\n"
                 +" 9. Animal Farm\n"
                 +"10. Burmese Days\n"
                 +"11. The Jungle Book\n"
                 +"12. Body Parts\n"
                 +"13. Peppa's First 100 Words\n"
                 +"14. Finishing the picture\n"
                 +"15. Grandma’s magic box\n"
                 +"16. Kind words are a Gift\n"
                 +"17. Joyful friends\n"
                 +"18. Disney Boys 365 Stories\n"
                 +"19. My Animal's ABC\n"
                 +"20. Buildablock\n"
                 +"21. Into The Magic Shop\n"
                 +"22. 12 Rules For Life\n"
                 +"23. Atomics Habits\n"
                 +"24. Thinking, Fast and Slow\n"
                 +"25. The Little Book of  Happiness\n"
                 +"26. Principles : Life & Work\n"
                 +"27. GRIT : The Power of Passion and Perseverance\n"
                 +"28. The Positive Shift\n"
                 +"29. A Life of Triumph\n"
                 +"30. Productivity"
                 ,font = "Arial 12")
    book.grid(row=1,column=1)

    btClosename = Button(shownamebook1,text="Back",width=10,command=shownamebook1.destroy)
    btClosename.grid(row=5,column=1,pady=10,sticky=SE,padx=10)

def winstatus(): #ตรวจสอบสถานะของหนังสือ
    def statusbook1():
        try:
            num  = int(inp.get())
            if num in booklist:
                lbl["text"] ="Book is Free"
            elif num not in booklist:
                if 1<= num <=30:
                    lbl["text"] ="Book is Not Free"
                elif num <=0 or num >=31:
                    lbl["text"] ="Book isn't in library"
        except Exception as e:
           lbl["text"] ="Please Enter 'Number' "

    def clear():
         inp.delete(0,"end")

    checkstatus1 = Tk()
    checkstatus1.title("Check Book Status")
    checkstatus1.minsize(100,210)
    
    lbl = Label(checkstatus1,pady=8,text="",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    head = Label(checkstatus1,text = "Check Book Status",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,padx=100,pady=20)
    head.configure(bg='goldenrod1')

    head1 = Label(checkstatus1,text = "Enter Number Book\nThat You Want To Check",font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)

    inp = Entry(checkstatus1,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()
    
    btOK= Button(checkstatus1,text="OK",width=10,command=statusbook1)
    btOK.grid(row=4,column=0)
    
    btCLEA = Button(checkstatus1,text = 'Clear',width = 10,command = clear)
    btCLEA.grid(row=4,column=1)

    bt = Button(checkstatus1,text="Back",command = checkstatus1.destroy,width=10)
    bt.grid(row=4,column=2)

def borrowbook(): #ทำการยืมหนังสือ
    def borrowbook1():
        try:
            num  = int(inp.get())
            if num in booklist:
                booklist.remove(num)
                bookborrow.append(num)
                write()
                bookborrow.remove(num) 
                
                lbl["text"] ="Success!"
            elif num not in booklist:
                if num <=0 or num >=31:
                    lbl["text"] ="Book isn't in library"
                elif 1 <= num <= 30:
                    lbl["text"] ="Book was borrowed"
        except Exception as e:
             lbl["text"] ="Please Enter 'Number' "

    def clear():
        inp.delete(0,"end")
   
    borrow1 = Tk()
    borrow1.title("Borrow A Book")
    borrow1.minsize(100,210)

    head = Label(borrow1,text = "Borrow A Book",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=130)
    head.configure(bg='goldenrod1')

    head1 = Label(borrow1,text = "Enter Number Book\nThat You Want To Borrow",font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)

    inp = Entry(borrow1,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(borrow1,pady=8,text="",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(borrow1,text="OK",width=10,command=borrowbook1)
    btOK.grid(row=4,column=0)

    btCLEAR = Button(borrow1,text = 'Clear',width = 10,command = clear)
    btCLEAR.grid(row=4,column=1)
   
    bt = Button(borrow1,text="Back",command = borrow1.destroy,width=10)
    bt.grid(row=4,column=2)
    
def returnbook(): #ทำการคืนหนังสือ
    def returnbook1():
        try:
            num  = int(inp.get())
            if num not in booklist:
                if num <=0 or num >= 31:
                    lbl["text"] ="Book isn't in library"
                elif 1 <= num <= 30:
                    booklist.append(num)
                    bookreturn.append(num)
                    write1()
                    bookreturn.remove(num)
                    lbl["text"] ="Success!"
            elif num in booklist:
                if 1<= num <= 30:
                    lbl["text"] ="Book was not borrowed"
        except Exception as e:
             lbl["text"] ="Please Enter 'Number' "

    def clear():
        inp.delete(0,"end")
    
    return1 = Tk()
    return1.title("Return A Book")
    return1.minsize(100,210)

    head = Label(return1,text = "Return A Book",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=130)
    head.configure(bg='goldenrod1')

    head1 = Label(return1,text = "Enter Number Book\nThat You Want To Return",font = "Arial 10")
    head1.grid(row=2,column=0,columnspan=2,sticky=W,padx=35)

    inp = Entry(return1,width=15)
    inp.grid(row=2,column=1,columnspan=3)
    inp.focus()

    lbl = Label(return1,pady=8,text="",fg="red",font="Arial 12")
    lbl.grid(row=3,column=0,pady=10,columnspan=3)
    
    btOK= Button(return1,text="OK",width=10,command=returnbook1)
    btOK.grid(row=4,column=0)

    btCLEAR = Button(return1,text = 'Clear',width = 10,command = clear)
    btCLEAR.grid(row=4,column=1)
   
    bt = Button(return1,text="Back",command = return1.destroy,width=10)
    bt.grid(row=4,column=2)
    
def pay(): #จ่ายค่าปรับ
    def pay1(baht):
        payfine = baht * 20
        return payfine

    def pay2():
         try:
             baht  = int(inp.get())
             money = pay1(baht)
             if 1 <= baht <=30:
                 lbl["text"] ="You must pay {} Baht".format(pay1(baht))
             elif baht <=0 or baht >30:
                 lbl["text"] ="There are 30 books in library"
         except Exception as e:
            lbl["text"] ="Please Enter 'Number' "

    def clear():
        inp.delete(0,"end")
        
    pay = Tk()
    pay.title("Pay A Fine")
    pay.minsize(200,210)

    head = Label(pay,text = "Pay A Fine",font = "Arial 16")
    head.grid(row=1,column=0,columnspan=3,pady=20,padx=135)
    head.configure(bg='goldenrod1')

    head1 = Label(pay,text = "How Many Book\nHave You Borrowed",font = "Arial 10")
    head1.grid(row=3,column=0,columnspan=2,sticky=W,padx=35)

    inp = Entry(pay,width=15)
    inp.grid(row=3,column=1,columnspan=3)
    inp.focus()
    
    lbl = Label(pay,pady=8,text="",fg="red",font="Arial 12")
    lbl.grid(row=4,column=0,pady=10,columnspan=3)
    
    btOK= Button(pay,text="OK",width=10,command=pay2)
    btOK.grid(row=5,column=0)

    btCLEAR = Button(pay,text = 'Clear',width = 10,command = clear)
    btCLEAR.grid(row=5,column=1)

    bt = Button(pay,text="Back",command = pay.destroy,width=10)
    bt.grid(row=5,column=2)

#mainprogram
def mainprocess(): #เป็นหน้าเมนูเชื่อมไปยังฟังก์ชันต่างๆ
    code = str(inp.get())
    readcode = len(code)
    if readcode != 13:
        lbl["text"] ="Student Code Must Be 13 Character"
    
    else:
        bookborrow.append(code)
        bookreturn.append(code)
        mainwin = Tk()
        mainwin.title("Borturn Library")
        mainwin.minsize(500,400)

        head = Label(mainwin ,text = "\nWelcome To Borturn library! ",font = "Century 16 bold")
        head.grid(row=0,column=0,columnspan=3,padx=150)

        head1 = Label(mainwin ,text = "If you borrowed books for more than 7 days"
              +"\n You must pay a fine of  20 baht per book\n",font = "Arial 12")
        head1.grid(row=1,column=0,columnspan=3)
        
        btShow = Button(mainwin,text="SHOW ALL BOOK",width=30,command=namebook)
        btShow.grid(row=2,pady=7,columnspan=3)

        btCheck = Button(mainwin,text="CHECK BOOK STATUS",width=30,command=winstatus)
        btCheck.grid(row=3,pady=7,columnspan=3)

        btBorrow = Button(mainwin,text="BORROW A BOOK",width=30,command=borrowbook)
        btBorrow.grid(row=4,pady=7,columnspan=3)

        btReturn = Button(mainwin,text="RETURN A BOOK",width=30,command=returnbook)
        btReturn.grid(row=5,pady=7,columnspan=3)

        btPay= Button(mainwin,text="PAY A FINE",width=30,command=pay)
        btPay.grid(row=6,pady=7,columnspan=3)

        btEnd= Button(mainwin,text="Back",width=30,command=mainwin.destroy)
        btEnd.grid(row=7,pady=7,columnspan=3)
    
             
#หน้าต่างแรก รับรหัสนักศึกษา
def clear():
    inp.delete(0,"end")
    bookborrow.clear()
    bookreturn.clear()

userwin = Tk()
userwin.title("Borturn Library")
userwin.minsize(300,250)

head = Label(userwin ,text = "\nWelcome To Borturn library! ",font = "Century 16 bold")
head.grid(row=0,column=0,columnspan=3,padx=20)

head1 = Label(userwin ,text = "Please Enter Your Student code",font = "Arial 12")
head1.grid(row=1,column=0,columnspan=3)

inp = Entry(userwin,width=30)
inp.grid(row=2,column=0,columnspan=3,pady = 20)
inp.focus()

lbl = Label(userwin,pady=8,text="",fg="red",font="Arial 12")
lbl.grid(row=3,column=0,columnspan=3)

btOK= Button(userwin,text="OK",width=10,command=mainprocess)
btOK.grid(row=4,column=0)

btlogout = Button(userwin,text = 'Logout',width = 10,command = clear)
btlogout.grid(row=4,column=1)

bt = Button(userwin,text="End Program",command = userwin.destroy,width=10)
bt.grid(row=4,column=2)

mainloop()

try:
    filepath = 'borrow.csv'
    with open(filepath,"r",encoding='utf-8') as infile:
        readborrow = csv.reader(infile)
        myborrow = list(readborrow)
    bookborrow = len(myborrow)
    print("All Book Was Borrowed = {}".format(bookborrow))
except Exception as e:
    print("You doesn't borrow book")

try:
    filepath = 'return.csv'
    with open(filepath,"r",encoding='utf-8') as infile:
        readreturn = csv.reader(infile)
        myreturn = list(readreturn)
    bookreturn = len(myreturn)
    print("All Book Was Returned = {}".format(bookreturn))
except Exception as e:
    print("You doesn't return book")
