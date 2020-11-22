from tkinter import *
import user
import block
class MyButtons:
    def __init__(self,root):
        self.tkWindow=root
        self.tkWindow.geometry('400x200')
        self.tkWindow.title('BITCOIN')
        self.tkWindow.propagate(0)

        # username label and text entry box
        self.register = Label(self.tkWindow, text="Register").grid(row=0, column=1)
        self.usernameLabel = Label(self.tkWindow, text="User Name").grid(row=1, column=0)
        self.username = StringVar()
        self.usernameEntry = Entry(self.tkWindow, textvariable=self.username)
        self.usernameEntry.grid(row=1, column=1)

        # password label and password entry box
        self.passwordLabel = Label(self.tkWindow, text="Password").grid(row=2, column=0)
        self.password = StringVar()
        self.passwordEntry = Entry(self.tkWindow, textvariable=self.password, show='*')
        self.passwordEntry.grid(row=2, column=1)

        # login button
        self.loginButton = Button(self.tkWindow, text="SIGNUP",command=buttonClick)
        self.loginButton.grid(row=4, column=1)
        self.signin = Label(self.tkWindow, text="ALREADY HAVE AN ACCOUNT-->").grid(row=6, column=1)
        self.signin = Button(self.tkWindow, text="SIGNIN",command=signin)
        self.signin.grid(row=6,column=2)
        self.explorer = Button(self.tkWindow, text="EXPLORE BLOCK", command=exploreblock)
        self.explorer.grid(row=7, column=1)

def buttonClick():
    user.user(obj.usernameEntry.get(),obj.passwordEntry.get()).register()
def onClick(u,p):
    user.signin(u,p)
def exploreblock():
    block.explore()




def signin():
    tkWindow=Tk()
    tkWindow.geometry('400x150')
    tkWindow.title('BITCOIN')
    tkWindow.propagate(0)

    # username label and text entry box
    signin = Label(tkWindow, text="SIGNIN").grid(row=0, column=1)
    usernameLabel = Label(tkWindow, text="User Name").grid(row=1, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username)
    usernameEntry.grid(row=1, column=1)

    # password label and password entry box
    passwordLabel = Label(tkWindow, text="Password").grid(row=2, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*')
    passwordEntry.grid(row=2, column=1)

    # login button
    loginButton = Button(tkWindow, text="SIGNIN", command=lambda :onClick(usernameEntry.get(),passwordEntry.get()))
    loginButton.grid(row=4, column=1)
    tkWindow.mainloop()

root=Tk()
obj=MyButtons(root)
root.mainloop()
