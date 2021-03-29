import NodeList
import tkinter as tk
from tkinter import messagebox

class Do_NodeList:
    def __init__(self, Numbers, Canvas):    #初始化Do_NodeList类
        self.The_NodeList = NodeList.LinkedList()
        self.The_NodeList._head = self.The_NodeList.create_NodeList(Numbers)
        self.The_Canvas = Canvas
        self.The_Lines = []
        self.The_Ovals = []
        self.The_Texts = []

    def Show(self):                         #可视化链表
        Ready = self.The_NodeList.Ready_Show_NodeList()
        x0, y0, x1, y1 = Ready[0]['coordinate']
        value = Ready[0]['value']
        the_oval = self.The_Canvas.create_oval(x0, y0, x1, y1)
        the_text = self.The_Canvas.create_text((x0 + 15, y0 + 15), text=value)
        self.The_Ovals.append(the_oval)
        self.The_Texts.append(the_text)
        
        for temp in Ready[1:]:
            x0, y0, x1, y1 = temp['coordinate']
            value = temp['value']
            the_line = self.The_Canvas.create_line(x0 - 20, (y0 + y1) / 2, x0, (y0 + y1) / 2, arrow=tk.LAST)
            the_oval = self.The_Canvas.create_oval(x0, y0, x1, y1)
            the_text = self.The_Canvas.create_text((x0 + 15, y0 + 15), text=value)
            self.The_Lines.append(the_line)
            self.The_Ovals.append(the_oval)
            self.The_Texts.append(the_text)

    def Clear(self):                        #撤销当前可视化链表
        for temp in self.The_Lines:
             self.The_Canvas.delete(temp)
        for temp in self.The_Ovals:
             self.The_Canvas.delete(temp)
        for temp in self.The_Texts:
             self.The_Canvas.delete(temp)

    def Clear_and_Show(self):               #撤销链表并再次展示
            self.Show()
            self.Clear()
            self.Show()

    def Add_and_Show(self):                 #根据用户输入，在当前链表中进行“增加”操作，并展示
        self.The_NodeList.insert(int(self.Add_e2.get()),int(self.Add_e1.get()))
        self.Clear_and_Show()

    def Add(self, Addwindow):               #弹出“增加”窗口并获取用户输入
        self.AddWindow = Addwindow
        self.Add_l = tk.Label(self.AddWindow, text='链表插入：',font=("华文行楷",12))
        self.Add_l.pack()
        self.Add_l1 = tk.Label(self.AddWindow, text='请输入你要插入的数：',font=("华文行楷",12))
        self.Add_l1.pack()
        self.Add_e1 = tk.Entry(self.AddWindow)
        self.Add_e1.pack()
        self.Add_l2 = tk.Label(self.AddWindow, text='请输入你要插入的位置：',font=("华文行楷",12))
        self.Add_l2.pack()
        self.Add_l3 = tk.Label(self.AddWindow, text='（输入小于0时插入到链表头，\n大于链表长度时插入到链表尾）',font=("华文行楷",12))
        self.Add_l3.pack()
        self.Add_e2 = tk.Entry(self.AddWindow)
        self.Add_e2.pack()
        self.Add_b = tk.Button(self.AddWindow, text='确定', command=self.Add_and_Show,font=("华文行楷",12))
        self.Add_b.pack()

    def Del_and_Show(self):                 #根据用户输入，在当前链表中进行“删除”操作，并展示
        if self.DelType.get() == 1:
            self.The_NodeList.remove_target(int(self.Del_e.get()))
        elif self.DelType.get() == 2:
            self.The_NodeList.remove_one(int(self.Del_e.get()))
        elif self.DelType.get() == 3:
            self.The_NodeList.remove(int(self.Del_e.get()))
        self.Clear_and_Show()            

    def Del(self, DelWindow):               #弹出“删除”窗口并获取用户输入
        self.DelWindow = DelWindow
        self.DelType = tk.IntVar(self.DelWindow)
        self.Del_l = tk.Label(self.DelWindow, text='链表删除：',font=("华文行楷",12))
        self.Del_l.pack()
        self.Del_r1 = tk.Radiobutton(self.DelWindow, text='指定索引，删除该元素       ', variable = self.DelType, value = 1,font=("华文行楷",12))
        self.Del_r2 = tk.Radiobutton(self.DelWindow, text='指定元素，删除第一个匹配节点', variable = self.DelType, value = 2,font=("华文行楷",12))        
        self.Del_r3 = tk.Radiobutton(self.DelWindow, text='指定元素，删除所有匹配节点  ', variable=self.DelType, value=3,font=("华文行楷",12))
        self.Del_r1.pack()
        self.Del_r2.pack()
        self.Del_r3.pack()
        self.Del_e = tk.Entry(self.DelWindow)
        self.Del_e.pack()
        self.Del_b = tk.Button(self.DelWindow, text='确定', command = self.Del_and_Show,font=("华文行楷",12))
        self.Del_b.pack()

    def Change_and_Show(self):              #根据用户输入，在当前链表中进行“更改”操作，并展示
        self.The_NodeList.alter(int(self.Change_e1.get()),int(self.Change_e2.get()))
        self.Clear_and_Show()

    def Change(self, ChangeWindow):         #弹出“更改”窗口并获取用户输入
        self.ChangeWindow = ChangeWindow
        self.Change_l = tk.Label(self.ChangeWindow, text='链表修改：',font=("华文行楷",12))
        self.Change_l.pack()
        self.Change_l1 = tk.Label(self.ChangeWindow, text='请输入你要修改的数的索引：',font=("华文行楷",12))
        self.Change_l1.pack()
        self.Change_e1 = tk.Entry(self.ChangeWindow)
        self.Change_e1.pack()
        self.Change_l2 = tk.Label(self.ChangeWindow, text='请输入修改后的数：',font=("华文行楷",12))
        self.Change_l2.pack()
        self.Change_e2 = tk.Entry(self.ChangeWindow)
        self.Change_e2.pack()
        self.Change_b = tk.Button(self.ChangeWindow, text='确定', command=self.Change_and_Show,font=("华文行楷",12))
        self.Change_b.pack()

    def Query_and_Show(self):               #根据用户输入，在当前链表中进行“查询”操作，并展示
        if self.QueryType.get() == 1:
            if self.The_NodeList.search(int(self.Query_e.get())):
                self.MSGB = messagebox.showinfo(title='查询结果：', message='该元素在链表中')
            else:
                self.MSGB = messagebox.showinfo(title='查询结果：', message='该元素不在链表中')
        elif self.QueryType.get() == 2:
            self.MSGB=messagebox.showinfo(title='查询结果：',message='该元素的索引为： ' + str(self.The_NodeList.index(int(self.Query_e.get()))))
        elif self.QueryType.get() == 3:
            self.MSGB=messagebox.showinfo(title='查询结果：',message='该索引对应的元素为： ' + str(self.The_NodeList.element(int(self.Query_e.get()))))

    def Query(self, QueryWindow):           #弹出“查询”窗口并获取用户输入
        self.QueryWindow = QueryWindow
        self.QueryType = tk.IntVar(self.QueryWindow)
        self.Query_l = tk.Label(self.QueryWindow, text='链表查询：',font=("华文行楷",12))
        self.Query_l.pack()
 
        self.Query_r1 = tk.Radiobutton(self.QueryWindow, text='查询元素是否在链表中', variable = self.QueryType, value = 1,font=("华文行楷",12))
        self.Query_r1.pack()

        self.Query_r2 = tk.Radiobutton(self.QueryWindow, text='查询指定元素的索引  ', variable = self.QueryType, value = 2,font=("华文行楷",12))
        self.Query_r2.pack()
        
        self.Query_r3 = tk.Radiobutton(self.QueryWindow, text='查询指定索引的元素  ', variable = self.QueryType, value = 3,font=("华文行楷",12))
        self.Query_r3.pack()

        self.Query_e = tk.Entry(self.QueryWindow)
        self.Query_e.pack()
        
        self.Query_b = tk.Button(self.QueryWindow, text='确定', command = self.Query_and_Show,font=("华文行楷",12))
        self.Query_b.pack()

