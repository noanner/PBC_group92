import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk
from tkinter import ttk

win = tk.Tk()  # 建立主視窗

# 視窗標題
win.title("Day1")

# 視窗大小
win.geometry("900x500+200+100")
win.minsize(width=900, height=500)
#win.maxsize(width=1024, height=768)

# 視窗顏色
win.config(background="#F3F3F3")

# 顯示 header
f1 = tkFont.Font(size=32, family="Courier New")
header = tk.Label(text="Day 1", bg="#F3F3F3", fg="black", font=f1)  # Day 1
header.place(x=20, y=20)

f1 = tkFont.Font(size=10, family="Courier New")
lb = tk.Label(text="辛苦了~下面是你今天營業的成果~~!!", bg="#F3F3F3", fg="black", font=f1)  # 辛苦了...
lb.place(x=200, y=40)
# lb.place(anchor=tk.CENTER, x=200, y=40) anchor=原點位置

# 行事曆按鈕
def show_calender():
    """
    show calender 等等再研究
    """
    pass

calender = tk.Button(text="Calender", width=18, height=4, bd=3)
calender.config(background="skyblue")  # 第二種方式
calender.config(command=show_calender)

calender.pack(side=tk.TOP, anchor=tk.NE)  # 行事曆封裝

# 做漢堡的圖片
#cooking_img = PhotoImage(file="C:\Users\\formo\\Documents\\python files\\finalproject\\mytest\\S__85836045.png")

# 品項表格
tree_item=ttk.Treeview(win)#表格
tree_item["columns"]=("牛肉漢堡","豬肉堡堡","雞肉漢堡","生菜堡","生酮堡堡")
tree_item.column("牛肉漢堡",width=70)   #表示列,不顯示
tree_item.column("豬肉堡堡",width=70)
tree_item.column("雞肉漢堡",width=70)
tree_item.column("生菜堡",width=70)
tree_item.column("生酮堡堡",width=70)

tree_item.heading("牛肉漢堡",text="牛肉漢堡")  #顯示錶頭
tree_item.heading("豬肉堡堡",text="豬肉堡堡")
tree_item.heading("雞肉漢堡",text="雞肉漢堡")
tree_item.heading("生菜堡",text="生菜堡")
tree_item.heading("生酮堡堡",text="生酮堡堡")

tree_item.insert("",0,text="期初庫存" ,values=("25","25","25","25","25")) #插入資料，
tree_item.insert("",1,text="需求量" ,values=("20","20","20","20","20"))
tree_item.insert("",2,text="賣出數量" ,values=("20","20","20","20","20"))
tree_item.insert("",3,text="營業額" ,values=("400","360","360","240","640"))
tree_item.insert("",4,text="營業額百分比" ,values=("20%","18%","18%","12%","32%"))

tree_item.place(x=20, y=140, height=180)

# 金額表格
tree_amount=ttk.Treeview(win)#表格
tree_amount["columns"]=("金額")
tree_amount.column("金額",width=70)   #表示列,不顯示
tree_amount.heading("金額",text="金額")  #顯示錶頭
tree_amount.insert("",0,text="今日收益" ,values=("2000")) #插入資料，
tree_amount.insert("",1,text="原料成本" ,values=("0"))
tree_amount.insert("",2,text="進貨成本" ,values=("0"))
tree_amount.insert("",3,text="存貨成本" ,values=("50"))
tree_amount.insert("",4,text="本日淨利" ,values=("1950"))

tree_amount.place(x=600, y=140, height=180)


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