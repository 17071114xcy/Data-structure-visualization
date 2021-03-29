from tkinter import messagebox
class SqQueue(object):
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0

    # 返回当前队列的长度
    def QueueLength(self):
        return (self.rear - self.front + self.maxsize) % self.maxsize

    # 如果队列未满，则在队尾插入元素，时间复杂度O(1)
    def EnQueue(self, data):
        if (self.rear + 1) % self.maxsize   == self.front:
            messagebox.showwarning(title='提示：', message='队列已满！')
            return False
            #print("The queue is full!")
        else:
            self.queue[self.rear] = data
           # self.queue.insert(self.rear,data)
            self.rear = (self.rear + 1) % self.maxsize
            return True

    # 如果队列不为空，则删除队头的元素,时间复杂度O(1)
    def DeQueue(self):
        if self.rear == self.front:
            messagebox.showwarning(title='提示：', message='队列已空！')
            return False
            # print("The queue is empty!")
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            return data

    # 输出队列中的元素
    def ShowQueue(self):
        # for i in range(self.maxsize):
        #     print(self.queue[i],end=',')
        # print(' ')
        print(self.queue)

    def CreateQueue(self, Numbers):
        for temp in Numbers:
            self.EnQueue(temp)
