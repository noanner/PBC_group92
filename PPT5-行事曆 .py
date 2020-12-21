import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


root = tk.Tk()  # 建立主視窗
admin_content = "經營背景1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]  
events = [1, 2, 3, 4, 5, 6, 7]

class PPT5_Calendar(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # 字體設定
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")


    # canvas =tk.Canvas(root, width =800,height = 600, bg="#fff")
    # canvas.place(x = 0, y = 0)

        # 元件內容
        lbl_calendar = tk.Label(root, text = "行事曆", font = f1) 
        lbl_admin = tk.Label(root, text = admin_content, font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left')
        btn_return = tk.Button(root, text = "返回", command = self.clickBtnReturn, width = 7,height = 2, font = f2, bg = 'Lavender')

        # 元件位置
        lbl_calendar.place(relx= 0.4, rely=0.1, width=120, height=80)
        lbl_admin.place(relx= 0.25, rely=0.5, width=350, height=200)
        btn_return.place(x= 780, y=480)



    # 行事曆表格
    tree_item=ttk.Treeview(root, selectmode="extended", columns=("Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"))#表格
    style = ttk.Style()
    style.configure(tree_item, font=("微軟正黑體", 14))

    # tree_item.pack(expand=YES, fill=BOTH)
    tree_item["columns"]=("Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7")
    tree_item.column("#0",minwidth=0,width=70, anchor='center')
    tree_item.column("Day 1",minwidth=0,width=100, anchor='center')   #表示列,不顯示
    tree_item.column("Day 2",minwidth=0,width=100, anchor='center')
    tree_item.column("Day 3",minwidth=0,width=100, anchor='center')
    tree_item.column("Day 4",minwidth=0,width=100, anchor='center')
    tree_item.column("Day 5",minwidth=0,width=100, anchor='center')
    tree_item.column("Day 6",minwidth=0,width=100, anchor='center')
    tree_item.column("Day 7",minwidth=0,width=100, anchor='center')

    tree_item.heading("#0",text="Day")
    tree_item.heading("Day 1",text="Day 1")  #顯示表頭
    tree_item.heading("Day 2",text="Day 2")
    tree_item.heading("Day 3",text="Day 3")
    tree_item.heading("Day 4",text="Day 4")
    tree_item.heading("Day 5",text="Day 5")
    tree_item.heading("Day 6",text="Day 6")
    tree_item.heading("Day 7",text="Day 7")

    # tree.heading("#0", text="C/C++ compiler")
    # tree.column("#0", minwidth=0, width=100, stretch=NO)


    tree_item.insert("",1,text="活動", values=events)#插入資料
    tree_item.place(x=50, y=140, height=120)

    
    # 點擊按鈕後指令
    def clickBtnReturn(self):
        lblNum.configure(text = self.lblNum.cget("text"))


operating_page = PPT5_Calendar()
operating_page.master.title("餐廳經營小遊戲")
operating_page.master.geometry("900x600+200+30")
# first_page.master.configure(background = 'Lavender')
 # 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

operating_page.mainloop()








