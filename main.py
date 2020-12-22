import tkinter as tk
import tkinter.font as tkFont

class StartPage(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")           

        self.lbl_gridonly = tk.Label(self, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.lbl_topic = tk.Label(self, text = "餐廳經營管理遊戲", height = 2, width = 15, font = f1) 
        self.btn_enter = tk.Button(self, text = "進入遊戲", command = self.clickBtnEnter, height = 2, width = 10, font = f2, bg = 'LightYellow')
        self.btn_rank = tk.Button(self, text = "排行榜", command = self.clickBtnRank, height = 2, width = 10, font = f2, bg = 'Lavender')
        
        self.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        self.lbl_topic.place(x=220, y=100)
        self.btn_enter.place(x=250, y=350)
        self.btn_rank.place(x=500, y=350)
    
    def clickBtnEnter(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")
    
    def clickBtnRank(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")


start_page = StartPage()
start_page.master.title("Restaurant Game")
start_page.master.geometry('900x600+200+30')
# start_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

# header_label = tk.Label(window, text = '餐廳經營管理遊戲')
# header_label.pack()



start_page.mainloop()
