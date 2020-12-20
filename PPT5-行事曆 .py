import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import texttable as tb

# 點擊按鈕後指令
def clickBtnReturn(self):
        lblNum.configure(text = self.lblNum.cget("text"))

admin_content = "經營背景11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"

root = tk.Tk()
root.geometry("800x600")

# canvas =tk.Canvas(root, width =800,height = 600, bg="#fff")
# canvas.place(x = 0, y = 0)

days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]  
events = [1, 2, 3, 4, 5, 6, 7]

# dict1 = {"日期": days, "活動": event}
# calendar = pd.DataFrame(dict1)

# 做行事曆表格時遇到困難，以下是用matplotlib.pyplot做的表格會跳出新視窗
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]  
events = [1, 2, 3, 4, 5, 6, 7]
table_vals = []
table_vals.append(days)
table_vals.append(events)

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')


df = pd.DataFrame(table_vals)
ax.table(cellText=df.values, loc='center')
fig.tight_layout()
plt.show()
"""


# 字體設定
f1 = tkFont.Font(size = 30, family = "微軟正黑體", weight="bold")
f2 = tkFont.Font(size = 14, family = "微軟正黑體") 

# 元件內容
lbl_calendar = tk.Label(root, text = "行事曆", font = f1) 
lbl_admin = tk.Label(root, text = admin_content, font = f2, borderwidth = 2, relief = "ridge", wraplength = 300, justify = 'left')
btn_return = tk.Button(root, text = "返回", command = clickBtnReturn, width = 10,height = 2, font = f2, bg = 'Lavender')

lbl_days = tk.Label(root, text = days, font = f2, borderwidth = 2, relief = "ridge", wraplength = 650)
lbl_events = tk.Label(root, text = events, font = f2, borderwidth = 2, relief = "ridge", wraplength = 650)

        
# 元件位置
lbl_calendar.place(relx= 0.4, rely=0.1, width=120, height=80)
lbl_admin.place(relx= 0.25, rely=0.5, width=350, height=200)
btn_return.place(relx= 0.8, rely=0.8)

lbl_days.place(relx= 0.1, rely=0.25, width=700, height=30)
lbl_events.place(relx= 0.1, rely=0.3, width=700, height=80)

# 遊戲表頭
root.title("Restaurant Game")

root.mainloop()







