import tkinter
import tkinter.messagebox


# OK按钮响应事件
def login():
    name = entryName.get()              # 获取用户名
    pwd = entryPwd.get()                # 获取密码
    if name == 'admin' and pwd == '123456':
        tkinter.messagebox.showinfo(title="python tkinter", message="welcome login")
    else:
        tkinter.messagebox.showerror(title="python tkinter", message="Wrong username or password")


# Cancel按钮响应事件
def cancel():
    varName.set('')
    varPwd.set('')


root = tkinter.Tk()

# 申明变量存储用户名和密码
varName = tkinter.StringVar(value='')
varPwd = tkinter.StringVar(value='')

# 建立用户名和密码输入提示和输入框:
labelName = tkinter.Label(root, text='User Name:', justify=tkinter.RIGHT, width=80)
labelName.place(x=10, y=5, width=80, height=20)
entryName = tkinter.Entry(root, width=80, textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)
labelPwd = tkinter.Label(root, text='User pwd:', justify=tkinter.RIGHT, width=80)
labelPwd.place(x=10, y=30, width=80, height=20)
entryPwd = tkinter.Entry(root, show='*', width=80, textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)

# 建立OK和Cancel按钮并绑定事件:
buttonOk = tkinter.Button(root, text='Login', command=login)
buttonOk.place(x=30, y=70, width=50, height=20)
buttonCancel = tkinter.Button(root, text='Cancel', command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)

root.mainloop()     # 启动消息循环
