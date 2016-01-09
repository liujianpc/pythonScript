# -*-coding: utf-8 -*-
#!/usr/bin/python
from Tkinter import *
from PIL import ImageTk,Image
import random
import time

'''新建canvas'''
count = 0
tk =Tk()#新建canvas对象tk
tk.title('Game')#窗口名
tk.resizable(0,0)#窗口大小不可调
tk.wm_attributes('-topmost',1)#窗口置于最前
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)#canvas画布设置
im = PhotoImage(file = "bg.gif")
#image = Image.open("pg.gif")
#im = ImageTk.PhotoImage(image)
canvas.create_image(250,200,image = im)
canvas.create_text(30,20,text="分数:",fill = "black",font=("Courier New",14,"bold"))
countId = canvas.create_text(70,20,text=count,fill = "red",font=("Courier New",20)) 
canvas.pack()#打包
tk.update()#更新显示效果


#构建球类
class Ball:
    def __init__(self,canvas,paddle,color):#初始化函数
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)#画出球类，并返回id
        self.canvas.move(self.id,245,100)#移动球类
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)#数组洗牌
        self.x =starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()#获取窗体的高度
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        
    def draw(self):
        global countId
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        global count
        #以下if语句为判断球类是否出界和是否撞击到了板子
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -5
            count = count + 1
            self.canvas.delete(countId)
            countId = self.canvas.create_text(70,20,text=count,fill = "red",font=("Courier New",20))
       
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
          #判断球类是否撞击到了板子
    def hit_paddle(self,pos):
    	paddle_pos = self.canvas.coords(self.paddle.id)
    	if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
    		if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
    			return True
    	return False


#构建板类
class Paddle:
    """docstring for Paddle"""
    def __init__(self, canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
    #绑定键盘按下事件
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    
    def turn_left(self,evt):
        self.x = -3

    def turn_right(self,evt):
        self.x = 3

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
     
paddle = Paddle(canvas,'blue')
ball = Ball(canvas,paddle,'red')

def mouseLeft(evt):
    for x in xrange(3,0,-1):
        textId = canvas.create_text(250,50,text = x,fill = "red",font = ("consolas",20),state="normal")
        #tk.uodate_idletasks()
        tk.update()
        time.sleep(1)
        canvas.delete(textId)
        #canvas.create_text(250,50,text ='',fill = "red",font = ("consolas",20),state="hidden")
        
canvas.bind_all('<Button-1>',mouseLeft)


while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        canvas.create_text(250,50,text="game over",fill = "red",font=("Courier New",30))
        tk.update()
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

#tk.mainloop()
#msg.set("game over")
