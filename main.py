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

        self.lbl_topic = tk.Label(self, text = "餐廳經營管理遊戲", height = 10, width = 40, font = f1) 
        self.btn_enter = tk.Button(self, text = "進入遊戲", command = self.clickBtnEnter, height = 2, width = 10, font = f2, bg = 'Lavender')
        self.btn_rank = tk.Button(self, text = "排行榜", command = self.clickBtnRank, height = 2, width = 10, font = f2, bg = 'Lavender')
        self.lbl_topic.grid(row = 0, column = 0, columnspan = 2)
        self.btn_enter.grid(row = 1, column = 0, pady = 30)
        self.btn_rank.grid(row = 1, column = 1, pady = 30)
    
    def clickBtnEnter(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")
    
    def clickBtnRank(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")


first_page = Window()
first_page.master.title("Restaurant Game")
# first_page.master.geometry('1000x600')
first_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

# header_label = tk.Label(window, text = '餐廳經營管理遊戲')
# header_label.pack()



first_page.mainloop()
