import pyglet,sys,inspect

current_module = sys.modules[__name__]
path=str(inspect.getfile(current_module))
print(path)
path=path[:(len(path)-29)]#29
pyglet.resource.path = [path+"ball_hop_images"] 
pyglet.resource.reindex()


def center(image):
    image.anchor_x=image.width/2
    image.anchor_y=image.height/2
def resize(image,width,height):
    image.width=width
    image.height=height

red_ball=pyglet.resource.image("ball.png")
resize(red_ball,100,100)
center(red_ball)


ball=pyglet.resource.image("ball2.png")
resize(ball,100,100)
center(ball)

basket_ball_1=pyglet.resource.image("basketball1.png")
resize(basket_ball_1,100,100)
center(basket_ball_1)

basket_ball_2=pyglet.resource.image("basketball2.png")
resize(basket_ball_2,100,100)
center(basket_ball_2)

basket_ball_hoop=pyglet.resource.image("basketballhoop.png")
resize(basket_ball_hoop,200,210)
center(basket_ball_hoop)



basket_ball_hoop_left=pyglet.resource.image("basketballhoop_left_sided.png")
basket_ball_hoop_right=pyglet.resource.image("basketballhoop_right_sided.png")
