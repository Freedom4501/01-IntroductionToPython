"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Mashengjun Li.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done?: 2.
#   Write code that accomplishes the following:
#     - Constructs a SimpleTurtle with a  blue  Pen.
#     - Makes the SimpleTurtle go straight UP 200 pixels.
#     - Tells the SimpleTurtle to make its pen go UP
#          (so that the next movements do NOT leave a "trail")
#          HINT: Use the "dot trick" to figure out how to do this.
#     - Tells the SimpleTurtle to go to (100, -40).
#     - Tells the SimpleTurtle to make its pen go DOWN
#          (so that the next movements will return to leaving a "trail")
#     - Makes the SimpleTurtle's pen have color "green" and thickness 10.
#     - Tells the SimpleTurtle to go 150 pixels straight DOWN.
#
# Don't forget to:
#     - import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     - ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
ashe = rg.SimpleTurtle('turtle')
ashe.pen = rg.Pen('blue', 10)
ashe.speed = 50
ashe.forward(200)
ashe.pen_up()
x=100
y=-40
ashe.x_cor()
ashe.y_cor()
ashe.go_to(x)
ashe.go_to(y)

ashe.pen_down()
ashe.pen = rg.Pen('green',10)
ashe.forward(150)
window.close_on_mouse_click()