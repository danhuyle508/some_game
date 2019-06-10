import pyglet
from pyglet.window import mouse
window = pyglet.window.Window()
image = pyglet.resource.image('random.jpg')

imageX = 50
imageY = 50

#Setting size and anchor points for the images
image.width = window.width//2
image.height = window.height//2
image.anchor_x = window.width//2
image.anchor_y = window.height//2

#Setting label stuff
label = pyglet.text.Label('Hello, world',
    font_name='Times New Roman',
    font_size=36,
    x=window.width//2, y=window.height//2,
    anchor_x='center', anchor_y='center')    

@window.event
def on_draw():
    window.clear()
    image.blit(image.anchor_x, image.anchor_y)
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    print('event works')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if(button == mouse.LEFT):
        print('mouse left was pressed')
    if(button == mouse.RIGHT):
        print('mouse right was pressed')
pyglet.app.run()

