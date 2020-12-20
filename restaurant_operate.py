import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk

win = tk.Tk()  # 建立主視窗

# 視窗標題
win.title("Day1")

# 視窗大小
win.geometry("900x500+200+100")
win.minsize(width=900, height=500)
#win.maxsize(width=1024, height=768)

# 視窗顏色
win.config(background="#F3F3F3")

# 顯示Day 1 
f1 = tkFont.Font(size=32, family="Courier New")
header = tk.Label(text="Day 1", bg="#F3F3F3", fg="black", font=f1)
header.place(x=20, y=20)

# 行事曆按鈕
def show_calender():
    """
    show calender 等等再研究
    """
    pass

calender = tk.Button(text="Calender", width=20, height=5, bd=3)
calender.config(background="skyblue")  # 第二種方式
calender.config(command=show_calender)

calender.pack(side=tk.TOP, anchor=tk.NE)  # 行事曆封裝

# 做漢堡的圖片
image = ImageTk.Image.open("C:\\Users\\formo\\Documents\\python files\\finalproject\\mytest\\S__85836045.png")
image = image.resize((400, 200), ImageTk.Image.ANTIALIAS)
cooking_img = ImageTk.PhotoImage(image)
panel = tk.Label(win, image = cooking_img)
panel.pack()
#panel.pack(side = "bottom", fill = "both", expand = "yes")

# 顯示Day 1 
f3 = tkFont.Font(size=15, family="Courier New")
text1 = tk.Label(text="餐廳開始營業囉，點選下一頁查看你今天的營業成果吧~", bg="#F3F3F3", fg="black", font=f3)
text1.place(x=200, y=350)

# 下一頁按鈕
def go_next_page():
    """
    show calender 等等再研究
    """
    pass

next_page = tk.Button(text="下一頁", width=20, height=5, bd=3)
next_page.config(background="skyblue")  # 第二種方式
next_page.config(command=show_calender)

next_page.pack(side=tk.BOTTOM, anchor=tk.SE)  # 下一頁按鈕封裝


win.mainloop()  # 常駐主視窗

# 輸入方框
"""
en = tk.Entry()
en.pack()
"""