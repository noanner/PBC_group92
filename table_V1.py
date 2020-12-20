from tkinter import *
from tkinter import ttk

root = Tk()  # 初始框的声明
columns = ("品項", "成本", "售價")
treeview = ttk.Treeview(root, height = 18, show = "headings", columns = columns)  # 表格

treeview.column("品項", width = 200, anchor = 'center', )
treeview.column("成本", width = 100, anchor = 'center')
treeview.column("售價", width = 100, anchor = 'center')

treeview.heading("品項", text = "品項")  # 显示表头
treeview.heading("成本", text = "成本")
treeview.heading("售價", text = "售價")

treeview.pack(side = LEFT, fill = BOTH)

name = ['牛肉漢堡', '豬肉漢堡', '雞肉漢堡', '生菜堡', '生酮堡']
cost = ['10', '9', '9', '6', '16']
price = cost * 2
for i in range(len(name)):  # 写入数据
    treeview.insert('', i, values = (name[i], cost[i], price[i]))
root.mainloop()  # 进入消息循环
