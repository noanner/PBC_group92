from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt

import tkinter as tk
import tkinter.font as tkFont

day = ["Day1","Day2","Day3","Day4","Day5","Day6","Day7"]

counts = 0
count_list = []
user_name = ""
material_price = [10, 9, 9, 6, 16]  # 原料價格
order_fixed_cost = 50
stock_list = [0,0,0,0,0]  # 預設存貨
order_cost_list = [0]
stock_cost_list = []
accumulated_profit_list = []
profit_list = []
accumulated_profit = 0
    
class StartPage(object):  # 開始畫面
    def __init__(self, master=None):
        # tk.Frame.__init__(self) 
        # self.grid()
        # self.createWidgets()
        
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame # 新增
        self.page.pack() # 新增
        
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")           

        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.page.lbl_topic = tk.Label(self.page, text = "餐廳經營管理遊戲", height = 2, width = 15, font = f1) 
        self.page.btn_enter = tk.Button(self.page, text = "進入遊戲", command = self.gotoIntro, height = 2, width = 10, font = f2, bg = 'LightYellow')
        self.page.btn_rank = tk.Button(self.page, text = "排行榜", command = self.gotoRanking1, height = 2, width = 10, font = f2, bg = 'Lavender')
        
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        self.page.lbl_topic.place(x=220, y=100)
        self.page.btn_enter.place(x=250, y=350)
        self.page.btn_rank.place(x=500, y=350)
    
    def gotoIntro(self):
        self.page.destroy()
        IntroPage(self.root)
    
    def gotoRanking1(self):
        self.page.destroy()
        RankingPage1(self.root)
    
class IntroPage(object):  # 說明、輸入姓名
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        self.username = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = '請輸入餐廳名稱: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Button(self.page, text='開始遊戲', command=self.gotoRule).grid(row=3, stick=W, pady=10)

    def gotoRule(self):
        global user_name
        name = self.username.get()
        user_name += name
        if name != '':
            self.page.destroy()
            RulePage(self.root)
        else:
            showinfo(title='錯誤', message='你的餐廳還沒命名喔！')


root = Tk()
root.title('小程式')
StartPage(root)
root.mainloop()
print(user_name)

