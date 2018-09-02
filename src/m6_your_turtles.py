"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Mashengjun Li.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
ashe = rg.SimpleTurtle('turtle')
ashe.pen = rg.Pen('red',1)
ashe.speed = 50
window.delay(50)

garen = rg.SimpleTurtle('turtle')
garen.pen_down()
garen.pen = rg.Pen('cyan', 1)
garen.speed= 50
garen.pen_up()
garen.forward(150)
garen.pen_down()

for k in range(19):
    ashe.forward(50)
    ashe.right(165)
    ashe.forward(98)
    ashe.right(165)
    ashe.forward(50)
    angle = 10
    ashe.right(angle+10)
    garen.forward(50)
    garen.right(165)
    garen.forward(98)
    garen.right(165)
    garen.forward(50)
    angle = 10
    garen.right(angle +10)

ashe.pen_up()
ashe.forward(100)
ashe.pen_down()

for k in range(10):
    ashe.draw_circle(20)
    ashe.forward(10)


window.close_on_mouse_click()
###############################################################################
#  Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
