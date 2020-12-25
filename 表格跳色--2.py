from tkinter import *
from tkinter.ttk import *

# 網址  https://bbs.csdn.net/topics/396863474


root = Tk()
root.title("ch18_6")

stateCity = {"伊利诺":"芝加哥","加州":"洛杉矶",
             "德州":"休斯顿","华盛顿州":"西雅图",
             "江苏":"南京","山东":"青岛",
             "广东":"广州","福建":"厦门"}

tree = Treeview(root,columns=("cities"))

tree.heading("#0",text="State")
tree.heading("cities",text="City")

tree.column("cities",anchor=CENTER)
tree.tag_configure("evenColor",background="lightblue")  # 設定顏色
rowCount = 1

for state in stateCity.keys():
    if rowCount % 2 == 1:
        tree.insert("",index=END,text=state,values=stateCity[state])
    else:
        tree.insert("",index=END,text=state,values=stateCity[state],tags=("evenColor"))  # tag變色的地方
    rowCount += 1

tree.pack()

root.mainloop()