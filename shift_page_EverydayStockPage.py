from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt

import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk
from tkinter import ttk
day = ["Day1","Day2","Day3","Day4","Day5","Day6","Day7"]

counts = 0
count_list = []
user_name = ""
material_price = [10, 9, 9, 6, 16]  # 原料價格
order_fixed_cost = 50
stock_list = [0,0,0,0,0]  # 預設存貨
order_cost_list = [0]
stock_cost_list = []
accumulated_profit_list = []
profit_list = []
accumulated_profit = 0


class EverydayStockPage(object):  # Day1~Day6 訂貨畫面 (是否加個計算功能?)
    
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        
        self.beef = StringVar()
        self.pork = StringVar()
        self.chicken = StringVar()
        self.vege = StringVar()
        self.keto = StringVar()
        
        self.createPage()

    def createPage(self):
        global counts
        self.page = Frame(self.root) #建立Frame
        self.page.pack()
        
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        f4 = tkFont.Font(size = 10, family = "微軟正黑體")
        
        # row0 標題、敘述、行事曆按鈕
        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 200, width = 30, font = f1) # 製造一個空的grid在底下
        self.page.lbl_topic = tk.Label(self.page, text = ("Day" + str(counts+1)), height = 1, width = 5, font = f1)
        self.page.lbl_description = tk.Label(self.page, text = "以下是目前的剩餘庫存，請問今天要訂多少貨呢?", height = 2, width = 40, font = f3)
        self.page.btn_schedule = tk.Button(self.page, text = "行事曆", command = self.openCalendar, height = 2, width = 7, font = f2, bg = 'Lavender')

        # row7 訂貨固定成本、目前訂購總價、訂購按鈕
        self.page.lbl_fixcost = tk.Label(self.page, text = " 各品項固定成本:$50元 ", height = 1, width = 18, font = f3, bg = 'LemonChiffon')
        self.page.lbl_note = tk.Label(self.page, text = " 沒有要訂購也要輸入0唷! ", height = 1, width = 18, font = f3, bg = 'LemonChiffon')
        self.page.lbl_cost = tk.Button(self.page, text = "總價試算", command = self.costCalculation, height = 2, width = 8, font = f2, bg = 'Lavender')
        if counts != 2 and counts < 6:
            self.page.btn_order = tk.Button(self.page, text = "訂購!", command = self.orderFinished, height = 2, width = 7, font = f2, bg = 'Lavender')
            self.page.btn_order.place(x = 780, y = 480)
        elif counts == 2:
            self.page.btn_order = tk.Button(self.page, text = "訂購!", command = self.orderFinishedgoto4, height = 2, width = 7, font = f2, bg = 'Lavender')
            self.page.btn_order.place(x = 780, y = 480)
      
        # row0 排版位置
        self.page.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        self.page.lbl_topic.place(x = 26, y = 20)
        self.page.lbl_description.place(x = 200, y = 30)
        self.page.btn_schedule.place(x = 780, y = 10)
        
        # row7 排版位置
        self.page.lbl_fixcost.place(x = 150, y = 480)
        self.page.lbl_note.place(x = 150, y = 520)
        self.page.lbl_cost.place(x = 511, y = 480)
        self.page.btn_order.place(x = 780, y = 480)
        #-----------------------------------------------------------------------------------------------------------
        
        # 品項表格
        columns = ("訂購單價","剩餘庫存","訂購數量")
        self.page.tree_item = ttk.Treeview(self.page, column = columns)  #表格
        
        self.page.tree_item.column("#0", minwidth=0, width=120, anchor="center")
        self.page.tree_item.column("訂購單價",width=120, anchor="center")
        self.page.tree_item.column("剩餘庫存",width=120, anchor="center")
        self.page.tree_item.column("訂購數量",width=123, anchor="center")

        self.page.tree_item.heading("#0", text="食材")
        self.page.tree_item.heading("訂購單價",text="訂購單價")  #顯示錶頭
        self.page.tree_item.heading("剩餘庫存",text="剩餘庫存")
        self.page.tree_item.heading("訂購數量",text="訂購數量")

        self.page.tree_item.insert("",0,text="牛肉漢堡" ,values=("10","剩餘庫存")) #插入資料，
        self.page.tree_item.insert("",1,text="豬肉漢堡" ,values=("9","剩餘庫存"))
        self.page.tree_item.insert("",2,text="雞肉漢堡" ,values=("9","剩餘庫存"))
        self.page.tree_item.insert("",3,text="生菜堡" ,values=("6","剩餘庫存"))
        self.page.tree_item.insert("",4,text="生酮堡" ,values=("16","剩餘庫存"))

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("微軟正黑體", 10))
        style.configure("Treeview", rowheight=50, font=("微軟正黑體", 10))
        self.page.tree_item.place(x=150, y=140, height=276)
        #-----------------------------------------------------------------------------------------------------------
        
        # 讓玩家輸入的表格
        self.page.txt_beef = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_pork = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_chick = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_vego = tk.Text (self.page, height = 2, width = 12 , font = f4)
        self.page.txt_keto = tk.Text (self.page, height = 2, width = 12 , font = f4)
    
        # 輸入的表格 排版位置
        self.page.txt_beef.place(x=511, y=165)
        self.page.txt_pork.place(x=511, y=215)
        self.page.txt_chick.place(x=511, y=265)
        self.page.txt_vego.place(x=511, y=315)
        self.page.txt_keto.place(x=511, y=365)
                
        
    def costCalculation(self):
        global material_price
        global order_fixed_cost
        order_list = []
        total_cost = 0
        beefnum = self.page.txt_beef.get("1.0",END)
        order_list.append(beefnum)
        porknum = self.page.txt_pork.get("1.0",END)
        order_list.append(porknum)
        chickennum = self.page.txt_chick.get("1.0",END)
        order_list.append(chickennum)
        vegenum = self.page.txt_vego.get("1.0",END)
        order_list.append(vegenum)
        ketonum = self.page.txt_keto.get("1.0",END)
        order_list.append(ketonum)
        
        result = "success"
        for order in order_list:
            try:
                order = int(order)
            except ValueError:
                result = "failed"
                break
        if result == "success":
            for i in range(len(order_list)):
                if int(order_list[i]) > 0:
                    total_cost += order_fixed_cost
                    total_cost += int(order_list[i]) * material_price[i]
                else:
                    pass
            showinfo(title="成本計算",message=("總成本為$" + str(total_cost)))
        else:
            showinfo(title="錯誤", message="累了嗎?請輸入正確格式")

    def orderFinished(self):
        global stock_list
        global order_cost_list
        global counts
        order_list = []
        total_cost = 0
        beefnum = self.beef.get()
        order_list.append(beefnum)
        porknum = self.pork.get()
        order_list.append(porknum)
        chickennum = self.chicken.get()
        order_list.append(chickennum)
        vegenum = self.vege.get()
        order_list.append(vegenum)
        ketonum = self.keto.get()
        order_list.append(ketonum)
        
        result = "success"
        for order in order_list:
            try:
                order = int(order)
            except ValueError:
                result = "failed"
                break
        if result == "success":
            for i in range(len(order_list)):
                if int(order_list[i]) > 0:
                    total_cost += order_fixed_cost
                    total_cost += int(order_list[i]) * material_price[i]
                    stock_list[i] += int(order_list[i])
                else:
                    pass
            order_cost_list.append(total_cost)
            counts += 1
            self.page.destroy()
            EverydayPage(root)
        else:
            showinfo(title="錯誤", message="累了嗎?請輸入正確格式")
        


    def orderFinishedgoto4(self):
        global stock_list
        global order_cost_list
        global counts
        order_list = []
        total_cost = 0
        beefnum = self.beef.get()
        order_list.append(beefnum)
        porknum = self.pork.get()
        order_list.append(porknum)
        chickennum = self.chicken.get()
        order_list.append(chickennum)
        vegenum = self.vege.get()
        order_list.append(vegenum)
        ketonum = self.keto.get()
        order_list.append(ketonum)
        
        result = "success"
        for order in order_list:
            try:
                order = int(order)
            except ValueError:
                result = "failed"
                break
        if result == "success":
            for i in range(len(order_list)):
                if int(order_list[i]) > 0:
                    total_cost += order_fixed_cost
                    total_cost += int(order_list[i]) * material_price[i]
                    stock_list[i] += int(order_list[i])
                else:
                    pass
            order_cost_list.append(total_cost)
            counts += 1
            self.page.destroy()
            Day4Page1(root)
        else:
            showinfo(title="錯誤", message="累了嗎?請輸入正確格式")

    def openCalendar(self):
        showinfo(title='行事曆', message='此處放行事曆')


root = Tk()
root.title('小程式')
EverydayStockPage(root)
root.mainloop()
print(user_name)

