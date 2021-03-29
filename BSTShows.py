import BST
import tkinter as tk
from tkinter import messagebox
import threading
import time

class Do_BSTree:
    def __init__(self, Numbers, Canvas):    #初始化Do_BSTree类
        Numbers.sort()
        self.The_BST = BST.BST(Numbers[0])
        self.The_BST.Arrange_Numbers(Numbers)
        self.The_BST.root = self.The_BST.Create_BST()
        self.The_Canvas = Canvas
        self.The_Lines = []
        self.The_Ovals = []
        self.The_Texts = []

    def PreOrder_Show(self,root):           #先序遍历实现可视化
        if root.left:
            the_line = self.The_Canvas.create_line((root.centerX, root.centerY),(root.left.centerX,root.left.centerY)) 
            self.The_Lines.append(the_line)
            root.line.append(the_line)
            root.left.line.append(the_line)
            self.PreOrder_Show(root.left)
        if root.right:
            the_line = self.The_Canvas.create_line((root.centerX, root.centerY),(root.right.centerX,root.right.centerY)) 
            self.The_Lines.append(the_line)
            root.line.append(the_line)
            root.right.line.append(the_line)
            self.PreOrder_Show(root.right)
        if root == None:
            return
        the_oval = self.The_Canvas.create_oval(root.centerX - 15, root.centerY - 15, root.centerX + 15, root.centerY + 15, fill='white')
        root.circle.append(the_oval)
        the_text = self.The_Canvas.create_text((root.centerX, root.centerY), text=root.data)
        root.text.append(the_text)
        self.The_Ovals.append(the_oval)
        self.The_Texts.append(the_text)

    def Calc_Show_BST(self,root):           #先序遍历计算每个点的坐标
        if root == None:
            return
        if root.left:
            root.left.centerX = root.centerX - 20 * (2**(root.Nodelevel-1))
            root.left.centerY = root.centerY + 100
            root.left.Nodelevel = root.Nodelevel -1
            self.Calc_Show_BST(root.left)
        if root.right:
            root.left.centerX = root.centerX + 20 * (2**(root.Nodelevel-1))
            root.left.centerY = root.centerY + 100
            root.right.Nodelevel = root.Nodelevel -1
            self.Calc_Show_BST(root.right)

    def Show(self):                         #调用PreOrder_Show()函数实现可视化 
        self.The_BST.LevelOrder()
        self.The_BST.Calc_Show_BST(self.The_BST.root)
        self.PreOrder_Show(self.The_BST.root)

    def Clear(self):                        #撤销当前可视化二叉搜索树
        for temp in self.The_Lines:
             self.The_Canvas.delete(temp)
        for temp in self.The_Ovals:
             self.The_Canvas.delete(temp)
        for temp in self.The_Texts:
             self.The_Canvas.delete(temp)
        
    def Clear_and_Show(self):               #撤销二叉搜索树并再次展示
            self.Show()
            self.Clear()
            self.Show()

    def Add_and_Show(self):                 #根据用户输入，在当前二叉搜索树中进行“增加”操作，并展示
        self.Clear()
        self.The_BST.insert(int(self.Add_e.get()))
        self.Show()

    def Add(self, AddWindow):               #弹出“增加”窗口并获取用户输入
        self.AddWindow = AddWindow
        self.Add_l = tk.Label(self.AddWindow, text='二叉搜索树插入：',font=("华文行楷",12))
        self.Add_l.pack()
        self.Add_l1 = tk.Label(self.AddWindow, text='请输入你要插入的数：',font=("华文行楷",12))
        self.Add_l1.pack()
        self.Add_e = tk.Entry(self.AddWindow)
        self.Add_e.pack()
        self.Add_b = tk.Button(self.AddWindow, text='确定', command=self.Add_and_Show,font=("华文行楷",12))
        self.Add_b.pack()

    def Del_and_Show(self):                 #根据用户输入，在当前二叉搜索树中进行“删除”操作，并展示
        self.Clear()
        self.The_BST.deleteNode(self.The_BST.root, int(self.Del_e.get()))
        if not self.The_BST.finded:
            messagebox.showwarning(title='提示：', message='抱歉，该数据不在本二叉搜索树中')
        self.Show()

    def Del(self, DelWindow):               #弹出“删除”窗口并获取用户输入
        self.DelWindow = DelWindow
        self.Del_l = tk.Label(self.DelWindow, text='二叉搜索树删除：',font=("华文行楷",12))
        self.Del_l.pack()
        self.Del_l1 = tk.Label(self.DelWindow, text='请输入你要删除的数：',font=("华文行楷",12))
        self.Del_l1.pack()
        self.Del_e = tk.Entry(self.DelWindow)
        self.Del_e.pack()
        self.Del_b = tk.Button(self.DelWindow, text='确定', command=self.Del_and_Show,font=("华文行楷",12))
        self.Del_b.pack()

    def Query_and_Show(self):               #根据用户输入，在当前二叉搜索树中进行“查询”操作，并展示
        if self.QueryType.get() == 1:
            messagebox.showinfo(title='查询结果：', message= '当前二叉搜索树数值最小节点为： ' + str(self.The_BST.findMin().data))
        elif self.QueryType.get() == 2:
            messagebox.showinfo(title='查询结果：', message= '当前二叉搜索树数值最大节点为： ' + str(self.The_BST.findMax().data))
        elif self.QueryType.get() == 3:
            messagebox.showinfo(title='查询结果：', message= '当前二叉搜索树数值共有： ' + str(self.The_BST.lenght()) + ' 个结点')
        elif self.QueryType.get() == 4:
            if self.The_BST.find(int(self.Query_e.get())):
                self.MSGB = messagebox.showinfo(title='查询结果：', message='该元素在二叉搜索树中')
            else:
                self.MSGB = messagebox.showinfo(title='查询结果：', message='该元素不在二叉搜索树中')
                      
    def Query(self, QueryWindow):           #弹出“查询”窗口并获取用户输入
        self.QueryWindow = QueryWindow
        self.QueryType = tk.IntVar(self.QueryWindow)
        self.Query_l = tk.Label(self.QueryWindow, text='二叉搜索树查询：',font=("华文行楷",12))
        self.Query_l.pack()
 
        self.Query_r1 = tk.Radiobutton(self.QueryWindow, text='当前二叉搜索树数值最小节点', variable = self.QueryType, value = 1,font=("华文行楷",12))
        self.Query_r1.pack()

        self.Query_r2 = tk.Radiobutton(self.QueryWindow, text='当前二叉搜索树数值最大节点', variable = self.QueryType, value = 2,font=("华文行楷",12))
        self.Query_r2.pack()
        
        self.Query_r3 = tk.Radiobutton(self.QueryWindow, text='当前二叉搜索树数大小     ', variable = self.QueryType, value = 3,font=("华文行楷",12))
        self.Query_r3.pack()

        self.Query_r4 = tk.Radiobutton(self.QueryWindow, text='查询指定元素是否在二叉搜索树中', variable = self.QueryType, value = 4,font=("华文行楷",12))
        self.Query_r4.pack()

        self.Query_e = tk.Entry(self.QueryWindow)
        self.Query_e.pack()

        self.Query_b = tk.Button(self.QueryWindow, text='确定', command = self.Query_and_Show,font=("华文行楷",12))
        self.Query_b.pack()

    def thread_it(self,func, *args):        #将函数打包进线程，目的是周游可以以动画的形式呈现

        # 创建
        t = threading.Thread(target=func, args=args) 
        # 守护 !!!
        t.setDaemon(True) 
        # 启动
        t.start()
        # 阻塞--卡死界面！
        #t.join()
            
    def Travel_and_Show1(self):             #根据用户输入，在当前二叉搜索树中进行“周游”操作，并展示
        if self.TravelType.get() == 1:
            self.PreTravel_and_Show(self.The_BST.root)
            self.Travel_t.insert('insert', '\n')
        elif self.TravelType.get() == 2:
            self.InTravel_and_Show(self.The_BST.root)
            self.Travel_t.insert('insert', '\n')
        elif self.TravelType.get() == 3:
            self.PostTravel_and_Show(self.The_BST.root)
            self.Travel_t.insert('insert', '\n')
        self.Clear_and_Show()

    def PreTravel_and_Show(self,root):      #先序周游并展示
        if root == None:
            return
        # the_oval = self.The_Canvas.create_oval(root.x0, root.y0, root.x1, root.y1, width=5, outline='red')
        the_oval = self.The_Canvas.create_oval(root.centerX - 15, root.centerY - 15, root.centerX + 15, root.centerY + 15, width=5, outline='red')
        
        self.The_Ovals.append(the_oval)
        self.Travel_t.insert('end', str(root.data) + ' ')
        time.sleep(1)
        the_oval = self.The_Canvas.create_oval(root.centerX - 15, root.centerY - 15, root.centerX + 15, root.centerY + 15, width=5, outline='pink')
        # the_oval = self.The_Canvas.create_oval(root.x0, root.y0, root.x1, root.y1,width = 5,outline = 'pink')
        self.The_Ovals.append(the_oval)       
        self.PreTravel_and_Show(root.left)
        self.PreTravel_and_Show(root.right)

    def InTravel_and_Show(self,root):       #中序周游并展示
        if root == None:
            return
        self.InTravel_and_Show(root.left)
        the_oval = self.The_Canvas.create_oval(root.centerX - 15, root.centerY - 15, root.centerX + 15, root.centerY + 15, width=5, outline='yellow')
        # the_oval = self.The_Canvas.create_oval(root.x0, root.y0, root.x1, root.y1,width = 5,outline = 'yellow')
        self.The_Ovals.append(the_oval)     
        time.sleep(1)
        the_oval = self.The_Canvas.create_oval(root.centerX - 15, root.centerY - 15, root.centerX + 15, root.centerY + 15, width=5, outline='pink')
        # the_oval = self.The_Canvas.create_oval(root.x0, root.y0, root.x1, root.y1,width = 5,outline = 'pink')
        self.The_Ovals.append(the_oval)
        self.Travel_t.insert('end', str(root.data) + ' ')
  

        self.InTravel_and_Show(root.right)
    
    def PostTravel_and_Show(self,root):     #后序周游并展示
        if root == None:
            return
        self.PostTravel_and_Show(root.left)
        self.PostTravel_and_Show(root.right)
        the_oval = self.The_Canvas.create_oval(root.centerX - 15, root.centerY - 15, root.centerX + 15, root.centerY + 15, width=5, outline='blue')
        # the_oval = self.The_Canvas.create_oval(root.x0, root.y0, root.x1, root.y1,width = 5,outline = 'blue')
        self.The_Ovals.append(the_oval)       
        time.sleep(1)
        self.Travel_t.insert('end', str(root.data) + ' ')
        the_oval = self.The_Canvas.create_oval(root.centerX - 15, root.centerY - 15, root.centerX + 15, root.centerY + 15, width=5, outline='pink')
        # the_oval = self.The_Canvas.create_oval(root.x0, root.y0, root.x1, root.y1,width = 5,outline = 'pink')
        self.The_Ovals.append(the_oval)       
    
    def Travel(self, TravelWindow):         #弹出“周游”窗口并获取用户输入
        self.TravelWindow = TravelWindow
        self.TravelType = tk.IntVar(self.TravelWindow)
        self.Travel_l = tk.Label(self.TravelWindow, text='二叉搜索树周游：',font=("华文行楷",12))
        self.Travel_l.pack()
 
        self.Travel_r1 = tk.Radiobutton(self.TravelWindow, text='前序周游', variable = self.TravelType, value = 1,font=("华文行楷",12))
        self.Travel_r1.pack()

        self.Travel_r2 = tk.Radiobutton(self.TravelWindow, text='中序周游', variable = self.TravelType, value = 2,font=("华文行楷",12))
        self.Travel_r2.pack()
        
        self.Travel_r3 = tk.Radiobutton(self.TravelWindow, text='后序周游', variable = self.TravelType, value = 3,font=("华文行楷",12))
        self.Travel_r3.pack()

        self.Travel_b = tk.Button(self.TravelWindow, text='确定', command = lambda :self.thread_it(self.Travel_and_Show1),font=("华文行楷",12))
        self.Travel_b.pack()
 
        self.Travel_l2 = tk.Label(self.TravelWindow, text='周游结果：',font=("华文行楷",12))
        self.Travel_l2.pack()
 
        self.Travel_t = tk.Text(self.TravelWindow, width=30, height=2)
        self.Travel_t.pack()
        self.TravelWindow.mainloop()
