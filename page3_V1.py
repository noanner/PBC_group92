import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

from PIL import Image, ImageTk, ImageSequence

# from PIL import ImageTk
root = Tk()
root.geometry("300x300")
canvas = Canvas(root,width=300, height=300,bg='white')
canvas.pack()
img = []

# 分解gif并逐帧显示
def pick(event):
    global a, flag
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


canvas.bind("<Enter>", pick)  # 这个事件是鼠标进入组件，用什么事件不重要，这里只是演示
root.mainloop()


class Window(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 20, family = "娃娃体-简")
        f2 = tkFont.Font(size = 14, family = "娃娃体-简")

        self.lbl_topic = tk.Label(self, text = "營業說明", height = 1, width = 40, font = f1)
        self.lbl_intro = tk.Label(self, text = "有一個經驗老道的前輩看你辛苦，於是給你提示，讓你的營業額在第一天能有收益，"
                                               "也可以有適當的存貨之後請你依照這個標準進行材料訂購喔~", wraplength = 200,
                                  height = 20, width = 100, font = f2)

        self.btn_enter = tk.Button(self, text = "開始遊戲", command = self.clickBtnRank, height = 2, width = 10, font = f2,
                                   bg = 'LavenderBlush')
        self.image_1 = ImageTk.PhotoImage(file = "restaurant-1.png")
        self.imagelbl_1 = tk.Label(self, image = self.image_1, bg = 'LavenderBlush', height = 100, width = 100)
        self.image_2 = ImageTk.PhotoImage(file = "burger_making.gif")
        self.imagelbl_2 = tk.Label(self, image = self.image_2, bg = 'LavenderBlush', height = 100, width = 100)

        '''background color'''
        self.lbl_topic.configure(bg = 'OldLace')
        self.lbl_intro.configure(bg = 'LavenderBlush')
        '''grid'''
        self.lbl_topic.grid(row = 0, columnspan = 2)
        self.lbl_intro.grid(row = 3, column = 1, sticky = tk.N)
        self.imagelbl_1.grid(row = 1, column = 0)
        self.imagelbl_2.grid(row = 1, column = 1)
        self.btn_enter.grid(row = 4, column = 1, pady = 30)

    def clickBtnEnter(self):
        pass

    def clickBtnRank(self):
        pass


first_page = Window()
first_page.master.title("Restaurant Game")
# first_page.master.geometry('1000x600')
first_page.configure(bg = 'LavenderBlush')
# 粉紫 LavenderBlush # 粉橘 OldLace # 薄荷奶油 MintCream # 淡鵝黃 LightYellow # 淡黃橘LemonChiffon

# header_label = tk.Label(window, text = '餐廳經營管理遊戲')
# header_label.pack()

first_page.mainloop()
