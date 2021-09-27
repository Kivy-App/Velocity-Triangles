from math import sqrt,cos,radians,acos,degrees

def a3_calculation(U,Vx,a1):
    PR = 2
    R = 0.287       #kJ/kg*K
    cp = 1.0005     #kJ/kg*K
    hp = 0.95
    gamma = 1.4
    c = (gamma-1)/gamma
    h_is = (PR**c - 1)/(PR**(c*(1/hp)) - 1)
    TR = PR**(c*(1/hp))

    T1 = Vx/(sqrt(cp*cos(radians(a1))**2)*(gamma-1)*gamma*R)
    k = (2*cp/Vx)*(T1*(1-TR) + U*Vx/cp)
    l = 1/(cos(radians(a1))**2)
    a3 = degrees(acos(sqrt(1/(l+k))))

    print(h_is,TR,T1,a3)



