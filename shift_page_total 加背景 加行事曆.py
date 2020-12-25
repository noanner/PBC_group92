import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from PIL import ImageTk

##### 需求背景 #####
# 跑Random決定這次遊戲玩哪個情境
Scen = 'Scen1'

# 經營背景 (行事曆) 【已加】
Scen_dict = {'Scen1' : "您的餐廳開在著名的觀光景點附近，每天會有不同的大型旅行團造訪!",
             'Scen2' : "您的餐廳舉辦了為期一周的活動，希望可以多加推廣並且慶祝各式各樣的節日!",
             'Scen3' : "本周的天氣變化很大，好在有精準的天氣預報，可以以此決定要備多少料!",
             'Scen4' : "這是禍不單行，但也好事成雙的一周，您的餐廳遇到很多突發狀況，您要如何解決呢？"}

# 每日活動 (行事曆) 【已加】
Events_dict = {'Scen1' : ["固定需求", "印度教", "高中畢旅", "美國人", "健身俱樂部", "阿拉伯人", "佛教徒"],
               'Scen2' : ["固定需求", "33五花肉日", "感恩節", "中秋節", "全球素食日", "兒童節", "情人節"],
               'Scen3' : ["固定需求", "下豪大雨", "出炎熱的大太陽", "風和日麗", "寒流來襲", "颱風天", "無風無雨"],
               'Scen4' : ["固定需求", "大樂透開獎", "店門口道路施工", "對面漢堡王休息一天", "新聞不實報導", "拿到安全衛生許可", "平凡的一天"]}

# 答對的小提示 (CorrectPage) 【已加 待調整】
Hint_dict = {'Scen1' : ["不吃牛肉豬肉，特愛雞肉，如果沒有咖哩的話，他們寧願少吃點", 
                        "健身的巨巨們喜歡選用蛋白質較高的牛肉雞肉，若是有生同這樣碳水低的選擇，他們在愛也不過了，通常可以吃上兩份"],
             'Scen2' : ["韓國人熱愛豬五花肉，甚至將3月3日正式訂為「五花肉日」", 
                        "全球素食日是一個完全不能吃肉的節日，連製作的食材都不會有任何的肉"],
             'Scen3' : ["因為午後的豪大雨，導致顧客出門意願降低，只想待在家叫Foodpanda或Ubereats，全品項銷量約減少25%", 
                        "寒流來襲，大口大口咬下漢堡，身體有熱量去禦寒，大家喜歡到漢堡店坐在店裡享用，全品項銷售量約增加25%"],
             'Scen4' : ["今日為大樂透開獎，得主就住在餐廳樓上，平常他最愛吃的就是牛肉漢堡，今天他決定拿獎金買下60個請台北車站的流浪漢吃", 
                        "新聞報導指控您的餐廳餐點不衛生，漢堡都是用組合肉，生菜也不新鮮，麵包更是都發霉了，讓業績只剩4成"]}

# 需求量 【還沒加】
demand_dict = {'Scen1' : [[20,20,20,20,20], [3,5,52,62,2], [31,28,27,8,11], [30,25,28,5,15], [21,6,25,12,65], [25,3,30,28,18], [4,6,8,62,10]],
               'Scen2' : [[20,20,20,20,20], [18,19,43,15,12], [21,18,31,17,19], [23,25,28,19,12], [0,0,0,110,0], [28,26,27,8,13], [22,23,21,19,18]],
               'Scen3' : [[20,20,20,20,20], [16,16,17,15,15], [22,23,23,19,21], [26,28,27,23,24], [24,23,26,24,25], [15,14,16,13,16], [21,20,22,20,21]],
               'Scen4' : [[20,20,20,20,20], [81,21,20,19,18], [16,13,15,15,16], [31,28,29,27,29], [8,7,7,8,6], [22,23,21,21,22], [21,21,21,21,21]]}


##### 原本的資訊 ######
# day = ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7"]  【不確定這行哪裡有用到?】
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

        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)  # 製造一個空的grid在底下
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 內容
        self.page.lbl_topic = tk.Label(self.page, text = "餐廳經營管理遊戲", height = 2, width = 18, font = f1, bg = 'White', fg = '#666666')
        self.page.btn_enter = tk.Button(self.page, text = "進入遊戲", command = self.gotoIntro, height = 2, width = 10,
                                        font = f2, bg = '#FFCC22', fg = 'White')
        self.page.btn_rank = tk.Button(self.page, text = "排行榜", command = self.gotoRanking1, height = 2, width = 10,
                                       font = f2, bg = '#666666', fg = 'White')
        
        self.page.lbl_topic.place(x = 220, y = 150)
        self.page.btn_enter.place(x = 260, y = 350)
        self.page.btn_rank.place(x = 495, y = 350)

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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 內容
        self.page.lbl_topic = tk.Label(self.page, text = "排行榜", height = 2, width = 10, font = f1, bg = 'White', fg = '#666666') 
        self.page.psystem = tk.Label(self.page, text = "第一名：", height = 2, width = 10, font = f3, bg = 'LightYellow')
        self.page.qsystem = tk.Label(self.page, text = "第二名：", height = 2, width = 10, font = f3, bg = 'OldLace')
        self.page.btn_main = tk.Button(self.page, text = "回主畫面", command = self.gotoStartPage, height = 2, width = 9, font = f2, bg = '#FFCC22', fg = 'White')
        
        self.page.lbl_topic.place(x=300, y=50)
        self.page.psystem.place(x=300, y=160)
        self.page.qsystem.place(x=300, y=230)
        self.page.btn_main.place(x = 730, y = 490)
        
    
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
        self.page = Frame(self.root)
        self.page.pack()
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x = 0, y = 0)
        
        self.button1 = tk.Label(root, text = "遊戲說明", font = f1, height = 2, width = 18, bg = 'White', fg = '#666666')
        self.button1.place(x = 220, y = 50)
        
        self.intro = tk.Label(root, text = "有沒有想過經營一間漢堡餐廳？\n\n在這個遊戲裡，你要發揮需求預測能力，進行訂貨及存貨管理。\n"
                                           "這個遊戲中，你將會面對每天不同的銷售情境，\n根據不同的情境，你必須預測菜單的需求變動狀況，"
                                           "進而去決定如何訂購產品原料。\n" "遊戲中，最重要的三個元素就是需求量、訂購的固定成本以及材料成本。\n"
                                           "遊戲將根據你的獲利情況計算分數，最後進行評價。",
                              font = f3, bg = 'LemonChiffon', fg = '#666666')
        self.intro.place(relx = 0.5, rely = 0.28, relwidth = 0.85, relheight = 0.35, anchor = 'n')

        self.button2 = tk.Button(root, text = "開始遊戲", font = f2, command = self.gotoRule, height = 2, width = 10, bg = '#FFCC22', fg = 'White')
        self.button2.place(x=720, y=490)
        
        # 建立框架
        self.frame = tk.Frame(root, bg = '#FFCC22', bd = 5)
        self.frame.place(relx = 0.5, rely = 0.68, relwidth = 0.75, relheight = 0.07, anchor = 'n')
        
        # 輸入框
        self.button1 = tk.Label(self.frame, text = "替你的餐廳取個會賺大錢的名字：", font = f3, bg = '#FFCC22', fg = 'White')
        self.button1.place(relx = 0.02, relheight = 1, relwidth = 0.45, anchor = 'nw')
        self.entry = tk.Entry(self.frame, textvariable = self.username, font = f3)
        self.entry.place(relwidth = 0.5, relx = 0.48, relheight = 1)

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
        self.page = Frame(self.root)
        self.page.pack()
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 背景圖片填滿畫布
        # self.background_image = ImageTk.PhotoImage(file = 'restaurant.jpg')
        # self.background_label = tk.Label(self.root, image = self.background_image)
        # self.background_label.place(relwidth = 1, relheight = 1)
        
        # 建立框架
        # self.frame = tk.Frame(root, bg = 'OldLace', bd = 5)
        # self.frame.place(relx = 0.5, rely = 0.1, relwidth = 0.7, relheight = 0.05, anchor = 'n')
        
        self.topic = tk.Label(root, text = "貼心小提醒", font = f1, height = 2, width = 18, bg = 'White', fg = '#666666')
        self.topic.place(x=220, y=50)
        
        # 輸入介紹
        self.page.intro = tk.Label(self.page, text = "有一位經驗老道的前輩傳授了他的經營祕訣，\n保證你開店第一天就有好成績，"
                                                        "\n要仔細記得存貨與需求量的資訊，\n之後進行食材訂購才會順利喔~", 
                                                        height = 5, width = 50, font = f3, bg = 'LemonChiffon', fg = '#666666')      
        self.page.intro.place(relx = 0.5, rely = 0.26, anchor = 'n')

        self.page.button = tk.Button(root, text = "開始遊戲", font = f2, command = self.gotoDay1, height = 2, width = 10, bg = '#FFCC22', fg = 'White')
        self.page.button.place(x=720, y=490)

        # 建立成本表格
        self.columns = ("品項", "成本", "售價", "期初存貨", "進貨成本", "存貨成本")
        self.treeview = ttk.Treeview(root, height = 7, show = "headings", columns = self.columns)  # 表格
        # 表格UI
        style = ttk.Style()
        style.configure("Treeview.Heading", font = ("華康娃娃體", 12))
        style.configure("Treeview", rowheight=25, font = ("華康娃娃體", 10))

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
        self.treeview.place(relx = 0.1, rely = 0.48, relwidth = 0.75, relheight = 0.27)

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
    def gotoDay1(self):
        self.page.destroy()
        Day1Page1(self.root)
    
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
    

know_content = "小知識1111111111111111111111111111111111111111111111111111111111111111111111111111"
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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 元件內容
        lbl_day = tk.Label(text = "Day1小知識問答", height = 2, width = 15, font = f1, bg = 'White', fg = '#666666') 
        lbl_know = tk.Label(text = know_content, font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left', bg = 'LemonChiffon', fg = '#666666')
        btn_optA = tk.Button(text = "選項A", command = self.gotoCorrect, width = 7,height = 2, font = f2, bg = '#FFCC22', fg = 'White')
        btn_optB = tk.Button(text = "選項B", command = self.gotoWrong, width = 7,height = 2, font = f2, bg = '#FFCC22', fg = 'White')
        btn_calendar = tk.Button(text = "行事曆", command = self.openCalendar, width = 7,height = 2, font = f2, bg = '#666666', fg = 'White')
        
        # 元件位置
        lbl_day.place(x= 50, y=40)
        lbl_know.place(relx= 0.28, rely=0.3, width=400, height=200)
        btn_optA.place(relx= 0.3, rely=0.75)
        btn_optB.place(relx= 0.6, rely=0.75)
        btn_calendar.place(x= 720, y=70)
    
    def gotoCorrect(self):
        self.page.destroy()
        CorrectPage(self.root)
        # showinfo(title='小提示', message='小提示輸入處')
        
    def gotoWrong(self):
        self.page.destroy()
        WrongPage(self.root)
    
    def openCalendar(self):
        # showinfo(title='行事曆', message='此處放行事曆')
        self.page.destroy()
        Calendar(self.root)


know_content = "小知識1111111111111111111111111111111111111111111111111111111111111111111111111111"
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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 元件內容
        lbl_day = tk.Label(text = "Day4小知識問答", height = 2, width = 15, font = f1, bg = 'White', fg = '#666666') 
        lbl_know = tk.Label(text = know_content, font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left', bg = 'LemonChiffon', fg = '#666666')
        btn_optA = tk.Button(text = "選項A", command = self.gotoCorrect, width = 7,height = 2, font = f2, bg = '#FFCC22', fg = 'White')
        btn_optB = tk.Button(text = "選項B", command = self.gotoWrong, width = 7,height = 2, font = f2, bg = '#FFCC22', fg = 'White')
        btn_calendar = tk.Button(text = "行事曆", command = self.openCalendar, width = 7,height = 2, font = f2, bg = '#666666', fg = 'White')
        
        # 元件位置
        lbl_day.place(x= 50, y=40)
        lbl_know.place(relx= 0.28, rely=0.3, width=400, height=200)
        btn_optA.place(relx= 0.3, rely=0.75)
        btn_optB.place(relx= 0.6, rely=0.75)
        btn_calendar.place(x= 720, y=70)
    
    def gotoCorrect(self):
        self.page.destroy()
        CorrectPage(self.root)
        # showinfo(title='小提示', message='小提示輸入處')
        
    def gotoWrong(self):
        self.page.destroy()
        WrongPage(self.root)
    
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')


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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 顯示恭喜答對 
        self.page.lbl_topic = tk.Label(self.page, text = 'Bingo!', height = 2, width = 8, font = f1, bg = 'White', fg = '#666666')
        self.page.lbl_topic.place(x= 50, y=40)

        # 行事曆按鈕
        Button(self.page, text='行事曆', width=7, height=2, font=f2, bg = '#666666', fg = 'White', command=self.openCalendar).place(x= 720, y=70)

        # 答對的圖片
        global cooking_img
        image = ImageTk.Image.open("Bingo.jpg")
        image = image.resize((300, 300), ImageTk.Image.ANTIALIAS)
        cooking_img = ImageTk.PhotoImage(image)
        Label(self.page, image = cooking_img).place(x=120, y=150)

        # 答對的小提示
        self.page.lbl_descripition = tk.Label(self.page, text = ("為了獎勵你答對，告訴你 Day" + str(counts+1) + "需求的小提示吧!"), font = f2, borderwidth = 2, wraplength = 300, justify = 'left', bg = 'White', fg = '#666666')
        self.page.lbl_descripition.place(x = 480, y = 220)
        
        day = 0  # 這裡要寫一個counts 判斷是day1還是day4
        hint = Hint_dict[Scen][day]
        self.page.lbl_hint = tk.Label(self.page, text = hint, font = f2, borderwidth = 15, wraplength = 320, justify = 'left', bg = 'LemonChiffon', fg = '#666666')
        self.page.lbl_hint.place(x = 460, y = 280)

        # 下一頁按鈕
        Button(self.page, text='繼續遊戲', width=10, height=2, font=f2, bg = '#FFCC22', fg = 'White', command=self.gotoDay1).place(x=720, y=490)
        
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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 顯示可惜答錯 
        self.page.lbl_topic = tk.Label(self.page, text = 'Oops!', height = 2, width = 7, font = f1, bg = 'White', fg = '#666666')
        self.page.lbl_topic.place(x= 50, y=40)

        # 行事曆按鈕
        Button(self.page, text='行事曆', width=7, height=2, font=f2, bg = '#666666', fg = 'White', command=self.openCalendar).place(x= 720, y=70)

        # 答錯的圖片
        global cooking_img
        image = ImageTk.Image.open("wrong.png")
        # image = ImageTk.Image.open("C:\\Users\\formo\\Documents\\python files\\finalproject\\mytest\\S__85836045.png")
        image = image.resize((300, 300), ImageTk.Image.ANTIALIAS)
        cooking_img = ImageTk.PhotoImage(image)
        Label(self.page, image = cooking_img).place(x=150, y=150)

        # 答錯的訊息
        self.page.lbl_hint = tk.Label(self.page, text = "答錯了 好可惜呀... 不要氣餒，繼續玩遊戲吧!", font = f2, borderwidth = 2, wraplength = 300, justify = 'left', bg = 'LemonChiffon', fg = '#666666')
        self.page.lbl_hint.place(x = 500, y = 200)
        # self.page.lbl_description = tk.Label(self.page, text="為了獎勵你答對，告訴你一個小提示吧~", height = 2, width = 40, bg="#F3F3F3", fg="black", font=f3)
        # self.page.lbl_description.place(x = 400, y = 300)

        # 下一頁按鈕
        Button(self.page, text='繼續遊戲', width=10, height=2, font=f2, bg = '#FFCC22', fg = 'White', command=self.gotoDay1).place(x=720, y=490)
        
    def gotoDay1(self):
        self.page.destroy()
        EverydayPage(self.root)
        
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')


class Calendar(object): # 行事曆(Day1Page1)
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame # 新增
        self.page.pack() # 新增
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 內容
        self.page.lbl_topic = tk.Label(self.page, text = "行事曆", height = 2, width = 10, font = f1, bg = 'White', fg = '#666666') 
        self.page.btn_main = tk.Button(self.page, text = "返回遊戲", command = self.backtopage, height = 2, width = 9, font = f2, bg = '#FFCC22', fg = 'White')
        
        self.page.lbl_topic.place(x=300, y=50)
        self.page.btn_main.place(x = 730, y = 490)
        
        # 左半邊 經營背景
        self.page.lbl_bg = tk.Label(self.page, text = Scen_dict[Scen], font = f2, borderwidth = 20, wraplength = 200, justify = 'left', bg = 'LemonChiffon', fg = '#666666')
        self.page.lbl_bg.place(x = 140, y = 220)
        
        # 右半邊 行事曆表格
        tree_item=ttk.Treeview(root, selectmode="extended", columns=("天數", "活動"))#表格
        tree_item["columns"]=("活動")
        tree_item.column("#0",minwidth=0,width=100, anchor='center')
        tree_item.column("活動",minwidth=0,width=200, anchor='center')   #表示列,不顯示

        tree_item.heading("#0",text="天數")
        tree_item.heading("活動",text="活動")  #顯示表頭

        tree_item.insert("",1,text="Day1", values=Events_dict[Scen][0])#插入資料
        tree_item.insert("",2,text="Day2", values=Events_dict[Scen][1])
        tree_item.insert("",3,text="Day3", values=Events_dict[Scen][2])
        tree_item.insert("",4,text="Day4", values=Events_dict[Scen][3])
        tree_item.insert("",5,text="Day5", values=Events_dict[Scen][4])
        tree_item.insert("",6,text="Day6", values=Events_dict[Scen][5])
        tree_item.insert("",7,text="Day7", values=Events_dict[Scen][6])
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("華康娃娃體", 10))
        style.configure("Treeview", rowheight=38, font=("華康娃娃體", 10))
        tree_item.place(x=410, y=160, height=300)
    
    def backtopage(self):
        self.page.destroy()
        Day1Page1(root)


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
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 顯示Day 1 
        self.page.lbl_topic = tk.Label(self.page, text = ("Day" + str(counts+1)), height = 2, width = 7, font = f1, bg = 'White', fg = '#666666')
        self.page.lbl_topic.place(x = 50, y = 40)
        
        # 行事曆按鈕
        Button(self.page, text='行事曆', width=7, height=2, font=f2, bg = '#666666', fg = 'White', command=self.openCalendar).place(x= 720, y=70)

        # 做漢堡的圖片
        global cooking_img
        image = ImageTk.Image.open("S__85836045.png")
        # image = ImageTk.Image.open("C:\\Users\\formo\\Documents\\python files\\finalproject\\mytest\\S__85836045.png")
        image = image.resize((600, 300), ImageTk.Image.ANTIALIAS)
        cooking_img = ImageTk.PhotoImage(image)
        Label(self.page, image = cooking_img).place(x=150, y=160)

        # 顯示 餐廳開始營業囉，點選下一頁查看你今天的營業成果吧~ 
        self.page.lbl_description = tk.Label(self.page, text="餐廳開始營業囉，點選下一頁查看你今天的營業成果吧~", height = 2, width = 50, bg = 'White', fg="#666666", font=f3)
        self.page.lbl_description.place(x = 205, y = 70)

        # 下一頁按鈕
        Button(self.page, text='繼續遊戲', width=10, height=2, font=f2, bg = '#FFCC22', fg = 'White', command=self.gotoDayResult).place(x=720, y=490)

    def gotoDayResult(self):
        self.page.destroy()
        EverydayResultPage(root)

    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')


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
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)

        # 顯示 header
        self.page.lbl_topic = tk.Label(self.page, text = ("Day" + str(counts+1)), height = 2, width = 7, font = f1, bg = 'White', fg = '#666666')
        self.page.lbl_topic.place(x= 50, y=40)

        self.page.lbl_description = tk.Label(self.page, text = "辛苦了~下面是你今天營業的成果~~", height = 2, width = 40, font = f3, bg = 'White')
        self.page.lbl_description.place(x = 200, y = 70)

        if counts < 6 : 
            # 下一頁按鈕
            Button(self.page, text='繼續遊戲', width=10, height=2, font=f2, bg = '#FFCC22', fg = 'White', command=self.gotoStockorder).place(x=720, y=490)
            
            # 行事曆按鈕
            Button(self.page, text='行事曆', width=7, height=2, font=f2, bg = '#666666', fg = 'White', command=self.openCalendar).place(x= 720, y=70)
            
        else:
            # 下一頁按鈕
            Button(self.page, text='繼續遊戲', width=10, height=2, font=f2, bg = '#FFCC22', fg = 'White', command=self.gotoResult).place(x=720, y=490)

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
        style.configure("Treeview.Heading", font=("華康娃娃體", 10))
        style.configure("Treeview", rowheight=50, font=("華康娃娃體", 10))

        self.page.tree_item.place(x=80, y=160, height=280)

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

        self.page.tree_amount.place(x=630, y=160, height=280)

    def gotoStockorder(self):
        self.page.destroy()
        EverydayStockPage(root)
        
    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')
    
    def gotoResult(self):
        self.page.destroy()
        FinalResultPage1(root)


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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        f4 = tkFont.Font(size = 10, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 行事曆按鈕
        Button(self.page, text='行事曆', width=7, height=2, font=f2, bg = '#666666', fg = 'White', command=self.openCalendar).place(x= 720, y=70)
        
        # row0 標題、敘述、行事曆按鈕
        self.page.lbl_topic = tk.Label(self.page, text = ("Day" + str(counts+1)), height = 2, width = 7, font = f1, bg = 'White', fg = '#666666')
        self.page.lbl_description = tk.Label(self.page, text = "以下是目前的剩餘庫存，請問今天要訂多少貨呢?", height = 2, width = 45, font = f3, bg = 'White')

        # row7 訂貨固定成本、目前訂購總價、訂購按鈕
        self.page.lbl_fixcost = tk.Label(self.page, text = " 各品項固定成本:$50元 ", height = 1, width = 22, font = f3, bg = 'LemonChiffon')
        self.page.lbl_note = tk.Label(self.page, text = " 沒有要訂購也要輸入0唷! ", height = 1, width = 22, font = f3, bg = 'LemonChiffon')
        self.page.lbl_cost = tk.Button(self.page, text = "總價試算", command = self.costCalculation, height = 2, width = 10, font = f2, bg = 'Lavender')
        if counts != 2 and counts < 6:
            # 訂購按鈕
            Button(self.page, text='訂購!', width=10, height=2, font=f2, bg = '#FFCC22', fg = 'White', command=self.orderFinished).place(x=720, y=490)
        elif counts == 2:
            # 訂購按鈕
            Button(self.page, text='訂購!', width=10, height=2, font=f2, bg = '#FFCC22', fg = 'White', command=self.orderFinishedgoto4).place(x=720, y=490)
      
        # row0 排版位置
        self.page.lbl_topic.place(x= 50, y=40)
        self.page.lbl_description.place(x = 200, y = 70)
        
        # row7 排版位置
        self.page.lbl_fixcost.place(x = 220, y = 480)
        self.page.lbl_note.place(x = 220, y = 520)
        self.page.lbl_cost.place(x = 511, y = 490)
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
        style.configure("Treeview.Heading", font=("華康娃娃體", 10))
        style.configure("Treeview", rowheight=50, font=("華康娃娃體", 10))
        self.page.tree_item.place(x=150, y=150, height=276)
        #-----------------------------------------------------------------------------------------------------------
        
        # 讓玩家輸入的表格
        self.page.txt_beef = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_pork = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_chick = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_vego = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_keto = tk.Text (self.page, height = 2, width = 12 , font = f4)
    
        # 輸入的表格 排版位置
        self.page.txt_beef.place(x=511, y=175)
        self.page.txt_pork.place(x=511, y=225)
        self.page.txt_chick.place(x=511, y=275)
        self.page.txt_vego.place(x=511, y=325)
        self.page.txt_keto.place(x=511, y=375)
                
        
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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 標題、敘述
        self.page.lbl_topic = tk.Label(self.page, text = "營業成果折線圖", height = 2, width = 15, font = f1, bg = 'White', fg = '#666666') 
        self.page.btn_next = tk.Button(self.page, text = "經營成就", command = self.gotoResult, width=10, height=2, font=f2, bg = '#FFCC22', fg = 'White')
        # 折線圖
        self.page.lbl_descripition = tk.Label(self.page, text = "來看看你本周的經營記錄吧!", height = 1, width = 30, font = f2, bg = 'White')
        self.page.btn_chart = tk.Canvas(self.page, height = 400, width = 500, bg = 'LightYellow')
        
        #-------------------------------------------------------------------------------------------
        # 標題、敘述
        self.page.lbl_topic.place(x=50, y=40)
        self.page.btn_next.place(x=720, y=490)
        # 折線圖
        self.page.lbl_descripition.place(x=430, y=75)
        self.page.btn_chart.place(x=200, y=140)


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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")

        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 要接最後的獲利，還有抓歷史還行榜，要排名次
        self.page.lbl_topic = tk.Label(self.page, text = "經營成就", height = 2, width = 10, font = f1, bg = 'White', fg = '#666666')
        self.page.lbl_descripition1 = tk.Label(self.page, text = "獲利：", height = 1, width = 15, font = f2, anchor = 'w', bg = 'White', fg = '#666666')
        self.page.lbl_descripition2 = tk.Label(self.page, text = "名次：", height = 1, width = 15, font = f2, anchor = 'w', bg = 'White', fg = '#666666')
        
        # 須依造分數給不一樣的敘述
        self.page.lbl_descripition3 = tk.Label(self.page, text = " 恭喜您的餐廳榮獲:", height = 2, width = 20, font = f2, anchor = 'w', bg = 'LemonChiffon')
        self.page.lbl_descripition4 = tk.Label(self.page, text = "  米其林三星殊榮", height = 2, width = 20, font = f2, anchor = 'w', bg = 'LemonChiffon')
        
        # 按鈕
        self.page.btn_tips = tk.Button(self.page, text = "高分秘訣", command = self.gotoHighscore, height = 2, width = 7, font = f2, bg = '#FFCC22', fg = 'White')
        self.page.btn_ranking = tk.Button(self.page, text = "排行榜", command = self.gotoRanking2, height = 2, width = 7, font = f2, bg = '#FFCC22', fg = 'White')
        self.page.btn_main = tk.Button(self.page, text = "回主畫面", command = self.page.quit, height = 2, width = 7, font = f2, bg = '#FFCC22', fg = 'White')
        
        self.page.lbl_topic.place(x=300, y=50)
        self.page.lbl_descripition1.place(x=330, y=160)
        self.page.lbl_descripition2.place(x=330, y=220)
        self.page.lbl_descripition3.place(x=310, y=280)
        self.page.lbl_descripition4.place(x=310, y=320)
        self.page.btn_tips.place(x = 200, y = 420)
        self.page.btn_ranking.place(x = 400, y = 420)
        self.page.btn_main.place(x = 600, y = 420)    

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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0)
        
        # 內容        
        self.page.lbl_topic = tk.Label(self.page, text = "排行榜", height = 2, width = 10, font = f1, bg = 'White', fg = '#666666') 
        self.page.psystem = tk.Label(self.page, text = "第一名：", height = 2, width = 10, font = f3, bg = 'LightYellow')
        self.page.qsystem = tk.Label(self.page, text = "第二名：", height = 2, width = 10, font = f3, bg = 'OldLace')
        self.page.btn_main = tk.Button(self.page, text = "經營成就", command = self.gotoResult2, height = 2, width = 9, font = f2, bg = '#FFCC22', fg = 'White')
        
        self.page.lbl_topic.place(x=300, y=50)
        self.page.psystem.place(x=300, y=160)
        self.page.qsystem.place(x=300, y=230)
        self.page.btn_main.place(x = 720, y = 490)
    
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
        
        f1 = tkFont.Font(size = 30, family = "華康娃娃體")
        f2 = tkFont.Font(size = 14, family = "華康娃娃體")
        f3 = tkFont.Font(size = 12, family = "華康娃娃體")
        
        # 底下的grid
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 300, font = f1)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
        
        # 背景圖
        global bg_img
        image = ImageTk.Image.open("背景設計.jpg")
        image = image.resize((900, 600), ImageTk.Image.ANTIALIAS)
        bg_img = ImageTk.PhotoImage(image)
        Label(self.page, image = bg_img).place(x=0, y=0) 
        
        # 標題
        self.page.lbl_topic = tk.Label(self.page, text = "高分秘訣", height = 2, width = 10, font = f1, bg = 'White', fg = '#666666')
        self.page.lbl_topic.place(x=300, y=50)
        
        # P系統
        self.page.psystem = tk.Label(self.page,
        text = "P系統\n\n又稱「定期」存貨控制系統，以訂購周期和最高庫存量為控制基準，例：固定每兩天訂購生菜漢堡，訂到設定的最高庫存量40個，每次訂的數量因剩下的量而有不同。\n\n適合需求比較穩定、次要的原料",
        height = 12, width = 30, font = f3, bg = 'LightYellow', wraplength = 300)
        
        # Q系統
        self.page.qsystem = tk.Label(self.page,
        text = "Q系統\n\n又稱「定量」存貨控制系統，以再次訂購點和固定量為控制基準。\n例：只要牛肉漢堡低於15個，就馬上訂購固定的量20個，可能一天訂好幾次，但量都固定為20。\n\n適合需求比較不穩定、主要的原料",
        height = 12, width = 30, font = f3, bg = 'OldLace', wraplength = 300)
        
        # 回經營成就頁面
        self.page.btn_main = tk.Button(self.page, text = "經營成就", command = self.gotoResult2, height = 2, width = 9, font = f2, bg = '#FFCC22', fg = 'White')
        
        self.page.psystem.place(relx = 0.12, rely = 0.32)
        self.page.qsystem.place(relx = 0.54, rely = 0.32)
        self.page.btn_main.place(x = 720, y = 490)
    
    def gotoResult2(self):
        self.page.destroy()
        FinalResultPage2(root) 


# 最後跑程式的指令
root = Tk()
root.title('小程式')
StartPage(root)
root.mainloop()
print(user_name)
