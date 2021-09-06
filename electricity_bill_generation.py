#ELECTRICITY BILL GENERATION

from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import datetime
from tkinter import messagebox
import time
import calendar

global e6
global st

#CHECK IF USER HAS ENTERED A NUMBER
def isnumber(num):
    try:
        n=int(num)
        return True
    except:
        return False
        
#INSERT DATA        
def insert():
    try:
        
        conn.execute("CREATE TABLE CUSTOMER \
            (ID INT PRIMARY KEY NOT NULL, \
         FNAME  TEXT    NOT     NULL, \
         LNAME  TEXT    NOT     NULL, \
         CITY  TEXT    NOT     NULL,\
        CURRENT  FLOAT    NOT     NULL, \
        PREVIOUS  FLOAT, \
        DATE_OF_CURRENT  TEXT    NOT     NULL );")
        #print("Table created successfully")
    except:
        None
        
    try:
        
        conn.execute("CREATE TABLE CUSTOMERDATA \
            (ID INT PRIMARY KEY NOT NULL, \
         JAN  INT  , \
         FEB  INT  , \
         MAR  INT  ,\
        APR  INT  ,\
       MAY  INT  ,\
       JUNE  INT  ,\
       JULY  INT  ,\
       AUG  INT  ,\
       SEP  INT  ,\
       OCT  INT  ,\
       NOV  INT  ,\
       DEC  INT   );")
        #print("Table 2 created successfully")
    except:
        None   
        
    
    
    
    if(e0.get()=='' or e1.get()=='' or e2.get()==0 or e3.get()==0):
        messagebox.showinfo("Error", "Please Enter all the details")
    else:
        try:
            if(isnumber(e4.get()) and int(e4.get())>=0):
                
            
                
                st=str(datetime.datetime.now().strftime("%d-%m-%Y"))
                
                #ENTERING DATA IN TABLE 1
                conn.execute("INSERT INTO CUSTOMER (ID,FNAME,LNAME,CITY,CURRENT,DATE_OF_CURRENT) \
                  VALUES (?,?,?,?,?,?)",(e0.get(),e1.get(),e2.get(),e3.get(),e4.get(),st));           
                conn.commit()
                
                
                #ENTERING DATA IN TABLE 2
                now=int(datetime.datetime.now().strftime("%m"))
                if(now==1):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,JAN) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));
                if(now==2):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,FEB) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));   
                if(now==3):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,MAR) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));            
                if(now==4):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,APR) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));    
                if(now==5):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,MAY) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));    
                if(now==6):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,JUNE) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));    
                if(now==7):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,JULY) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));    
                if(now==8):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,AUG) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));    
                if(now==9):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,SEP) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));    
                if(now==10):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,OCT) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));
                if(now==11):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,NOV) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));
                if(now==12):
                    conn.execute("INSERT INTO CUSTOMERDATA (ID,DEC) \
                    VALUES (?,?)",(e0.get(),int(e4.get())));
                conn.commit()    
                messagebox.showinfo("Success", "DATA ENTERED SUCCESSFULLY")
                e0.delete(0,END)
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
            else:
                messagebox.showinfo("Error","Invalid data")
        except sqlite3.IntegrityError:
            messagebox.showinfo("Error", "The entered ID is already present")
        except Exception as ex:
                print(ex)
       
#DISPLAY FUNCTION       
def display():
    try:
        if(e0.get()==''):
            messagebox.showinfo("Error", "Please Enter the ID")
        else:
            cursor=conn.execute("SELECT ID,FNAME,LNAME,CITY,CURRENT,DATE_OF_CURRENT from CUSTOMER where ID=?",(e0.get(),))
            if(len(cursor.fetchall())==0):               
                messagebox.showinfo("Error",'There is no record with ID %s'%e0.get()) 
            else:
                cursor=conn.execute("SELECT ID,FNAME,LNAME,CITY,CURRENT,DATE_OF_CURRENT from CUSTOMER where ID=?",(e0.get(),))
           
            
                for row in cursor:                                    
                    id=int(row[0])
                    name=str(row[1])
                    lname=str(row[2])
                    city=str(row[3])
                    current=str(row[4])
                    date=str(row[5])
                    final="ID : "+str(id)+"\n"+"First name : "+name+"\n"+"Last name : "+lname+"\n"+"City : "+city+"\nCurrent reading : "+current+"\n"+"Date of reading : "+date
                #row=str(row)
                #row=row.replace(',','\n')
                    messagebox.showinfo("Data",final)#"%d\t%s\t%s\t%s\t%.2f\t\t%s"%(row[0],row[1],row[2],row[3],row[4],row[5]))'''			           
    except Exception as ex:
        print(ex)
		
def update():
    if(e0.get()==''):
        messagebox.showinfo("Error","Please enter the ID to be updated")
    else:
        st=str(datetime.datetime.now().strftime("%d-%m-%Y"))
        cursor=conn.execute("UPDATE CUSTOMER set FNAME=?, LNAME=?, CITY=?, CURRENT=?, DATE_OF_CURRENT=? \
                    where ID=?",(e1.get(),e2.get(),e3.get(),e4.get(),st,e0.get()))
        conn.commit()
#UPDATING THE SECOND TABLE
        try:
            st=str(datetime.datetime.now().strftime("%d-%m-%Y"))
           
            
            #ENTERING DATA IN TABLE 2
            now=int(datetime.datetime.now().strftime("%m"))
            if(now==1):
                conn.execute("UPDATE CUSTOMERDATA set JAN=? where ID=?", (e4.get(),e0.get()))
                conn.commit()                
            if(now==2):
                conn.execute("UPDATE CUSTOMERDATA set FEB=? where ID=?", (e4.get(),e0.get()))
                conn.commit()   
            if(now==3):
                conn.execute("UPDATE CUSTOMERDATA set MAR=? where ID=?", (e4.get(),e0.get()))
                conn.commit()            
            if(now==4):
                conn.execute("UPDATE CUSTOMERDATA set APR=? where ID=?", (e4.get(),e0.get()))
                conn.commit()     
            if(now==5):
                conn.execute("UPDATE CUSTOMERDATA set MAY=? where ID=?", (e4.get(),e0.get()))
                conn.commit()     
            if(now==6):
                conn.execute("UPDATE CUSTOMERDATA set JUNE=? where ID=?", (e4.get(),e0.get()))
                conn.commit()     
            if(now==7):
                conn.execute("UPDATE CUSTOMERDATA set JULY=? where ID=?", (e4.get(),e0.get()))
                conn.commit()     
            if(now==8):
                conn.execute("UPDATE CUSTOMERDATA set AUG=? where ID=?", (e4.get(),e0.get()))
                conn.commit()    
            if(now==9):
                conn.execute("UPDATE CUSTOMERDATA set SEP=? where ID=?", (e4.get(),e0.get()))
                conn.commit()     
            if(now==10):
                conn.execute("UPDATE CUSTOMERDATA set OCT=? where ID=?", (e4.get(),e0.get()))
                conn.commit() 
            if(now==11):
                conn.execute("UPDATE CUSTOMERDATA set NOV=? where ID=?", (e4.get(),e0.get()))
                conn.commit() 
            if(now==12):
                conn.execute("UPDATE CUSTOMERDATA set DEC=? where ID=?", (e4.get(),e0.get()))
                conn.commit() 
                
            #messagebox.showinfo("Success", "DATA ENTERED SUCCESSFULLY")
            e0.delete(0,END)
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
        except sqlite3.IntegrityError:
            messagebox.showinfo("Error", "The entered ID is already present")
        except Exception as ex:
                print(ex)                
        messagebox.showinfo("Update", "Details updated successfully")
   
#DELETE FUNCTION  
def delete():
    if(e0.get()==''):
        messagebox.showinfo("Error","Please enter the ID to be deleted")
    else:
        cursor=conn.execute("DELETE from CUSTOMER where ID=%d"%(int(e0.get())))
        conn.commit()
        cursor=conn.execute("DELETE from CUSTOMERDATA where ID=%d"%(int(e0.get())))
        conn.commit()
        messagebox.showinfo("Delete", "Record deleted successfully")
    
#CLOSE THE PROGRAM    
def exit1():
    conn.close()
    exit()

    
#DISPLAY BOTH TABLES   
def tab2():
    try:
        print("Details:")
        cursor=conn.execute("SELECT ID,JAN,FEB,MAR,APR,MAY,JUNE,JULY,AUG,SEP,OCT,NOV,DEC from CUSTOMERDATA")
        '''print("ID\tFNAME\tLNAME\t\tCITY\tCURRENT\t\tDATE_OF_CURRENT")
        messagebox.showinfo("Success",str(cursor))'''
        for row in cursor:                    
            print(row)#"%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))'''			           
    except Exception as ex:
        print(ex)

def tab1():
    try:
        print("Details:")
        cursor=conn.execute("SELECT ID,FNAME,LNAME,CITY,CURRENT,DATE_OF_CURRENT from CUSTOMER")       
        for row in cursor:                    
            print(row)#"%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))'''			           
    except Exception as ex:
        print(ex)

#FETCH DATA INTO TEXTFIELDS        
def fetch():
    try:
        if(e0.get()==''):
            messagebox.showinfo("Error", "Please Enter the ID")
     
        else:
            cursor=conn.execute("SELECT ID,FNAME,LNAME,CITY,CURRENT,DATE_OF_CURRENT from CUSTOMER where ID=?",(e0.get(),))
            if(len(cursor.fetchall())==0):               
                messagebox.showinfo("Error",'There is no record with ID %s'%e0.get()) 
            else:
                cursor=conn.execute("SELECT ID,FNAME,LNAME,CITY,CURRENT,DATE_OF_CURRENT from CUSTOMER where ID=?",(e0.get(),))
           
            
                for row in cursor:                                    
                    e1.insert(0,row[1])
                    e2.insert(0,row[2])
                    e3.insert(0,row[3])
                    e4.insert(0,row[4])
                    
                    
                    
                			           
    except Exception as ex:
        print(ex)
		







        
#CREATE THE NEW FRAME FOR DISPLAYING 1 YEAR RECORD  
def show():
    global e6
    global st
    flag=0
    
    #FETCHING DATA FROM DATABASE
    try:
        if(e6.get()==''):
            messagebox.showinfo("Error", "Please Enter the ID")
        else:
            cursor=conn.execute("SELECT ID,FNAME,LNAME,CITY,CURRENT,DATE_OF_CURRENT from CUSTOMER where ID=?",(e6.get(),))
            if(len(cursor.fetchall())==0):               
                messagebox.showinfo("Error",'There is no record with ID %s'%e6.get()) 
            else:
                cursor=conn.execute("SELECT ID,FNAME,LNAME,CITY,CURRENT,DATE_OF_CURRENT from CUSTOMER where ID=?",(e6.get(),))
                flag=1
                for row in cursor:                                    
                    id=int(row[0])
                    name=str(row[1])
                    lname=str(row[2])
                    st=name+" "+lname
                    
                    
    except Exception as ex:
        print(ex)
                    
    

    
    
    
    if(flag==1):
        window=tk.Toplevel(root)
        w = 602 # width for the Tk root
        h = 450 # height for the Tk root

# get screen width and height
        ws = window.winfo_screenwidth() # width of the screen
        hs = window.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window.title("Customer record")

        
    #CREATING TABLE           
        tree = ttk.Treeview(window,height=1)

        tree["columns"]=("one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve")

        tree['show'] = 'headings'       #TO SUPPRESS THE DEFAULT FIRST COLUMN OF TREEVIEW
        tree.column("one", width=50 )
        tree.column("two", width=50)
        tree.column("three", width=50 )
        tree.column("four", width=50)
        tree.column("five", width=50 )
        tree.column("six", width=50)
        tree.column("seven", width=50 )
        tree.column("eight", width=50)
        tree.column("nine", width=50 )
        tree.column("ten", width=50)
        tree.column("eleven", width=50 )
        tree.column("twelve", width=50)

        tree.heading("#0", text="Name")
        tree.heading("one", text="Jan")
        tree.heading("two", text="Feb")
        tree.heading("three", text="Mar")
        tree.heading("four", text="Apr")
        tree.heading("five", text="May")
        tree.heading("six", text="Jun")
        tree.heading("seven", text="Jul")
        tree.heading("eight", text="Aug")
        tree.heading("nine", text="Sep")
        tree.heading("ten", text="Oct")
        tree.heading("eleven", text="Nov")
        tree.heading("twelve", text="Dec")

        
        tree.place(x=0,y=120)
       
        e5=Entry(window,width=20)
        e5.place(x=55,y=30)
        l7=Label(window,text="ID")
        l7.place(x=10,y=30)
        e7=Entry(window,width=30)
        e7.place(x=300,y=30)
        l8=Label(window,text="Name")
        l8.place(x=245,y=30)
        a="Record of year "+str(datetime.datetime.now().strftime("%Y"))
        l9=Label(window,text=a)
        l9.place(x=220,y=95)
        l10=Label(window,text="Current reading")
        l10.place(x=10,y=200)
        e8=Entry(window,width=30)
        e8.place(x=115,y=200)
        mydate = datetime.datetime.now()
        
        s1="Your bill for "+mydate.strftime("%b")
        l11=Label(window,text=s1)
        l11.place(x=10,y=240)
        e9=Entry(window,width=30)
        e9.place(x=115,y=240)
        
        e5.insert(0,id)  
        e5.config(state="readonly")
        e7.insert(0,st)
        e7.config(state="readonly")
        try:        
            
                
            cursor=conn.execute("SELECT ID,JAN,FEB,MAR,APR,MAY,JUNE,JULY,AUG,SEP,OCT,NOV,DEC from CUSTOMERDATA where ID=?",(int(e5.get()),))
            
            for row in cursor: 
                
                tree.insert("" , 0, values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
                now=int(datetime.datetime.now().strftime("%m"))
                if(now==1):
                    #cursor=conn.execute("SELECT ID,JAN from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[1])
                    e8.config(state="readonly")
                if(now==2):
                    #cursor=conn.execute("SELECT ID,FEB from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[2])
                    e8.config(state="readonly")
                if(now==3):
                    #cursor=conn.execute("SELECT ID,MAR from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[3])
                    e8.config(state="readonly")
                if(now==4):
                    #cursor=conn.execute("SELECT ID,APR from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[4])
                    e8.config(state="readonly")
                if(now==5):
                    #cursor=conn.execute("SELECT ID,MAY from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[5])
                    e8.config(state="readonly")
                if(now==6):
                    #cursor=conn.execute("SELECT ID,JUNE from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[6])
                    e8.config(state="readonly")
                if(now==7):
                    #cursor=conn.execute("SELECT ID,JULY from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[7])
                    e8.config(state="readonly")
                if(now==8):
                    #cursor=conn.execute("SELECT ID,AUG from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[8])
                    e8.config(state="readonly")
                if(now==9):
                    #cursor=conn.execute("SELECT ID,SEP from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[9])
                    e8.config(state="readonly")
                if(now==10):
                    #cursor=conn.execute("SELECT ID,OCT from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[10])
                    e8.config(state="readonly")
                if(now==11):
                    #cursor=conn.execute("SELECT ID,NOV from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[11])
                    e8.config(state="readonly")
                if(now==12):
                    #cursor=conn.execute("SELECT ID,DEC from CUSTOMERDATA where ID=?",(int(e5.get()),))
                    e8.insert(0,row[12])
                    e8.config(state="readonly")
                if(int(e8.get())<500):
                    e9.insert(0,int(e8.get())*5)
                    e9.config(state="readonly")
                elif(int(e8.get())>=500 and int(e8.get())<1000):
                    e9.insert(0,int(e8.get())*7)
                    e9.config(state="readonly")
                else:
                    e9.insert(0,int(e8.get())*9)
                    e9.config(state="readonly")
        except Exception as ex:
            print(ex)
 
#DELETE TABLES
def cleartab():
    try:
        conn.execute("drop table CUSTOMER")
        conn.execute("drop table CUSTOMERDATA")
    except Exception as ex:
        print(ex)
    
 
    
    
    
    
#====================================CREATING THE MAIN WINDOW	==============================================
root=tk.Tk()
root.title("Electricity bill generation")
root.geometry('500x500')

#CREATING FRAMES
nb=ttk.Notebook(root)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)


nb.add(page1, text='Customer info')
nb.add(page2,text="Bill generation")
nb.pack(expand=2,fill="both")

e0=Entry(page1,width=20)
e0.place(x=100,y=10)

l1=Label(page1,text="First name",)
l1.place(x=10,y=30)

e1=Entry(page1,width=20)
e1.place(x=100,y=30)

l2=Label(page1,text="Last name")
l2.place(x=10,y=50)

e2=Entry(page1,width=20)
e2.place(x=100,y=50)

l3=Label(page1,text="City")
l3.place(x=10,y=70)

e3=Entry(page1,width=20)
e3.place(x=100,y=70)

l0=Label(page1,text="ID")    
l0.place(x=10,y=10)

l4=Label(page1,text="Units")
l4.place(x=10,y=90)

e4=Entry(page1,width=20)
e4.place(x=100,y=90)


bn1=Button(page1, text="TABLE 1", command=tab1)
bn1.place(x=10,y=230)

bn2=Button(page1, text="TABLE 2", command=tab2)
bn2.place(x=70,y=230)

bn2=Button(page1, text="CLEAR DATA", command=cleartab)
bn2.place(x=135,y=190)




conn=sqlite3.connect('test.db')
#conn.execute("drop table CUSTOMER")
try:
	
    conn.execute("CREATE TABLE CUSTOMER \
        (ID INT PRIMARY KEY NOT NULL, \
     FNAME  TEXT    NOT     NULL, \
     LNAME  TEXT    NOT     NULL, \
     CITY  TEXT    NOT     NULL,\
    CURRENT  FLOAT    NOT     NULL, \
    PREVIOUS  FLOAT, \
    DATE_OF_CURRENT  TEXT    NOT     NULL );")
    #print("Table created successfully")
except:
    None
    
try:
	
    conn.execute("CREATE TABLE CUSTOMERDATA \
        (ID INT PRIMARY KEY NOT NULL, \
     JAN  INT  , \
     FEB  INT  , \
     MAR  INT  ,\
    APR  INT  ,\
   MAY  INT  ,\
   JUNE  INT  ,\
   JULY  INT  ,\
   AUG  INT  ,\
   SEP  INT  ,\
   OCT  INT  ,\
   NOV  INT  ,\
   DEC  INT   );")
    #print("Table 2 created successfully")
except:
    None   
    
    

b1=Button(page1, text="INSERT", command=insert)
b1.place(x=10,y=150)

b3=Button(page1, text="DISPLAY", command=display)
b3.place(x=70,y=150)

b2=Button(page1,text="UPDATE",command=update)
b2.place(x=135,y=150)

b4=Button(page1,text="DELETE",command=delete)
b4.place(x=10,y=190)

b5=Button(page1,text="EXIT",command=exit)
b5.place(x=70,y=190,width=50)




l5=Label(page2,text="ID")    
l5.place(x=60,y=30)
e6=Entry(page2,width=20)
e6.place(x=100,y=30)
b6=tk.Button(page2,text="SHOW", command=show)
b6.place(x=150,y=80,width=100)

b7=tk.Button(page1,text="FETCH DATA", command=fetch)
b7.place(x=200,y=150,width=100)


root.mainloop()

