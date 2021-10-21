from kivy.core.window import Window
from math import sin,cos,radians


def arrows(x0,y0,x1,y1,a1e,a2e,b1e,b2e):

    # ############## Window factors  ############################
    factor_x = (Window.size[0] / 400)
    factor_y = (Window.size[1] / 700)

    # ############## Computing base angles  ############################
    a1d = 180 + float(a1e) - 90
    a2d = 180 - float(a2e) - 90
    b1d = 180 - float(b1e) - 90
    b2d = 180 - float(b2e) - 90

    # ############## Computing rotating arrow points  ############################

    xL1u = x0 + factor_x * 25 * cos(radians(a1d + 11.3))
    yL1u = y0 + factor_y * 25 * sin(radians(a1d + 11.3))
    xL1d = x0 + factor_x * 25 * cos(radians(a1d - 11.3))
    yL1d = y0 + factor_y * 25 * sin(radians(a1d - 11.3))

    xL2u = x0 + factor_x * 25 * cos(radians(a2d + 11.3))
    yL2u = y0 + factor_y * 25 * sin(radians(a2d + 11.3))
    xL2d = x0 + factor_x * 25 * cos(radians(a2d - 11.3))
    yL2d = y0 + factor_y * 25 * sin(radians(a2d - 11.3))

    xR1u = x1 - factor_x * 25 * cos(radians(b1d + 11.3))
    yR1u = y1 + factor_y * 25 * sin(radians(b1d + 11.3))
    xR1d = x1 - factor_x * 25 * cos(radians(b1d - 11.3))
    yR1d = y1 + factor_y * 25 * sin(radians(b1d - 11.3))

    xR2u = x1 + factor_x * 25 * cos(radians(b2d + 11.3))
    yR2u = y1 + factor_y * 25 * sin(radians(b2d + 11.3))
    xR2d = x1 + factor_x * 25 * cos(radians(b2d - 11.3))
    yR2d = y1 + factor_y * 25 * sin(radians(b2d - 11.3))
    
    return xL1u, yL1u, xL1d, yL1d, xL2u, yL2u, xL2d, yL2d, xR1u, yR1u, xR1d, yR1d, xR2u, yR2u, xR2d, yR2d