import tkinter as tk
import tkinter.font as tkFont

class WeelCal(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體") 
        f3 = tkFont.Font(size = 12, family = "微軟正黑體") 

        # 空表格、標題、下一頁
        self.lbl_gridonly = tk.Label(self, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.lbl_topic = tk.Label(self, text = "周結算", height = 1, width = 10, font = f1) 
        self.btn_next = tk.Button(self, text = "下一頁", command = self.clickBtnRank, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        # 左半邊 折線圖
        self.lbl_descripition = tk.Label(self, text = "營業成果折線圖", height = 1, width = 15, font = f2)
        self.btn_chart = tk.Canvas(self, height = 400, width = 600, bg = 'LightYellow')

        # 右半邊 獲利、名次、殊榮
        self.lbl_descripition1 = tk.Label(self, text = "獲利：$100000", height = 1, width = 15, font = f2, anchor = 'w')
        self.lbl_descripition2 = tk.Label(self, text = "名次：3", height = 1, width = 15, font = f2, anchor = 'w')
        self.lbl_descripition3 = tk.Label(self, text = "恭喜您的餐廳榮獲", height = 2, width = 15, font = f2, anchor = 'w', bg = 'OldLace')
        self.lbl_descripition4 = tk.Label(self, text = "米其林三星殊榮", height = 2, width = 15, font = f2, anchor = 'w', bg = 'OldLace')
        # self.lbl_descripition5 = tk.Label(self, text = "感謝遊玩!", height = 1, width = 10, font = f2, anchor = 'w')
        
        #-------------------------------------------------------------------------------------------
        # 空表格、標題、下一頁
        self.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        self.lbl_topic.place(x=300, y=20)
        self.btn_next.place(x=780, y=480)
        
        # 左半邊 折線圖
        self.lbl_descripition.place(x=200, y=120)
        self.btn_chart.place(x=15, y=160)
        
        # 右半邊 獲利、名次、殊榮
        self.lbl_descripition1.place(x=640, y=170)
        self.lbl_descripition2.place(x=640, y=220)
        self.lbl_descripition3.place(x=640, y=270)
        self.lbl_descripition4.place(x=640, y=320)
        # self.lbl_descripition5.place(x=640, y=400)

    def clickBtnEnter(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")
    
    def clickBtnRank(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")


week_cal_page = WeelCal()
week_cal_page.master.title("餐廳經營小遊戲")
week_cal_page.master.geometry("900x600+200+30")
# week_cal_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon


week_cal_page.mainloop()
