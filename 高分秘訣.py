import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class ScoreTips(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體") 
        f3 = tkFont.Font(size = 12, family = "微軟正黑體") 

        self.lbl_topic = tk.Label(self, text = "高分秘訣", height = 2, width = 30, font = f1) 

        self.psystem = tk.Label(self,
        text = "P系統\n\n又稱「定期」存貨控制系統，以訂購周期和最高庫存量為控制基準，例：固定每兩天訂購生菜漢堡，訂到設定的最高庫存量40個，每次訂的數量因剩下的量而有不同。\n\n適合需求比較穩定、次要的原料",
        height = 12, width = 27, font = f3, bg = 'LightYellow', wraplength = 300)

        self.qsystem = tk.Label(self,
        text = "Q系統\n\n又稱「定量」存貨控制系統，以再次訂購點和固定量為控制基準，例：只要牛肉漢堡低於15個，就馬上訂購固定的量20個，可能一天訂好幾次，但是量都固定為20。\n\n適合需求比較不穩定、主要的原料",
        height = 12, width = 27, font = f3, bg = 'OldLace', wraplength = 300)
        
        self.btn_main = tk.Button(self, text = "回主畫面", command = self.clickBtnRank, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        self.lbl_topic.grid(row = 0, column = 0, columnspan = 4)
        self.psystem.grid(row = 1, column = 0, columnspan = 2)
        self.qsystem.grid(row = 1, column = 2, columnspan = 2)
        self.btn_main.place(x = 780, y = 380)
        
    
    def clickBtnRank(self):
        pass
        #self.lblNum.configure(text = self.lblNum.cget("text") + "1")
    # 缺一個command要做跳轉頁面


scoretips_page = ScoreTips()
scoretips_page.master.title("餐廳經營小遊戲")
scoretips_page.master.geometry('900x600+200+30')
scoretips_page.mainloop()

# first_page.master.configure(background = 'Lavender')
# 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

