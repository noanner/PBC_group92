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
        # RankingPage1(self.root)


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
                                           "也可以有適當的存貨之後請你依照這個標準進行材料訂購喔~", wraplength = 400,
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
        EverydayPage(self.root)

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


root = Tk()
root.title('小程式')
StartPage(root)
root.mainloop()
print(user_name)
