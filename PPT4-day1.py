import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk

root = tk.Tk()  # 建立主視窗
know_content = "小知識11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"

class PPT4_Day1(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 元件內容
        lbl_day = tk.Label(text = "Day 1", font = f1) 
        lbl_know = tk.Label(text = know_content, font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left')
        btn_optA = tk.Button(text = "OptA", command = self.clickBtnOptA, width = 7,height = 2, font = f2, bg = 'Lavender')
        btn_optB = tk.Button(text = "OptB", command = self.clickBtnOptB, width = 7,height = 2, font = f2, bg = 'Lavender')
        btn_calendar = tk.Button(text = "行事曆", command = self.clickBtnCalendar, width = 7,height = 2, font = f2, bg = 'Lavender')
        
        # 元件位置
        lbl_day.place(x= 26, y=20, width=100, height=80)
        lbl_know.place(relx= 0.2, rely=0.35, width=350, height=200)
        btn_optA.place(relx= 0.2, rely=0.75)
        btn_optB.place(relx= 0.5, rely=0.75)
        btn_calendar.place(x= 780, y=20)

        # 點擊按鈕後指令
    def clickBtnOptA(self):
        print("aaaaaa")
            
    def clickBtnOptB(self):
        pass

    def clickBtnCalendar(self):
        pass


operating_page = PPT4_Day1()
operating_page.master.title("餐廳經營小遊戲")
operating_page.master.geometry("900x600+200+30")
# first_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

operating_page.mainloop()

