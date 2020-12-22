import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk

class Day1_Operating(tk.Frame):

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
        self.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)

        # 顯示Day 1 
        self.lbl_topic = tk.Label(self, text = "Day1", height = 1, width = 5, font = f1)
        self.lbl_topic.place(x = 26, y = 20)

        # 行事曆按鈕
        def show_calender():
            """
            show calender 等等再研究
            """
            pass

        self.calender = tk.Button(self, command=show_calender(), text="行事曆", width=7, height=2, font=f2, background="Lavender")
        # self.calender.config(background="Lavender")  # 第二種方式

        self.calender.place(x=780, y=10)  # 行事曆封裝

        # 做漢堡的圖片
        global cooking_img
        image = ImageTk.Image.open("C:\\Users\\formo\\Documents\\python files\\finalproject\\PBC_group92\\S__85836045.png")
        image = image.resize((600, 300), ImageTk.Image.ANTIALIAS)
        cooking_img = ImageTk.PhotoImage(image)
        self.panel = tk.Label(self, image = cooking_img)
        self.panel.place(x=150, y=150)
        #panel.pack(side = "bottom", fill = "both", expand = "yes")

        # 顯示 餐廳開始營業囉，點選下一頁查看你今天的營業成果吧~ 
        self.lbl_description = tk.Label(self, text="餐廳開始營業囉，點選下一頁查看你今天的營業成果吧~", height = 2, width = 40, bg="#F3F3F3", fg="black", font=f3)
        self.lbl_description.place(x = 200, y = 30)

        # 下一頁按鈕
        self.btn_next = tk.Button(self, text = "下一頁", command = self.clickBtnRank, height = 2, width = 7, font = f2, bg = 'Lavender')
        self.btn_next.place(x=780, y=480)
        # next_page.config(background="Lavender")  # 第二種方式

        self.btn_next.place(x=780, y=480)

    def clickBtnEnter(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")
    
    def clickBtnRank(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")

operating_page = Day1_Operating()
operating_page.master.title("餐廳經營小遊戲")
operating_page.master.geometry("900x600+200+30")
# first_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

operating_page.mainloop()

"""
# 視窗標題
win.title("餐廳經營小遊戲")

# 視窗大小
win.geometry("900x600+200+30")
win.minsize(width=900, height=600)
#win.maxsize(width=1024, height=768)
"""

# 視窗顏色
# win.config(background="#F3F3F3")