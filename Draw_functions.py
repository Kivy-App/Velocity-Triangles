from math import radians,degrees,log,atan,cos,sqrt
def drawing_triangles(U_i,Um,U,x0,y0,x1,Vth1_i,Vth2_i,fe1_i,fe2_i):
    Up = (U_i / Um) * U
    dif = U - Up
    x0_i = x0 + dif / 2
    x1_i = x1 - dif / 2
    xL_i = x0_i + (Vth1_i / U_i) * Up
    yL_i = y0 + Up * float(fe1_i)
    xR_i = x0_i + (Vth2_i / U_i) * Up
    yR_i = y0 + Up * float(fe2_i)

    return Up, x0_i, x1_i, xL_i, yL_i, xR_i, yR_i

def calculating_variables(n, Um, rne, Vth2, r_i, rm, Vx, U_i):
    
    a = Um * (1 - float(rne))
    b = Vth2 - a

    Vth1_i = a * (r_i / rm) ** n - b * (rm / r_i)
    Vth2_i = a * (r_i / rm) ** n + b * (rm / r_i)

    if n == 0:
        Vx1_i = sqrt(abs(Vx ** 2 - 2 * a * (a*log(r_i / rm) + b * ((1 / r_i) - (1/rm)))))
        Vx2_i = sqrt(abs(Vx ** 2 - 2 * a * (a*log(r_i / rm) + b * ((1 / rm) - (1/r_i)))))

    else:
        Vx1_i = sqrt(abs(Vx ** 2 - 2 * a * (n + 1) * (
                    (a / 2 * n) * (r_i ** (2 * n) - rm ** (2 * n)) - (b / (n - 1)) * (r_i ** (n - 1) - rm ** (n - 1)))))
        Vx2_i = sqrt(abs(Vx ** 2 - 2 * a * (n + 1) * (
                    (a / 2 * n) * (r_i ** (2 * n) - rm ** (2 * n)) + (b / (n - 1)) * (r_i ** (n - 1) - rm ** (n - 1)))))

    dVth_i = Vth2_i - Vth1_i
    rne_i = 1 - (a / Um) * (r_i / rm) ** (n - 1)
    fe_i1 = Vx1_i / U_i
    fe_i2 = Vx2_i / U_i
    pe_i = dVth_i / U_i

    Wth1_i = Vth1_i - U_i
    Wth2_i = Vth2_i - U_i

    a1e_i = -degrees(atan(Vth1_i / Vx1_i))
    a2e_i = degrees(atan(Vth2_i / Vx2_i))
    b1e_i = -degrees(atan(Wth1_i / Vx1_i))
    b2e_i = degrees(atan(Wth2_i / Vx2_i))

    V1_i = Vx1_i / cos(radians(float(a1e_i)))
    V2_i = Vx2_i / cos(radians(float(a2e_i)))
    W1_i = Vx1_i / cos(radians(float(b1e_i)))
    W2_i = Vx2_i / cos(radians(float(b2e_i)))
    
    return Vth1_i, Vth2_i, Vx1_i, Vx2_i, dVth_i, rne_i, fe_i1, fe_i2, pe_i, Wth1_i, Wth2_i, a1e_i, a2e_i, b1e_i, b2e_i, V1_i, V2_i, W1_i, W2_i
