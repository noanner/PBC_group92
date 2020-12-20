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

        self.lbl_topic = tk.Label(self, text = "總結算", height = 2, width = 40, font = f1) 
        
        # 要接最後的獲利，還有抓歷史還行榜，要排名次
        self.lbl_descripition1 = tk.Label(self, text = "獲利：", height = 1, width = 40, font = f2)
        self.lbl_descripition2 = tk.Label(self, text = "名次：", height = 1, width = 40, font = f2)
        
        # 須依造分數給不一樣的敘述
        self.lbl_descripition3 = tk.Label(self, text = "恭喜您的餐廳榮獲米其林三星殊榮", height = 1, width = 40, font = f2)
        
        self.lbl_descripition4 = tk.Label(self, text = "感謝遊玩", height = 1, width = 40, font = f2)
        self.btn_tips = tk.Button(self, text = "高分秘訣", command = self.clickBtnRank, height = 1, width = 6, font = f3, bg = 'Lavender')
        self.btn_ranking = tk.Button(self, text = "排行榜", command = self.clickBtnRank, height = 1, width = 6, font = f3, bg = 'Lavender')
        self.btn_main = tk.Button(self, text = "回主畫面", command = self.clickBtnRank, height = 1, width = 6, font = f3, bg = 'Lavender')
        
        self.lbl_topic.grid(row = 0, column = 0, columnspan = 3)
        self.lbl_descripition1.grid(row = 1, column = 0, columnspan = 3)
        self.lbl_descripition2.grid(row = 2, column = 0, columnspan = 3)
        self.lbl_descripition3.grid(row = 3, column = 0, columnspan = 3)
        self.lbl_descripition4.grid(row = 4, column = 0, columnspan = 3)
        self.btn_tips.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tk.SE)
        self.btn_ranking.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = tk.S)
        self.btn_main.grid(row = 5, column = 2, padx = 10, pady = 10, sticky = tk.SW)
    
    
    def clickBtnRank(self):
        pass
        #self.lblNum.configure(text = self.lblNum.cget("text") + "1")

    # 缺三個command要做跳轉頁面

first_page = Window()
first_page.master.title("Restaurant Game")
first_page.master.geometry('1000x600')
first_page.master.configure(background = 'Lavender')

# 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon
# header_label = tk.Label(window, text = '餐廳經營管理遊戲')
# header_label.pack()

first_page.mainloop()
