import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk

win = tk.Tk()  # 建立主視窗

class Operating(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")


        # 顯示Day 1 
        f1 = tkFont.Font(size=30, family="微軟正黑體")
        header = tk.Label(text="Day 1", bg="#F3F3F3", fg="black", font=f1)
        header.place(x=26, y=20)

        # 行事曆按鈕
        def show_calender():
            """
            show calender 等等再研究
            """
            pass

        f2 = tkFont.Font(size=14, family="微軟正黑體")
        calender = tk.Button(command=show_calender(), text="行事曆", width=7, height=2, font=f2)
        calender.config(background="Lavender")  # 第二種方式

        calender.place(x=780, y=10)  # 行事曆封裝

        # 做漢堡的圖片
        image = ImageTk.Image.open("C:\\Users\\formo\\Documents\\python files\\finalproject\\PBC_group92\\S__85836045.png")
        image = image.resize((600, 300), ImageTk.Image.ANTIALIAS)
        cooking_img = ImageTk.PhotoImage(image)
        self.panel = tk.Label(win, image = cooking_img)
        self.panel.place(x=150, y=100)
        #panel.pack(side = "bottom", fill = "both", expand = "yes")

        # 顯示Day 1 
        f3 = tkFont.Font(size=15, family="微軟正黑體")
        text1 = tk.Label(text="餐廳開始營業囉，點選下一頁查看你今天的營業成果吧~", bg="#F3F3F3", fg="black", font=f3)
        text1.place(x=200, y=450)

        # 下一頁按鈕
        def go_next_page():
            """
            show calender 等等再研究
            """
            pass

        next_page = tk.Button(text="下一頁", width=7, height=2, font=f2)
        next_page.config(background="Lavender")  # 第二種方式
        next_page.config(command=show_calender())

        next_page.place(x=780, y=480)  # 下一頁按鈕封裝


#win.mainloop()  # 常駐主視窗

# 輸入方框
"""
en = tk.Entry()
en.pack()
"""

operating_page = Operating()
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