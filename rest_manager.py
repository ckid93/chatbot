from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from bert_model import sentiment_score

class Customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Management Module")
        self.root.geometry("1540x800+0+0")

        #setting data variables
        self.fn = StringVar()
        self.ln = StringVar()
        self.eid = StringVar()
        self.nov = StringVar()
        self.conu = StringVar()
        self.oex = StringVar()
        self.rev = StringVar()
        self.refno = StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="CUSTOMER MODULE",fg="#0000B9",bg="#ABB2B9",
                       font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP, fill=X)
        # fg is dark blue and bg is grey

        #Dataframe
        Dataframe= Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft = LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,text="Customer Info",
                         font=("times new roman",12,"bold"))
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight = LabelFrame(Dataframe,bd=10,padx=10,relief=RIDGE,text="Summary",
                                   font=("times new roman",12,"bold"))
        DataframeRight.place(x=990,y=5,width=460,height=350)

        #Buttonframe
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=80)

        # DetailsFrame
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=610, width=1530, height=150)

        # Left side dataframe
        lbl1=Label(DataframeLeft,font=("arial",11,"bold"),text="First Name",padx=2,pady=6)
        lbl1.grid(row=0,column=0,sticky=W)
        txt1=Entry(DataframeLeft,textvariable=self.fn,font=("arial",13,"bold"),width=35)
        txt1.grid(row=0, column=1)

        lbl2 = Label(DataframeLeft, font=("arial", 11, "bold"), text="Last Name", padx=2, pady=6)
        lbl2.grid(row=1, column=0, sticky=W)
        txt2 = Entry(DataframeLeft,textvariable=self.ln, font=("arial", 13, "bold"), width=35)
        txt2.grid(row=1, column=1)

        lbl3 = Label(DataframeLeft, font=("arial", 11, "bold"), text="Email ID", padx=2, pady=6)
        lbl3.grid(row=2, column=0, sticky=W)
        txt3 = Entry(DataframeLeft,textvariable=self.eid,font=("arial", 13, "bold"), width=35)
        txt3.grid(row=2, column=1)

        lbl4 = Label(DataframeLeft, font=("arial", 11, "bold"), text="No of visitors", padx=2, pady=6)
        lbl4.grid(row=3, column=0, sticky=W)
        comtxt4 = ttk.Combobox(DataframeLeft,textvariable=self.nov,state="readonly", font=("arial", 13, "bold"), width=33)
        comtxt4['value']=("1","2","3","4","5","5+","10+")
        comtxt4.current(0)
        comtxt4.grid(row=3, column=1)

        lbl5 = Label(DataframeLeft, font=("arial", 11, "bold"), text="Contact Number", padx=2, pady=6)
        lbl5.grid(row=4, column=0, sticky=W)
        txt5 = Entry(DataframeLeft,textvariable=self.conu,font=("arial", 13, "bold"), width=35)
        txt5.grid(row=4, column=1)

        lbl5 = Label(DataframeLeft, font=("arial", 11, "bold"), text="Overall Experience", padx=2, pady=6)
        lbl5.grid(row=5, column=0, sticky=W)
        comtxt5 = ttk.Combobox(DataframeLeft,textvariable=self.oex,state="readonly", font=("arial", 13, "bold"), width=33)
        comtxt5['value'] = ("1", "2", "3", "4", "5",)
        comtxt5.current(0)
        comtxt5.grid(row=5, column=1)

        lbl6 = Label(DataframeLeft, font=("arial", 11, "bold"), text="Comments", padx=2, pady=6)
        lbl6.grid(row=6, column=0, sticky=W)
        txt6 = Entry(DataframeLeft, textvariable=self.rev, font=("arial", 13, "bold"), width=60)
        txt6.grid(row=6, column=1)

        lbl6 = Label(DataframeLeft, font=("arial", 11, "bold"), text="Reference ID", padx=2, pady=6)
        lbl6.grid(row=7, column=0, sticky=W)
        txt6 = Entry(DataframeLeft, textvariable=self.refno, font=("arial", 13, "bold"), width=60)
        txt6.grid(row=7, column=1)

        # Right side dataframe
        self.txtsummary=Text(DataframeRight,font=("arial", 11, "bold"),width=50,height=16,padx=2,pady=6)
        self.txtsummary.grid(row=0,column=0)

        #Buttons
        btn1=Button(Buttonframe,text="Summary",font=("arial", 11, "bold"),
                    fg="#aa0066",bg="#ffcc99",width=20,height=1,padx=2,pady=6,command=self.summary)
        btn1.grid(row=0, column=0)

        btn2 = Button(Buttonframe, text="Insert Data", font=("arial", 11, "bold"),
                      fg="#aa0066", bg="#ffcc99", width=20, height=1, padx=2, pady=6,command=self.revdata)
        btn2.grid(row=0, column=1)

        btn3 = Button(Buttonframe, text="Update", font=("arial", 11, "bold"),
                      fg="#aa0066", bg="#ffcc99", width=20, height=1, padx=2, pady=6,command=self.update_data)
        btn3.grid(row=0, column=2)

        btn7 = Button(Buttonframe, text="Find", font=("arial", 11, "bold"),
                      fg="#aa0066", bg="#ffcc99", width=20, height=1, padx=2, pady=6,command=self.find_data)
        btn7.grid(row=0, column=3)

        btn4 = Button(Buttonframe, text="Delete", font=("arial", 11, "bold"),
                      fg="#aa0066", bg="#ffcc99", width=20, height=1, padx=2, pady=6,command=self.delete_data)
        btn4.grid(row=0, column=4)

        btn5 = Button(Buttonframe, text="Clear", font=("arial", 11, "bold"),
                      fg="#aa0066", bg="#ffcc99", width=20, height=1, padx=2, pady=6,command=self.clear_data)
        btn5.grid(row=0, column=5)

        btn6 = Button(Buttonframe, text="Exit", font=("arial", 11, "bold"),
                      fg="#aa0066", bg="#ffcc99", width=20, height=1, padx=2, pady=6,command=self.exit_window)
        btn6.grid(row=0, column=6)

        #Table

        #Scrollbar
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.cmdet=ttk.Treeview(Detailsframe,column=("fn","ln","eid","nov","conu","oex","rev","refno"),
                                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.cmdet.xview)
        scroll_y=ttk.Scrollbar(command=self.cmdet.yview)

        self.cmdet.heading("fn",text="First Name")
        self.cmdet.heading("ln", text="Last Name")
        self.cmdet.heading("eid", text="Email ID")
        self.cmdet.heading("nov", text="No of visitors")
        self.cmdet.heading("conu", text="Phone Number")
        self.cmdet.heading("oex", text="Overall Experience")
        self.cmdet.heading("rev", text="Comments")
        self.cmdet.heading("refno", text="Reference Number")


        self.cmdet["show"]="headings"

        self.cmdet.pack(fill=BOTH, expand=1)
        self.cmdet.bind("<<TreeviewSelect>>", self.get_cursor)
        self.fetch_data()

    # database
    def revdata(self):
        if self.fn.get()=="" or self.ln.get()=="" or self.eid.get()=="" or self.nov.get()=="" or self.conu.get()=="" or self.oex.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="mymysqlZ666#",database="cmdet")
            cmdet_cursor=conn.cursor()
            cmdet_cursor.execute("insert into restcdata(first_name,last_name,email_id,no_of_visitors,phone_number,overall_exp,comments,ref_no,rev_score) "
                                 "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (self.fn.get(),self.ln.get(),self.eid.get(),self.nov.get(),self.conu.get(),
                                    self.oex.get(),self.rev.get(),self.refno.get(),sentiment_score(self.rev.get())
                                    )
                                )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Data inserted successfully!")

    def update_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mymysqlZ666#", database="cmdet")
        cmdet_cursor = conn.cursor()
        cmdet_cursor.execute("update restcdata set first_name=%s,last_name=%s,email_id=%s,no_of_visitors=%s,"
                             "overall_exp=%s,comments=%s,phone_number=%s,rev_score=%s where ref_no=%s",
            (self.fn.get(), self.ln.get(), self.eid.get(), self.nov.get(),
             self.oex.get(), self.rev.get(), self.conu.get(),sentiment_score(self.rev.get()) ,self.refno.get()
             )
            )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data updated successfully!")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mymysqlZ666#", database="cmdet")
        cmdet_cursor = conn.cursor()
        cmdet_cursor.execute("select first_name,last_name,email_id,no_of_visitors,phone_number,overall_exp,comments,ref_no from restcdata")
        rows=cmdet_cursor.fetchall()
        if len(rows)!=0:
            self.cmdet.delete(*self.cmdet.get_children())
            for i in rows:
                self.cmdet.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.cmdet.focus()
        content=self.cmdet.item(cursor_row)
        row=content["values"]
        self.fn.set(row[0])
        self.ln.set(row[1])
        self.eid.set(row[2])
        self.nov.set(row[3])
        self.conu.set(row[4])
        self.oex.set(row[5])
        self.rev.set(row[6])
        self.refno.set(row[7])

    def summary(self):
        self.txtsummary.insert(END,"Reference Number: \t\t\t"+self.refno.get()+"\n")
        self.txtsummary.insert(END,"First Name: \t\t\t"+self.fn.get()+"\n")
        self.txtsummary.insert(END,"Last Name: \t\t\t"+self.ln.get()+"\n")
        self.txtsummary.insert(END,"E-mail ID: \t\t\t"+self.eid.get()+"\n")
        self.txtsummary.insert(END,"Number of Visitors: \t\t\t"+self.nov.get()+"\n")
        self.txtsummary.insert(END,"Phone Number: \t\t\t"+self.conu.get()+"\n")
        self.txtsummary.insert(END,"Overall Rating: \t\t\t"+self.oex.get()+"\n")
        self.txtsummary.insert(END,"Misc. Comments: \t\t\t"+self.rev.get()+"\n")

    def delete_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mymysqlZ666#", database="cmdet")
        cmdet_cursor = conn.cursor()
        query="delete from restcdata where ref_no=%s"
        value=(self.refno.get(),)
        cmdet_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Deleted successfully!")

    def clear_data(self):
        self.fn.set("")
        self.ln.set("")
        self.eid.set("")
        self.nov.set("")
        self.conu.set("")
        self.oex.set("")
        self.rev.set("")
        self.refno.set("")
        self.txtsummary.delete("1.0",END)

    def find_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mymysqlZ666#", database="cmdet")
        cmdet_cursor = conn.cursor()
        query = "select first_name,last_name,email_id,no_of_visitors,phone_number,overall_exp,comments from restcdata where ref_no=%s"
        value = (self.refno.get(),)
        cmdet_cursor.execute(query, value)
        rows = cmdet_cursor.fetchall()
        if len(rows) != 0:
            self.cmdet.delete(*self.cmdet.get_children())
            for i in rows:
                self.cmdet.insert("", END, values=i)
            conn.commit()
            messagebox.showinfo("Success", "Data found!")
        else:
            messagebox.showinfo("Abort", "No Data found!")
        conn.close()

    def exit_window(self):
        exitw=messagebox.askyesno("Closing Window","Do you want to exit?")
        if exitw>0:
            root.destroy()
            return

root=Tk()
ob=Customer(root)
root.mainloop()