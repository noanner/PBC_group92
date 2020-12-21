import tkinter as tk
import tkinter.font as tkFont


# 點擊按鈕後指令
def clickBtnOptA(self):
        lblNum.configure(text = self.lblNum.cget("text"))
    
def clickBtnOptB(self):
        lblNum.configure(text = self.lblNum.cget("text"))
    
def clickBtnCalendar(self):
        lblNum.configure(text = self.lblNum.cget("text"))

know_content = "小知識11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"

root = tk.Tk()
root.geometry("900x600+200+30")

# canvas =tk.Canvas(root, width =800,height = 600, bg="#fff")
# canvas.place(x = 0, y = 0)

# 字體設定
f1 = tkFont.Font(size = 30, family = "微軟正黑體")
f2 = tkFont.Font(size = 14, family = "微軟正黑體") 
f3 = tkFont.Font(size = 12, family = "微軟正黑體") 

# 元件內容
lbl_day = tk.Label(root, text = "Day 1", font = f1) 
lbl_know = tk.Label(root, text = know_content, font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left')
btn_optA = tk.Button(root, text = "OptA", command = clickBtnOptA, width = 7,height = 2, font = f2, bg = 'Lavender')
btn_optB = tk.Button(root, text = "OptB", command = clickBtnOptB, width = 7,height = 2, font = f2, bg = 'Lavender')
btn_calendar = tk.Button(root, text = "行事曆", command = clickBtnCalendar, width = 7,height = 2, font = f2, bg = 'Lavender')
        
# 元件位置
lbl_day.place(x= 26, y=20, width=100, height=80)
lbl_know.place(relx= 0.2, rely=0.35, width=350, height=200)
btn_optA.place(relx= 0.2, rely=0.75)
btn_optB.place(relx= 0.5, rely=0.75)
btn_calendar.place(x= 780, y=20)

# 遊戲表頭
root.title("餐廳經營小遊戲")

root.mainloop()







