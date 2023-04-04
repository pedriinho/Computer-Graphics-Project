from LoadObjBlender.objloader import OBJ
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

cx, cy, cz, fx, fy, fz, ux, uy, uz = 4, 10, 3.2, -4.18, -5.97, -3.38, 0, 1, 0
anglePorta, angleVent, mouseSens, mouseVel, ang_x, ang_y = 0.0, 0.0, 0.001, 0.1, -1.2, 1
antigo_x, antigo_y, fAspect, rotX, rotY, obsZ, medida = 0, 0, 1.6, 0, -2, 2, 7
objTeclado = ''

def square(A, B, C, D):
    glBegin(GL_POLYGON)
    glVertex3fv(A)
    glVertex3fv(B)
    glVertex3fv(C)
    glVertex3fv(D)
    glEnd()

def cubo(t0, t1, t2, t3, t4, t5, t6, t7, colorR, colorG, colorB):
    glColor3f(colorR, colorG, colorB)
    square(t0, t1, t2, t3)

    glColor3f(colorR, colorG, colorB)
    square(t4, t5, t6, t7)

    glColor3f(colorR, colorG, colorB)
    square(t0, t4, t7, t3)

    glColor3f(colorR, colorG, colorB)
    square(t1, t5, t6, t2)

    glColor3f(colorR, colorG, colorB)
    square(t3, t2, t6, t7)

    glColor3f(colorR, colorG, colorB)
    square(t0, t1, t5, t4)

def modelar_objeto( x_max, x_min,  y_max, y_min,  z_max, z_min, colorR, colorG, colorB):
    global medida
    objeto = [
        [x_min*medida, y_max*medida, z_min*medida],
        [x_min*medida, y_max*medida, z_max*medida],
        [x_max*medida, y_max*medida, z_max*medida],
        [x_max*medida, y_max*medida, z_min*medida],
        [x_min*medida, y_min*medida, z_min*medida],
        [x_min*medida, y_min*medida, z_max*medida],
        [x_max*medida, y_min*medida, z_max*medida],
        [x_max*medida, y_min*medida, z_min*medida],
    ]
    
    cubo(objeto[0], objeto[1], objeto[2], objeto[3], objeto[4], objeto[5], objeto[6], objeto[7], colorR, colorG, colorB)

def keyboard(ch, x, y):
    global cx, cy, cz, fx, fy, fz, ux, uy, uz, anglePorta, angleVent
    ch = ch.decode("utf-8")

    if ch == 'r':
        cx, cy, cz, fx, fy, fz, ux, uy, uz = 4, 10, 3.2, -4.18, -5.97, -3.38, 0, 1, 0
    elif ch == 'a':
        cz -= 0.5
    elif ch == 'd':
        cz += 0.5
    elif ch == 'w':
        cx += 0.5
    elif ch == 's':
        cx -= 0.5
    elif ch == 'y':
        cy += 0.5
    elif ch == 'Y':
        cy -= 0.5
    elif ch == 'o':
        if (anglePorta < 90):
            anglePorta += 1
    if ch == 'c':
        if (anglePorta >= 0):
            anglePorta -= 1
    if ch == 'v':
        angleVent += 5
        if (angleVent >= 360):
            angleVent = 0
    if ch == 'V':
        angleVent -= 5
        if (angleVent <= 0):
            angleVent = 360 

    glutPostRedisplay()

def montar_monitores():
    # base dos monitores do lado direito
    x_max, x_min, y_max, y_min, z_max, z_min = 6.5, 6.35,  0.815, 0.8001,  4.235,  3.985
    while(x_min > 0):
        z_max, z_min = 4.235, 3.985
        while(z_max < 6.4):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71

    # parte 2 da base dos monitores lado direito
    x_max, x_min, y_max, y_min, z_max, z_min = 6.48, 6.45, 1.115, 0.815, 4.135,4.085
    while(x_min > 0):
        z_max, z_min = 4.135, 4.085
        while(z_max < 6.4):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # monitores do lado direito
    x_max, x_min, y_max, y_min, z_max, z_min = 6.455, 6.445, 1.165, 0.915, 4.4, 3.82
    while(x_min > 0):
        z_max, z_min = 4.4, 3.82
        while(z_max < 6.4):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # gabinetes do lado direito
    x_max, x_min, y_max, y_min = 6.75, 6.25, 1.2, 0.8001
    while(x_min > 0):
        z_max, z_min = 4.58, 4.43
        while(z_max < 6.4):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.1, 0.1, 0.1)
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # botão power do lado direito
    x_max, x_min, y_max, y_min = 6.245, 6.25001, 0.91, 0.9
    while(x_min > 0):
        z_max, z_min = 4.51, 4.49
        while(z_max < 6.4):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.35, 0.35, 0.35)
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # base dos monitores do lado esquerdo
    x_max, x_min, y_max, y_min = 6.5, 6.35, 0.815, 0.8001
    while(x_min > 0):
        z_max, z_min = 2.415, 2.165
        while(z_min > 0):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)
            z_max-=0.9
            z_min-= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # parte 2 da base dos monitores lado esquerdo
    x_max, x_min, y_max, y_min = 6.48, 6.45, 1.115, 0.815
    while(x_min > 0):
        z_max, z_min = 2.315, 2.265
        while(z_max > 0):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
            z_max-=0.9
            z_min-= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # monitores do lado esquerdo
    x_max, x_min, y_max, y_min = 6.455, 6.445, 1.165, 0.915
    while(x_min > 0):
        z_max, z_min = 2.58, 2
        while(z_max > 0):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)
            z_max-=0.9
            z_min-= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # gabinetes do lado esquerdo
    x_max, x_min, y_max, y_min, z_max, z_min = 6.75, 6.25, 1.2, 0.8001, 4.58, 4.43
    while(x_min > 0):
        z_max, z_min = 1.95, 1.82
        while(z_max > 0):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.1, 0.1, 0.1)
            z_max-=0.9
            z_min-= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # botão power do lado esquerdo
    x_max, x_min, y_max, y_min = 6.245, 6.25001, 0.91, 0.9
    while(x_min > 0):
        z_max, z_min = 1.9, 1.88
        while(z_max > 0):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.35, 0.35, 0.35)
            z_max-=0.9
            z_min-= 0.9
        x_max-=1.71
        x_min-= 1.71

def montar_mesas():
    # mesas do lado direito
    x_max, x_min, y_max, y_min, z_max, z_min = 6.85, 6, 0.8, 0.76, 6.4, 3.71
    while(x_min > 0):
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.85, 0.85, 0.85)
        x_max-=1.71
        x_min-= 1.71
    
    # divisórias da mesa do lado direito
    y_max, y_min, x_max, x_min = 1.3, 0, 6.86, 5.99
    while(x_min > 0):
        z_max, z_min = 3.74, 3.7
        while(z_max < 6.4):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.78, 0.78, 0.78)
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # fundo da mesa do laso direito
    x_max, x_min, y_max, y_min, z_max, z_min = 6.85, 6.8, 0.8, 0, 6.4, 3.71
    while(x_min > 0):
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.85, 0.85, 0.85)
        x_max-=1.71
        x_min-= 1.71
    
    # mesas do lado esquerdo
    x_max, x_min, y_max, y_min, z_max, z_min = 6.85, 6, 0.8, 0.76, 2.69, 0
    while(x_min > 0):
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.85, 0.85, 0.85)
        x_max-=1.71
        x_min-= 1.71
    
    # divisórias da mesa do lado esquerdo
    y_max, y_min, x_max, x_min = 1.3, 0, 6.86, 5.99
    while(x_min > 0):
        z_max, z_min = 2.7, 2.66
        while(z_min > 0):
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.78, 0.78, 0.78)
            z_max-=0.9
            z_min-= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # fundo da mesa do lado esquerdo
    x_max, x_min, y_max, y_min, z_max, z_min = 6.85, 6.8, 0.8, 0, 2.69, 0
    while(x_min > 0):
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.85, 0.85, 0.85)
        x_max-=1.71
        x_min-= 1.71
    
    # mesa do professor
    x_max, x_min, y_max, y_min, z_max, z_min = 7.35, 6.85, 0.8, 0.76, 1.75, 0.95
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.85, 0.85, 0.85)

def montar_paredes():
    #piso
    x_max, x_min, y_max, y_min, z_max, z_min = 8.15, -0.15, 0, -0.15, 6.55, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.5, 0.5, 0.5)

    #teto
    x_max, x_min, y_max, y_min, z_max, z_min = 8.15, -0.15, 3.15, 3, 6.55, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.5, 0.5, 0.5)
    
    #parede direita, lado da porta
    x_max, x_min, y_max, y_min, z_max, z_min = 7, -0.15, 3, 0, 6.55, 6.4
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    #parede menor a direita, lado da porta
    x_max, x_min, y_max, y_min, z_max, z_min = 7, 6.85, 3, 0, 6.55, 5.55
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    #parede esquerda
    x_max, x_min, y_max, y_min, z_max, z_min = 8.15, -0.15, 3, 0, 0, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    #parede do fundo
    x_max, x_min, y_max, y_min, z_max, z_min = 0, -0.15, 3, 0, 6.55, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    #parede da frente, no quadro
    x_max, x_min, y_max, y_min, z_max, z_min = 8.15, 8, 3, 0, 6.55, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

def montar_quadro():
    x_max, x_min, y_max, y_min, z_max, z_min = 8, 7.98, 2.44, 0.71, 4, 1.55
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.87, 0.87, 0.87)

def montar_estruturas_da_porta():
    #estrutura da porta solta da parede
    x_max, x_min, y_max, y_min, z_max, z_min = 7.18, 7.16, 3, 0, 5.6, 5.55
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.4, 0.4, 0.4)

    #estrutura da porta encostado na parede
    x_max, x_min, y_max, y_min, z_max, z_min = 8, 7.98, 3, 0, 5.6, 5.55
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.4, 0.4, 0.4)

    #estrutura da porta superior da porta
    x_max, x_min, y_max, y_min, z_max, z_min = 8, 7, 2.22, 2.2, 5.6, 5.55
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.4, 0.4, 0.4)

    #estrutura da porta superior encostado no teto
    x_max, x_min, y_max, y_min, z_max, z_min = 8, 7, 3, 2.98, 5.6, 5.55
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.4, 0.4, 0.4)

    #estrutura da porta encostado na parede direita
    x_max, x_min, y_max, y_min, z_max, z_min = 7.02, 7, 3, 0, 5.6, 5.55
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.4, 0.4, 0.4)

def montar_porta():
    #porta branca x -> 7.975 # z -> 5,585
    x_max, x_min, y_max, y_min, z_max, z_min = 0, -0.590, 2.195, 0.005, 0, -0.02
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.8, 0.8, 0.8)

    #porta azul
    x_max, x_min, y_max, y_min, z_max, z_min = -0.590, -0.79, 2.195, 0.005, 0, -0.02
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.07, 0.3, 0.56)

    #ferro do trinco da porta
    x_max, x_min, y_max, y_min, z_max, z_min = -0.750, -0.76, 1.155, 1.145, 0.03, -0.05
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.43, 0.5, 0.57)

    #trinco da porta, por fora da sala
    x_max, x_min, y_max, y_min, z_max, z_min = -0.69, -0.76, 1.155, 1.145, 0.03, 0.02
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.43, 0.5, 0.57)

    #trinco da porta, por dentro da sala
    x_max, x_min, y_max, y_min, z_max, z_min = -0.69, -0.76, 1.155, 1.145, -0.05, -0.06
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.43, 0.5, 0.57)

def circulo_B(raio, x_center, y_center, z_center, colorR, colorG, colorB):
    num_segments = 50
    theta = 2.0 * 3.1415926 / num_segments
    glColor3f(colorR, colorG, colorB)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(x_center*medida, y_center*medida, z_center*medida)
    for i in range(num_segments):
        y = raio * math.sin(i * theta)
        z = raio * math.cos(i * theta)
        glVertex3f(x_center*medida, y + y_center*medida, z + z_center*medida)
    glEnd()

def escrever_no_quadro():
    # L
    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.8, 1.25, 2.15, 2.1
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.3, 1.25, 2.35, 2.1
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    # A
    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.8, 1.25, 2.7, 2.65
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.8, 1.25, 2.45, 2.4
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.8, 1.75, 2.7, 2.4
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.6, 1.55, 2.7, 2.4
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    # B
    circulo_B(medida*0.15, 7.9799, 1.67, 2.8, 0, 0, 0)
    circulo_B((medida*0.15)-0.2, 7.97985, 1.67, 2.8, 0.87, 0.87, 0.87)
    circulo_B(medida*0.16, 7.9799, 1.4, 2.8, 0, 0, 0)
    circulo_B((medida*0.15)-0.2, 7.97985, 1.4, 2.8, 0.87, 0.87, 0.87)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9797, 1.8, 1.25, 2.8, 2.75
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9797, 1.85, 1.25, 2.75, 2.6
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.87, 0.87, 0.87)

    # 2
    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.5, 1.25, 3.15, 3.1
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.8, 1.5, 3.3, 3.25
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.8, 1.75, 3.3, 3.1
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.525, 1.4725, 3.3, 3.1
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.98, 7.9795, 1.3, 1.25, 3.3, 3.1
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)

def montar_bases_dos_ventiladores():
    #ventilador 1
    x_max, x_min, y_max, y_min, z_max, z_min = 5.05, 4.95, 3, 2.97, 3.25, 3.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.54, 0.27, 0.07)

    x_max, x_min, y_max, y_min, z_max, z_min = 5.01, 4.99, 3, 2.85, 3.21, 3.19
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.54, 0.27, 0.07)

    glPushMatrix()
    glTranslatef(5*medida, 2.85*medida, 3.2*medida)
    glColor3f(0.54, 0.27, 0.07)
    glutSolidSphere(0.15, 50, 50)
    glPopMatrix()

    #ventilador 2
    x_max, x_min, y_max, y_min, z_max, z_min = 2.05, 1.95, 3, 2.97, 3.25, 3.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.54, 0.27, 0.07)

    x_max, x_min, y_max, y_min, z_max, z_min = 2.01, 1.99, 3, 2.85, 3.21, 3.19
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.54, 0.27, 0.07)

    glPushMatrix()
    glTranslatef(2*medida, 2.85*medida, 3.2*medida)
    glColor3f(0.54, 0.27, 0.07)
    glutSolidSphere(0.15, 50, 50)
    glPopMatrix()


def montar_ventilador():
    #ventilador 1
    x_max, x_min, y_max, y_min, z_max, z_min = -0.5, 0.5, 0, 0, 0.05, -0.05
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)

    x_max, x_min, y_max, y_min, z_max, z_min = 0.05, -0.05, 0, 0,-0.5, 0.5
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)



def myInit():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def montar_teclado():
    # lado lideiro
    x, y, z = 6.2, 0.81, 3.9
    for linha in range(4):
        for coluna in range(3):
            glPushMatrix()
            glTranslatef(x*medida, y*medida, z*medida)
            glScale(0.05, 0.05, 0.05)
            glRotatef(-90, 0, 1, 0)
            glCallList(objTeclado.gl_list)
            glPopMatrix()
            z+=0.9
        x-=1.71
        z = 3.9

    # lado esquerdo
    x, y, z = 6.2, 0.81, 2.1
    for linha in range(4):
        for coluna in range(3):
            glPushMatrix()
            glTranslatef(x*medida, y*medida, z*medida)
            glScale(0.05, 0.05, 0.05)
            glRotatef(-90, 0, 1, 0)
            glCallList(objTeclado.gl_list)
            glPopMatrix()
            z-=0.9
        x-=1.71
        z = 2.1



def Draw():
    global medida, cx, cy, cz, fx, fy, fz, ux, uy, uz, anglePorta, angleVent, objTeclado
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(cx, cy, cz, cx + fx, cy + fy, cz + fz, ux, uy, uz)

    glPushMatrix()
    montar_paredes()
    montar_mesas()
    montar_monitores()
    montar_quadro()
    montar_estruturas_da_porta()
    glPopMatrix()

    glPushMatrix()
    montar_teclado()
    glPopMatrix()

    glPushMatrix()  
    glTranslatef(7.975*medida, 0, 5.585*medida)
    glRotatef(anglePorta, 0, 1, 0)
    montar_porta()
    glPopMatrix()

    glPushMatrix()  
    escrever_no_quadro()
    glPopMatrix()

    glPushMatrix()  
    montar_bases_dos_ventiladores()
    glPushMatrix()
    glTranslatef(5*medida, 2.875*medida, 3.2*medida)
    glRotatef(angleVent, 0, 1, 0)
    montar_ventilador()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2*medida, 2.875*medida, 3.2*medida)
    glRotatef(angleVent, 0, 1, 0)
    montar_ventilador()
    glPopMatrix()
    glPopMatrix()

    glutSwapBuffers()

def myInit():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def gerenciaMouse(button,state, x, y):
    global antigo_x, antigo_y

    antigo_x = x
    antigo_y = y

def mouse_camera(mouse_x, mouse_y):
    global ang_x, ang_y, antigo_x, antigo_y, fx, fy, fz

    ang_x -= (mouse_x - antigo_x) * mouseSens
    ang_y -= (mouse_y - antigo_y) * mouseSens

    fx = math.cos(ang_x) * math.sin(ang_y)
    fy = math.cos(ang_y)
    fz = math.sin(ang_x) * math.sin(ang_y)

    antigo_x = mouse_x
    antigo_y = mouse_y

    glutPostRedisplay()

def main():
    global objTeclado

    glutInit()
    glutInitWindowSize(1600, 1000)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow("lab 2")
    myInit()
    objTeclado = OBJ('ObjBlender/teclado.obj')
    glutDisplayFunc(Draw)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(gerenciaMouse)
    glutMotionFunc(mouse_camera)
    glutMainLoop()

if __name__ == '__main__':
    main()