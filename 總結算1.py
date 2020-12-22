import tkinter as tk
import tkinter.font as tkFont

class FinalResultPage1(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createPage()

    def createPage(self):
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體") 
        f3 = tkFont.Font(size = 12, family = "微軟正黑體") 

        # 空表格、標題、下一頁
        self.lbl_gridonly = tk.Label(self, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.lbl_topic = tk.Label(self, text = "總結算1", height = 1, width = 10, font = f1) 
        self.btn_next = tk.Button(self, text = "總結算2", command = self.gotoResult, height = 2, width = 7, font = f2, bg = 'Lavender')
        # 左半邊 折線圖
        self.lbl_descripition = tk.Label(self, text = "營業成果折線圖", height = 1, width = 15, font = f2)
        self.btn_chart = tk.Canvas(self, height = 400, width = 500, bg = 'LightYellow')
        
        #-------------------------------------------------------------------------------------------
        # 空表格、標題、下一頁
        self.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        self.lbl_topic.place(x=300, y=20)
        self.btn_next.place(x=780, y=480)
        # 左半邊 折線圖
        self.lbl_descripition.place(x=350, y=120)
        self.btn_chart.place(x=200, y=160)


    def gotoResult(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")
    


FinalResultPage1 = FinalResultPage1()
FinalResultPage1.master.title("餐廳經營小遊戲")
FinalResultPage1.master.geometry("900x600+200+30")
# week_cal_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon


FinalResultPage1.mainloop()
