import tkinter
import tkinter.filedialog
import os
from PIL import ImageGrab
from time import sleep
import main
def begin():
    root1 = tkinter.Tk()
    root1.geometry('500x120+400+300')
    root1.resizable(False, False)
    class MyCapture:
        def __init__(self, png):
            self.X = tkinter.IntVar(value=0)
            self.Y = tkinter.IntVar(value=0)
            screenWidth = root1.winfo_screenwidth()
            screenHeight = root1.winfo_screenheight()
            self.top = tkinter.Toplevel(root1, width=screenWidth, height=screenHeight)
            self.top.overrideredirect(True)
            self.canvas = tkinter.Canvas(self.top,bg='white', width=screenWidth, height=screenHeight)
            self.image = tkinter.PhotoImage(file=png)
            self.canvas.create_image(screenWidth//2, screenHeight//2, image=self.image)
            def onLeftButtonDown(event):
                self.X.set(event.x)
                self.Y.set(event.y)
                self.sel = True
            self.canvas.bind('<Button-1>', onLeftButtonDown)
            def onLeftButtonMove(event):
                if not self.sel:
                    return
                global lastDraw
                try:
                    self.canvas.delete(lastDraw)
                except Exception as e:
                    pass
                lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='red')
            self.canvas.bind('<B1-Motion>', onLeftButtonMove)
            def onLeftButtonUp(event):
                self.sel = False
                try:
                    self.canvas.delete(lastDraw)
                except Exception as e:
                    pass
                sleep(0.1)
                left, right = sorted([self.X.get(), event.x])
                top, bottom = sorted([self.Y.get(), event.y])
                pic = ImageGrab.grab((left+1, top+1, right, bottom))
                pic.save('temp.png')
                self.top.destroy()
                root1.destroy()
                main.main(True).show()
            self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
            self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    def buttonCaptureClick():
        root1.state('icon')
        sleep(0.2)
        filename = 'temp.png'
        im = ImageGrab.grab()
        im.save(filename)
        im.close()
        w = MyCapture(filename)
        buttonCapture.wait_window(w.top)
        os.remove(filename)
    label = tkinter.Label(root1,text='切换到的想要截图的窗口，点击下方的截图按钮\n按住鼠标左键框选区域')
    label.place(x=0, y=0, width=500, height=60)
    buttonCapture = tkinter.Button(root1, text='截图', command=buttonCaptureClick,font=10)
    buttonCapture.place(x=200, y=70, width=80, height=30)
    root1.mainloop()