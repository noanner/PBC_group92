import tkinter as tk
import tkinter.font as tkFont

class Window(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 20, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體") 
        f3 = tkFont.Font(size = 12, family = "微軟正黑體") 

        self.lbl_topic = tk.Label(self, text = "高分秘訣", height = 2, width = 40, font = f1) 

        self.psystem = tk.Label(self,
        text = "P系統\n採定量訂購方式，又稱定量管制系統。存貨量時時審核、更新，一旦量降到最低水準(訂購點s)時，即開始訂購一固定數量Q，故又稱為(s,Q)制或定貨點制。此存貨控制系統的優點是：",
        height = 10, width = 25, font = f2, bg = 'LightYellow', wraplength = 300)

        self.qsystem = tk.Label(self,
        text = "Q系統\n",
        height = 10, width = 25, font = f2, bg = 'OldLace', wraplength = 300)
        
        self.btn_total_statement = tk.Button(self, text = "總結算", command = self.clickBtnRank, height = 1, width = 6, font = f3, bg = 'Lavender')
        self.btn_ranking = tk.Button(self, text = "排行榜", command = self.clickBtnRank, height = 1, width = 6, font = f3, bg = 'Lavender')
        self.btn_main = tk.Button(self, text = "回主畫面", command = self.clickBtnRank, height = 1, width = 6, font = f3, bg = 'Lavender')
        
        self.lbl_topic.grid(row = 0, column = 0, columnspan = 6)
        self.psystem.grid(row = 1, column = 1, columnspan = 2)
        self.qsystem.grid(row = 1, column = 3, columnspan = 2)
        self.btn_total_statement.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = tk.SE)
        self.btn_ranking.grid(row = 2, column = 2, columnspan = 2, padx = 10, pady = 10, sticky = tk.S)
        self.btn_main.grid(row = 2, column = 4, columnspan = 2, padx = 10, pady = 10, sticky = tk.SW)
    
    
    def clickBtnRank(self):
        pass
        #self.lblNum.configure(text = self.lblNum.cget("text") + "1")

    # 缺三個command要做跳轉頁面

# 名字要改一下
first_page = Window()
first_page.master.title("Restaurant Game")
first_page.master.geometry('1000x600')
first_page.master.configure(background = 'Lavender')

# 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon
# header_label = tk.Label(window, text = '餐廳經營管理遊戲')
# header_label.pack()

first_page.mainloop()
