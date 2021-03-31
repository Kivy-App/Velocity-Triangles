from kivy.core.window import Window

def cambers(y0,Uhp,Uh,feh2,feh1,Vth1h,Vth2h,Wth1h,Wth2h,tc):

    if tc == 0 :
        ys_cent = y0 + Window.size[1] * 125 / 700
        scl_coeff = 0.75 
    else:
        ys_cent = y0 + Window.size[1] * 70 / 700
        scl_coeff = 0.6

    xs_cent = Window.size[0] * 200 / 400
    xRh_camb = xs_cent + scl_coeff*Uhp * float(feh2)
    yRh_camb = ys_cent - scl_coeff*(Vth2h/Uh)*Uhp
    yLh_camb = ys_cent + scl_coeff*(Vth1h/Uh)*Uhp
    xLh_camb = xs_cent - scl_coeff*Uhp * float(feh1)

    yRh_rotor = ys_cent - scl_coeff * (Wth2h / Uh) * Uhp
    yLh_rotor = ys_cent + scl_coeff * (Wth1h / Uh) * Uhp

    return xs_cent, ys_cent, xRh_camb,yRh_camb, yLh_camb, xLh_camb, yLh_rotor, yRh_rotor

def mid_cambers(U,fe,rne,pe,y0,tc):
    if tc == 0:
        ys_cent = y0 + Window.size[1] * 125 / 700
        scl_coeff = 0.75
    else:
        ys_cent = y0 + Window.size[1] * 70 / 700
        scl_coeff = 0.6

    xs_cent = Window.size[0] * 200 / 400
    xRm_camb = xs_cent + scl_coeff * (U * float(fe))
    yRm_camb = ys_cent - scl_coeff * (U * (1 - float(rne)) + U * float(pe) / 2)
    xLm_camb = xs_cent - scl_coeff * (U * float(fe))
    yLm_camb = ys_cent + scl_coeff * (U * (1 - float(rne)) - U * float(pe) / 2)

    yRm_rotor = ys_cent - scl_coeff*(- U * float(rne) + U * float(pe) / 2)
    yLm_rotor = ys_cent + scl_coeff*(- U * float(rne) - U * float(pe) / 2)
    return xs_cent, ys_cent, xRm_camb, yRm_camb, yLm_camb, xLm_camb,yLm_rotor, yRm_rotor
