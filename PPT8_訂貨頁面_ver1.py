import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk

class Ordering(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        
        # row0 標題、敘述、行事曆按鈕
        self.lbl_gridonly = tk.Label(self, text = " ", height = 2, width = 30, font = f1)
        self.lbl_topic = tk.Label(self, text = "Day1", height = 1, width = 5, font = f1)
        self.lbl_description = tk.Label(self, text = "以下是目前的剩餘庫存，請問今天要訂多少貨呢?", height = 2, width = 40, font = f3)
        self.btn_schedule = tk.Button(self, text = "行事曆", command = self.clickBtnSchedule, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        # row1 訂購數量表格的標題欄
        self.lbl_r1c1 = tk.Label(self, text = "食材", height = 2, width = 8, font = f3, bg = 'LemonChiffon')
        self.lbl_r1c2 = tk.Label(self, text = "訂購單價", height = 2, width = 7, font = f3, bg = 'LemonChiffon')
        self.lbl_r1c3 = tk.Label(self, text = "剩於庫存", height = 2, width = 7, font = f3, bg = 'LemonChiffon')
        self.lbl_r1c4 = tk.Label(self, text = "訂購數量", height = 2, width = 7, font = f3, bg = 'LemonChiffon')
        
        # row2 牛肉漢堡
        self.lbl_r2c1 = tk.Label(self, text = "牛肉漢堡", height = 2, width = 8, font = f3, bg = 'LightYellow')
        self.lbl_r2c2 = tk.Label(self, text = "$10", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r2c3 = tk.Label(self, text = "5", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r2c4 = tk.Label(self, text = "???", height = 2, width = 7, font = f3, bg = 'OldLace')
        
        # row3 豬肉漢堡
        self.lbl_r3c1 = tk.Label(self, text = "豬肉漢堡", height = 2, width = 8, font = f3, bg = 'LightYellow')
        self.lbl_r3c2 = tk.Label(self, text = "$9", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r3c3 = tk.Label(self, text = "5", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r3c4 = tk.Label(self, text = "???", height = 2, width = 7, font = f3, bg = 'OldLace')
        
        # row4 雞肉漢堡
        self.lbl_r4c1 = tk.Label(self, text = "雞肉漢堡", height = 2, width = 8, font = f3, bg = 'LightYellow')
        self.lbl_r4c2 = tk.Label(self, text = "$9", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r4c3 = tk.Label(self, text = "5", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r4c4 = tk.Label(self, text = "???", height = 2, width = 7, font = f3, bg = 'OldLace')
        
        # row5 生菜堡
        self.lbl_r5c1 = tk.Label(self, text = "生菜堡", height = 2, width = 8, font = f3, bg = 'LightYellow')
        self.lbl_r5c2 = tk.Label(self, text = "$6", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r5c3 = tk.Label(self, text = "5", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r5c4 = tk.Label(self, text = "???", height = 2, width = 7, font = f3, bg = 'OldLace')
        
        # row6 生酮堡
        self.lbl_r6c1 = tk.Label(self, text = "生酮堡", height = 2, width = 8, font = f3, bg = 'LightYellow')
        self.lbl_r6c2 = tk.Label(self, text = "$16", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r6c3 = tk.Label(self, text = "5", height = 2, width = 7, font = f3, bg = 'LightYellow')
        self.lbl_r6c4 = tk.Label(self, text = "???", height = 2, width = 7, font = f3, bg = 'OldLace')
        
        # row7 訂貨固定成本、目前訂購總價、訂購按鈕
        self.lbl_fixcost = tk.Label(self, text = " 訂貨固定成本:$50元 ", height = 2, width = 15, font = f3, bg = 'LemonChiffon')
        self.lbl_cost = tk.Label(self, text = "總價:$$$$$", height = 2, width = 7, font = f3, bg = 'OldLace')
        self.btn_order = tk.Button(self, text = "訂購!", command = self.clickBtnOrder, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        #-----------------------------------------------------------------------------------------------
        # row0
        self.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        # self.lbl_topic.grid(row = 0, column = 0, sticky = tk.NW)
        # self.lbl_description.grid(row = 0, column = 1, sticky = tk.NW)
        # self.btn_schedule.grid(row = 0, column = 6, padx = 10, pady = 10)
        self.lbl_topic.place(x = 26, y = 20)
        self.lbl_description.place(x = 200, y = 30)
        self.btn_schedule.place(x = 780, y = 10)
        
        
        # row1
        self.lbl_r1c1.grid(row = 1, column = 1, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r1c2.grid(row = 1, column = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r1c3.grid(row = 1, column = 3, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r1c4.grid(row = 1, column = 4, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        # self.lbl_r1c1.place(x = 80, y = 120)
        # self.lbl_r1c2.place(x = 185, y = 120)
        # self.lbl_r1c3.place(x = 290, y = 120)
        # self.lbl_r1c4.place(x = 395, y = 120)
                       
        # row2
        self.lbl_r2c1.grid(row = 2, column = 1, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r2c2.grid(row = 2, column = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r2c3.grid(row = 2, column = 3, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r2c4.grid(row = 2, column = 4, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        
        # row3
        self.lbl_r3c1.grid(row = 3, column = 1, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r3c2.grid(row = 3, column = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r3c3.grid(row = 3, column = 3, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r3c4.grid(row = 3, column = 4, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        
        # row4
        self.lbl_r4c1.grid(row = 4, column = 1, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r4c2.grid(row = 4, column = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r4c3.grid(row = 4, column = 3, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r4c4.grid(row = 4, column = 4, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        
        # row5
        self.lbl_r5c1.grid(row = 5, column = 1, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r5c2.grid(row = 5, column = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r5c3.grid(row = 5, column = 3, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r5c4.grid(row = 5, column = 4, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        
        # row6
        self.lbl_r6c1.grid(row = 6, column = 1, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r6c2.grid(row = 6, column = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r6c3.grid(row = 6, column = 3, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        self.lbl_r6c4.grid(row = 6, column = 4, sticky = tk.NW + tk.SE, padx = 1, pady = 1)
        
        # row7
        self.lbl_fixcost.grid(row = 7, column = 1, columnspan = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 15)
        self.lbl_cost.grid(row = 7, column = 4, columnspan = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 15)
        # self.btn_order.grid(row = 7, column = 6, padx = 1, pady = 15)
        self.btn_order.place(x = 780, y = 480)
        
    
    def clickBtnSchedule(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")
    
    def clickBtnOrder(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")



ordering_page = Ordering()
ordering_page.master.title("餐廳經營小遊戲")
ordering_page.master.geometry("900x600+200+30")
# first_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

ordering_page.mainloop()

