from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import tkinter.font as tkFont
from PIL import ImageTk
import matplotlib.pyplot as plt
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
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (300, 500)) #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = '開始頁面: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='進入遊戲', command=self.gotoIntro).grid(row=3, stick=W, pady=10)
        Button(self.page, text='排行榜', command=self.gotoRanking1).grid(row=3, column=1, stick=E)

    def gotoIntro(self):
        self.page.destroy()
        IntroPage(self.root)
    
    def gotoRanking1(self):
        self.page.destroy()
        RankingPage1(self.root)


class RankingPage1(object):  # 排行榜(前)
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
        Label(self.page, text = '開始排行榜: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼3: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='回首頁', command=self.gotoStart).grid(row=3, stick=W, pady=10)
    
    def gotoStart(self):
        self.page.destroy()
        StartPage(self.root)


class IntroPage(object):  # 說明、輸入姓名
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (300, 500)) #設定視窗大小
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


class RulePage(object):  #營業說明
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
        Label(self.page, text = '營業說明: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='開始遊戲', command=self.gotoDay1).grid(row=3, stick=W, pady=10)

    def gotoDay1(self):
        self.page.destroy()
        Day1Page1(self.root)


class Day1Page1(object):  # Day 1 小知識的日子
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
        Label(self.page, text = 'day1小知識: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='選項 A', command=self.gotoCorrect).grid(row=3, stick=W, pady=10)
        Button(self.page, text='選項 B', command=self.gotoWrong).grid(row=3, column=1, stick=E)
        Button(self.page, text='行事曆', command=self.openCalendar).grid(row=0, column=1, stick=E)

    def gotoCorrect(self):
        self.page.destroy()
        CorrectPage(self.root)
        showinfo(title='小提示', message='小提示輸入處')
        
    def gotoWrong(self):
        self.page.destroy()
        WrongPage(self.root)
    
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')

class Day4Page1(object):  # Day 1 小知識的日子
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
        Label(self.page, text = 'day4小知識: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='選項 A', command=self.gotoCorrect).grid(row=3, stick=W, pady=10)
        Button(self.page, text='選項 B', command=self.gotoWrong).grid(row=3, column=1, stick=E)
        Button(self.page, text='行事曆', command=self.openCalendar).grid(row=0, column=1, stick=E)

    def gotoCorrect(self):
        self.page.destroy()
        CorrectPage(self.root)
        showinfo(title='小提示', message='小提示輸入處')
        
    def gotoWrong(self):
        self.page.destroy()
        WrongPage(self.root)
    
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')

class CorrectPage(object):  # Day 1 答對頁面
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
        Label(self.page, text = '恭喜答對: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='繼續遊戲', command=self.gotoDay1).grid(row=3, stick=W, pady=10)
        Button(self.page, text='行事曆', command=self.openCalendar).grid(row=0, column=1, stick=E)

    def gotoDay1(self):
        self.page.destroy()
        EverydayPage(self.root)
        
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')

class WrongPage(object):  # Day 1 答錯頁面
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
        Label(self.page, text = '答錯了: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='繼續遊戲', command=self.gotoDay1).grid(row=3, stick=W, pady=10)
        Button(self.page, text='行事曆', command=self.openCalendar).grid(row=0, column=1, stick=E)

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
        image = ImageTk.Image.open("C:\\Users\\formo\\Documents\\python files\\finalproject\\mytest\\S__85836045.png")
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
        self.root.geometry("900x600+200+30") #設定視窗大小
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
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = ("Day " + str(counts+1) + "訂貨:")).grid(row=0, column=0, stick=W)
        Label(self.page, text = '牛肉: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.beef).grid(row=1, column=1, stick=E)
        Label(self.page, text = '豬肉: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.pork).grid(row=2, column=1, stick=E)
        Label(self.page, text = '雞肉: ').grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.chicken).grid(row=3, column=1, stick=E)
        Label(self.page, text = '生菜: ').grid(row=4, stick=W, pady=10)
        Entry(self.page, textvariable=self.vege).grid(row=4, column=1, stick=E)
        Label(self.page, text = '生酮: ').grid(row=5, stick=W, pady=10)
        Entry(self.page, textvariable=self.keto).grid(row=5, column=1, stick=E)
        Button(self.page, text='試算', command=self.costCalculation).grid(row=6, stick=W, pady=10)
        Button(self.page, text='行事曆', command=self.openCalendar).grid(row=0, column=1, stick=E)
        if counts != 2 and counts < 6:
            Button(self.page, text='訂購', command=self.orderFinished).grid(row=6, column=1, stick=E)
        elif counts == 2:
            Button(self.page, text='訂購3', command=self.orderFinishedgoto4).grid(row=6, column=1, stick=E)

    def costCalculation(self):
        global material_price
        global order_fixed_cost
        order_list = []
        total_cost = 0
        beefnum = self.beef.get()
        order_list.append(beefnum)
        porknum = self.pork.get()
        order_list.append(porknum)
        chickennum = self.chicken.get()
        order_list.append(chickennum)
        vegenum = self.vege.get()
        order_list.append(vegenum)
        ketonum = self.keto.get()
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
            showinfo(title="成本計算",message=("總成本為 " + str(total_cost)))
        else:
            showinfo(title="錯誤", message="累了嗎?請輸入正確格式")

    def orderFinished(self):
        global stock_list
        global order_cost_list
        global counts
        order_list = []
        total_cost = 0
        beefnum = self.beef.get()
        order_list.append(beefnum)
        porknum = self.pork.get()
        order_list.append(porknum)
        chickennum = self.chicken.get()
        order_list.append(chickennum)
        vegenum = self.vege.get()
        order_list.append(vegenum)
        ketonum = self.keto.get()
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
        beefnum = self.beef.get()
        order_list.append(beefnum)
        porknum = self.pork.get()
        order_list.append(porknum)
        chickennum = self.chicken.get()
        order_list.append(chickennum)
        vegenum = self.vege.get()
        order_list.append(vegenum)
        ketonum = self.keto.get()
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

class FinalResultPage1(object):  # 總結算(折線圖)
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
        Label(self.page, text = '結算1: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼3: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='看評價', command=self.gotoResult).grid(row=3, column=1, stick=E)
        Button(self.page, text='看統計圖', command=self.plot_result).grid(row=3, stick=W, pady=10)

    def gotoResult(self):
        self.page.destroy()
        FinalResultPage2(root)
    
    def plot_result(self):
        global order_cost_list
        global day
        plt.figure(figsize=(10,5),dpi=100,linewidth = 2)
        plt.plot(day,order_cost_list,'s-',color = 'y', label="Day Order Cost")
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.xlabel("Day", fontsize=20, labelpad = 10)
        plt.ylabel("$", fontsize=20, labelpad = 10)
        plt.legend(loc = "best", fontsize=10)
        plt.show()

class FinalResultPage2(object):  # 總結算(總分、評價)、再玩一次、高分秘訣、離開
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (300, 500)) #設定視窗大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = '結算2: ').grid(row=1, stick=W, pady=10)
        Button(self.page, text='排行榜', command=self.gotoRanking2).grid(row=2, stick=W, pady=10)
        Button(self.page, text='高分秘訣', command=self.gotoHighscore).grid(row=3, stick=W, pady=10)
        Button(self.page, text='離開', command=self.page.quit).grid(row=3, column=1, stick=E)
    
    def gotoRanking2(self):
        self.page.destroy()
        RankingPage2(root)
        
    def gotoHighscore(self):
        self.page.destroy()
        HighscorePage(root)

class RankingPage2(object):  # 排行榜、可回總結算(2)、高分秘訣
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
        Label(self.page, text = '排行榜2: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼3: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='回總結算', command=self.gotoResult2).grid(row=3, stick=W, pady=10)
        Button(self.page, text='高分秘訣', command=self.gotoHighscore).grid(row=3, column=1, stick=E)  # 按了會消失= =

    def gotoResult2(self):
        self.page.destroy()
        FinalResultPage2(root)
        
    def gotoHighscore(self):
        self.page.destroy()
        HighscorePage(root)

class HighscorePage(object):  # 高分秘訣、可回總結算(2)
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
        Label(self.page, text = '高分秘訣: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密碼3: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='回總結算', command=self.gotoResult2).grid(row=3, stick=W, pady=10)
    def gotoResult2(self):
        self.page.destroy()
        FinalResultPage2(root)

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
StartPage(root)
root.mainloop()
print(user_name)

