import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from PIL import ImageTk

day = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7"]

counts = 0
count_list = []
user_name = ""
material_price = [10, 9, 9, 6, 16]  # 原料價格
order_fixed_cost = 50
stock_list = [0, 0, 0, 0, 0]  # 預設存貨
order_cost_list = [0]
stock_cost_list = []
accumulated_profit_list = []
profit_list = []
accumulated_profit = 0


class StartPage(object):  # 開始畫面
    def __init__(self, master = None):
        # tk.Frame.__init__(self)
        # self.grid()
        # self.createWidgets()

        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame # 新增
        self.page.pack()  # 新增

        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)  # 製造一個空的grid在底下
        self.page.lbl_topic = tk.Label(self.page, text = "餐廳經營管理遊戲", height = 2, width = 15, font = f1)
        self.page.btn_enter = tk.Button(self.page, text = "進入遊戲", command = self.gotoIntro, height = 2, width = 10,
                                        font = f2, bg = 'LightYellow')
        self.page.btn_rank = tk.Button(self.page, text = "排行榜", command = self.gotoRanking1, height = 2, width = 10,
                                       font = f2, bg = 'Lavender')

        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        self.page.lbl_topic.place(x = 220, y = 100)
        self.page.btn_enter.place(x = 250, y = 350)
        self.page.btn_rank.place(x = 500, y = 350)

    def gotoIntro(self):
        self.page.destroy()
        IntroPage(self.root)

    def gotoRanking1(self):
        self.page.destroy()
        RankingPage1(self.root)


class RankingPage1(object):  # 排行榜(前)
    def __init__(self, master=None):
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

        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 20, width = 30, font = f1)
        self.page.lbl_topic = tk.Label(self.page, text = "排行榜", height = 2, width = 30, font = f1) 
        self.page.psystem = tk.Label(self.page, text = "第一名：", height = 2, width = 30, font = f3, bg = 'LightYellow')
        self.page.qsystem = tk.Label(self.page, text = "第二名：", height = 2, width = 30, font = f3, bg = 'OldLace')
        self.page.btn_main = tk.Button(self.page, text = "回主畫面", command = self.gotoStartPage, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        self.page.lbl_topic.grid(row = 0, column = 0)
        self.page.psystem.grid(row = 1, column = 0)
        self.page.qsystem.grid(row = 2, column = 0)
        self.page.btn_main.place(x = 780, y = 480)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
    
    def gotoStartPage(self):
        self.page.destroy()
        StartPage(root)


class IntroPage(object):  # 說明、輸入姓名

    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry("900x600+200+30")  # 設定視窗大小
        self.username = StringVar()
        self.createPage()

    def createPage(self):
        f1 = tkFont.Font(size = 15, family = "娃娃体-简")
        f2 = tkFont.Font(size = 14, family = "娃娃体-简")
        # self.page = tk.Canvas(root, height = HEIGHT, width = WIDTH)
        self.page = Frame(self.root)
        self.page.pack()
        # 背景圖片填滿畫布
        self.background_image = ImageTk.PhotoImage(file = 'restaurant.jpg')
        self.background_label = tk.Label(self.root, image = self.background_image)
        self.background_label.place(relwidth = 1, relheight = 1)
        # 建立框架
        self.frame = tk.Frame(root, bg = 'LavenderBlush', bd = 5)
        self.frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
        # 輸入框
        self.button1 = tk.Button(self.frame, text = "請輸入你的名字：", font = f1)
        self.button1.place(relx = 0, relheight = 1, relwidth = 0.3, anchor = 'nw')

        self.intro = tk.Label(root, text = "有沒有想過經營一間漢堡餐廳？\n\n在這個遊戲裡，你要盡自己的需求預測能力，進行訂貨以及存貨管理。\n"
                                           "這個遊戲中，你將會面對每天不同的銷售情境，\n根據不同的情境，你必須預測菜單的需求變動狀況，"
                                           "進而去決定如何訂購產品原料。\n" "遊戲中，最重要的三個元素就是需求數量、訂購的固定成本以及材料成本。\n"
                                           "遊戲將根據你的獲利情況計算分數，最後進行評價。",
                              font = f2, bg = 'OldLace')
        self.intro.place(relx = 0.5, rely = 0.3, relwidth = 0.8, relheight = 0.3, anchor = 'n')

        self.button2 = tk.Button(root, text = "開始遊戲", font = f1, command = self.gotoRule)
        self.button2.place(relx = 0.7, rely = 0.9, relheight = 0.05, relwidth = 0.1, anchor = 'se')

        self.entry = tk.Entry(self.frame, textvariable = self.username, font = 40)
        self.entry.place(relwidth = 0.65, relx = 0.3, relheight = 1)

    def gotoRule(self):
        global user_name
        name = self.username.get()
        print(name)
        # user_name += name
        if name != '':
            self.page.destroy()
            RulePage(self.root)
        else:
            showinfo(title = '錯誤', message = '你的餐廳還沒命名喔！')


class RulePage(object):  # 營業說明
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry("900x600+200+30")  # 設定視窗大小
        self.username = StringVar()
        self.createPage()

    def createPage(self):
        f1 = tkFont.Font(size = 15, family = "娃娃体-简")
        f2 = tkFont.Font(size = 14, family = "娃娃体-简")
        # self.page = tk.Canvas(root, height = HEIGHT, width = WIDTH)
        self.page = Frame(self.root)
        self.page.pack()
        # 背景圖片填滿畫布
        self.background_image = ImageTk.PhotoImage(file = 'restaurant.jpg')
        self.background_label = tk.Label(self.root, image = self.background_image)
        self.background_label.place(relwidth = 1, relheight = 1)
        # 建立框架
        self.frame = tk.Frame(root, bg = 'OldLace', bd = 5)
        # self.frame.place(relx = 0.5, rely = 0.1, relwidth = 0.7, relheight = 0.05, anchor = 'n')
        # 輸入框
        self.intro = tk.Label(root, text = "有一個經驗老道的前輩看你辛苦，於是給你提示，讓你的營業額在第一天能有收益，"
                                           "也可以有適當的存貨之後請你依照這個標準進行食材訂購喔~", wraplength = 400,
                              font = f2, bg = 'OldLace')
        self.intro.place(relx = 0.5, rely = 0.2, relwidth = 0.75, relheight = 0.15, anchor = 'n')

        self.button = tk.Button(root, text = "開始遊戲", font = f1, command = self.gotoDay1)
        self.button.place(relx = 0.7, rely = 0.9, relheight = 0.05, relwidth = 0.1, anchor = 'se')

        # 建立成本表格
        self.columns = ("品項", "成本", "售價", "期初存貨", "進貨成本", "存貨成本")
        self.treeview = ttk.Treeview(root, height = 7, show = "headings", columns = self.columns)  # 表格
        # 表格UI
        style = ttk.Style()
        style.configure("Treeview.Heading", font = ("娃娃体-简", 12))
        style.configure("Treeview", font = ("娃娃体-简", 10))

        # 表格格式
        self.treeview.column("品項", width = 30, anchor = 'center')
        self.treeview.column("成本", width = 30, anchor = 'center')
        self.treeview.column("售價", width = 30, anchor = 'center')
        self.treeview.column("期初存貨", width = 40, anchor = 'center')
        self.treeview.column("進貨成本", width = 40, anchor = 'center')
        self.treeview.column("存貨成本", width = 40, anchor = 'center')
        # 显示表头
        self.treeview.heading("品項", text = "品項")
        self.treeview.heading("成本", text = "成本")
        self.treeview.heading("售價", text = "售價")
        self.treeview.heading("期初存貨", text = "期初存貨")
        self.treeview.heading("進貨成本", text = "進貨成本")
        self.treeview.heading("存貨成本", text = "存貨成本")

        # treeview.pack(side = LEFT, fill = BOTH)
        self.treeview.place(relx = 0.1, rely = 0.4, relwidth = 0.75, relheight = 0.2)

        self.name = ['牛肉漢堡', '豬肉漢堡', '雞肉漢堡', '生菜堡', '生酮堡']
        self.unitCost = ['10', '9', '9', '6', '16']
        self.unitPrice = ['20', '18', '18', '12', '32']
        self.inventory = ['25', '25', '25', '25', '25']
        self.orderingCost = ['$50元/次', '$50元/次', '$50元/次', '$50元/次', '$50元/次']
        self.inventoryCost = ['$2/單位', '$2/單位', '$2/單位', '$2/單位', '$2/單位']
        for i in range(len(self.name)):  # 寫入数据
            self.treeview.insert('', i, values = (self.name[i], self.unitCost[i],
                                                  self.unitPrice[i], self.inventory[i], self.orderingCost[i],
                                                  self.inventoryCost[i]))

    def gotoRule(self):
        global user_name
        name = self.username.get()
        print(name)
        # user_name += name
        if name != '':
            self.page.destroy()
            RulePage(self.root)
        else:
            showinfo(title = '錯誤', message = '你的餐廳還沒命名喔！')

    def gotoDay1(self):
        self.page.destroy()
        Day1Page1(self.root)


know_content = "小知識11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
class Day1Page1(object):  # Day 1 小知識的日子
    
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()
    
    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        
        # 元件內容
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 30, font = f1) # 製造一個空的grid在底下
        lbl_day = tk.Label(text = "Day1小知識問答", height = 1, width = 15, font = f1) 
        lbl_know = tk.Label(text = know_content, font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left')
        btn_optA = tk.Button(text = "選項A", command = self.gotoCorrect, width = 7,height = 2, font = f2, bg = 'Lavender')
        btn_optB = tk.Button(text = "選項B", command = self.gotoWrong, width = 7,height = 2, font = f2, bg = 'Lavender')
        btn_calendar = tk.Button(text = "行事曆", command = self.openCalendar, width = 7,height = 2, font = f2, bg = 'Lavender')
        
        # 元件位置
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        lbl_day.place(x= 26, y=20)
        lbl_know.place(relx= 0.2, rely=0.35, width=350, height=200)
        btn_optA.place(relx= 0.2, rely=0.75)
        btn_optB.place(relx= 0.5, rely=0.75)
        btn_calendar.place(x= 780, y=20)
    
    def gotoCorrect(self):
        self.page.destroy()
        CorrectPage(self.root)
        # showinfo(title='小提示', message='小提示輸入處')
        
    def gotoWrong(self):
        self.page.destroy()
        WrongPage(self.root)
    
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')


class Day4Page1(object):  # Day 4 小知識的日子
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()
    
    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        
        # 元件內容
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 30, font = f1) # 製造一個空的grid在底下
        lbl_day = tk.Label(text = "Day4小知識問答", height = 1, width = 15, font = f1) 
        lbl_know = tk.Label(text = know_content, font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left')
        btn_optA = tk.Button(text = "選項A", command = self.gotoCorrect, width = 7,height = 2, font = f2, bg = 'Lavender')
        btn_optB = tk.Button(text = "選項B", command = self.gotoWrong, width = 7,height = 2, font = f2, bg = 'Lavender')
        btn_calendar = tk.Button(text = "行事曆", command = self.openCalendar, width = 7,height = 2, font = f2, bg = 'Lavender')
        
        # 元件位置
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        lbl_day.place(x= 26, y=20)
        lbl_know.place(relx= 0.2, rely=0.35, width=350, height=200)
        btn_optA.place(relx= 0.2, rely=0.75)
        btn_optB.place(relx= 0.5, rely=0.75)
        btn_calendar.place(x= 780, y=20)
    
    def gotoCorrect(self):
        self.page.destroy()
        CorrectPage(self.root)
        # showinfo(title='小提示', message='小提示輸入處')
        
    def gotoWrong(self):
        self.page.destroy()
        WrongPage(self.root)
    
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')


hint = '為了獎勵你答對，告訴你一個小提示吧~ !!!!!!!!!!'
class CorrectPage(object):  # Day 1 答對頁面
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        
        # 顯示恭喜答對 
        self.page.lbl_topic = tk.Label(self.page, text = 'Bingo!', height = 1, width = 5, font = f1)
        self.page.lbl_topic.place(x = 26, y = 20)

        # 行事曆按鈕
        Button(self.page, text='行事曆', width=7, height=2, font=f2, background="Lavender", command=self.openCalendar).place(x=780, y=10)

        # 答對的圖片
        global cooking_img
        image = ImageTk.Image.open("Bingo.jpg")
        # image = ImageTk.Image.open("C:\\Users\\formo\\Documents\\python files\\finalproject\\mytest\\S__85836045.png")
        image = image.resize((300, 300), ImageTk.Image.ANTIALIAS)
        cooking_img = ImageTk.PhotoImage(image)
        Label(self.page, image = cooking_img).place(x=150, y=150)

        # 答對的小提示
        self.page.lbl_hint = tk.Label(self.page, text = hint, font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left')
        self.page.lbl_hint.place(x = 500, y = 200)
        # self.page.lbl_description = tk.Label(self.page, text="為了獎勵你答對，告訴你一個小提示吧~", height = 2, width = 40, bg="#F3F3F3", fg="black", font=f3)
        # self.page.lbl_description.place(x = 400, y = 300)

        # 下一頁按鈕
        Button(self.page, text='繼續遊戲', width=7, height=2, font=f2, background="Lavender", command=self.gotoDay1).place(x=780, y=480)
        
    def gotoDay1(self):
        self.page.destroy()
        EverydayPage(self.root)
        
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')

class WrongPage(object):  # Day 1 答錯頁面
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        
        # 顯示可惜答錯 
        self.page.lbl_topic = tk.Label(self.page, text = 'Oops', height = 1, width = 5, font = f1)
        self.page.lbl_topic.place(x = 26, y = 20)

        # 行事曆按鈕
        Button(self.page, text='行事曆', width=7, height=2, font=f2, background="Lavender", command=self.openCalendar).place(x=780, y=10)

        # 答錯的圖片
        global cooking_img
        image = ImageTk.Image.open("wrong.png")
        # image = ImageTk.Image.open("C:\\Users\\formo\\Documents\\python files\\finalproject\\mytest\\S__85836045.png")
        image = image.resize((300, 300), ImageTk.Image.ANTIALIAS)
        cooking_img = ImageTk.PhotoImage(image)
        Label(self.page, image = cooking_img).place(x=150, y=150)

        # 答錯的訊息
        self.page.lbl_hint = tk.Label(self.page, text = "答錯了 好可惜呀... 不要氣餒，繼續玩遊戲吧!", font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left')
        self.page.lbl_hint.place(x = 500, y = 200)
        # self.page.lbl_description = tk.Label(self.page, text="為了獎勵你答對，告訴你一個小提示吧~", height = 2, width = 40, bg="#F3F3F3", fg="black", font=f3)
        # self.page.lbl_description.place(x = 400, y = 300)

        # 下一頁按鈕
        Button(self.page, text='繼續遊戲', width=7, height=2, font=f2, background="Lavender", command=self.gotoDay1).place(x=780, y=480)
        
    def gotoDay1(self):
        self.page.destroy()
        EverydayPage(self.root)
        
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')


class EverydayPage(object):  # 每日漢堡製作畫面

    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry("900x600+200+30") #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 空表格、標題、下一頁
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)

        # 顯示Day 1 
        self.page.lbl_topic = tk.Label(self.page, text = ("Day " + str(counts+1)), height = 1, width = 5, font = f1)
        self.page.lbl_topic.place(x = 26, y = 20)

        # 行事曆按鈕
        Button(self.page, text='行事曆', width=7, height=2, font=f2, background="Lavender", command=self.openCalendar).place(x=780, y=10)

        # 做漢堡的圖片
        global cooking_img
        image = ImageTk.Image.open("S__85836045.png")
        # image = ImageTk.Image.open("C:\\Users\\formo\\Documents\\python files\\finalproject\\mytest\\S__85836045.png")
        image = image.resize((600, 300), ImageTk.Image.ANTIALIAS)
        cooking_img = ImageTk.PhotoImage(image)
        Label(self.page, image = cooking_img).place(x=150, y=150)

        # 顯示 餐廳開始營業囉，點選下一頁查看你今天的營業成果吧~ 
        self.page.lbl_description = tk.Label(self.page, text="餐廳開始營業囉，點選下一頁查看你今天的營業成果吧~", height = 2, width = 40, bg="#F3F3F3", fg="black", font=f3)
        self.page.lbl_description.place(x = 200, y = 30)

        # 下一頁按鈕
        Button(self.page, text='下一頁', width=7, height=2, font=f2, background="Lavender", command=self.gotoDayResult).place(x=780, y=480)

    def gotoDayResult(self):
        self.page.destroy()
        EverydayResultPage(root)

    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')

    """
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (300, 500)) #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = ("Day " + str(counts+1) + "製作:")).grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼2: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='看看今天的營業成果', command=self.gotoDayResult).grid(row=3, stick=W, pady=10)
        Button(self.page, text='行事曆', command=self.openCalendar).grid(row=0, column=1, stick=E)

    def gotoDayResult(self):
        self.page.destroy()
        EverydayResultPage(root)

    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')
    """


class EverydayResultPage(object):  # 每日結算畫面
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry("900x600+200+30") #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 空表格、標題、下一頁
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)

        # 顯示 header
        self.page.lbl_topic = tk.Label(self.page, text = ("Day " + str(counts+1)), height = 1, width = 5, font = f1)
        self.page.lbl_topic.place(x = 26, y = 20)

        self.page.lbl_description = tk.Label(self.page, text = "辛苦了~下面是你今天營業的成果~~", height = 2, width = 40, font = f3)
        self.page.lbl_description.place(x = 200, y = 30)

        if counts < 6 : 
            # 下一頁按鈕
            self.page.btn_next = tk.Button(self.page, text = "下一頁", command = self.gotoStockorder, height = 2, width = 7, font = f2, bg = 'Lavender')
            self.page.btn_next.place(x=780, y=480)
            
            # 行事曆按鈕
            Button(self.page, text='行事曆', width=7, height=2, font=f2, background="Lavender", command=self.openCalendar).place(x=780, y=10)
        else:
            # 下一頁按鈕
            self.page.btn_next = tk.Button(self.page, text = "最終結算", command = self.gotoResult, height = 2, width = 7, font = f2, bg = 'Lavender')
            self.page.btn_next.place(x=780, y=480)

        # 品項表格
        columns = ("牛肉漢堡","豬肉堡堡","雞肉漢堡","生菜堡","生酮堡堡")
        self.page.tree_item = ttk.Treeview(self.page, column = columns)  #表格

        self.page.tree_item.column("#0", minwidth=0, width=110, anchor="center")
        self.page.tree_item.column("牛肉漢堡",width=80, anchor="center")   #表示列,不顯示
        self.page.tree_item.column("豬肉堡堡",width=80, anchor="center")
        self.page.tree_item.column("雞肉漢堡",width=80, anchor="center")
        self.page.tree_item.column("生菜堡",width=80, anchor="center")
        self.page.tree_item.column("生酮堡堡",width=80, anchor="center")

        self.page.tree_item.heading("#0", text="品項")  #顯示錶頭
        self.page.tree_item.heading("牛肉漢堡",text="牛肉漢堡")
        self.page.tree_item.heading("豬肉堡堡",text="豬肉堡堡")
        self.page.tree_item.heading("雞肉漢堡",text="雞肉漢堡")
        self.page.tree_item.heading("生菜堡",text="生菜堡")
        self.page.tree_item.heading("生酮堡堡",text="生酮堡堡")

        self.page.tree_item.insert("",0,text="期初庫存" ,values=("25","25","25","25","25")) #插入資料，
        self.page.tree_item.insert("",1,text="需求量" ,values=("20","20","20","20","20"))
        self.page.tree_item.insert("",2,text="賣出數量" ,values=("20","20","20","20","20"))
        self.page.tree_item.insert("",3,text="營業額" ,values=("400","360","360","240","640"))
        self.page.tree_item.insert("",4,text="營業額百分比" ,values=("20%","18%","18%","12%","32%"))

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("微軟正黑體", 10))
        style.configure("Treeview", rowheight=50, font=("微軟正黑體", 10))

        self.page.tree_item.place(x=60, y=140, height=300)

        # 金額表格
        columns = ("金額")
        self.page.tree_amount = ttk.Treeview(self.page, column = columns)  #表格

        self.page.tree_amount.column("#0", minwidth=0, width=100, anchor="center")
        self.page.tree_amount.column("金額",width=100, anchor="center")   #表示列,不顯示

        self.page.tree_amount.heading("#0", text="品項")
        self.page.tree_amount.heading("金額",text="金額")  #顯示錶頭

        self.page.tree_amount.insert("",0,text="今日收益" ,values=("2000")) #插入資料，
        self.page.tree_amount.insert("",1,text="原料成本" ,values=("0"))
        self.page.tree_amount.insert("",2,text="進貨成本" ,values=("0"))
        self.page.tree_amount.insert("",3,text="存貨成本" ,values=("50"))
        self.page.tree_amount.insert("",4,text="本日淨利" ,values=("1950"))

        self.page.tree_amount.place(x=620, y=140, height=300)

    def gotoStockorder(self):
        self.page.destroy()
        EverydayStockPage(root)
        
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')
    
    def gotoResult(self):
        self.page.destroy()
        FinalResultPage1(root)
"""
    def createPage(self):
        global counts
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = ("Day " + str(counts+1) + "結算:")).grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼2: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        if counts < 6 : 
            Button(self.page, text='準備訂貨', command=self.gotoStockorder).grid(row=3, stick=W, pady=10)
            Button(self.page, text='行事曆', command=self.openCalendar).grid(row=0, column=1, stick=E)
        else:
            Button(self.page, text='最終結算', command=self.gotoResult).grid(row=3, stick=W, pady=10)

    def gotoStockorder(self):
        self.page.destroy()
        EverydayStockPage(root)
        
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')
    
    def gotoResult(self):
        self.page.destroy()
        FinalResultPage1(root)
"""


class EverydayStockPage(object):  # Day1~Day6 訂貨畫面 (是否加個計算功能?)
    
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        
        self.beef = StringVar()
        self.pork = StringVar()
        self.chicken = StringVar()
        self.vege = StringVar()
        self.keto = StringVar()
        
        self.createPage()

    def createPage(self):
        global counts
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        f4 = tkFont.Font(size = 10, family = "微軟正黑體")
        
        # row0 標題、敘述、行事曆按鈕
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 30, font = f1) # 製造一個空的grid在底下
        self.page.lbl_topic = tk.Label(self.page, text = ("Day" + str(counts+1)), height = 1, width = 5, font = f1)
        self.page.lbl_description = tk.Label(self.page, text = "以下是目前的剩餘庫存，請問今天要訂多少貨呢?", height = 2, width = 40, font = f3)
        self.page.btn_schedule = tk.Button(self.page, text = "行事曆", command = self.openCalendar, height = 2, width = 7, font = f2, bg = 'Lavender')

        # row7 訂貨固定成本、目前訂購總價、訂購按鈕
        self.page.lbl_fixcost = tk.Label(self.page, text = " 各品項固定成本:$50元 ", height = 1, width = 18, font = f3, bg = 'LemonChiffon')
        self.page.lbl_note = tk.Label(self.page, text = " 沒有要訂購也要輸入0唷! ", height = 1, width = 18, font = f3, bg = 'LemonChiffon')
        self.page.lbl_cost = tk.Button(self.page, text = "總價試算", command = self.costCalculation, height = 2, width = 8, font = f2, bg = 'Lavender')
        if counts != 2 and counts < 6:
            self.page.btn_order = tk.Button(self.page, text = "訂購!", command = self.orderFinished, height = 2, width = 7, font = f2, bg = 'Lavender')
            self.page.btn_order.place(x = 780, y = 480)
        elif counts == 2:
            self.page.btn_order = tk.Button(self.page, text = "訂購!", command = self.orderFinishedgoto4, height = 2, width = 7, font = f2, bg = 'Lavender')
            self.page.btn_order.place(x = 780, y = 480)
      
        # row0 排版位置
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        self.page.lbl_topic.place(x = 26, y = 20)
        self.page.lbl_description.place(x = 200, y = 30)
        self.page.btn_schedule.place(x = 780, y = 10)
        
        # row7 排版位置
        self.page.lbl_fixcost.place(x = 150, y = 480)
        self.page.lbl_note.place(x = 150, y = 520)
        self.page.lbl_cost.place(x = 511, y = 480)
        self.page.btn_order.place(x = 780, y = 480)
        #-----------------------------------------------------------------------------------------------------------
        
        # 品項表格
        columns = ("訂購單價","剩餘庫存","訂購數量")
        self.page.tree_item = ttk.Treeview(self.page, column = columns)  #表格
        
        self.page.tree_item.column("#0", minwidth=0, width=120, anchor="center")
        self.page.tree_item.column("訂購單價",width=120, anchor="center")
        self.page.tree_item.column("剩餘庫存",width=120, anchor="center")
        self.page.tree_item.column("訂購數量",width=123, anchor="center")

        self.page.tree_item.heading("#0", text="食材")
        self.page.tree_item.heading("訂購單價",text="訂購單價")  #顯示錶頭
        self.page.tree_item.heading("剩餘庫存",text="剩餘庫存")
        self.page.tree_item.heading("訂購數量",text="訂購數量")

        self.page.tree_item.insert("",0,text="牛肉漢堡" ,values=("10","剩餘庫存")) #插入資料，
        self.page.tree_item.insert("",1,text="豬肉漢堡" ,values=("9","剩餘庫存"))
        self.page.tree_item.insert("",2,text="雞肉漢堡" ,values=("9","剩餘庫存"))
        self.page.tree_item.insert("",3,text="生菜堡" ,values=("6","剩餘庫存"))
        self.page.tree_item.insert("",4,text="生酮堡" ,values=("16","剩餘庫存"))

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("微軟正黑體", 10))
        style.configure("Treeview", rowheight=50, font=("微軟正黑體", 10))
        self.page.tree_item.place(x=150, y=140, height=276)
        #-----------------------------------------------------------------------------------------------------------
        
        # 讓玩家輸入的表格
        self.page.txt_beef = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_pork = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_chick = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_vego = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_keto = tk.Text (self.page, height = 2, width = 12 , font = f4)
    
        # 輸入的表格 排版位置
        self.page.txt_beef.place(x=511, y=165)
        self.page.txt_pork.place(x=511, y=215)
        self.page.txt_chick.place(x=511, y=265)
        self.page.txt_vego.place(x=511, y=315)
        self.page.txt_keto.place(x=511, y=365)
                
        
    def costCalculation(self):
        global material_price
        global order_fixed_cost
        order_list = []
        total_cost = 0
        beefnum = self.page.txt_beef.get("1.0",END)
        order_list.append(beefnum)
        porknum = self.page.txt_pork.get("1.0",END)
        order_list.append(porknum)
        chickennum = self.page.txt_chick.get("1.0",END)
        order_list.append(chickennum)
        vegenum = self.page.txt_vego.get("1.0",END)
        order_list.append(vegenum)
        ketonum = self.page.txt_keto.get("1.0",END)
        order_list.append(ketonum)
        
        result = "success"
        for order in order_list:
            try:
                order = int(order)
            except ValueError:
                result = "failed"
                break
        if result == "success":
            for i in range(len(order_list)):
                if int(order_list[i]) > 0:
                    total_cost += order_fixed_cost
                    total_cost += int(order_list[i]) * material_price[i]
                else:
                    pass
            showinfo(title="成本計算",message=("總成本為$" + str(total_cost)))
        else:
            showinfo(title="錯誤", message="累了嗎?請輸入正確格式")

    def orderFinished(self):
        global stock_list
        global order_cost_list
        global counts
        order_list = []
        total_cost = 0
        beefnum = self.page.txt_beef.get("1.0",END)
        order_list.append(beefnum)
        porknum = self.page.txt_pork.get("1.0",END)
        order_list.append(porknum)
        chickennum = self.page.txt_chick.get("1.0",END)
        order_list.append(chickennum)
        vegenum = self.page.txt_vego.get("1.0",END)
        order_list.append(vegenum)
        ketonum = self.page.txt_keto.get("1.0",END)
        order_list.append(ketonum)
        
        result = "success"
        for order in order_list:
            try:
                order = int(order)
            except ValueError:
                result = "failed"
                break
        if result == "success":
            for i in range(len(order_list)):
                if int(order_list[i]) > 0:
                    total_cost += order_fixed_cost
                    total_cost += int(order_list[i]) * material_price[i]
                    stock_list[i] += int(order_list[i])
                else:
                    pass
            order_cost_list.append(total_cost)
            counts += 1
            self.page.destroy()
            EverydayPage(root)
        else:
            showinfo(title="錯誤", message="累了嗎?請輸入正確格式")
        


    def orderFinishedgoto4(self):
        global stock_list
        global order_cost_list
        global counts
        order_list = []
        total_cost = 0
        beefnum = self.page.txt_beef.get("1.0",END)
        order_list.append(beefnum)
        porknum = self.page.txt_pork.get("1.0",END)
        order_list.append(porknum)
        chickennum = self.page.txt_chick.get("1.0",END)
        order_list.append(chickennum)
        vegenum = self.page.txt_vego.get("1.0",END)
        order_list.append(vegenum)
        ketonum = self.page.txt_keto.get("1.0",END)
        order_list.append(ketonum)
        
        result = "success"
        for order in order_list:
            try:
                order = int(order)
            except ValueError:
                result = "failed"
                break
        if result == "success":
            for i in range(len(order_list)):
                if int(order_list[i]) > 0:
                    total_cost += order_fixed_cost
                    total_cost += int(order_list[i]) * material_price[i]
                    stock_list[i] += int(order_list[i])
                else:
                    pass
            order_cost_list.append(total_cost)
            counts += 1
            self.page.destroy()
            Day4Page1(root)
        else:
            showinfo(title="錯誤", message="累了嗎?請輸入正確格式")

    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')


class FinalResultPage1(object):
    def __init__(self, master=None):
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

        # 空表格、標題、下一頁
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.page.lbl_topic = tk.Label(self.page, text = "總結算1", height = 1, width = 10, font = f1) 
        self.page.btn_next = tk.Button(self.page, text = "總結算2", command = self.gotoResult, height = 2, width = 7, font = f2, bg = 'Lavender')
        # 左半邊 折線圖
        self.page.lbl_descripition = tk.Label(self.page, text = "營業成果折線圖", height = 1, width = 15, font = f2)
        self.page.btn_chart = tk.Canvas(self.page, height = 400, width = 500, bg = 'LightYellow')
        
        #-------------------------------------------------------------------------------------------
        # 空表格、標題、下一頁
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        self.page.lbl_topic.place(x=300, y=20)
        self.page.btn_next.place(x=780, y=480)
        # 左半邊 折線圖
        self.page.lbl_descripition.place(x=350, y=120)
        self.page.btn_chart.place(x=200, y=160)


    def gotoResult(self):
        self.page.destroy()
        FinalResultPage2(self.root)


class FinalResultPage2(object):
    def __init__(self, master=None):
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

        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 20, width = 30, font = f1)
        self.page.lbl_topic = tk.Label(self.page, text = "總結算", height = 2, width = 30, font = f1) 
        
        # 要接最後的獲利，還有抓歷史還行榜，要排名次
        self.page.lbl_descripition1 = tk.Label(self.page, text = "獲利：", height = 1, width = 40, font = f3)
        self.page.lbl_descripition2 = tk.Label(self.page, text = "名次：", height = 1, width = 40, font = f3)
        
        # 須依造分數給不一樣的敘述
        self.page.lbl_descripition3 = tk.Label(self.page, text = "恭喜您的餐廳榮獲米其林三星殊榮", height = 1, width = 40, font = f3)
        
        self.page.lbl_descripition4 = tk.Label(self.page, text = "感謝遊玩", height = 1, width = 40, font = f3)
        self.page.btn_tips = tk.Button(self.page, text = "高分秘訣", command = self.gotoHighscore, height = 2, width = 7, font = f2, bg = 'Lavender')
        self.page.btn_ranking = tk.Button(self.page, text = "排行榜", command = self.gotoRanking2, height = 2, width = 7, font = f2, bg = 'Lavender')
        self.page.btn_main = tk.Button(self.page, text = "回主畫面", command = self.page.quit, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        self.page.lbl_topic.grid(row = 0, column = 0, columnspan = 3)
        self.page.lbl_descripition1.grid(row = 1, column = 0, columnspan = 3)
        self.page.lbl_descripition2.grid(row = 2, column = 0, columnspan = 3)
        self.page.lbl_descripition3.grid(row = 3, column = 0, columnspan = 3)
        self.page.lbl_descripition4.grid(row = 4, column = 0, columnspan = 3)
        self.page.btn_tips.place(x = 200, y = 420)
        self.page.btn_ranking.place(x = 400, y = 420)
        self.page.btn_main.place(x = 600, y = 420)
        self.page.lbl_gridonly.grid(row = 5, column = 0, columnspan = 3, sticky = tk.S)

    def gotoHighscore(self):
        self.page.destroy()
        HighscorePage(self.root)

    def gotoRanking2(self):
        self.page.destroy()
        RankingPage2(self.root)


class RankingPage2(object):
    def __init__(self, master=None):
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

        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 20, width = 30, font = f1)
        self.page.lbl_topic = tk.Label(self.page, text = "排行榜", height = 2, width = 30, font = f1) 
        self.page.psystem = tk.Label(self.page, text = "第一名：", height = 2, width = 30, font = f3, bg = 'LightYellow')
        self.page.qsystem = tk.Label(self.page, text = "第二名：", height = 2, width = 30, font = f3, bg = 'OldLace')
        self.page.btn_main = tk.Button(self.page, text = "回總結算2", command = self.gotoResult2, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        self.page.lbl_topic.grid(row = 0, column = 0)
        self.page.psystem.grid(row = 1, column = 0)
        self.page.qsystem.grid(row = 2, column = 0)
        self.page.btn_main.place(x = 780, y = 480)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
    
    def gotoResult2(self):
        self.page.destroy()
        FinalResultPage2(root)


class HighscorePage(object):
    def __init__(self, master=None):
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

        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 20, width = 30, font = f1)
        self.page.lbl_topic = tk.Label(self.page, text = "高分秘訣", height = 2, width = 30, font = f1) 

        self.page.psystem = tk.Label(self.page,
        text = "P系統\n\n又稱「定期」存貨控制系統，以訂購周期和最高庫存量為控制基準，例：固定每兩天訂購生菜漢堡，訂到設定的最高庫存量40個，每次訂的數量因剩下的量而有不同。\n\n適合需求比較穩定、次要的原料",
        height = 12, width = 27, font = f3, bg = 'LightYellow', wraplength = 300)

        self.page.qsystem = tk.Label(self.page,
        text = "Q系統\n\n又稱「定量」存貨控制系統，以再次訂購點和固定量為控制基準。\n例：只要牛肉漢堡低於15個，就馬上訂購固定的量20個，可能一天訂好幾次，但量都固定為20。\n\n適合需求比較不穩定、主要的原料",
        height = 12, width = 27, font = f3, bg = 'OldLace', wraplength = 300)
        
        self.page.btn_main = tk.Button(self.page, text = "回總結算2", command = self.gotoResult2, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        self.page.lbl_topic.grid(row = 0, column = 0, columnspan = 4)
        self.page.psystem.grid(row = 1, column = 0, columnspan = 2)
        self.page.qsystem.grid(row = 1, column = 2, columnspan = 2)
        self.page.btn_main.place(x = 780, y = 480)
        self.page.lbl_gridonly.grid(row = 2, column = 0, columnspan = 4, sticky = tk.S)
    
    def gotoResult2(self):
        self.page.destroy()
        FinalResultPage2(root) 


# 最後跑程式的指令
root = Tk()
root.title('小程式')
StartPage(root)
root.mainloop()
print(user_name)
