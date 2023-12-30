from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
from tkinter import *
import mysql.connector
from bert_model import review
from chat import get_response

# making GUI App

bot_name = "Serra"
bg_gray = "#ABB2B9"
bg_color = "#17202A"
text_color = "#EAECEE"
font = "Helvetica 10"
font_bold = "Helvetica 10 bold"

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Hi!.. I'm Serra !!")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=400, height=600, bg=bg_color)

        # head label
        head_label = Label(self.window, bg=bg_color, fg=text_color,
                           text="Main menu: '1' for feedback '2' to quit '3' to chat.\n Type 'back' for main menu",
                           font=font_bold,pady=15)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=bg_gray)
        line.place(relwidth=1, rely=0.11, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=bg_color, fg=text_color, font=font, padx=5, pady=5)
        self.text_widget.place(relheight=0.7, relwidth=1, rely=0.12)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=bg_gray, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=text_color, font=font)
        self.msg_entry.place(relx=0.011, rely=0.008, relheight=0.06, relwidth=0.74)
        self.msg_entry.focus() # automatically sets cursor for typing
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=font_bold, width=20, bg=bg_gray,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        conn = mysql.connector.connect(host="localhost", username="root", password="mymysqlZ666#", database="cmdet")
        cmdet_cursor = conn.cursor()
        cmdet_cursor.execute("SELECT first_name,last_name,ref_no FROM restcdata WHERE ref_no = %s", (msg,))
        result = cmdet_cursor.fetchone()
        if msg=="1":
            self._insert_message1(msg, "You")
        elif result:
            fn, ln, ref1 = result
            self._insert_message3(msg, "You", fn, ln, ref1)
        elif msg=="2":
            self.window.destroy()
        elif msg=="3":
            self._insert_message5(msg, "You")
        else:
            self._insert_message2(msg, "You")

    def _on_enter_pressed2(self, event, ref1):
        msg = self.msg_entry.get()
        conn = mysql.connector.connect(host="localhost", username="root", password="mymysqlZ666#", database="cmdet")
        cmdet_cursor = conn.cursor()
        cmdet_cursor.execute("update restcdata set comments=%s where ref_no=%s", (msg,ref1))
        conn.commit()
        conn.close()
        self._insert_message4(msg, "You", ref1)

    def _on_enter_pressed3(self, event):
        msg = self.msg_entry.get()
        if msg.lower() == "quit":
            self.window.destroy()
        elif msg.lower() == "back":
            self._insert_message7(msg, "You")
        else:
            self._insert_message6(msg, "You")
    def _insert_message1(self, msg, sender):
        if not msg:
            return

        # user dialogue display
        self.msg_entry.delete(0, END)
        msg1 = f"\n\n{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)  # enabled for entry of msg
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)  # disabled space after entry of msg

        # response from bot
        msg2 = f"{bot_name}: Please enter your Reference ID"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)  # scrolling to end to see the last message

    def _insert_message2(self, msg, sender):
        if not msg:
            return

        # user dialogue display
        self.msg_entry.delete(0, END)
        msg1 = f"\n\n{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)  # enabled for entry of msg
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)  # disabled space after entry of msg

        # response from bot
        msg2 = f"{bot_name}: Invalid Entry !!..."
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)  # scrolling to end to see the last message

    def _insert_message3(self, msg, sender, fn, ln, ref1):
        if not msg:
            return

        # user dialogue display
        self.msg_entry.delete(0, END)
        msg1 = f"\n\n{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)  # enabled for entry of msg
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)  # disabled space after entry of msg

        # response from bot
        msg2 = f"{bot_name}: Hi {fn} {ln} \nPlease leave your feedback/review."
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)  # scrolling to end to see the last message
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", lambda event: self._on_enter_pressed2(event, ref1))
    def _insert_message4(self, msg, sender, ref1):
        if not msg:
            return

        # user dialogue display
        self.msg_entry.delete(0, END)
        msg1 = f"\n\n{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)  # enabled for entry of msg
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)  # disabled space after entry of msg

        # response from bot
        msg2 = f"{bot_name}: {review(msg,ref1)}"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)  # scrolling to end to see the last message
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

    def _insert_message5(self, msg, sender):
        if not msg:
            return

        # user dialogue display
        self.msg_entry.delete(0, END)
        msg1 = f"\n\n{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)  # enabled for entry of msg
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)  # disabled space after entry of msg

        # response from bot
        msg2 = f"{bot_name}: Welcome to the chat session."
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)  # scrolling to end to see the last message
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed3)

    def _insert_message6(self, msg, sender):
        if not msg:
            return

        # user dialogue display
        self.msg_entry.delete(0, END)
        msg1 = f"\n\n{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)  # enabled for entry of msg
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)  # disabled space after entry of msg

        # response from bot
        msg2 = f"{bot_name}: {get_response(msg)}"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)  # scrolling to end to see the last message
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed3)

    def _insert_message7(self, msg, sender):
        if not msg:
            return

        # user dialogue display
        self.msg_entry.delete(0, END)
        msg1 = f"\n\n{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)  # enabled for entry of msg
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)  # disabled space after entry of msg

        # response from bot
        msg2 = f"{bot_name}: You are back in main menu...!! "
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)  # scrolling to end to see the last message
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

ChatApplication().run()