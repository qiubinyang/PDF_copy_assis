import tkinter

import tkinter.filedialog

import os

from PIL import ImageGrab

from time import sleep

import main

def begin():

    root1 = tkinter.Tk()

    #设置窗口大小与位置

    root1.geometry('500x120+400+300')

    #设置窗口大小不可改变

    root1.resizable(False, False)

    #用来显示全屏幕截图并响应二次截图的窗口类

    class MyCapture:

        def __init__(self, png):

            #变量X和Y用来记录鼠标左键按下的位置

            self.X = tkinter.IntVar(value=0)

            self.Y = tkinter.IntVar(value=0)

            #屏幕尺寸

            screenWidth = root1.winfo_screenwidth()

            screenHeight = root1.winfo_screenheight()

            #创建顶级组件容器

            self.top = tkinter.Toplevel(root1, width=screenWidth, height=screenHeight)

            #不显示最大化、最小化按钮

            self.top.overrideredirect(True)

            self.canvas = tkinter.Canvas(self.top,bg='white', width=screenWidth, height=screenHeight)

            #显示全屏截图，在全屏截图上进行区域截图

            self.image = tkinter.PhotoImage(file=png)

            self.canvas.create_image(screenWidth//2, screenHeight//2, image=self.image)

            #鼠标左键按下的位置

            def onLeftButtonDown(event):

                self.X.set(event.x)

                self.Y.set(event.y)

                #开始截图

                self.sel = True

            self.canvas.bind('<Button-1>', onLeftButtonDown)

            #鼠标左键移动，显示选取的区域

            def onLeftButtonMove(event):

                if not self.sel:

                    return

                global lastDraw

                try:

                    #删除刚画完的图形，要不然鼠标移动的时候是黑乎乎的一片矩形

                    self.canvas.delete(lastDraw)

                except Exception as e:

                    pass

                lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='red')

            self.canvas.bind('<B1-Motion>', onLeftButtonMove)

            #获取鼠标左键抬起的位置，保存区域截图

            def onLeftButtonUp(event):

                self.sel = False

                try:

                    self.canvas.delete(lastDraw)

                except Exception as e:

                    pass

                sleep(0.1)

                #考虑鼠标左键从右下方按下而从左上方抬起的截图

                left, right = sorted([self.X.get(), event.x])

                top, bottom = sorted([self.Y.get(), event.y])

                pic = ImageGrab.grab((left+1, top+1, right, bottom))

                #弹出保存截图对话框

                # fileName = tkinter.filedialog.asksaveasfilename(title='保存截图', filetypes=[('image', '*.jpg *.png')])

                # if fileName:

                pic.save('temp.png')

                #关闭当前窗口

                self.top.destroy()
                root1.destroy()
                main.begin(1)

            self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)

    #让canvas充满窗口，并随窗口自动适应大小

            self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

     #开始截图

    def buttonCaptureClick():

        #最小化主窗口

        root1.state('icon')

        sleep(0.2)

        filename = 'temp.png'

    #grab()方法默认对全屏幕进行截图

        im = ImageGrab.grab()

        im.save(filename)

        im.close()

        #显示全屏幕截图

        w = MyCapture(filename)

        buttonCapture.wait_window(w.top)

        #截图结束，恢复主窗口，并删除临时的全屏幕截图文件

        # root1.state('normal')

        os.remove(filename)

    label = tkinter.Label(root1,text='切换到的想要截图的窗口，点击下方的截图按钮\n按住鼠标左键框选区域')
    label.place(x=0, y=0, width=500, height=60)

    buttonCapture = tkinter.Button(root1, text='截图', command=buttonCaptureClick,font=10)

    buttonCapture.place(x=200, y=70, width=80, height=30)

    #启动消息主循环

    root1.mainloop()