

import tkinter as tk
import shows
import BSTShows
import QueueShow
from tkinter import messagebox



class App(tk.Frame):                    #初始化APP类
    def __init__(self, master):
        self.CreateWidgets(master)
        master.after(10, self.move_balll)

    def Show(self):                     #实例化各个类，并调用各个类的show函数，完成数据结构可视化
        self.Numbers = list(map(int, self.e.get().split()))
        if not self.Numbers:
            messagebox.showwarning(title='提示：', message='请输入数据！')
        if self.Choose.get() == 1:
            self.BSTDo = BSTShows.Do_BSTree(self.Numbers, self.c)
            self.BSTDo.Show()
        elif self.Choose.get() == 2:
            self.NodeListDo = shows.Do_NodeList(self.Numbers, self.c)
            self.NodeListDo.Clear_and_Show()
        elif self.Choose.get() == 3:
            self.QueueDo = QueueShow.Do_Queue(self.Numbers, self.c)
            self.QueueDo.The_Queue.ShowQueue()
            self.QueueDo.Show()
    
    def Clear(self):                    #调用各个类的Clear函数，完成撤销操作
        if self.Choose.get() == 1:
            self.BSTDo.Clear()
        elif self.Choose.get() == 2:
            self.NodeListDo.Clear()
        elif self.Choose.get() == 3:
            self.QueueDo.Clear()

    def Clear_All(self):                #清空屏幕
        self.c.destroy()
        self.hbar.destroy()
        self.vbar.destroy()
        self.c = tk.Canvas(self.f3, height=1500, width=1500, bg = 'white',scrollregion=(0,0,1500,1500))
        self.hbar=tk.Scrollbar(self.f3,orient='horizontal')
        self.hbar.pack(side='bottom',fill='x')
        self.hbar.config(command=self.c.xview)     
        self.vbar=tk.Scrollbar(self.f3,orient='vertical')
        self.vbar.pack(side='right',fill='y')
        self.vbar.config(command=self.c.yview)
        self.c.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.c.pack(side='left',expand=True,fill='both')

    def Add(self):                      #调用各个类的Add函数，完成增加操作
        self.AddWindow = tk.Tk()
        self.AddWindow.geometry('300x300')
        self.AddWindow.title('添加')        
        if self.Choose.get() == 1:
            self.BSTDo.Add(self.AddWindow)        
        if self.Choose.get() == 2:
            self.NodeListDo.Add(self.AddWindow)
        if self.Choose.get() == 3:
            self.QueueDo.Add(self.AddWindow)
    
    def Del(self):                      #调用各个类的Del函数，完成删除操作
        if self.Choose.get() == 1:
            self.DelWindow = tk.Tk()
            self.DelWindow.geometry('300x300')
            self.DelWindow.title('删除')            
            self.BSTDo.Del(self.DelWindow)         
        if self.Choose.get() == 2:
            self.DelWindow = tk.Tk()
            self.DelWindow.geometry('300x300')
            self.DelWindow.title('删除')
            self.NodeListDo.Del(self.DelWindow)
        if self.Choose.get() == 3:
            messagebox.showinfo(title='提示：', message='当前出队的数为：' + str(self.QueueDo.Numbers[self.QueueDo.The_Queue.front]))
            self.QueueDo.Numbers[self.QueueDo.The_Queue.front] = None
            self.QueueDo.The_Queue.DeQueue()
            self.QueueDo.The_Queue.ShowQueue()
            self.QueueDo.Clear_and_Show()
    
    def Change(self):                   #调用各个类的Change函数，完成更改操作
        if self.Choose.get() == 1:
            messagebox.showwarning(title='提示：', message='抱歉，二叉搜索树不支持修改数据操作！')
        if self.Choose.get() == 2:
            self.ChangeWindow = tk.Tk()
            self.ChangeWindow.geometry('300x300')
            self.ChangeWindow.title('更改')        
            self.NodeListDo.Change(self.ChangeWindow)
        if self.Choose.get() == 3:
            messagebox.showwarning(title='提示：', message='抱歉，队列不支持修改数据操作！')

    def Query(self):                    #调用各个类的Query函数，完成查询操作      
        if self.Choose.get() == 1:
            self.QueryWindow = tk.Tk()
            self.QueryWindow.geometry('300x300')
            self.QueryWindow.title('查询') 
            self.BSTDo.Query(self.QueryWindow)
        elif self.Choose.get() == 2:
            self.QueryWindow = tk.Tk()
            self.QueryWindow.geometry('300x300')
            self.QueryWindow.title('查询')     
            self.NodeListDo.Query(self.QueryWindow)
        elif self.Choose.get() == 3:
            messagebox.showwarning(title='提示：', message='抱歉，循环队列不支持查询数据操作！')

    def Travel(self):                   #调用Do_BSTree的Travel函数，完成周游操作
        if self.Choose.get() == 1:
            self.TravelWindow = tk.Tk()
            self.TravelWindow.geometry('300x300')
            self.TravelWindow.title('周游')
            self.BSTDo.Travel(self.TravelWindow)
        else:
            messagebox.showwarning(title='提示：', message='抱歉，只有二叉搜索树支持周游数据操作！')

    def CreateWidgets(self, master):    #创建初始化界面
        self.Choose = tk.IntVar(master)

        self.f1 = tk.Frame(master, width=300, height=300, borderwidth=5, relief='groove')
        
        self.f1.place(x=0, y=0)
        self.l1 = tk.Label(self.f1, text='请选择数据结构类型:',font=("华文行楷",15))
        self.l1.place(x = 10 , y = 5)
        self.r1 = tk.Radiobutton(self.f1, text='二叉搜索树', variable=self.Choose, value = 1,font=("华文行楷",12))
        self.r1.place(x = 20 , y = 40)
        self.r2 = tk.Radiobutton(self.f1, text='链表', variable = self.Choose, value = 2,font=("华文行楷",12))
        self.r2.place(x = 20 , y = 70)
        self.r3 = tk.Radiobutton(self.f1, text='循环队列（第一位输入最大长度）', variable=self.Choose, value = 3,font=("华文行楷",12))
        self.r3.place(x = 20 , y = 100)
        self.l2 = tk.Label(self.f1, text='请输入数据,以空格隔开：',font=("华文行楷",12))
        self.l2.place(x = 10 , y = 130)
        self.e = tk.Entry(self.f1, width=30)
        self.e.place(x=20, y=160)
        self.b1 = tk.Button(self.f1, text='确定', command = self.Show,font=("华文行楷",12))
        self.b1.place(x=30, y=190)
        self.b6 = tk.Button(self.f1, text='撤销', command = self.Clear,font=("华文行楷",12))
        self.b6.place(x=90, y=190)
        self.b7 = tk.Button(self.f1, text='清空', command = self.Clear_All,font=("华文行楷",12))
        self.b7.place(x=150, y=190)

        self.f2 = tk.Frame(master, width=300, height=300, borderwidth=5, relief='groove')
        
        self.f2.place(x=0, y=250)
        self.l3 = tk.Label(self.f2, text='请选择你要进行的操作：',font=("华文行楷",15))
        self.l3.place(x = 10 , y = 8)
        self.b2 = tk.Button(self.f2, text='添加', command = self.Add,font=("华文行楷",12))
        self.b2.place(x=60, y=50)
        self.b3 = tk.Button(self.f2, text='删除', command = self.Del,font=("华文行楷",12))
        self.b3.place(x=150, y=50)
        self.b4 = tk.Button(self.f2, text='更改', command = self.Change,font=("华文行楷",12))
        self.b4.place(x=60, y=150)
        self.b5 = tk.Button(self.f2, text='查询', command = self.Query,font=("华文行楷",12))
        self.b5.place(x=60, y=100)
        self.b8 = tk.Button(self.f2, text='周游', command = self.Travel,font=("华文行楷",12))
        self.b8.place(x=150, y=100)

        self.f3 = tk.Frame(master, width=595, height=550, borderwidth=5, relief='groove')
        
        self.f3.pack_propagate(0)
        self.f3.place(x=300, y=0)
        self.c = tk.Canvas(self.f3, height=1500, width=1500, bg = 'white',scrollregion=(0,0,1500,1500))
        self.hbar=tk.Scrollbar(self.f3,orient='horizontal')
        self.hbar.pack(side='bottom',fill='x')
        self.hbar.config(command=self.c.xview)     
        self.vbar=tk.Scrollbar(self.f3,orient='vertical')
        self.vbar.pack(side='right',fill='y')
        self.vbar.config(command=self.c.yview)
        self.c.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.c.pack(side='left',expand=True,fill='both')

    def mouseRelease(self, event):      #鼠标松开判定（用于二叉搜索树拖动）
        tk.Widget.unbind(self.c, "<B1-Motion>")

    def preorder(self, root):           #先序遍历二叉搜索树（用于二叉搜索树拖动）
        """递归实现先序遍历"""
        if root == None:
            return
        j1 = self.mouse_x1 > root.centerX - 15
        j3 = self.mouse_y1 > root.centerY - 15
        j4 = self.mouse_y1 < root.centerY + 15
        j2 = self.mouse_x1 < root.centerX + 15
        # print('root.centerX',root.centerX)
        # print('root.centerY', root.centerY)
        # print('mouse_x1', self.mouse_x1)
        # print('mouse_y1', self.mouse_y1)
        # print(j1)
        # print(j2)
        # print(j3)
        # print(j4)
        # print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        def mouseMove(event):
            self.mouse_x = event.x + 1500*self.hbar.get()[0]
            self.mouse_y = event.y + 1500*self.vbar.get()[0]
            letter_ball_x2 = self.mouse_x
            letter_ball_y2 = self.mouse_y
            for a in root.circle:
                self.c.delete(a)
            for a in root.text:
                self.c.delete(a)
            for a in root.line:
                self.c.delete(a)
            if root.parent:
                l = self.c.create_line((root.centerX, root.centerY), (root.parent.centerX, root.parent.centerY))
                self.BSTDo.The_Lines.append(l)
                root.line.append(l)
                root.parent.line.append(l)
                o = self.c.create_oval(root.parent.centerX - 15, root.parent.centerY - 15, root.parent.centerX + 15, root.parent.centerY + 15,fill = 'white')
                root.parent.circle.append(o)
                self.BSTDo.The_Lines.append(o)
                t = self.c.create_text(root.parent.centerX, root.parent.centerY, text=root.parent.data)
                root.parent.text.append(t)
                self.BSTDo.The_Lines.append(t)
            if root.left:
                l = self.c.create_line((root.centerX, root.centerY),(root.left.centerX,root.left.centerY))
                self.BSTDo.The_Lines.append(l)
                root.line.append(l)
                root.left.line.append(l)
                o = self.c.create_oval(root.left.centerX - 15, root.left.centerY - 15, root.left.centerX + 15, root.left.centerY + 15,fill = 'white')
                root.left.circle.append(o)
                self.BSTDo.The_Lines.append(o)
                t = self.c.create_text(root.left.centerX, root.left.centerY, text=root.left.data)
                root.left.text.append(t)
                self.BSTDo.The_Lines.append(t)
            if root.right:
                l = self.c.create_line((root.centerX, root.centerY),(root.right.centerX,root.right.centerY))
                self.BSTDo.The_Lines.append(l)
                root.line.append(l)
                root.right.line.append(l)
                o = self.c.create_oval(root.right.centerX - 15, root.right.centerY - 15, root.right.centerX + 15, root.right.centerY + 15,fill = 'white')
                root.right.circle.append(o)
                self.BSTDo.The_Lines.append(o)
                t = self.c.create_text(root.right.centerX, root.right.centerY, text=root.right.data)
                root.right.text.append(t)
                self.BSTDo.The_Lines.append(t)
            o = self.c.create_oval(letter_ball_x2 - 15, letter_ball_y2 - 15, letter_ball_x2 + 15, letter_ball_y2 + 15,fill = 'white')
            root.circle.append(o)
            self.BSTDo.The_Lines.append(o)
            t = self.c.create_text(letter_ball_x2, letter_ball_y2, text=root.data)
            root.text.append(t)
            self.BSTDo.The_Lines.append(t)
            root.centerX = letter_ball_x2
            root.centerY = letter_ball_y2

        if j1 and j2 and j3 and j4:
            tk.Widget.bind(self.c, "<B1-Motion>", mouseMove)
            tk.Widget.bind(self.c, "<ButtonRelease-1>", self.mouseRelease)
        self.preorder(root.left)
        self.preorder(root.right)

    def mouseMovee(self, event):        #鼠标拖动判定（用于二叉搜索树拖动）
        self.mouse_x1 = event.x + 1500*self.hbar.get()[0]
        self.mouse_y1 = event.y + 1500 *self.vbar.get()[0]
        self.preorder(self.BSTDo.The_BST.root)

    def move_balll(self, *args):        #鼠标点击判定（用于二叉搜索树拖动）
        tk.Widget.bind(self.c, "<Button-1>", self.mouseMovee)


def main():                             #主函数实例化APP类
    window = tk.Tk()
    window.title('数据结构可视化')
    window.geometry('900x550')
    App(master=window)
    window.mainloop()
    
if __name__ == '__main__':              #调用主函数
    main()














#    messagebox.showinfo(title='欢迎！', message='欢迎使用数据结构可视化软件！')