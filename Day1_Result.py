import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk
from tkinter import ttk

class Day1_Result(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()
        self.createTreeview()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        # 空表格、標題、下一頁
        self.lbl_gridonly = tk.Label(self, text = " ", height = 200, width = 300, font = f1) # 製造一個空的grid在底下
        self.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)

        # 顯示 header
        self.lbl_topic = tk.Label(self, text = "Day1", height = 1, width = 5, font = f1)
        self.lbl_topic.place(x = 26, y = 20)
        # self.header = tk.Label(self, text="Day 1", bg="#F3F3F3", fg="black", font=f1)  # Day 1
        # self.header.place(x=26, y=20)

        # self.lb = tk.Label(self, text="辛苦了~下面是你今天營業的成果~~!!", bg="#F3F3F3", fg="black", font=f2)  # 辛苦了
        self.lbl_description = tk.Label(self, text = "辛苦了~下面是你今天營業的成果~~", height = 2, width = 40, font = f3)
        self.lbl_description.place(x = 200, y = 30)
        # lb.place(anchor=tk.CENTER, x=200, y=40) anchor=原點位置

        # 下一頁按鈕
        self.btn_next = tk.Button(self, text = "下一頁", command = self.clickBtnRank, height = 2, width = 7, font = f2, bg = 'Lavender')
        self.btn_next.place(x=780, y=480)

        # 行事曆按鈕
        def show_calender():
            """
            show calender 等等再研究
            """
            pass

        self.calender = tk.Button(self, command=show_calender(), text="行事曆", width=7, height=2, font=f2,background="Lavender")
        # self.calender.config(self, background="Lavender")  # 第二種方式
        self.calender.place(x=780, y=10)  # 行事曆封裝

    def createTreeview(self):
        # 品項表格
        columns = ("牛肉漢堡","豬肉堡堡","雞肉漢堡","生菜堡","生酮堡堡")
        self.tree_item = ttk.Treeview(self, column = columns)  #表格

        self.tree_item.column("#0", minwidth=0, width=110, anchor="center")
        self.tree_item.column("牛肉漢堡",width=80, anchor="center")   #表示列,不顯示
        self.tree_item.column("豬肉堡堡",width=80, anchor="center")
        self.tree_item.column("雞肉漢堡",width=80, anchor="center")
        self.tree_item.column("生菜堡",width=80, anchor="center")
        self.tree_item.column("生酮堡堡",width=80, anchor="center")

        self.tree_item.heading("#0", text="品項")  #顯示錶頭
        self.tree_item.heading("牛肉漢堡",text="牛肉漢堡")
        self.tree_item.heading("豬肉堡堡",text="豬肉堡堡")
        self.tree_item.heading("雞肉漢堡",text="雞肉漢堡")
        self.tree_item.heading("生菜堡",text="生菜堡")
        self.tree_item.heading("生酮堡堡",text="生酮堡堡")

        self.tree_item.insert("",0,text="期初庫存" ,values=("25","25","25","25","25")) #插入資料，
        self.tree_item.insert("",1,text="需求量" ,values=("20","20","20","20","20"))
        self.tree_item.insert("",2,text="賣出數量" ,values=("20","20","20","20","20"))
        self.tree_item.insert("",3,text="營業額" ,values=("400","360","360","240","640"))
        self.tree_item.insert("",4,text="營業額百分比" ,values=("20%","18%","18%","12%","32%"))

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("微軟正黑體", 10))
        style.configure("Treeview", rowheight=50, font=("微軟正黑體", 10))
        # style.configure("Treeview.Heading", font=(None, 12))

        self.tree_item.place(x=60, y=140, height=300)

        # 金額表格
        columns = ("金額")
        self.tree_amount = ttk.Treeview(self, column = columns)  #表格

        self.tree_amount.column("#0", minwidth=0, width=100, anchor="center")
        self.tree_amount.column("金額",width=100, anchor="center")   #表示列,不顯示

        self.tree_amount.heading("#0", text="品項")
        self.tree_amount.heading("金額",text="金額")  #顯示錶頭

        self.tree_amount.insert("",0,text="今日收益" ,values=("2000")) #插入資料，
        self.tree_amount.insert("",1,text="原料成本" ,values=("0"))
        self.tree_amount.insert("",2,text="進貨成本" ,values=("0"))
        self.tree_amount.insert("",3,text="存貨成本" ,values=("50"))
        self.tree_amount.insert("",4,text="本日淨利" ,values=("1950"))

        self.tree_amount.place(x=620, y=140, height=300)
        
    def clickBtnEnter(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")
    
    def clickBtnRank(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")

result_page = Day1_Result()
result_page.master.title("餐廳經營小遊戲")
result_page.master.geometry("900x600+200+30")
# first_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

result_page.mainloop()


# 輸入方框
"""
en = tk.Entry()
en.pack()
"""