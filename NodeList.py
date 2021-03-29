from tkinter import messagebox
# 定义node类
class Node:
    def __init__(self, value_=None):
        self._value = value_
        self._next = None

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, new_value):
        self._value = new_value

    def setNext(self, new_next):
        self._next = new_next


# 定义链表类
class LinkedList:
    """
    属性：
        _head 链表头
        _tail 链表尾
        _length 链表长度
    方法：
        length() 返回链表长度
        notEmpty() 判断链表是否为空
        getAll() 打印当前链表

        add() 在链表头增加元素
        append() 在链表尾添加元素
        insert() 指定位置插入元素

        remove_target() 指定节点，删除改元素
        remove_one() 指定元素，删除第一个匹配节点
        remove() 指定元素，删除所有匹配节点

        alert() 修改元素

        search() 判断元素是否在链表中
        index() 返回指定元素的索引
        element() 返回指定索引的元素
    """
    def __init__(self):
        self._head = Node()
        self._tail = self._head
        self._length = 1

    def length(self):
        return self._length

    def notEmpty(self):
        if self._tail == self._head:
            return False
        else:
            return True

    def getAll(self):
        current = self._head
        linkedlist = []
        while current:
            linkedlist.append(current.getValue())
            current = current.getNext()
        return linkedlist

    def add(self, value):
        newnode = Node(value)
        self._length += 1
        if not self.notEmpty():
            self._head.setNext(newnode)
            self._tail = Node()
            self._length += 1
            newnode.setNext(self._tail)
        else:
            newnode.setNext(self._head.getNext())
            self._head.setNext(newnode)

    def append(self, value):
        newnode = Node(value)
        self._length += 1
        if not self.notEmpty():
            self._head.setNext(newnode)
            self._tail = Node()
            self._length += 1
            newnode.setNext(self._tail)
        else:
            current = self._head
            while current.getNext() != self._tail:
                current = current.getNext()
            newnode.setNext(self._tail)
            current.setNext(newnode)

    def insert(self, pos, value):
        if pos <= 0:
            self.add(value)
        elif pos >= self.length()-1:
            self.append(value)
        else:
            temp = Node(value)
            self._length += 1

            current = self._head
            count = 0
            while count < pos:
                current = current.getNext()
                count += 1
            temp.setNext(current.getNext())
            current.setNext(temp)

    def remove_target(self, index):
        current = self._head.getNext()
        pre = self._head
        count = 0
        if index < 0 or index >= self.length():
            messagebox.showwarning(title='提示：', message='抱歉，索引超出范围！')
            return
        else:
            while count != index:
                pre = current
                current = current.getNext()
                count += 1
            pre.setNext(current.getNext())
            self._length -= 1

    def remove_one(self, value):
        current = self._head.getNext()
        pre = self._head
        found = False
        while current:
            if current.getValue() == value:
                pre.setNext(current.getNext())
                self._length -= 1
                found  = True
                break
            else:
                pre = current
                current = current.getNext()
        if not found:
            messagebox.showwarning(title='提示：', message='抱歉，该数据不在链表中')            

    def remove(self, value):
        current = self._head.getNext()
        pre = self._head
        found = False
        while current:
            if current.getValue() == value:
                pre.setNext(current.getNext())
                self._length -= 1
                current = current.getNext()
                found  = True
            else:
                pre = current
                current = current.getNext()
        if not found:
            messagebox.showwarning(title='提示：', message='抱歉，该数据不在链表中')
            
    def alter(self, index, value):
        if index <= 0 or index >= self.length():
            messagebox.showwarning(title='提示：', message='抱歉，索引超出范围！')
            return 
        else:
            current = self._head
            count = -1
            while count != index:
                current = current.getNext()
                count += 1
            current.setValue(value)

    def search(self, value):
        current = self._head
        found = False
        while current and not found:
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, value):
        current = self._head
        count = 0
        found = False
        while current and not found:
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
                count += 1
        if found:
            return count-1
        else:
            return '{} 不在该链表中！'.format(value)

    def element(self, index):
        if index <= 0 or index >= self.length():
            # messagebox.showwarning(title='提示：', message='抱歉，索引超出范围！')
            return '抱歉，索引超出范围！'
        else:
            current = self._head
            count = -1
            while count != index:
                current = current.getNext()
                count += 1
            element = current.getValue()
            return element
    
    def create_NodeList(self, numbers):
        self._head = Node()
        self._tail = self._head
        self._length = 1
        for number in numbers:
            self.append(number)
        return self._head
    
    def Ready_Show_NodeList(self):
        root = self._head
        current = root._next
        x0 = 50
        y0 = 250
        x1 = 80
        y1 = 280
        shows = []
        for i in range(0,self._length-2):
            x0 += 50
            x1 += 50
            coordinate = [x0, y0, x1, y1]
            value = current._value
            show = {'coordinate': coordinate, 'value': value}
            shows.append(show)
            current = current._next
        return shows    
        
