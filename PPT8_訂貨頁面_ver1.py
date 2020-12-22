import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk
from tkinter import ttk

class EverydayStockPage(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()
        self.createTreeview()
        self.createText()

    def createWidgets(self):
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")
        
        # row0 標題、敘述、行事曆按鈕
        self.lbl_gridonly = tk.Label(self, text = " ", height = 200, width = 30, font = f1) # 製造一個空的grid在底下
        self.lbl_topic = tk.Label(self, text = "Day1", height = 1, width = 5, font = f1)
        self.lbl_description = tk.Label(self, text = "以下是目前的剩餘庫存，請問今天要訂多少貨呢?", height = 2, width = 40, font = f3)
        self.btn_schedule = tk.Button(self, text = "行事曆", command = self.clickBtnSchedule, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        
        # row7 訂貨固定成本、目前訂購總價、訂購按鈕
        self.lbl_fixcost = tk.Label(self, text = " 訂貨固定成本:$50元 ", height = 2, width = 18, font = f2, bg = 'LemonChiffon')
        self.lbl_cost = tk.Button(self, text = "總價試算", command = self.clickBtnCal, height = 2, width = 8, font = f2, bg = 'Lavender')
        self.btn_order = tk.Button(self, text = "訂購!", command = self.clickBtnOrder, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        #-----------------------------------------------------------------------------------------------
        # row0
        self.lbl_gridonly.grid(row = 0, column = 0, columnspan = 10, sticky = tk.NW)
        # self.lbl_topic.grid(row = 0, column = 0, sticky = tk.NW)
        # self.lbl_description.grid(row = 0, column = 1, sticky = tk.NW)
        # self.btn_schedule.grid(row = 0, column = 6, padx = 10, pady = 10)
        self.lbl_topic.place(x = 26, y = 20)
        self.lbl_description.place(x = 200, y = 30)
        self.btn_schedule.place(x = 780, y = 10)
        
        
        # row7
        self.lbl_fixcost.grid(row = 7, column = 1, columnspan = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 15)
        self.lbl_cost.grid(row = 7, column = 4, columnspan = 2, sticky = tk.NW + tk.SE, padx = 1, pady = 15)
        # self.btn_order.grid(row = 7, column = 6, padx = 1, pady = 15)
        self.lbl_fixcost.place(x = 150, y = 480)
        self.lbl_cost.place(x = 511, y = 480)
        self.btn_order.place(x = 780, y = 480)
        
        
        
    def createTreeview(self):    
        
        # 品項表格
        columns = ("訂購單價","剩餘庫存","訂購數量")
        self.tree_item = ttk.Treeview(self, column = columns)  #表格
        
        self.tree_item.column("#0", minwidth=0, width=120, anchor="center")
        self.tree_item.column("訂購單價",width=120, anchor="center")
        self.tree_item.column("剩餘庫存",width=120, anchor="center")
        self.tree_item.column("訂購數量",width=123, anchor="center")


        self.tree_item.heading("#0", text="食材")
        self.tree_item.heading("訂購單價",text="訂購單價")  #顯示錶頭
        self.tree_item.heading("剩餘庫存",text="剩餘庫存")
        self.tree_item.heading("訂購數量",text="訂購數量")


        self.tree_item.insert("",0,text="牛肉漢堡" ,values=("10","剩餘庫存")) #插入資料，
        self.tree_item.insert("",1,text="豬肉漢堡" ,values=("9","剩餘庫存"))
        self.tree_item.insert("",2,text="雞肉漢堡" ,values=("9","剩餘庫存"))
        self.tree_item.insert("",3,text="生菜堡" ,values=("6","剩餘庫存"))
        self.tree_item.insert("",4,text="生酮堡" ,values=("16","剩餘庫存"))

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("微軟正黑體", 10))
        style.configure("Treeview", rowheight=50, font=("微軟正黑體", 10))

        self.tree_item.place(x=150, y=140, height=276)
        
    def createText(self):
        f3 = tkFont.Font(size = 10, family = "微軟正黑體")
        # 輸入表格
        self.txt_beef = tk.Text (self, height = 2, width = 12 , font = f3)
        self.txt_pork = tk.Text (self, height = 2, width = 12 , font = f3)
        self.txt_chick = tk.Text (self, height = 2, width = 12 , font = f3)
        self.txt_vego = tk.Text (self, height = 2, width = 12 , font = f3)
        self.txt_keto = tk.Text (self, height = 2, width = 12 , font = f3)
    
        # 輸入表格
        self.txt_beef.place(x=511, y=165)
        self.txt_pork.place(x=511, y=215)
        self.txt_chick.place(x=511, y=265)
        self.txt_vego.place(x=511, y=315)
        self.txt_keto.place(x=511, y=365)
    
    
    def clickBtnSchedule(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")
    
    def clickBtnOrder(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")

    def clickBtnCal(self):
        self.lblNum.configure(text = self.lblNum.cget("text") + "1")


ordering_page = EverydayStockPage()
ordering_page.master.title("餐廳經營小遊戲")
ordering_page.master.geometry("900x600+200+30")
# first_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

ordering_page.mainloop()

