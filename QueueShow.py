import Queue
import tkinter as tk
import math
from tkinter import messagebox

class Do_Queue:
    def __init__(self, Numbers, Canvas):    #初始化Do_Queue类
        self.The_Queue = Queue.SqQueue(Numbers[0])
        self.The_Queue.ShowQueue()
        self.Numbers = [None] * Numbers[0]
        try:
            for i in range(1,len(Numbers)):
                    if (self.The_Queue.EnQueue(Numbers[i])):
                        self.Numbers[i-1] = Numbers[i]
                    else:
                        messagebox.showwarning(title='提示：', message='输入异常！请撤销后再次输入')
                        break
        except:
            messagebox.showwarning(title='提示：', message='输入异常！请撤销后再次输入')

        self.The_Canvas = Canvas
        self.The_Arcs = []
        self.The_Texts = []

    def Show(self):                         #可视化队列
        Rotate_Degree = 360 / self.The_Queue.maxsize
        Now_Degree = 0 
        print('self.Numbers',self.Numbers)
        for i in range(self.The_Queue.maxsize):
            Text_Degree = Now_Degree / 180 * math.pi + Rotate_Degree / 2 / 180 * math.pi
            if i == self.The_Queue.front:          
                The_arc = self.The_Canvas.create_arc(100, 100, 500, 500, start=Now_Degree%360, extent=Rotate_Degree%360, width=3, fill="white",outline = 'blue')
                self.The_Arcs.append(The_arc)
            elif i == self.The_Queue.rear:
                The_arc = self.The_Canvas.create_arc(100, 100, 500, 500, start=Now_Degree%360, extent=Rotate_Degree%360, width=3, fill="white",outline = 'red')
                self.The_Arcs.append(The_arc)
            else:
                The_arc = self.The_Canvas.create_arc(100, 100, 500, 500, start=Now_Degree%360, extent=Rotate_Degree%360, width=1, fill="white")
                self.The_Arcs.append(The_arc)
            if i < len(self.Numbers):
                the_text = self.The_Canvas.create_text(300+150*math.cos(Text_Degree),300-150*math.sin(Text_Degree),text = self.Numbers[i])
            self.The_Texts.append(the_text)
            Now_Degree += Rotate_Degree
        print('rear', self.The_Queue.rear)
        print('front', self.The_Queue.front)
        self.The_Oval = self.The_Canvas.create_oval(200, 200, 400, 400, fill='white', width=1)
        self.The_Oval1 = self.The_Canvas.create_oval(32,450,52,470,fill = 'blue')
        self.The_text1 = self.The_Canvas.create_text(100,460,text = '—— 队头', font=("华文行楷",12))
        self.The_Oval2 = self.The_Canvas.create_oval(32,480,52,500,fill = 'red')
        self.The_text2 = self.The_Canvas.create_text(100,490,text = '—— 队尾', font=("华文行楷",12))

    def Clear(self):                        #撤销当前可视化队列
        for temp in self.The_Arcs:
            self.The_Canvas.delete(temp)
        self.The_Canvas.delete(self.The_Oval)
        self.The_Canvas.delete(self.The_Oval1)
        self.The_Canvas.delete(self.The_Oval2)
        self.The_Canvas.delete(self.The_text1)
        self.The_Canvas.delete(self.The_text2)
        for temp in self.The_Texts:
             self.The_Canvas.delete(temp)

    def Clear_and_Show(self):               #撤销可视化队列并再次展示
            self.Show()
            self.Clear()
            self.Show()

    def Add_and_Show(self):                 #根据用户输入，在当前二叉搜索树中进行“增加”（Push）操作，并展示
        self.Clear()
        if self.The_Queue.EnQueue(int(self.Add_e.get())):
            self.Numbers[(self.The_Queue.rear-1) % (self.The_Queue.maxsize)] = int(self.Add_e.get())        
        self.Show()

    def Add(self, AddWindow):               #弹出“增加”窗口并获取用户输入（pop操作较为简单，在主文件Course_Design中完成操作）
        self.AddWindow = AddWindow
        self.Add_l = tk.Label(self.AddWindow, text='循环队列插入：',font=("华文行楷",12))
        self.Add_l.pack()
        self.Add_l1 = tk.Label(self.AddWindow, text='请输入你要插入的数：',font=("华文行楷",12))
        self.Add_l1.pack()
        self.Add_e = tk.Entry(self.AddWindow)
        self.Add_e.pack()
        self.Add_b = tk.Button(self.AddWindow, text='确定', command=self.Add_and_Show,font=("华文行楷",12))
        self.Add_b.pack()

                                            