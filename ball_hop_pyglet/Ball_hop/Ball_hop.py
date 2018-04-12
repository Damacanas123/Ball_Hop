import class_module as c
import pyglet,kaynak
from pyglet.window import mouse
import random
from win32api import GetSystemMetrics
import fonts # fonts are navigated directly by python
import numpy
import sys,inspect
from pyglet.window import key


#graphics groups
group_0=pyglet.graphics.OrderedGroup(0)
group_1=pyglet.graphics.OrderedGroup(1)
group_2=pyglet.graphics.OrderedGroup(2)



if (GetSystemMetrics (0))/GetSystemMetrics (1)==16/9:
    width,height=1600,900
if (GetSystemMetrics (0))/GetSystemMetrics (1)==4/3:
    width,height=1600,1200
if (GetSystemMetrics (0))/GetSystemMetrics (1)==16/10:
    width,height=1680,1050

window=pyglet.window.Window(width,height,fullscreen=True)


b=pyglet.graphics.Batch()

#back menu variable
preivous_activity=None

#update booleans for different screens
on_activity=False
on_zen_mode=False
on_classic=False
on_basket_downwards=False

#ball hop physics elements
vertical_hit_force = 900
horizontal_hit_force = 25
hit_distance=(60**2)*2

#basket score initial
basket_score=0

#balls
balls=[]
# menu list
menu_list=[]

#save block
current_module = sys.modules[__name__]
path=str(inspect.getfile(current_module))
print(path)
path=path[:(len(path)-36)]#36
print(path)
#basketball time
time=0

try:
    numpy.load(path+r"ball_hop_saves\classic_highscore.npy")
except:
    numpy.save(path+r"ball_hop_saves\classic_highscore",0)
try:
    numpy.load(path+r"ball_hop_saves\unreal_highscore.npy")
except:
    numpy.save(path+r"ball_hop_saves\unreal_highscore",0)



@window.event()
def on_draw():
    pyglet.gl.glClearColor(0.7,0.35,0,1)
    window.clear()
    b.draw()

@window.event()
def on_key_press(symbol,modifiers):
    if symbol==key.ESCAPE:
        if previous_activity == None:
            return pyglet.event.EVENT_HANDLED
        else:
            previous_activity()
            return pyglet.event.EVENT_HANDLED
@window.event()
def on_mouse_motion(x, y, dx, dy):
    if on_activity:
        for element in menu_list:
            if y>= element.y and y<= element.y+element.height and x >= element.x and x <= element.x+element.width:
                element.color=(0,0,0,255)
                element.font_size=element.main_font_size + 20
                element.x,element.y= element.main_position[0]-element.width/10,element.main_position[1]-element.height/7
            else :
                element.color=element.main_color
                element.font_size=element.main_font_size
                element.x,element.y= element.main_position
    if on_basket_downwards:
        global mouse_ball
        mouse_ball.set_position(x, y)
    
@window.event()   
def on_mouse_press(x, y, button, modifiers):
    if on_activity:
        for element in menu_list:
            if y>= element.y and y<= element.y+element.height and x >= element.x and x <= element.x+element.width:
                element.on_enter()
                
    if on_zen_mode:
        if button==mouse.LEFT:
            
            for ball in balls:
                if (x-ball.x)**2 + (y-ball.y)**2 <=hit_distance:
                    
                    ball.hit=True
                    ball.v=[0,0]
                    
                    
                    if (ball.y-y) < 0:
                        ball.hit_force = [(ball.x-x)*horizontal_hit_force,-vertical_hit_force]
                        
                    if (ball.y-y) > 0:
                        ball.hit_force = [(ball.x-x)*horizontal_hit_force,vertical_hit_force]
                        
    if on_classic:
        if button==mouse.LEFT:
            
            for ball in balls:
                if (x-ball.x)**2 + (y-ball.y)**2 <=hit_distance:
                    
                    ball.hit=True
                    ball.v=[0,0]
                    
                    global score
                    score += 1
                    
                    if (ball.y-y) < 0:
                        ball.hit_force = [(ball.x-x)*horizontal_hit_force,-vertical_hit_force]
                        
                    if (ball.y-y) > 0:
                        ball.hit_force = [(ball.x-x)*horizontal_hit_force,vertical_hit_force]                   

def first_activity():
    set_update_booleans_false()
    unschedule()
    global menu_list
    for i in range(len(menu_list)):
        menu_list[0].delete()
        del menu_list[0]
    global balls
    for i in range(len(balls)):
        balls[0].delete()
        del balls[0]
        
    global basket_ball_hoop
    try:
        del basket_ball_hoop
    except:
        pass
        
    global on_activity
    on_activity=True
    
    
    
    global previous_activity
    previous_activity=None
    
    menu_list.append(c.MenuElement(second_activity,
                                   text="PLAY",
                                   font_size=130,
                                   x=width/3,
                                   y=height*2/3,
                                   batch=b,
                                   height=130,
                                   width=500,
                                   align="center",))
    menu_list.append(c.MenuElement(window.close,
                                   text="EXIT",
                                   font_size= 50,
                                   x=width*5/7,
                                   y=height/6,
                                   batch=b,
                                   height=50,
                                   width=200,
                                   align="center",
                                   ))
    menu_list.append(c.MenuElement(high_scores,
                                   text="HIGH SCORES",
                                   font_size= 70,
                                   x=width/7,
                                   y=height/6,
                                   batch=b,
                                   height=100,
                                   width=700,
                                   align="center"))
    


def high_scores():
    set_update_booleans_false()
    unschedule()
    global menu_list
    for i in range(len(menu_list)):
        menu_list[0].delete()
        del menu_list[0]
    global balls
    for i in range(len(balls)):
        balls[0].delete()
        del balls[0]
        
    global basket_ball_hoop
    try:
        del basket_ball_hoop
    except:
        pass
    
    global previous_activity
    previous_activity=first_activity  
        
    menu_list.append(pyglet.text.Label(text="CLASSIC ="+" "+str(numpy.load(path+r"ball_hop_saves\classic_highscore.npy")),
                                       font_size=50,
                                       font_name="HelloHandMeDown",
                                       x=width*1/7,
                                       y=height*5/6,
                                       batch=b))
    menu_list.append(pyglet.text.Label(text="UNREAL BASKET ="+" "+str(numpy.load(path+r"ball_hop_saves\unreal_highscore.npy")),
                                       font_size=50,
                                       font_name="HelloHandMeDown",
                                       x=width*1/7,
                                       y=height*3/6,
                                       batch=b))
    

def second_activity():
    set_update_booleans_false()
    unschedule()
    global menu_list
    for i in range(len(menu_list)):
        menu_list[0].delete()
        del menu_list[0]
    global balls
    for i in range(len(balls)):
        balls[0].delete()
        del balls[0]
        
    global basket_ball_hoop
    try:
        del basket_ball_hoop
    except:
        pass
        
    global on_activity
    on_activity=True
    
    global previous_activity
    previous_activity=first_activity
    
    menu_list.append(c.MenuElement(classic,
                                   text="CLASSIC",
                                   font_size=70,
                                   x=width/7,
                                   y=height*8/9,
                                   batch=b,
                                   height=70,
                                   width=400,
                                   align="center"))

    menu_list.append(c.MenuElement(zen_mode,
                                   text="ZEN",
                                   font_size=70,
                                   x=width*5/8,
                                   y=height/8,
                                   batch=b,
                                   height=70,
                                   width=400,
                                   align="center"))
    menu_list.append(c.MenuElement(basket_downwards,
                                   text="UNREAL BASKET",
                                   font_size=70,
                                   x=width*2/7,
                                   y=height*3/9,
                                   batch=b,
                                   height=70,
                                   width=800,
                                   align="center"))


    
    
    
def classic():
    set_update_booleans_false()
    unschedule()
    global menu_list
    for i in range(len(menu_list)):
        menu_list[0].delete()
        del menu_list[0]
    global balls
    for i in range(len(balls)):
        balls[0].delete()
        del balls[0]
        
    global basket_ball_hoop
    try:
        del basket_ball_hoop
    except:
        pass
    
    global on_classic
    on_classic=True
    
    global previous_activity
    previous_activity=second_activity
    
    global score
    score = 0
    
    
    score_label=pyglet.text.Label(text="",
                           font_size=40,
                           x=width/3,
                           y=height*5/7,
                           font_name="HelloHandMeDown",
                           batch=b,
                           group=group_1)
    menu_list.append(score_label)
    ball=c.classicBall(img=kaynak.red_ball,
                       x=width/2,
                       y=height/2,
                       batch=b,
                       window_dimension=window.get_size(),
                       group=group_0)
    ball._set_color((50,50,50))
    balls.append(ball)
    
    pyglet.clock.schedule_interval(classic_update, 1/120,ball,score_label)
    
def classic_update(dt,ball,score_label):
    global score
    if ball.update(dt)==True:
        score = 0
    score_label.text=("Score :"+ " "+ str(score))
    classic_highscore=numpy.load(path+r"ball_hop_saves\classic_highscore.npy")
    
    if score > classic_highscore:
        numpy.save(path+r"ball_hop_saves\classic_highscore",score)
        
    
        
    
def zen_mode():
    set_update_booleans_false()
    unschedule()
    global menu_list
    for i in range(len(menu_list)):
        menu_list[0].delete()
        del menu_list[0]
    global balls
    for i in range(len(balls)):
        balls[0].delete()
        del balls[0]
        
    global basket_ball_hoop
    try:
        del basket_ball_hoop
    except:
        pass
    
    global on_zen_mode
    on_zen_mode=True
    
    global previous_activity
    previous_activity=second_activity
    
    for i in range(10):
        x=random.randrange(window.get_size()[0])
        y=random.randrange(window.get_size()[1])
        ball=c.Ball(img=kaynak.ball,x=x,y=y,batch=b,window_dimension=window.get_size())
        red=random.randrange(255)
        blue=random.randrange(255)
        green=random.randrange(255)
        ball._set_color((red,blue,green))
        balls.append(ball)
    
    pyglet.clock.schedule_interval(zen_mode_update, 1/120)
    
def zen_mode_update(dt):
    for o in balls:
        o.update(dt,balls,10)    
        
        
            
    
def basket_downwards():
    set_update_booleans_false()
    unschedule()
    global menu_list
    for i in range(len(menu_list)):
        menu_list[0].delete()
        del menu_list[0]
    global balls
    for i in range(len(balls)):
        balls[0].delete()
        del balls[0]
        
    global basket_ball_hoop
    try:
        del basket_ball_hoop
    except:
        pass
    
    global on_basket_downwards
    on_basket_downwards=True
    
    
    
    
    global window
    window.set_mouse_visible(False)
    
    def previous():
        window.set_mouse_visible(True)
        second_activity()
    global previous_activity
    previous_activity=previous
    
    basket_position=[110,400]
    edge_1=[basket_position[0]-90,basket_position[1]+95]
    edge_2=[basket_position[0]+90,basket_position[1]+95]
    
    time_label=pyglet.text.Label(text="40",
                                 font_name="HelloHandMeDown",
                                 x=50,
                                 y=height*7/8,
                                 font_size=40,
                                 batch=b,
                                 group=group_2)
    score_label=pyglet.text.Label(text="0",
                                 font_name="HelloHandMeDown",
                                 x=50,
                                 y=height*15/16,
                                 font_size=40,
                                 batch=b,
                                 group=group_2)
    menu_list.append(time_label)
    menu_list.append(score_label)
    
    
    basket_ball_hoop=c.basketHoop(edge_1=edge_1,edge_2=edge_2,img=kaynak.basket_ball_hoop,batch=b,group=group_2)
    basket_ball_hoop.position=basket_position
    
    
    global mouse_ball
    mouse_ball=pyglet.sprite.Sprite(img=kaynak.basket_ball_2,batch=b,group=group_1)
    balls.append(mouse_ball)
    
    balls.append(c.basketBall(img=kaynak.basket_ball_1,x=400,y=500,batch=b,window_dimension=window.get_size(),group=group_1))
    
    pyglet.clock.schedule_interval(basket_downwards_update, 1/120,balls,basket_ball_hoop,time_label,score_label)
    
def basket_downwards_finish_activity(basket_scor):
    set_update_booleans_false()
    unschedule()
    global menu_list
    for i in range(len(menu_list)):
        menu_list[0].delete()
        del menu_list[0]
    global balls
    for i in range(len(balls)):
        balls[0].delete()
        del balls[0]
        
    global basket_ball_hoop
    try:
        del basket_ball_hoop
    except:
        pass
    
    global basket_score
    basket_score=0
    
    menu_list.append(pyglet.text.Label(text="Your score is : "+str(basket_scor),
                                       font_name="HelloHandMeDown",
                                       font_size=70,
                                       x=50,
                                       y=height/2,
                                       batch=b))
    

    window.set_mouse_visible(True)
    
    global previous_activity
    previous_activity=second_activity
    
    global time
    time=0
    
def basket_downwards_update(dt,balls,basket_ball_hoop,time_label,score_label):
    limit_time=30
    global time
    global basket_score
    time += dt
    time_label.text = str(limit_time-time)[:5]
    
    
    balls[1].update(dt,balls,10)
    if basket_ball_hoop.update(balls[1]):
        basket_score += 1
        score_label.text= str(basket_score)
        balls[1].position=(random.randrange(600,width),random.randrange(500,height))
    balls[1].reference_y=balls[1].y  # to count the score
    if time > limit_time:
        basket_downwards_finish_activity(basket_score)
    if basket_score > numpy.load(path+r"ball_hop_saves\unreal_highscore.npy"):
        numpy.save(path+r"ball_hop_saves\unreal_highscore.npy",basket_score)
    
    
    
    

        

    
def unschedule():
    pyglet.clock.unschedule(zen_mode_update)  
    pyglet.clock.unschedule(classic_update)  
    pyglet.clock.unschedule(basket_downwards_update)  
def set_update_booleans_false():
    global on_activity
    global on_zen_mode
    global on_classic
    global on_basket_downwards
    on_activity=False
    on_zen_mode=False     
    on_classic=False
    on_basket_downwards=False

        

first_activity()
pyglet.app.run()