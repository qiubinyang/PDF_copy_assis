import tkinter as tk
from tkinter import scrolledtext
import OCR
import screen_shoot
import pyperclip

def begin(photo=0):
    root = tk.Tk()
    root.title('PDF复制助手 v 1.0--powered by Kevin 邱')
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    width = 1000
    height = 950
    root.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, 10))

    title = tk.Label(root,
        text='PDF复制助手',
        font=('宋体', 12),
        width=15, height=2
        )
    title.pack()


    label1 = tk.Label(root,
        text='输入：',
        font=('宋体', 12, 'bold'),
        width=15, height=2
        )
    label1.pack(fill=tk.NONE, expand=tk.NO, side=tk.TOP, anchor=tk.W, padx=1,pady=10)
    input1 = scrolledtext.ScrolledText(root, bd =1, height=13, width=80, font=12)
    input1.pack()

    label2 = tk.Label(root,
        text='输出：',
        font=('宋体', 12, 'bold'),
        width=15, height=2
        )
    label2.pack(fill=tk.NONE, expand=tk.NO, side=tk.TOP, anchor=tk.W, padx=1,pady=10)
    input2 = scrolledtext.ScrolledText(root, bd=1, height=13, width=80, font=12)
    input2.pack()

    # 放置截图
    if (photo == 1):
        photo = tk.PhotoImage(file='temp.png')
        input1.image_create(tk.INSERT, image=photo)
        ocr = OCR.OCR('temp.png')
        input2.insert(tk.INSERT,ocr)

    def organize():
        input2.delete('0.0', 'end')
        text = input1.get(0.0,tk.END)
        text = text.replace(' ', '')
        text = text.replace('\n', '')
        text = text.replace(',', '，')
        pyperclip.copy(text)
        input2.insert(tk.INSERT,text)

    def shoot():
        root.destroy()
        screen_shoot.begin()

    submit = tk.Button(root,
        text='整理',
        width=15, height=2,
        command=organize)
    submit.pack()

    screen_cut = tk.Button(root,
        text='截图识字',
        width=15, height=2,
        command=shoot)
    screen_cut.pack()


    root.mainloop()