from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt

import tkinter as tk
import tkinter.font as tkFont

# =========================================================================================
# ===================================== 總結算1 ===========================================
# =========================================================================================

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

# =========================================================================================
# ===================================== 總結算2 ===========================================
# =========================================================================================

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

# =========================================================================================
# ===================================== 高分秘訣 ===========================================
# =========================================================================================

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

# =========================================================================================
# ===================================== 排行榜 ===========================================
# =========================================================================================

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

# =========================================================================================
# ===================================== 主code ===========================================
# =========================================================================================

root = Tk()
root.title("餐廳經營小遊戲")
FinalResultPage1(root)
root.mainloop()



