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
        Day1Page1(self.root)


root = Tk()
root.title('小程式')
StartPage(root)
root.mainloop()
print(user_name)
