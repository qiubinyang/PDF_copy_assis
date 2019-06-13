import tkinter as tk
from tkinter import scrolledtext,ttk
import OCR
import pyperclip
import screen_shoot
from Simplified_Traditional.langconv import Converter

class main():
    def __init__(self,photo=False):
        self.CHINESE_SYMBOL = True
        self.DELETE_SPACE = True
        self.DELETE_WRAP = True
        self.DELETE_TABS = True
        self.CLIPBOARD = True
        self.HALF_WIDTH = 1
        self.SIMPLE = 1
        self.photo = photo
    def show(self):
        root = tk.Tk()
        root.resizable(width=False, height=False)
        root.title('PDF复制助手 v 1.0--powered by Kevin 邱')
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width = 950
        height = 900
        root.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, 10))

        # 菜单栏
        menuBar = tk.Menu(root)
        root.config(menu=menuBar)

        def Config():
            top = tk.Toplevel()
            top.resizable(width=False, height=False)
            top.geometry('%dx%d+%d+%d' % (500, 100, (screenwidth - 500) / 2, (screenheight - 100) / 2))
            top.title('关于')

            msg = "开发中。。。"
            Mes = tk.Label(top, text=msg, font=12)
            Mes.pack()
        def About():
            top = tk.Toplevel()
            top.resizable(width=False, height=False)
            top.geometry('%dx%d+%d+%d' % (500, 100, (screenwidth - 500) / 2, (screenheight - 100) / 2))
            top.title('关于')

            msg = "Kevin 邱 制作\n欢迎反馈和交流：qiubinyang98@163.com"
            Mes = tk.Label(top,text=msg,font=12)
            Mes.pack()
        def Exit():
            root.destroy()

        configMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="开始", menu=configMenu)
        configMenu.add_command(label="设置", command=Config)
        configMenu.add_command(label="退出", command=Exit)

        helpMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="帮助", menu=helpMenu)
        helpMenu.add_command(label="关于", command=About)

        title = tk.Label(root,
                         text='PDF复制助手',
                         font=('宋体', 15, 'bold'),
                         width=15, height=2
                         )
        title.pack()

        frame = tk.Frame(root)
        frame.pack()
        def checkCall(i):
            if i == 0:
                self.CHINESE_SYMBOL = var[i].get()
            elif i == 1:
                self.DELETE_SPACE = var[i].get()
            elif i == 2:
                self.DELETE_WRAP = var[i].get()
            elif i == 3:
                self.DELETE_TABS = var[i].get()
            elif i == 4:
                self.CLIPBOARD = var[i].get()

        checkstr = ["使用中文符号","去除空格","去除换行","去除制表符","自动复制到剪贴板"]
        checkboxs = []
        var = [tk.BooleanVar() for _ in range(len(checkstr))]
        def init(i):
            checkboxs.append(ttk.Checkbutton(frame, text=checkstr[i], variable=var[i],
                                            onvalue=True, offvalue=False,
                                            command=lambda: checkCall(i)))
            checkboxs[i].pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)
            var[i].set(1)
        for i in range(len(checkstr)):
            init(i)

        sub_frame1 = tk.Frame(frame)
        sub_frame1.pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)
        sub_frame2 = tk.Frame(frame)
        sub_frame2.pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)

        def radio1():
            self.HALF_WIDTH = radio_var1.get()
        def radio2():
            self.SIMPLE = radio_var2.get()
        radio_var1 = tk.IntVar()
        ttk.Radiobutton(sub_frame1,text='半角',value=1,variable=radio_var1,command=radio1).pack()
        ttk.Radiobutton(sub_frame1,text='全角',value=0,variable=radio_var1,command=radio1).pack()
        radio_var1.set(1)

        radio_var2 = tk.IntVar()
        ttk.Radiobutton(sub_frame2, text='简体', value=1, variable=radio_var2,command=radio2).pack()
        ttk.Radiobutton(sub_frame2, text='繁体', value=0, variable=radio_var2,command=radio2).pack()
        radio_var2.set(1)

        def paste():
            text = pyperclip.paste()
            input1.insert('insert',text)

        label_frame1 = tk.Frame(root)
        label_frame1.pack(anchor=tk.W)
        label1 = tk.Label(label_frame1,
                          text='贴入复制文字：',
                          font=('宋体', 12, 'bold'),
                          width=15, height=2
                          )
        label1.pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)
        paste_button = ttk.Button(label_frame1, text='从剪贴板中粘贴', command=paste)
        paste_button.pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)
        label0 = tk.Label(label_frame1,
                          text='英文较多建议使用截图识别功能',
                          fg='gray',
                          font=('等线', 9),
                          width=25, height=2
                          )
        label0.pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)
        input1 = scrolledtext.ScrolledText(root, bd=1, height=11, width=75, font=12)
        input1.pack()

        def copy():
            pyperclip.copy(input2.get(0.0, tk.END))
        label_frame2 = tk.Frame(root)
        label_frame2.pack(anchor=tk.W)
        label2 = tk.Label(label_frame2,
                          text='整理文字：',
                          font=('宋体', 12, 'bold'),
                          width=15, height=2
                          )
        label2.pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)
        copy_button = ttk.Button(label_frame2,text='复制到剪贴板',command=copy)
        copy_button.pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)
        input2 = scrolledtext.ScrolledText(root, bd=1, height=11, width=75, font=12)
        input2.pack()

        # 放置截图
        if (self.photo):
            photo = tk.PhotoImage(file='temp.png')
            input1.image_create(tk.INSERT, image=photo)
            ocr = OCR.OCR('temp.png')
            input2.insert(tk.INSERT, ocr)

        def organize():
            input2.delete('0.0', 'end')
            text = input1.get(0.0, tk.END)
            text = self.words_process(text)
            input2.insert(tk.INSERT, text)

        def shoot():
            root.destroy()
            screen_shoot.begin()

        submit = ttk.Button(label_frame2,
                           text='整理',
                           # width=15,
                           # font=12,
                           command=organize)
        submit.pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)

        line = tk.Canvas(root, height=30, width=900)
        line.pack()
        line.create_line(0, 20, 900, 20)
        label_frame3 = tk.Frame(root)
        label_frame3.pack(anchor=tk.W)
        label3 = tk.Label(label_frame3,
                          text='使用截图进行文字识别：',
                          font=('宋体', 12, 'bold'),
                          width=30, height=1
                          )
        label3.pack(side=tk.LEFT, anchor=tk.W, expand=tk.YES)


        screen_cut = ttk.Button(root,
                               text='截图识字',
                               width=15,
                               # font=12,
                               command=shoot)
        screen_cut.pack()

        root.mainloop()


    def words_process(self,text):
        if self.DELETE_SPACE:
            text = text.replace(' ', '')
        if self.DELETE_WRAP:
            text = text.replace('\n', '')
        if self.DELETE_TABS:
            text = text.replace('\t', '')
        if self.CHINESE_SYMBOL:
            text = text.replace(',', '，')
        if self.CLIPBOARD:
            pyperclip.copy(text)
        if self.HALF_WIDTH == 1:
            rstring = ""
            for uchar in text:
                inside_code = ord(uchar)
                if inside_code == 12288:  # 全角空格直接转换
                    inside_code = 32
                elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
                    inside_code -= 65248
                rstring += chr(inside_code)
            text = rstring
        else:
            rstring = ""
            for uchar in text:
                inside_code = ord(uchar)
                if inside_code == 32:  # 半角空格直接转化
                    inside_code = 12288
                elif inside_code >= 32 and inside_code <= 126:  # 半角字符（除空格）根据关系转化
                    inside_code += 65248
                rstring += chr(inside_code)
            text = rstring
        if self.SIMPLE == 1:
            text = Converter('zh-hans').convert(text)
        else:
            text = Converter('zh-hant').convert(text)
        return text