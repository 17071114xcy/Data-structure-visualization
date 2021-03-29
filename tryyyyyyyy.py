from tkinter import *
 
#1.获取到小圆当前的圆心坐标(x1, y1)
#2.获取到小圆移动的圆心坐标(x2, y2)
#3.把小圆从坐标(x1, y1)移动到坐标(x2, y2)
 
__author__ = {'name' : 'Hongten',
              'mail' : 'hongtenzone@foxmail.com',
              'blog' : 'http://www.cnblogs.com/',
              'QQ': '648719819',
              'created' : '2013-09-20'}
 
class Eay(Frame):

    isBind = False
     
    def createWidgets(self):
        ## The playing field
        self.draw = Canvas(self, width=500, height=500)
 
        #鼠标位置
        self.mouse_x = 450
        self.mouse_y = 250
         
        #圆心坐标(x,y)
        self.oval_zero_x = 250
        self.oval_zero_y = 250
        #外面大圆半径
        self.oval_r = 100
         
        #里面小圆半径
        self.oval_R = 30
 
        self.oval_r1 = self.oval_r - self.oval_R + 0.5
        self.oval_r2 = self.oval_r - self.oval_R - 0.5
 
        #小圆
        self.letter_ball_x1 = 250
        self.letter_ball_y1 = 250
  
        self.ball_over = self.draw.create_oval((self.oval_zero_x - self.oval_R),
                                               (self.oval_zero_y - self.oval_R),
                                               (self.oval_zero_x + self.oval_R),
                                               (self.oval_zero_y + self.oval_R),
                                               fill="red")
 
        self.draw.pack(side=LEFT)
 
    def mouseMove(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        # if self.mouse_x > self.letter_ball_x1 - self.oval_R and self.mouse_x < self.letter_ball_x1 + self.oval_R and self.mouse_y > self.letter_ball_y1 + self.oval_R and self.mouse_y < self.letter_ball_y1 - self.oval_R:
        
        #小圆移动后的坐标
        letter_ball_x2 = self.mouse_x
        letter_ball_y2 = self.mouse_y

        #把小圆从坐标(x1, y1)移动到坐标(x2, y2)
        self.moved_x2 = letter_ball_x2 - self.letter_ball_x1
        self.moved_y2 = letter_ball_y2 - self.letter_ball_y1
        self.draw.move(self.ball_over, int(self.moved_x2), int(self.moved_y2))
        self.letter_ball_x1 = letter_ball_x2
        self.letter_ball_y1 = letter_ball_y2

    def mouseRelease(self, event):
        Widget.unbind(self.draw, "<B1-Motion>")

    def mouseMovee(self, event):
        self.mouse_x1 = event.x
        self.mouse_y1 = event.y
        j1 = self.mouse_x1 > self.letter_ball_x1 - self.oval_R
        j2 = self.mouse_x1 < self.letter_ball_x1 + self.oval_R
        j3 = self.mouse_y1 > self.letter_ball_y1 - self.oval_R
        j4 = self.mouse_y1 < self.letter_ball_y1 + self.oval_R
        if j1 and j2 and j3 and j4:
            Widget.bind(self.draw, "<B1-Motion>", self.mouseMove)
            Widget.bind(self.draw, "<ButtonRelease-1>", self.mouseRelease)

    def move_balll(self, *args):
        Widget.bind(self.draw, "<Button-1>", self.mouseMovee)

    def __init__(self, master=None):
        global letter_ball_x2
        letter_ball_x2 = 0
        global letter_ball_y2
        letter_ball_y2 = 0
         
        Frame.__init__(self, master)
        Pack.config(self)
        self.createWidgets()
        self.after(10, self.move_balll)
 
game = Eay()
 
game.mainloop()