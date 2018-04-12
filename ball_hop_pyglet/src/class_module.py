import pyglet
import math

def check_collision(a,b):
    if (a.x-b.x)**2+(a.y-b.y)**2<=((a.width+b.width)/2)**2:
        return True
class classicBall(pyglet.sprite.Sprite):
    def __init__(self,gravity=[0,-15],window_dimension=None, *args, **kwargs):
        super(classicBall, self).__init__(*args, **kwargs)
        self.mass=1
        self.v=[0,0]
        self.window_dimension=window_dimension
        self.gravity = gravity
        self.hit_reference_time = 0
        self.hit= False
        self.hit_force = [0,0]
        self.hit_acceleration = [self.hit_force[0]/self.mass,self.hit_force[1]/self.mass]
        self.net_acceleration = [self.gravity[0]+self.hit_acceleration[0],self.gravity[1]+self.hit_acceleration[1]]
        
    def update(self,dt):
        if self.hit_reference_time > 0.5 and self.hit:
            self.hit_force= [0,0]
            self.hit_reference_time = 0
            self.hit = False
        elif self.hit:
            self.hit_reference_time +=dt
            self.hit_force = [self.hit_force[0]*(0.5-self.hit_reference_time),self.hit_force[1]*(0.5-self.hit_reference_time)]
            
        self.hit_acceleration = [self.hit_force[0]/self.mass,self.hit_force[1]/self.mass]
        self.net_acceleration = [self.gravity[0]+self.hit_acceleration[0],self.gravity[1]+self.hit_acceleration[1]]
        if self.x<self.width/2:
            self.x=self.width/2
            self.hit_acceleration = [-self.hit_acceleration[0],self.hit_acceleration[1]]
            self.v = [-self.v[0]*5/8,self.v[1]*5/8]
        if self.x >self.window_dimension[0]-self.width/2:
            self.x = self.window_dimension[0]-self.width/2
            self.hit_acceleration = [-self.hit_acceleration[0],self.hit_acceleration[1]]
            self.v = [-self.v[0]*5/8,self.v[1]*5/8]
        if self.y < self.height/2:
            self.y=self.height/2
            self.hit_acceleration = [self.hit_acceleration[0],-self.hit_acceleration[1]]
            self.v = [self.v[0]*5/8,-self.v[1]*5/8]
            return True
        if self.y > self.window_dimension[1]-self.height/2:
            self.y=self.window_dimension[1]-self.height/2
            self.hit_acceleration = [self.hit_acceleration[0],-self.hit_acceleration[1]]
            self.v = [self.v[0]*5/8,-self.v[1]*5/8]
        self.v[0] += self.net_acceleration[0]*dt 
        self.v[1] += self.net_acceleration[1]*dt
        
        self.x += self.v[0]
        self.y += self.v[1]
        
        
class Ball(pyglet.sprite.Sprite):
    def __init__(self,gravity=[0,-15],window_dimension=None, *args, **kwargs):
        super(Ball, self).__init__(*args, **kwargs)
        self.mass=1
        self.v=[0,0]
        self.window_dimension=window_dimension
        self.gravity = gravity
        self.hit_reference_time = 0
        self.hit= False
        self.hit_force = [0,0]
        self.hit_acceleration = [self.hit_force[0]/self.mass,self.hit_force[1]/self.mass]
        self.net_acceleration = [self.gravity[0]+self.hit_acceleration[0],self.gravity[1]+self.hit_acceleration[1]]
        
    def update(self,dt,balls,force):
        if self.hit_reference_time > 0.5 and self.hit:
            self.hit_force= [0,0]
            self.hit_reference_time = 0
            self.hit = False
        elif self.hit:
            self.hit_reference_time +=dt
            self.hit_force = [self.hit_force[0]*(0.5-self.hit_reference_time),self.hit_force[1]*(0.5-self.hit_reference_time)]
            
        self.hit_acceleration = [self.hit_force[0]/self.mass,self.hit_force[1]/self.mass]
        self.net_acceleration = [self.gravity[0]+self.hit_acceleration[0],self.gravity[1]+self.hit_acceleration[1]]
        if self.x<self.width/2:
            self.x=self.width/2
            self.hit_acceleration = [-self.hit_acceleration[0],self.hit_acceleration[1]]
            self.v = [-self.v[0]*5/8,self.v[1]*5/8]
        if self.x >self.window_dimension[0]-self.width/2:
            self.x = self.window_dimension[0]-self.width/2
            self.hit_acceleration = [-self.hit_acceleration[0],self.hit_acceleration[1]]
            self.v = [-self.v[0]*5/8,self.v[1]*5/8]
        if self.y < self.height/2:
            self.y=self.height/2
            self.hit_acceleration = [self.hit_acceleration[0],-self.hit_acceleration[1]]
            self.v = [self.v[0]*5/8,-self.v[1]*5/8]
        if self.y > self.window_dimension[1]-self.height/2:
            self.y=self.window_dimension[1]-self.height/2
            self.hit_acceleration = [self.hit_acceleration[0],-self.hit_acceleration[1]]
            self.v = [self.v[0]*5/8,-self.v[1]*5/8]
        self.v[0] += self.net_acceleration[0]*dt 
        self.v[1] += self.net_acceleration[1]*dt
        
        self.x += self.v[0]
        self.y += self.v[1]
        
        #collision block
        
        for o in balls:
            if check_collision(self, o) and self!=o:
                self.v=[0,0]
                self.hit=True
                self.hit_force=[force*(self.x-o.x),force*(self.y-o.y)]
                
class basketBall(Ball):
    def __init__(self, *args, **kwargs):
        super(basketBall, self).__init__(*args, **kwargs)
        self.reference_y=self.y
    def update(self,dt,balls,force):
        if self.hit_reference_time > 0.5 and self.hit:
            self.hit_force= [0,0]
            self.hit_reference_time = 0
            self.hit = False
        elif self.hit:
            self.hit_reference_time +=dt
            self.hit_force = [self.hit_force[0]*(0.5-self.hit_reference_time),self.hit_force[1]*(0.5-self.hit_reference_time)]
            
        self.hit_acceleration = [self.hit_force[0]/self.mass,self.hit_force[1]/self.mass]
        self.net_acceleration = [self.gravity[0]+self.hit_acceleration[0],self.gravity[1]+self.hit_acceleration[1]]
        if self.x<self.width/2:
            self.x=self.width/2
            self.hit_acceleration = [-self.hit_acceleration[0],self.hit_acceleration[1]]
            self.v = [-self.v[0]*5/8,self.v[1]*5/8]
        if self.x >self.window_dimension[0]-self.width/2:
            self.x = self.window_dimension[0]-self.width/2
            self.hit_acceleration = [-self.hit_acceleration[0],self.hit_acceleration[1]]
            self.v = [-self.v[0]*5/8,self.v[1]*5/8]
        if self.y < self.height/2:
            self.y=self.height/2
            self.hit_acceleration = [self.hit_acceleration[0],-self.hit_acceleration[1]]
            self.v = [self.v[0]*5/8,-self.v[1]*5/8]
        if self.y > self.window_dimension[1]-self.height/2:
            self.y=self.window_dimension[1]-self.height/2
            self.hit_acceleration = [self.hit_acceleration[0],-self.hit_acceleration[1]]
            self.v = [self.v[0]*5/8,-self.v[1]*5/8]
        self.v[0] += self.net_acceleration[0]*dt 
        self.v[1] += self.net_acceleration[1]*dt
        
        self.x += self.v[0]
        self.y += self.v[1]
        #collision block
        
        for o in balls:
            if check_collision(self, o) and self!=o:
                distance_vector= [o.x-self.x,o.y-self.y]
                distance = math.sqrt(distance_vector[0]**2+distance_vector[1]**2)
                wanted_distance =(self.width+o.width)/2
                distance_vector = distance_vector[0]*(wanted_distance)/distance,distance_vector[1]*(wanted_distance)/distance
                self.set_position(o.x-distance_vector[0],o.y-distance_vector[1])
                self.v=[0,0]
                self.hit=True
                self.hit_force=[force*(self.x-o.x),force*(self.y-o.y)]
        

class basketHoop(pyglet.sprite.Sprite):
    def __init__(self,edge_1,edge_2,*args,**kwargs):
        super(basketHoop,self).__init__(*args,**kwargs)
        self.edge_coordinates=[edge_1,edge_2]#edges are 2 indexed lists that contain edge coordinates
        self.edge_1=edge_1
        self.edge_2=edge_2
    def update(self,ball):
        if ball.y > self.edge_1[1]-ball.height/2 and ball.x < self.edge_2[0] and ball.x > self.edge_1[0] and ball.reference_y < self.edge_1[1]-40 and ball.y > self.edge_1[1]-40 :
            ball.y=self.edge_1[1]-ball.height/2
            ball.hit_acceleration = [ball.hit_acceleration[0],-ball.hit_acceleration[1]]
            ball.v = [ball.v[0]*5/8,-ball.v[1]*5/8]
        for edge in self.edge_coordinates:
            
            if math.sqrt((edge[0]-ball.x)**2+(edge[1]-ball.y)**2 ) < ball.width/2 + 10:
                distance_vector= [ball.x-edge[0],ball.y-edge[1]]
                distance = math.sqrt(distance_vector[0]**2+distance_vector[1]**2)
                wanted_distance =ball.width/2 + 10
                distance_vector = distance_vector[0]*(wanted_distance)/distance,distance_vector[1]*(wanted_distance)/distance
                ball.set_position(edge[0]+distance_vector[0],edge[1]+distance_vector[1])
                force= math.sqrt(ball.v[0]**2+ball.v[1]**2)
                ball.v=[0,0]
                ball.hit=True
                ball.hit_force=[force*(ball.x-edge[0]),force*(ball.y-edge[1])]
        if ball.x > self.edge_1[0] and ball.x < self.edge_2[0] and ball.y<=self.edge_1[1]-40 and ball.reference_y>=self.edge_1[1]-40 and ball.v[1] < 0 :
            return True
        
class MenuElement(pyglet.text.Label):
    def __init__(self,next_activity,*args,**kwargs):
        super(MenuElement, self).__init__(*args, **kwargs)
        self.next_activity=next_activity
        self.font_name="HelloHandMeDown"
        self.main_position=(self.x,self.y)
        self.main_font_size=self.font_size
        self.main_color=self.color
    def on_enter(self):
        self.next_activity()
        
    