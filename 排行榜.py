
# 並不能執行，我只是放一個排行榜的code在這，方便保存跟更改

# =========================================================================================
# ===================================== 排行榜 ===========================================
# =========================================================================================

class RankingPage2(object):
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('900x600+200+30') #設定視窗大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root) #建立Frame # 新增
        self.page.pack() # 新增
        
        f1 = tkFont.Font(size = 30, family = "微軟正黑體")
        f2 = tkFont.Font(size = 14, family = "微軟正黑體")
        f3 = tkFont.Font(size = 12, family = "微軟正黑體")

        self.page.lbl_gridonly = tk.Label(self.page, text = " ", height = 20, width = 30, font = f1)
        self.page.lbl_topic = tk.Label(self.page, text = "排行榜", height = 2, width = 30, font = f1) 
        self.page.psystem = tk.Label(self.page, text = "第一名：", height = 2, width = 30, font = f3, bg = 'LightYellow')
        self.page.qsystem = tk.Label(self.page, text = "第二名：", height = 2, width = 30, font = f3, bg = 'OldLace')
        self.page.btn_main = tk.Button(self.page, text = "回總結算2", command = self.gotoResult2, height = 2, width = 7, font = f2, bg = 'Lavender')
        
        self.page.lbl_topic.grid(row = 0, column = 0)
        self.page.psystem.grid(row = 1, column = 0)
        self.page.qsystem.grid(row = 2, column = 0)
        self.page.btn_main.place(x = 780, y = 480)
        self.page.lbl_gridonly.grid(row = 3, column = 0, sticky = tk.S)
    
    def gotoResult2(self):
        self.page.destroy()
        FinalResultPage2(root)