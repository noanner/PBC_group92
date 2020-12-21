from tkinter import *
from tkinter.messagebox import *

counts = 0
count_list = []
user_name = []
    
class LoginPage(object):
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (300, 180)) #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        global counts
        global count_list
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = '賬戶: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        if counts < 6:
            Button(self.page, text='登陸', command=self.loginCheck).grid(row=3, stick=W, pady=10)
            Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)
            counts += 1
            count_list.append(counts)
        else:
            Button(self.page, text='登陸', command=self.gotoLast).grid(row=3, stick=W, pady=10)
            Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        global user_name
        name = self.username.get()
        user_name.append(name)
        secret = self.password.get()
		# if name=='wangliang' and secret=='123456':
        self.page.destroy()
        MainPage(self.root)
		#else:
			#showinfo(title='錯誤', message='賬號或密碼錯誤！')
    def gotoLast(self):
        self.page.destroy()
        LastPage(root)

class MainPage(object):
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (300, 180)) #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = '賬戶2: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼2: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陸2', command=self.returnLogin).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出2', command=self.page.quit).grid(row=3, column=1, stick=E)

    def returnLogin(self):
        self.page.destroy()
        LoginPage(root)
    def gotoLast(self):
        self.page.destroy()
        LastPage(root)

class LastPage(object):
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (300, 180)) #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = '賬戶3: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼3: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陸3', command=self.page.quit).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出3', command=self.page.quit).grid(row=3, column=1, stick=E)
    '''
        self.inputPage = InputFrame(self.root) # 建立不同Frame
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        self.inputPage.pack() #預設顯示資料錄入介面
        menubar = Menu(self.root)
        menubar.add_command(label='資料錄入', command = self.inputData)
        menubar.add_command(label='查詢', command = self.queryData)
        menubar.add_command(label='統計', command = self.countData)
        menubar.add_command(label='關於', command = self.aboutDisp)
        self.root['menu'] = menubar  # 設定選單欄
    '''

'''
    def inputData(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def countData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()

    def aboutDisp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()
'''
'''
class InputFrame(Frame): # 繼承Frame類
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master #定義內部變數root
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = '藥品名稱: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)
        Label(self, text = '進價 /元: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.importPrice).grid(row=2, column=1, stick=E)
        Label(self, text = '售價 /元: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.sellPrice).grid(row=3, column=1, stick=E)
        Label(self, text = '優惠 /元: ').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.deductPrice).grid(row=4, column=1, stick=E)
        Button(self, text='錄入', command=self.returnLogin).grid(row=6, column=1, stick=E, pady=10)
    
    def returnLogin(self):
        self.page.destroy()
        LoginPage(self.root)


class QueryFrame(Frame): # 繼承Frame類
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定義內部變數root
		self.itemName = StringVar()
		self.createPage()

	def createPage(self):
		Label(self, text='查詢介面').pack()

class CountFrame(Frame): # 繼承Frame類
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定義內部變數root
		self.createPage()

	def createPage(self):
		Label(self, text='統計介面').pack()


class AboutFrame(Frame): # 繼承Frame類
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定義內部變數root
		self.createPage()

	def createPage(self):
		Label(self, text='關於介面').pack()
'''
root = Tk()
root.title('小程式')
LoginPage(root)
root.mainloop()
print(user_name)

