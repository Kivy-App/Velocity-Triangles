from kivy.core.window import Window

def camber_stator(y0,Uhp,Uh,feh2,feh1,Vth1h,Vth2h,Wth1h,Wth2h):

    xs_cent = Window.size[0] * 200 / 400
    ys_cent = y0 + Window.size[1] * 125 / 700
    xRh_camb = xs_cent + 0.75*Uhp * float(feh2)
    yRh_camb = ys_cent - 0.75*(Vth2h/Uh)*Uhp
    yLh_camb = ys_cent + 0.75*(Vth1h/Uh)*Uhp
    xLh_camb = xs_cent - 0.75*Uhp * float(feh1)

    yRh_rotor = ys_cent - 0.75 * (Wth2h / Uh) * Uhp
    yLh_rotor = ys_cent + 0.75 * (Wth1h / Uh) * Uhp

    return xs_cent, ys_cent, xRh_camb,yRh_camb, yLh_camb, xLh_camb, yLh_rotor, yRh_rotor

def mid_camb_stator(U,fe,rne,pe,y0):
    xs_cent = Window.size[0] * 200 / 400
    ys_cent = y0 + Window.size[1] * 125 / 700
    xRm_camb = xs_cent + 0.75 * (U * float(fe))
    yRm_camb = ys_cent - 0.75 * (U * (1 - float(rne)) + U * float(pe) / 2)
    xLm_camb = xs_cent - 0.75 * (U * float(fe))
    yLm_camb = ys_cent + 0.75 * (U * (1 - float(rne)) - U * float(pe) / 2)

    yRm_rotor = xs_cent - 0.75*(- U * float(rne) + U * float(pe) / 2)
    yLm_rotor = xs_cent + 0.75*(- U * float(rne) - U * float(pe) / 2)
    return xs_cent, ys_cent, xRm_camb, yRm_camb, yLm_camb, xLm_camb,yLm_rotor, yRm_rotor
