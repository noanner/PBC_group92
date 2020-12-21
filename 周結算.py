import tkinter as tk
import tkinter.font as tkFont

class WeelCal(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 20, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體") 
        f3 = tkFont.Font(size = 12, family = "微軟正黑體") 

        self.lbl_topic = tk.Label(self, text = "周結算", height = 2, width = 40, font = f1) 
        self.lbl_descripition = tk.Label(self, text = "折線圖(損益情況、存貨總成本)", height = 1, width = 40, font = f2)
        self.btn_chart = tk.Canvas(self, height = 400, width = 600, bg = 'LightYellow')
        self.btn_next = tk.Button(self, text = "下一頁", command = self.clickBtnRank, height = 1, width = 6, font = f3, bg = 'Lavender')
        
        self.lbl_topic.grid(row = 0, column = 0, columnspan = 2)
        self.lbl_descripition.grid(row = 1, column = 0, columnspan = 2)
        self.btn_chart.grid(row = 2, column = 0, pady = 5)
        self.btn_next.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = tk.SE)
    
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
