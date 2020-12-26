import os
import random
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import matplotlib.pyplot as plt
from PIL import ImageTk

scenario = 0
# print(scenario)

'''
#########需求背景資訊#############
'''
# 經營背景-------------------------------------------------------------------
scen_list = ["您的餐廳開在著名的觀光景點附近，每天會有不同的大型旅行團造訪!",
             "您的餐廳舉辦了為期一周的活動，希望可以推廣並且慶祝各式各樣的節日!",
             "這一周的天氣變化很大，好在你可以先看天氣預報，再決定要備多少料!",
             "這是禍不單行，但也好事成雙的一周，您的餐廳遇到很多突發狀況，您要如何解決呢？"]
scen_dict = dict()
for i in range(4):
    scen_dict[i + 1] = scen_list[i]
# print(scen_dict.get(scenario))

# 行事曆---------------------------------------------------------------------
# [第0天, 第1天, 第2天, 第3天, 第4天, 第5天, 第6天]
cal_list = [["固定需求", "印度教", "高中畢旅", "美國人", "健身俱樂部", "阿拉伯人", "佛教徒"],
            ["固定需求", "33五花肉日", "感恩節", "中秋節", "全球素食日", "兒童節", "情人節"],
            ["固定需求", "下豪大雨", "出炎熱的大太陽", "風和日麗", "寒流來襲", "颱風天", "無風無雨"],
            ["固定需求", "大樂透開獎", "店門口道路施工", "對面漢堡王休息一天", "新聞不實報導", "拿到安全衛生許可", "平凡的一天"]]
cal_dict = dict()
for i in range(4):
    cal_dict[i + 1] = cal_list[i]
# print(cal_dict.get(scenario))

# 小提示----------------------------------------------------------------------
# [第1天的提示, 第4天的提示]
hint_list = [["印度教徒不吃牛肉、豬肉，特愛雞肉，如果沒有咖哩的話，他們寧願少吃點有肉的漢堡",
              "健身的巨巨們喜歡選用蛋白質較高的牛肉、雞肉，若是有生酮這樣碳水低的選擇，他們再愛也不過了，通常可以吃兩份以上"],
             ["韓國人熱愛豬五花肉，甚至將3月3日正式訂為「五花肉日」", "全球素食日是一個完全不能吃肉的節日，連製作的食材都不會有任何的肉"],
             ["因為午後的豪大雨，導致顧客出門意願降低，只想待在家叫Foodpanda或Ubereats，全品項銷量約減少25%",
              "寒流來襲，大口大口咬下漢堡，身體有熱量去禦寒，大家喜歡到漢堡店坐在店裡享用，全品項銷售量約增加25%"],
             ["今日為大樂透開獎，得主就住在餐廳樓上，平常他最愛吃的就是漢堡，今天他決定拿獎金買下60個至尊和牛堡請台北車站的流浪漢吃",
              "新聞報導指控您的餐廳餐點不衛生，漢堡都是用組合肉，生菜也不新鮮，麵包更是都發霉了，讓業績只剩4成"]]
hint_dict = dict()
for i in range(4):
    hint_dict[i + 1] = hint_list[i]
# print(hint_dict.get(scenario))

# 每日需求量----------------------------------------------------------------------
demand_list1 = [[20, 20, 20, 20, 20], [3, 5, 52, 26, 2], [31, 28, 27, 8, 11], [30, 25, 28, 5, 15], [21, 6, 25, 12, 65],
                [25, 3, 30, 28, 18], [4, 6, 8, 62, 10]]
demand_list2 = [[20, 20, 20, 20, 20], [18, 43, 19, 15, 12], [21, 18, 31, 17, 19], [23, 25, 28, 19, 12],
                [0, 0, 0, 110, 0], [28, 26, 27, 8, 13], [22, 23, 21, 19, 18]]
demand_list3 = [[20, 20, 20, 20, 20], [16, 16, 17, 15, 15], [22, 23, 23, 19, 21], [26, 28, 27, 23, 24],
                [24, 23, 26, 24, 25], [15, 14, 16, 13, 16], [21, 20, 22, 20, 21]]
demand_list4 = [[20, 20, 20, 20, 20], [81, 21, 20, 19, 18], [16, 13, 15, 15, 16], [31, 28, 29, 27, 29], [8, 7, 7, 8, 6],
                [22, 23, 21, 21, 22], [21, 21, 21, 21, 21]]

demand_dict = dict()
demand_dict[1] = demand_list1
demand_dict[2] = demand_list2
demand_dict[3] = demand_list3
demand_dict[4] = demand_list4
# print(demand_dict.get(scenario))

# 不知道哪裡有用到?----------------------------------------------------------------
day = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7"]

# 預設資訊-------------------------------------------------------------------------
counts = 0
correct = 0
count_list = []
user_name = ""
material_price = [10, 9, 9, 6, 16]  # 原料價格
price_list = [20, 18, 18, 12, 32]
order_fixed_cost = 50
stock_cost = 2
stock_list = [0, 0, 0, 0, 0]  # 預設存貨
order_list = [0, 0, 0, 0, 0]
order_cost_list = []  # 畫圖
profit_list = []  # 畫圖
accumulated_profit = 0  # 總分
accumulated_profit_list = []  # 畫圖
stock_cost_list = []  # 畫圖
revenue_list = []  # 畫圖

# 小知識題庫1-------------------------------------------------------------------------
ques_list1 = [[2,
               "First in, First out (FIFO)是指先進的貨品先出貨，Last in, First out (LIFO)是讓後進的貨品先出貨。如果你賣的是市場價格呈上升趨勢的商品如貴金屬，或是沒有特定保存期限者如煉油業，適合哪種存貨管理方法?",
               "FIFO", "LIFO"],
              [3,
               "安全庫存：安全庫存又稱保險庫存，是指為了防止不確定性因素的保險庫存量。小明開了一間漢堡店，平常總是備100個漢堡的庫存供日常販售，地下室裡另外放了25個漢堡的庫存以備不時之需。請問漢堡安全庫存數量為？",
               "100", "25"],
              [3,
               "訂購週期：訂購週期為連續訂購之間的時間間隔。小明開了一間漢堡店，漢堡需要用到麵包、生菜及肉排。麵包每3天需要訂貨一次，生菜與肉排則是每2天訂貨一次。請問生菜的訂購週期為？",
               "3天", "2天"],
              [3,
               "訂購點：當商品庫存低至特定水位時，再次訂購商品的時間點。小明開了一間漢堡店，漢堡需要用到麵包、生菜及肉排。每天開店前都要準備300個麵包，只要麵包庫存少於50個，小明就會擔心缺貨。請問麵包的訂購點為？",
               "300個", "50個"],
              [2,
               "最大存貨量：所能存放的最大物品數量。小明開了一間漢堡店，漢堡店的食物儲藏室最多可以裝500個漢堡的材料，但是小明希望留一條走道方便拿東西，所以規定最多只能放450份漢堡食材。請問漢堡食材的最大庫存量為？",
               "450個", "500個"],
              [3,
               "最小訂購量：每筆訂單的最低起訂量。小明開了一間漢堡店，每天開店時會準備5公斤的生菜，但賣生菜的老闆說每次只送5公斤連付油錢都不夠，要買8公斤以上才送貨。請問生菜的最小訂購量為？",
               "4公斤", "8公斤"]]
ques_dict1 = dict()
for i in range(len(ques_list1)):
    ques_dict1[i + 1] = ques_list1[i]

# 小知識題庫2-------------------------------------------------------------------------
ques_list2 = [[3,
               "期末庫存：期末庫存=期初庫存+期間進貨-期間需求。小明開了一間漢堡店，開店前有12公斤麵包、10公斤生菜、8公斤肉排。今天進貨7公斤生菜、4公斤肉排，消耗4公斤麵包、6公斤生菜、5公斤肉排。請問關店後肉排的期末庫存為？",
               "5公斤", "7公斤"],
              [2,
               "訂單達成率：給定時間內實際完成訂單的百分比。小明開了一間漢堡店，今天午餐時段售出100個漢堡、晚餐時段售出300個漢堡，但實際上因為缺貨還有100個訂單沒有被滿足。請問漢堡店今天的訂單達成率為？",
               "80%", "90%"],
              [3,
               "前置時間：指從買方開始下單訂購到賣方交貨所間隔的時間。小明開了一間漢堡店，顧客下單後需要經過以下程序：確認訂單(10秒)→廚房製作漢堡(320秒)→出餐(30秒)。請問顧客訂購一個漢堡的前置時間為？",
               "3分鐘", "6分鐘"],
              [2,
               "毛利率：毛利率計算的是產品的成本以及收入的關係，毛利率計算公式＝(銷售收入－銷售成本) / 銷售收入 x 100%。小明開了一間漢堡店，一個漢堡售價60元，已知材料成本是45元。請問漢堡的毛利率為？",
               "75%", "85%"],
              [3,
               "營收：又稱為營業額，是指企業在某段時間內，經由商業行為取得的收入。小明開了一間漢堡店，販售雞塊、沙拉與漢堡，售價分別為40元、30元、60元。已知今日雞塊、沙拉與漢堡分別售出10份、20份、15份。請問今天的營收為？",
               "1,500元", "1,900元"],
              [2,
               "固定成本：不會隨著營業收入變動而變動的成本，包括店面租金、機械設備租金、人事費等等。小明開了一間漢堡店，店裡聘僱了一位正職月薪2,000元，機器租金每年12,000元、店面租金每月5,000元。請問每個月的固定成本為？",
               "8,000元", "19,000元"]]
ques_dict2 = dict()
for i in range(len(ques_list1)):
    ques_dict2[i + 1] = ques_list2[i]



'''
#########每個頁面Class#############
'''
class StartPage(object):  # 開始畫面
    def __init__(self, master = None):
        # tk.Frame.__init__(self)
        # self.grid()
        # self.createWidgets()
        global scenario
        global counts
        global stock_list
        global order_list
        global stock_cost_list
        global order_cost_list
        global profit_list
        global accumulated_profit
        global accumulated_profit_list
        global revenue_list
        scenario = random.randint(1, 4)
        counts = 0
        stock_list = [0, 0, 0, 0, 0]  # 預設存貨
        order_list = [0, 0, 0, 0, 0]
        order_cost_list = []  # 畫圖
        stock_cost_list = []
        profit_list = []  # 畫圖
        revenue_list = []  # 畫圖
        accumulated_profit = 0  # 總分
        accumulated_profit_list = []  # 畫圖
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame # 新增
        self.page.pack()  # 新增

        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)  # 製造一個空的grid在底下
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)

        # 背景圖
        global bg_img
        image = ImageTk.Image.open("startpage_bg.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 內容
        # self.page.lbl_topic = tk.Label(self.page, text = "PBC讓你睡不堡  餐廳遊戲", height = 2, width = 23, font = f1,
                                       # bg = 'black', fg = 'white')
        self.page.btn_enter = tk.Button(self.page, text = "進入遊戲", command = self.gotoIntro, height = 2, width = 10,
                                        font = f2, bg = 'black', fg = 'white')
        self.page.btn_rank = tk.Button(self.page, text = "成就榜", command = self.gotoRanking1, height = 2, width = 10,
                                       font = f2, bg = 'black', fg = 'white')

        # self.page.lbl_topic.place(x = 150, y = 150)
        self.page.btn_enter.place(x = 170, y = 400)
        self.page.btn_rank.place(x = 350, y = 400)

    def gotoIntro(self):
        self.page.destroy()
        IntroPage(self.root)

    def gotoRanking1(self):
        self.page.destroy()
        RankingPage1(self.root)


class RankingPage1(object):  # 現在是成就榜(前)
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame # 新增
        self.page.pack()  # 新增

        f1 = tkFont.Font(size = 30, family = "微軟正黑體", weight = "bold")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        global ranking_list
        image = ImageTk.Image.open("成就榜_bg1.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 內容
        # self.page.lbl_topic = tk.Label(self.page, text = "成就榜", height = 2, width = 10, font = f1, bg = 'Black',
                                       # fg = 'White')

        self.page.btn_main = tk.Button(self.page, text = "回主畫面", command = self.gotoStartPage, height = 2, width = 9,
                                       font = f2, bg = 'Black', fg = 'White')

        # self.page.lbl_topic.place(x = 75, y = 100)
        self.page.btn_main.place(x = 730, y = 490)

    def gotoStartPage(self):
        self.page.destroy()
        StartPage(root)


class IntroPage(object):  # 輸入姓名頁面

    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry("900x600+200+30")  # 設定視窗大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.username = StringVar()
        self.page.pack()

        f1 = tkFont.Font(size = 18, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        image = ImageTk.Image.open("輸入名字_bg.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        self.button2 = tk.Button(self.page, text = "開始遊戲", font = f2, command = self.gotoRule, height = 2, width = 10,
                                 bg = '#FFCC22', fg = 'White')
        self.button2.place(x = 720, y = 490)

        # 輸入框
        self.button1 = tk.Label(self.page, text = "替你的餐廳取個會賺大錢的名字：", font = f1, bg = 'black', fg = 'White')
        self.button1.place(relx = 0.1, rely = 0.45, relheight = 0.1, relwidth = 0.52, anchor = 'nw')
        self.entry = tk.Entry(self.page, textvariable = self.username, font = f1)
        self.entry.place(relx = 0.61, rely = 0.45, relwidth = 0.28, relheight = 0.1)

    def gotoRule(self):
        global user_name
        name = self.username.get()
        user_name = name
        if 0 < len(name) <= 8:
            self.page.destroy()
            RulePage(self.root)
        if len(name) > 8:
            showinfo(title = '錯誤', message = '餐廳名稱太長囉！')
        if len(name) == 0:
            showinfo(title = '錯誤', message = '你的餐廳還沒命名喔！')


class RulePage(object):  # 營業說明
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry("900x600+200+30")  # 設定視窗大小
        self.username = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()

        f1 = tkFont.Font(size = 28, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        f4 = tkFont.Font(size = 10, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        global user_name
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        self.topic = tk.Label(self.page, text = ("Hello, " + user_name + "的老闆"), font = f1, bg = '#f9f7f1',
                              fg = '#666666', height = 2, width = 25)
        self.topic.place(x = 50, y = 40)

        # 左半邊 經營背景   
        self.page.intro_topic = tk.Label(self.page, text = "遊戲說明", height = 2, width = 8, font = f3, bg = '#f9f7f1',
                                         fg = '#666666')
        self.page.intro_topic.place(x = 120, y = 148)
        
        self.page.intro = tk.Label(self.page, text = "· 5種漢堡，每種平均賣20個\n· 根據每天情境有所增減"
                                                     "\n· 小知識問答答對有提示！\n· 記得看右邊行事曆！！",
                                   font = f4, borderwidth = 20, wraplength = 280, justify = 'left', bg = 'LemonChiffon',
                                   fg = '#666666')
        self.page.intro.place(x = 120, y = 193)

        self.page.bg_topic = tk.Label(self.page, text = "經營背景", height = 2, width = 8, font = f3, bg = '#f9f7f1',
                                      fg = '#666666')
        self.page.bg_topic.place(x = 120, y = 325)
        self.page.lbl_bg = tk.Label(self.page, text = scen_dict[scenario], font = f4, borderwidth = 20,
                                    wraplength = 280, justify = 'left', bg = 'LemonChiffon', fg = '#666666')
        self.page.lbl_bg.place(x = 120, y = 370)

        # 右半邊 行事曆表格
        tree_item = ttk.Treeview(self.page, selectmode = "extended", columns = ("天數", "活動"))  # 表格
        tree_item["columns"] = ("活動")
        tree_item.column("#0", minwidth = 0, width = 100, anchor = 'center')
        tree_item.column("活動", minwidth = 0, width = 200, anchor = 'center')  # 表示列,不顯示

        tree_item.heading("#0", text = "天數")
        tree_item.heading("活動", text = "活動")  # 顯示表頭

        tree_item.insert("", 1, text = "Day1", values = cal_dict[scenario][0])  # 插入資料
        tree_item.insert("", 2, text = "Day2", values = cal_dict[scenario][1])
        tree_item.insert("", 3, text = "Day3", values = cal_dict[scenario][2])
        tree_item.insert("", 4, text = "Day4", values = cal_dict[scenario][3])
        tree_item.insert("", 5, text = "Day5", values = cal_dict[scenario][4])
        tree_item.insert("", 6, text = "Day6", values = cal_dict[scenario][5])
        tree_item.insert("", 7, text = "Day7", values = cal_dict[scenario][6])

        style = ttk.Style()
        style.configure("Treeview.Heading", font = ("微軟正黑體", 10))
        style.configure("Treeview", rowheight = 38, font = ("微軟正黑體", 10))
        tree_item.place(x = 480, y = 160, height = 300)

        # 開始遊戲
        if counts == 0:
            self.page.button = tk.Button(self.page, text = "開始遊戲", font = f3, command = self.gotoDay1, height = 2,
                                        width = 10, bg = '#FFCC22', fg = 'White')       
        else:
            self.page.button = tk.Button(self.page, text = "開始遊戲", font = f3, command = self.gotoEveryday, height = 2,
                                        width = 10, bg = '#FFCC22', fg = 'White')
        self.page.button.place(x = 720, y = 490)

    def gotoDay1(self):
        self.page.destroy()
        FirstdayStockPage(self.root)

    def gotoEveryday(self):
        self.page.destroy()
        EverydayPage(self.root)


class KnowledgePage(object):  # Day 1 小知識的日子
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame
        self.page.pack()

        f1 = tkFont.Font(size = 28, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        global counts
        image = ImageTk.Image.open("小知識_bg.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 元件內容
        global know_num
        know_num = random.randint(1, 6)
        if counts == 0:
            know_content = (ques_dict1.get(know_num))[1]
        else:
            know_content = (ques_dict2.get(know_num))[1]
        lbl_day = tk.Label(self.page, text = ("Day" + str(counts + 2) + "需求提示"), height = 1, width = 12, font = f1,
                           bg = 'black', fg = 'white')
        lbl_hint = tk.Label(self.page, text = ("這裡有一道小知識問答，\n答對了就能獲得明天的需求提示噢！"), height = 2, width = 15,
                            font = f2, bg = 'black', fg = 'white')
        lbl_know = tk.Label(self.page, text = know_content, font = f3, wraplength = 350,
                            justify = 'left', bg = 'LemonChiffon', fg = '#666666')
        if counts == 0:
            btn_optA = tk.Button(self.page, text = (ques_dict1.get(know_num))[2], command = self.gotoVerify1, width = 7,
                                 height = 2, font = f3, bg = '#FFCC22',
                                 fg = 'White')
            btn_optB = tk.Button(self.page, text = (ques_dict1.get(know_num))[3], command = self.gotoVerify2, width = 7,
                                 height = 2, font = f3, bg = '#FFCC22',
                                 fg = 'White')
        else:
            btn_optA = tk.Button(self.page, text = (ques_dict2.get(know_num))[2], command = self.gotoVerify1, width = 7,
                                 height = 2, font = f3, bg = '#FFCC22',
                                 fg = 'White')
            btn_optB = tk.Button(self.page, text = (ques_dict2.get(know_num))[3], command = self.gotoVerify2, width = 7,
                                 height = 2, font = f3, bg = '#FFCC22',
                                 fg = 'White')
        # btn_calendar = tk.Button(self.page, text = "行事曆", command = self.openCalendar, width = 7, height = 2, font = f2,
        # bg = '#666666', fg = 'White')

        # 元件位置
        lbl_day.place(x = 50, y = 50)
        lbl_hint.place(width = 400, height = 80, x = 60, y = 130)
        lbl_know.place(relx = 0.05, rely = 0.38, width = 400, height = 200)
        btn_optA.place(relx = 0.12, rely = 0.8)
        btn_optB.place(relx = 0.30, rely = 0.8)
        # btn_calendar.place(x = 720, y = 70)

    def gotoVerify1(self):
        self.page.destroy()
        choose = 2
        if counts == 0:
            if (ques_dict1.get(know_num))[0] == choose:
                CorrectPage(self.root)
            else:
                WrongPage(self.root)
        else:
            if (ques_dict2.get(know_num))[0] == choose:
                CorrectPage(self.root)
            else:
                WrongPage(self.root)

    def gotoVerify2(self):
        self.page.destroy()
        choose = 3
        if counts == 0:
            if (ques_dict1.get(know_num))[0] == choose:
                CorrectPage(self.root)
            else:
                WrongPage(self.root)
        else:
            if (ques_dict2.get(know_num))[0] == choose:
                CorrectPage(self.root)
            else:
                WrongPage(self.root)


class CorrectPage(object):  # Day 1 答對頁面
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame
        self.page.pack()

        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        global correct
        correct = 1
        image_name = "答對_Day" + str(counts + 2) + "_bg.jpg"
        image = ImageTk.Image.open(image_name)
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        if counts == 0:
            hint = hint_dict[scenario][0]
        else:
            hint = hint_dict[scenario][1]
        self.page.lbl_hint = tk.Label(self.page, text = hint, font = f3, borderwidth = 15, wraplength = 320,
                                      justify = 'left', bg = 'LemonChiffon', fg = '#666666')
        self.page.lbl_hint.place(x = 460, y = 300)

        # 下一頁按鈕
        Button(self.page, text = '繼續遊戲', width = 10, height = 2, font = f3, bg = 'black', fg = 'White',
               command = self.gotoStockorder).place(x = 660, y = 445)

    def gotoStockorder(self):
        self.page.destroy()
        EverydayStockPage(self.root)


class WrongPage(object):  # Day 1 答錯頁面
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame
        self.page.pack()

        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        global correct
        correct = 0
        image = ImageTk.Image.open("答錯_bg.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 下一頁按鈕
        Button(self.page, text = '繼續遊戲', width = 10, height = 2, font = f3, bg = 'black', fg = 'White',
               command = self.gotoStockorder).place(x = 150, y = 440)

    def gotoStockorder(self):
        self.page.destroy()
        EverydayStockPage(self.root)


class EverydayPage(object):  # 每日漢堡製作畫面

    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry("900x600+200+30")  # 設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame
        self.page.pack()
        f1 = tkFont.Font(size = 28, family = "微軟正黑體")
        f2 = tkFont.Font(size = 18, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        f4 = tkFont.Font(size = 20, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        image = ImageTk.Image.open("day_background.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 顯示Day 1
        self.page.lbl_topic = tk.Label(self.page, text = ("Day" + str(counts + 1)), height = 1, width = 7, font = f1,
                                       bg = '#f9f7f1', fg = '#666666')
        self.page.lbl_topic.place(x = 365, y = 160)

        # 顯示 餐廳開始營業囉，點選下一頁查看你今天的營業成果吧~
        self.page.lbl_description1 = tk.Label(self.page, text = "餐廳開始營業囉，", height = 1, width = 15, bg = '#f9f7f1', fg = "#666666", font = f2)
        self.page.lbl_description1.place(x = 330, y = 240)
        self.page.lbl_description2 = tk.Label(self.page, text = "點選繼續遊戲查看你今天的營業成果吧~", height = 1, width = 30, bg = '#f9f7f1', fg = "#666666", font = f2)
        self.page.lbl_description2.place(x = 180, y = 290)

        # 下一頁按鈕
        Button(self.page, text = '繼續遊戲', width = 10, height = 2, font = f3, bg = '#FFCC22', fg = 'White',
               command = self.gotoDayResult).place(x = 395, y = 400)

    def gotoDayResult(self):
        self.page.destroy()
        EverydayResultPage(root)


class EverydayResultPage(object):  # 每日結算畫面
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry("900x600+200+30")  # 設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame
        self.page.pack()
        f1 = tkFont.Font(size = 28, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 顯示 header
        self.page.lbl_topic = tk.Label(self.page, text = ("Day" + str(counts + 1)), height = 2, width = 7, font = f1,
                                       bg = '#f9f7f1', fg = '#666666')
        self.page.lbl_topic.place(x = 50, y = 40)

        global user_name

        self.page.lbl_description = tk.Label(self.page, text = ("辛苦了~" + user_name + "的老闆，下面是你今天營業的成果~~"), height = 2,
                                             width = 50, font = f3,
                                             bg = '#f9f7f1')
        self.page.lbl_description.place(x = 214, y = 72)

        if counts == 0 or counts == 3:
            # 下一頁按鈕
            Button(self.page, text = '知識問答', width = 10, height = 2, font = f3, bg = '#FFCC22', fg = 'White',
                   command = self.gotoKnowledge).place(x = 720, y = 490)

        elif counts == 6:
            # 下一頁按鈕
            Button(self.page, text = '繼續遊戲', width = 10, height = 2, font = f3, bg = '#FFCC22', fg = 'White',
                   command = self.gotoResult).place(x = 720, y = 490)
        else:
            Button(self.page, text = '繼續遊戲', width = 10, height = 2, font = f3, bg = '#FFCC22', fg = 'White',
                   command = self.gotoStockorder).place(x = 720, y = 490)

        global stock_list
        global price_list
        # 品項表格
        columns = ("至尊和牛堡", "豬肉滿福堡", "嫩煎雞腿堡", "好多蔬食堡", "健康生酮堡")
        self.page.tree_item = ttk.Treeview(self.page, column = columns)  # 表格

        self.page.tree_item.column("#0", minwidth = 0, width = 90, anchor = "center")
        self.page.tree_item.column("至尊和牛堡", width = 90, anchor = "center")  # 表示列,不顯示
        self.page.tree_item.column("豬肉滿福堡", width = 90, anchor = "center")
        self.page.tree_item.column("嫩煎雞腿堡", width = 90, anchor = "center")
        self.page.tree_item.column("好多蔬食堡", width = 90, anchor = "center")
        self.page.tree_item.column("健康生酮堡", width = 90, anchor = "center")

        self.page.tree_item.heading("#0", text = "品項")  # 顯示錶頭
        self.page.tree_item.heading("至尊和牛堡", text = "至尊和牛堡")
        self.page.tree_item.heading("豬肉滿福堡", text = "豬肉滿福堡")
        self.page.tree_item.heading("嫩煎雞腿堡", text = "嫩煎雞腿堡")
        self.page.tree_item.heading("好多蔬食堡", text = "好多蔬食堡")
        self.page.tree_item.heading("健康生酮堡", text = "健康生酮堡")

        stock = stock_list
        demand = demand_dict.get(scenario)[counts]
        sold = []
        for i in range(len(stock)):
            a = min(stock[i], demand[i])
            sold.append(a)
        revenue = []
        total_revenue = 0
        for i in range(len(sold)):
            b = sold[i] * price_list[i]
            revenue.append(b)
            total_revenue += b
        
        revenue_list.append(total_revenue)

        pct = []
        for i in range(len(sold)):
            if stock[i] < demand[i]:
                pct.append("缺貨")
            else:
                pct.append(" ")

        self.page.tree_item.insert("", 0, text = "庫存",
                                   values = (stock[0], stock[1], stock[2], stock[3], stock[4]))  # 插入資料，
        self.page.tree_item.insert("", 1, text = "需求量",
                                   values = (demand[0], demand[1], demand[2], demand[3], demand[4]))
        self.page.tree_item.insert("", 2, text = "賣出數量", values = (sold[0], sold[1], sold[2], sold[3], sold[4]))
        self.page.tree_item.insert("", 3, text = "營業額",
                                   values = (revenue[0], revenue[1], revenue[2], revenue[3], revenue[4]))

        self.page.tree_item.insert("", 4, text = "缺貨提醒", values = (pct[0], pct[1], pct[2], pct[3], pct[4]))

        style = ttk.Style()
        style.configure("Treeview.Heading", font = ("微軟正黑體", 9))
        style.configure("Treeview", rowheight = 50, font = ("微軟正黑體", 9))

        self.page.tree_item.place(x = 80, y = 160, height = 280)

        # 金額表格
        global order_list
        global material_price
        global order_fixed_cost
        global stock_cost
        global accumulated_profit
        global accumulated_profit_list
        global profit_list
        columns = ("金額")
        self.page.tree_amount = ttk.Treeview(self.page, column = columns)  # 表格

        self.page.tree_amount.column("#0", minwidth = 0, width = 90, anchor = "center")
        self.page.tree_amount.column("金額", width = 100, anchor = "center")  # 表示列,不顯示

        self.page.tree_amount.heading("#0", text = "品項")
        self.page.tree_amount.heading("金額", text = "金額")  # 顯示錶頭

        mate_cost = []
        material_total_cost = 0
        material_fixed_cost = 0
        stock_day_cost = 0
        for i in range(len(order_list)):
            material_total_cost += int(order_list[i]) * material_price[i]
            if int(order_list[i]) != 0:
                material_fixed_cost += order_fixed_cost
        for i in range(len(stock_list)):
            stock_day_cost += (stock_list[i] - sold[i]) * stock_cost
        stock_cost_list.append(stock_day_cost)
        day_profit = total_revenue - material_total_cost - material_fixed_cost - stock_day_cost
        profit_list.append(day_profit)
        accumulated_profit += day_profit
        accumulated_profit_list.append(accumulated_profit)
        self.page.tree_amount.insert("", 0, text = "今日收益", values = (total_revenue))  # 插入資料，
        self.page.tree_amount.insert("", 1, text = "原料成本", values = (material_total_cost))
        self.page.tree_amount.insert("", 2, text = "進貨成本", values = (material_fixed_cost))
        self.page.tree_amount.insert("", 3, text = "存貨成本", values = (stock_day_cost))
        self.page.tree_amount.insert("", 4, text = "本日淨利", values = (day_profit))
        self.page.tree_amount.place(x = 630, y = 160, height = 280)
        for i in range(len(stock_list)):
            stock_list[i] = stock_list[i] - sold[i]

        # 顯示累積淨利
        accumulated_profit_str = ("總淨利：$" + str(accumulated_profit))
        if len(accumulated_profit_str) > 15:
            accumulated_profit_str = accumulated_profit_str[0:12]
        self.page.lbl_topic = tk.Label(self.page, text = accumulated_profit_str, height = 2, width = 15, font = f3,
                                       fg = '#666666', bg = 'LemonChiffon')
        self.page.lbl_topic.place(x = 490, y = 497)

    def gotoStockorder(self):
        self.page.destroy()
        EverydayStockPage(root)

    def gotoResult(self):
        self.page.destroy()
        FinalResultPage1(root)

    def gotoKnowledge(self):
        self.page.destroy()
        KnowledgePage(root)


class FirstdayStockPage(object):  # Day1 訂貨畫面 (教學訂購)

    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小

        self.beef = StringVar()
        self.pork = StringVar()
        self.chicken = StringVar()
        self.vege = StringVar()
        self.keto = StringVar()

        self.createPage()

    def createPage(self):
        global counts
        self.page = Frame(self.root)  # 建立Frame
        self.page.pack()

        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        f4 = tkFont.Font(size = 10, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        img_name = "scenario_" + str(scenario) + "_day_" + str(counts + 1) + ".jpg"  # scenario_1_day_1
        image = ImageTk.Image.open(img_name)
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 標題、敘述、行事曆按鈕
        self.page.lbl_topic = tk.Label(self.page, text = ("經驗老道的前輩建議你Day1各品項都訂25個，\n"
                                        "也可以按\"總價試算\"看看需要花多少錢唷!"), height = 2, width = 40, font = f2,
                                       bg = '#f9f7f1', fg = '#666666')
        self.page.lbl_fixcost = tk.Label(self.page, text = " 各品項固定成本:$50元\n每單位存貨成本:$2元\n沒有要訂購也要輸入0唷!", height = 4, width = 22, font = f3,
                                         bg = 'LemonChiffon')
        self.page.lbl_cost = tk.Button(self.page, text = "總價試算", command = self.costCalculation, height = 2, width = 10,
                                       font = f3, bg = 'Lavender')
        
        self.page.lbl_topic.place(x = 60, y = 60)
        self.page.lbl_fixcost.place(x = 220, y = 450)
        self.page.lbl_cost.place(x = 511, y = 490)
        
        if counts != 2 and counts < 6:
            # 訂購按鈕
            Button(self.page, text = '訂購!', width = 10, height = 2, font = f3, bg = '#FFCC22', fg = 'White',
                   command = self.orderFinished).place(x = 720, y = 490)
        elif counts == 2:
            # 訂購按鈕
            Button(self.page, text = '訂購!', width = 10, height = 2, font = f3, bg = '#FFCC22', fg = 'White',
                   command = self.orderFinished).place(x = 720, y = 490)
        # -----------------------------------------------------------------------------------------------------------

        # 品項表格
        columns = ("訂購單價", "售價", "剩餘庫存", "訂購數量")
        self.page.tree_item = ttk.Treeview(self.page, column = columns)  # 表格

        self.page.tree_item.column("#0", minwidth = 0, width = 110, anchor = "center")
        self.page.tree_item.column("訂購單價", width = 95, anchor = "center")
        self.page.tree_item.column("售價", width = 95, anchor = "center")
        self.page.tree_item.column("剩餘庫存", width = 95, anchor = "center")
        self.page.tree_item.column("訂購數量", width = 110, anchor = "center")

        self.page.tree_item.heading("#0", text = "食材")
        self.page.tree_item.heading("訂購單價", text = "訂購單價")  # 顯示表頭
        self.page.tree_item.heading("售價", text = "售價")
        self.page.tree_item.heading("剩餘庫存", text = "剩餘庫存")
        self.page.tree_item.heading("訂購數量", text = "訂購數量")

        global stock_list
        global price_list
        global material_price
        self.page.tree_item.insert("", 0, text = "至尊和牛堡", values = (material_price[0], price_list[0], 0, 25))  # 插入資料
        self.page.tree_item.insert("", 1, text = "豬肉滿福堡", values = (material_price[1], price_list[1], 0, 25))
        self.page.tree_item.insert("", 2, text = "嫩煎雞腿堡", values = (material_price[2], price_list[2], 0, 25))
        self.page.tree_item.insert("", 3, text = "好多蔬食堡", values = (material_price[3], price_list[3], 0, 25))
        self.page.tree_item.insert("", 4, text = "健康生酮堡", values = (material_price[4], price_list[4], 0, 25))

        style = ttk.Style()
        style.configure("Treeview.Heading", font = ("微軟正黑體", 10))
        style.configure("Treeview", rowheight = 50, font = ("微軟正黑體", 10))
        self.page.tree_item.place(x = 85, y = 150, height = 276)
        
    def costCalculation(self):
        showinfo(title = "成本計算", message = ("總成本為 $1500"))

    def orderFinished(self):
        global stock_list
        global order_cost_list
        global counts
        global order_list
        total_cost = 0
        order_list = [25,25,25,25,25]

        for i in range(len(order_list)):
            stock_list[i] += int(order_list[i])
            total_cost += order_fixed_cost
            total_cost += int(order_list[i]) * material_price[i]     
        order_cost_list.append(total_cost)
        self.page.destroy()
        EverydayPage(root)


class EverydayStockPage(object):  # Day2~Day7 訂貨畫面 (玩家自行訂購)

    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小

        self.beef = StringVar()
        self.pork = StringVar()
        self.chicken = StringVar()
        self.vege = StringVar()
        self.keto = StringVar()

        self.createPage()

    def createPage(self):
        global counts
        self.page = Frame(self.root)  # 建立Frame
        self.page.pack()

        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        f4 = tkFont.Font(size = 10, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        img_name = "scenario_" + str(scenario) + "_day_" + str(counts + 2) + ".jpg"  # scenario_1_day_1
        image = ImageTk.Image.open(img_name)
        # image = ImageTk.Image.open('scenario_1_day_1.jpg')
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # row0 標題、敘述、行事曆按鈕
        self.page.lbl_topic = tk.Label(self.page, text = ("請根據目前的剩餘庫存，決定Day" + str(counts + 2) +"要訂多少貨!"), height = 2, width = 40, font = f2,
                                       bg = '#f9f7f1', fg = '#666666')

        # row7 訂貨固定成本、目前訂購總價、訂購按鈕
        self.page.lbl_fixcost = tk.Label(self.page, text = " 各品項固定成本:$50元\n每單位存貨成本:$2元\n沒有要訂購也要輸入0唷!", height = 4, width = 22, font = f3,
                                         bg = 'LemonChiffon')
        self.page.lbl_cost = tk.Button(self.page, text = "總價試算", command = self.costCalculation, height = 2, width = 10,
                                       font = f3, bg = 'Lavender')
        if correct == 1 and counts == 0:
            self.page.lbl_hint = tk.Button(self.page, text = '小提示', width = 7, height = 2, font = f3, bg = '#666666', fg = 'White',
                                            command = self.openHint1).place(x = 720, y = 70)
        elif correct == 1 and counts == 3:
            self.page.lbl_hint = tk.Button(self.page, text = '小提示', width = 7, height = 2, font = f3, bg = '#666666', fg = 'White',
                                            command = self.openHint4).place(x = 720, y = 70)            
        if counts != 2 and counts < 6:
            # 訂購按鈕
            Button(self.page, text = '訂購!', width = 10, height = 2, font = f3, bg = '#FFCC22', fg = 'White',
                   command = self.orderFinished).place(x = 720, y = 490)
        elif counts == 2:
            # 訂購按鈕
            Button(self.page, text = '訂購!', width = 10, height = 2, font = f3, bg = '#FFCC22', fg = 'White',
                   command = self.orderFinished).place(x = 720, y = 490)

        # row0 排版位置
        self.page.lbl_topic.place(x = 50, y = 60)

        # row7 排版位置
        self.page.lbl_fixcost.place(x = 220, y = 450)
        # self.page.lbl_stockcost.place(x = 220, y = 500)
        # self.page.lbl_note.place(x = 220, y = 520)
        self.page.lbl_cost.place(x = 511, y = 490)
        # -----------------------------------------------------------------------------------------------------------

        # 品項表格
        columns = ("訂購單價", "售價", "剩餘庫存", "訂購數量")
        self.page.tree_item = ttk.Treeview(self.page, column = columns)  # 表格

        self.page.tree_item.column("#0", minwidth = 0, width = 110, anchor = "center")
        self.page.tree_item.column("訂購單價", width = 95, anchor = "center")
        self.page.tree_item.column("售價", width = 95, anchor = "center")
        self.page.tree_item.column("剩餘庫存", width = 95, anchor = "center")
        self.page.tree_item.column("訂購數量", width = 112, anchor = "center")

        self.page.tree_item.heading("#0", text = "食材")
        self.page.tree_item.heading("訂購單價", text = "訂購單價")  # 顯示表頭
        self.page.tree_item.heading("售價", text = "售價")
        self.page.tree_item.heading("剩餘庫存", text = "剩餘庫存")
        self.page.tree_item.heading("訂購數量", text = "訂購數量")

        global stock_list
        global price_list
        global material_price
        self.page.tree_item.insert("", 0, text = "至尊和牛堡",
                                   values = (material_price[0], price_list[0], stock_list[0]))  # 插入資料
        self.page.tree_item.insert("", 1, text = "豬肉滿福堡", values = (material_price[1], price_list[1], stock_list[1]))
        self.page.tree_item.insert("", 2, text = "嫩煎雞腿堡", values = (material_price[2], price_list[2], stock_list[2]))
        self.page.tree_item.insert("", 3, text = "好多蔬食堡", values = (material_price[3], price_list[3], stock_list[3]))
        self.page.tree_item.insert("", 4, text = "健康生酮堡", values = (material_price[4], price_list[4], stock_list[4]))

        style = ttk.Style()
        style.configure("Treeview.Heading", font = ("微軟正黑體", 10))
        style.configure("Treeview", rowheight = 50, font = ("微軟正黑體", 10))
        self.page.tree_item.place(x = 85, y = 150, height = 276)
        # -----------------------------------------------------------------------------------------------------------

        # 讓玩家輸入的表格
        self.page.txt_beef = tk.Text(self.page, height = 2, width = 11, font = f4)
        self.page.txt_pork = tk.Text(self.page, height = 2, width = 11, font = f4)
        self.page.txt_chick = tk.Text(self.page, height = 2, width = 11, font = f4)
        self.page.txt_vege = tk.Text(self.page, height = 2, width = 11, font = f4)
        self.page.txt_keto = tk.Text(self.page, height = 2, width = 11, font = f4)

        # 輸入的表格 排版位置
        self.page.txt_beef.place(x = 480, y = 175)
        self.page.txt_pork.place(x = 480, y = 225)
        self.page.txt_chick.place(x = 480, y = 275)
        self.page.txt_vege.place(x = 480, y = 325)
        self.page.txt_keto.place(x = 480, y = 375)

    def costCalculation(self):
        global material_price
        global order_fixed_cost
        order_list = []
        total_cost = 0
        beefnum = self.page.txt_beef.get("1.0", END)
        order_list.append(beefnum)
        porknum = self.page.txt_pork.get("1.0", END)
        order_list.append(porknum)
        chickennum = self.page.txt_chick.get("1.0", END)
        order_list.append(chickennum)
        vegenum = self.page.txt_vege.get("1.0", END)
        order_list.append(vegenum)
        ketonum = self.page.txt_keto.get("1.0", END)
        order_list.append(ketonum)

        result = "success"
        for order in order_list:
            try:
                order = int(order)
                if order < 0:
                    result = "failed"
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
            showinfo(title = "成本計算", message = ("總成本為$" + str(total_cost)))
        else:
            showinfo(title = "錯誤", message = "累了嗎?請輸入正確格式")

    def orderFinished(self):
        global stock_list
        global order_cost_list
        global counts
        global order_list
        total_cost = 0
        beefnum = self.page.txt_beef.get("1.0", END)
        order_list[0] = beefnum
        porknum = self.page.txt_pork.get("1.0", END)
        order_list[1] = porknum
        chickennum = self.page.txt_chick.get("1.0", END)
        order_list[2] = chickennum
        vegenum = self.page.txt_vege.get("1.0", END)
        order_list[3] = vegenum
        ketonum = self.page.txt_keto.get("1.0", END)
        order_list[4] = ketonum

        result = "success"
        for order in order_list:
            try:
                order = int(order)
                if order < 0:
                    result = "failed"
                elif order > 800:
                    result = "over"
                    break
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
        elif result == "over":
            showinfo(title = "前輩的提醒", message = "傻孩子，訂那麼多貨你會賠爆!")
        else:
            showinfo(title = "錯誤", message = "累了嗎?請輸入正確格式")

    def openHint1(self):
        showinfo(title = "小提示", message = hint_dict[scenario][0])
    
    def openHint4(self):
        showinfo(title = "小提示", message = hint_dict[scenario][1])


class FinalResultPage1(object):
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame # 新增
        self.page.pack()  # 新增

        f1 = tkFont.Font(size = 24, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 標題、敘述
        self.page.lbl_topic = tk.Label(self.page, text = "營業成果折線圖", height = 1, width = 12, font = f1, bg = '#f9f7f1',
                                       fg = '#666666')
        self.page.btn_next = tk.Button(self.page, text = "經營成就", command = self.gotoResult, width = 10, height = 2,
                                       font = f3, bg = '#FFCC22', fg = 'White')
        # 折線圖
        self.page.lbl_descripition = tk.Label(self.page, text = "來看看你本周的經營記錄吧!", height = 1, width = 20, font = f2,
                                              bg = '#f9f7f1')

        # -------------------------------------------------------------------------------------------
        # 標題、敘述
        self.page.lbl_topic.place(x = 53, y = 45)
        self.page.btn_next.place(x = 720, y = 490)
        # 折線圖
        self.page.lbl_descripition.place(x = 380, y = 68)

        # 折線圖
        self.page.csvMain = tk.Canvas(self.page, width = 636, height = 354, bg = "LightYellow")
        self.page.csvMain.place(x = 146, y = 110)

        global order_cost_list
        global day
        global accumulated_profit_list
        global profit_list
        plt.figure(figsize = (4.7, 2.5), dpi = 150, linewidth = 2)
        plt.plot(day, order_cost_list, 's-', color = 'y', label = "Day Order Cost")
        plt.plot(day, accumulated_profit_list, 's-', color = 'r', label = "Accumulated Profit")
        plt.plot(day, profit_list, 's-', color = 'b', label = "Profit")
        plt.plot(day, stock_cost_list, 's-', color = 'g', label = "Stock Cost")
        plt.plot(day, revenue_list, 's-', color = 'black', label = "Revenue")
        plt.xticks(fontsize = 6)
        plt.yticks(fontsize = 6)
        plt.xlabel("Day", fontsize = 10, labelpad = 6)
        plt.ylabel("$", fontsize = 10, labelpad = 10)
        plt.legend(loc = "upper right", fontsize = 6)
        # plt.show()
        plt.savefig("temp.png")

        self.page.imageMain = ImageTk.PhotoImage(file = "temp.png")
        self.page.csvMain.create_image(326, 170, image = self.page.imageMain, anchor = tk.CENTER)
        os.system("del temp.png")

    def gotoResult(self):
        global ranking_list
        self.page.destroy()
        FinalResultPage2(self.root)
        # ranking_list.append([accumulated_profit, user_name])
        print(user_name)
        print(order_cost_list)
        print(profit_list)
        print(accumulated_profit_list)


class FinalResultPage2(object):
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小
        self.createPage()

    def createPage(self):

        self.page = Frame(self.root)  # 建立Frame # 新增
        self.page.pack()  # 新增

        f1 = tkFont.Font(size = 28, family = "微軟正黑體", weight = "bold")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        global user_name
        image = ImageTk.Image.open("成就榜_bg.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 要接最後的獲利，還有抓歷史還行榜，要排名次
        self.page.lbl_topic = tk.Label(self.page, text = "經營成就", height = 2, width = 10, font = f1, bg = 'Black',
                                       fg = 'White')
        self.page.lbl_descripition1 = tk.Label(self.page, text = ("總分：" + str(accumulated_profit)), height = 1,
                                               width = 15, font = f2, anchor = 'w', bg = 'Black', fg = 'White')
        if accumulated_profit >= 5000:
            achiev = "米其林三星"
        elif accumulated_profit >= 4750:
            achiev = "必比登百大美食"
        elif accumulated_profit >= 4250:
            achiev = "「我就讚」美食獎"
        elif accumulated_profit >= 3500:
            achiev = "街訪第一名"
        elif accumulated_profit >= 2750:
            achiev = "Google 評價 ★★★"
        elif accumulated_profit >= 1500:
            achiev = "Google 評價 ★★"
        elif accumulated_profit >= 0:
            achiev = "Google 評價 ★"
        else:
            achiev = "金「我就爛」獎"
        self.page.lbl_descripition2 = tk.Label(self.page, text = "獲得成就：", height = 1, width = 15, font = f2, anchor = 'w',
                                               bg = 'Black', fg = 'White')
        self.page.lbl_descripition3 = tk.Label(self.page, text = achiev, height = 1, width = 15, font = f2, anchor = 'w',
                                               bg = 'Black', fg = 'White')
        
        # 按鈕
        self.page.btn_tips = tk.Button(self.page, text = "高分秘訣", command = self.gotoHighscore, height = 2, width = 7,
                                       font = f3, bg = 'Black', fg = 'White')
        
        self.page.btn_main = tk.Button(self.page, text = "再玩一次", command = self.againtoStart, height = 2, width = 7,
                                       font = f3, bg = 'Black', fg = 'White')

        self.page.lbl_topic.place(x = 70, y = 25)
        self.page.lbl_descripition1.place(x = 140, y = 120)
        self.page.lbl_descripition2.place(x = 140, y = 155)
        self.page.lbl_descripition3.place(x = 140, y = 195)
        self.page.btn_tips.place(x = 760, y = 420)
        # self.page.btn_ranking.place(x = 400, y = 420)
        self.page.btn_main.place(x = 760, y = 500)

    def gotoHighscore(self):
        self.page.destroy()
        HighscorePage(self.root)

    # def gotoRanking2(self):
        # self.page.destroy()
        # RankingPage2(self.root)

    def againtoStart(self):
        self.page.destroy()
        StartPage(self.root)


class HighscorePage(object):
    def __init__(self, master = None):
        self.root = master  # 定義內部變數root
        self.root.geometry('900x600+200+30')  # 設定視窗大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 建立Frame # 新增
        self.page.pack()  # 新增

        f1 = tkFont.Font(size = 28, family = "微軟正黑體",)
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)

        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)

        # 標題
        self.page.lbl_topic = tk.Label(self.page, text = "高分秘訣", height = 2, width = 10, font = f1, bg = '#f9f7f1',
                                       fg = '#666666')
        self.page.lbl_topic.place(x = 300, y = 40)

        # P系統
        self.page.psystem = tk.Label(self.page,
                                     text = "P系統\n\n又稱「定期」存貨控制系統，以訂購周期和最高庫存量為控制基準，例：固定每兩天訂購生菜漢堡，訂到設定的最高庫存量40個，每次訂的數量因剩下的量而有不同。\n\n適合需求比較穩定、次要的原料",
                                     height = 12, width = 30, font = f3, bg = 'LightYellow', wraplength = 310)

        # Q系統
        self.page.qsystem = tk.Label(self.page,
                                     text = "Q系統\n\n又稱「定量」存貨控制系統，以再次訂購點和固定量為控制基準。\n例：只要至尊和牛堡低於15個，就馬上訂購固定的量20個，可能一天訂好幾次，但量都固定為20。\n\n適合需求比較不穩定、主要的原料",
                                     height = 12, width = 30, font = f3, bg = 'OldLace', wraplength = 310)

        # 回經營成就頁面
        self.page.btn_main = tk.Button(self.page, text = "經營成就", command = self.gotoResult2, height = 2, width = 9,
                                       font = f3, bg = '#FFCC22', fg = 'White')

        self.page.psystem.place(relx = 0.08, rely = 0.25)
        self.page.qsystem.place(relx = 0.52, rely = 0.25)
        self.page.btn_main.place(x = 720, y = 490)

    def gotoResult2(self):
        self.page.destroy()
        FinalResultPage2(root)



##### 最後跑程式的指令#####
root = Tk()
root.title('PBC讓你睡不堡')
StartPage(root)
root.mainloop()
print(user_name)
print(order_cost_list)
print(profit_list)
print(accumulated_profit_list)
