import pyglet,sys,inspect

current_module = sys.modules[__name__]
path=str(inspect.getfile(current_module))
path=path[:(len(path)-28)]
pyglet.font.add_file(path+"ball_hop_fonts\HelloHandMeDown.ttf")
action_man = pyglet.font.load('HelloHandMeDown')