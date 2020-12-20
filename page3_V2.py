import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

from PIL import Image, ImageTk, ImageSequence

HEIGHT = 500
WIDTH = 600


def switch_function():
    pass


root = tk.Tk()

f1 = tkFont.Font(size = 15, family = "娃娃体-简")
f2 = tkFont.Font(size = 14, family = "娃娃体-简")
# 建立畫布
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()
# 背景圖片填滿畫布
background_image = ImageTk.PhotoImage(file = 'restaurant.jpg')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)
# 建立框架
frame = tk.Frame(root, bg = 'OldLace', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')
# 輸入框
entry = tk.Entry(frame, font = 40)
entry.place(relwidth = 0.65, relx = 0.3, relheight = 1)

button1 = tk.Button(frame, text = "請輸入你的名字：", font = f1, command = switch_function())
button1.place(relx = 0, relheight = 1, relwidth = 0.3, anchor = 'nw')

button2 = tk.Button(root, text = "開始遊戲", font = f1, command = switch_function())
button2.place(relx = 0.7, rely = 0.9, relheight = 0.05, relwidth = 0.1, anchor = 'se')

intro = tk.Label(root, text = "有一個經驗老道的前輩看你辛苦，於是給你提示，讓你的營業額在第一天能有收益，"
                              "也可以有適當的存貨之後請你依照這個標準進行材料訂購喔~", wraplength = 400,
                 font = f2, bg = 'OldLace')
intro.place(relx = 0.5, rely = 0.2, relwidth = 0.75, relheight = 0.15, anchor = 'n')
# 期初存货
inventory = tk.Label(root, text = "期初存貨:\n牛肉漢堡 25個\n豬肉漢堡 25個\n雞肉漢堡 25個\n生菜堡 25個\n生酮堡 25個",
                     font = f2, bg = 'LavenderBlush')
inventory.place(relx = 0.2, rely = 0.4, relwidth = 0.3, relheight = 0.29)

# 建立成本表格
columns = ("品項", "成本", "售價")
treeview = ttk.Treeview(root, height = 15, show = "headings", columns = columns)  # 表格

style_head = ttk.Style()
style_head.configure("Treeview.Heading", font = ("娃娃体-简", 12))

treeview.column("品項", width = 50, anchor = 'center')
treeview.column("成本", width = 50, anchor = 'center')
treeview.column("售價", width = 50, anchor = 'center')

treeview.heading("品項", text = "品項")  # 显示表头
treeview.heading("成本", text = "成本")
treeview.heading("售價", text = "售價")

# treeview.pack(side = LEFT, fill = BOTH)
treeview.place(relx = 0.6, rely = 0.4, relwidth = 0.3, relheight = 0.25)

name = ['牛肉漢堡', '豬肉漢堡', '雞肉漢堡', '生菜堡', '生酮堡']
cost = ['10', '9', '9', '6', '16']
price = ['20', '18', '18', '12', '32']
for i in range(len(name)):  # 写入数据
    treeview.insert('', i, values = (name[i], cost[i], price[i]))
# 會動的漢堡圖
img = []
while 1:
    im = Image.open('burger_making.gif')
    # GIF图片流的迭代器
    iter = ImageSequence.Iterator(im)
    # frame就是gif的每一帧，转换一下格式就能显示了
    for frame in iter:
        pic = ImageTk.PhotoImage(frame)
        canvas.create_image((100, 150), image = pic)
        time.sleep(0.1)
        root.update_idletasks()  # 刷新
        root.update()

root.mainloop()
