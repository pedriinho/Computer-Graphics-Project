from LoadObjBlender.objloader import OBJ
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
from PIL import Image

angleJanela, anglePorta, angleVent, mouseSens, mouseVel, ang_x, ang_y = 0.0, 0.0, 0.0, 0.001, 0.1, 0.3, 1.3
antigo_x, antigo_y, fAspect, rotX, rotY, obsZ, medida = 710, 519, 1.6, 0, -2, 2, 7
cx, cy, cz, fx, fy, fz, ux, uy, uz = 0.3*medida, 1.3*medida, 3.2*medida, 0.98, 0.16, -0.05, 0, 1, 0
objTeclado, objMonitorOn = '', ''
isDay = True
turnOnPc = []
turnSwitch = []
turnLampPc = False
turnLampRoof = []
texture_board, texture_fan, texture_floor = 0, 0, 0

def square(A, B, C, D):
    glBegin(GL_POLYGON)
    glVertex3fv(A)
    glVertex3fv(B)
    glVertex3fv(C)
    glVertex3fv(D)
    glEnd()

def cubo(v0, v1, v2, v3, v4, v5, v6, v7, colorR, colorG, colorB):
    glPushMatrix()
    glColor3f(colorR, colorG, colorB)
    square(v0, v1, v2, v3)

    glColor3f(colorR, colorG, colorB)
    square(v4, v5, v6, v7)

    glColor3f(colorR, colorG, colorB)
    square(v0, v4, v7, v3)

    glColor3f(colorR, colorG, colorB)
    square(v1, v5, v6, v2)

    glColor3f(colorR, colorG, colorB)
    square(v3, v2, v6, v7)

    glColor3f(colorR, colorG, colorB)
    square(v0, v1, v5, v4)
    glPopMatrix()

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
    global cx, cy, cz, fx, fy, fz, ux, uy, uz, anglePorta, angleVent, turnOnPc, angleJanela, isDay, turnLampPc
    ch = ch.decode("utf-8")

    if ch == 'r':
        cx, cy, cz, fx, fy, fz, ux, uy, uz = 0.3*medida, 1.3*medida, 3.2*medida, 0.98, 0.16, -0.05, 0, 1, 0
    elif ch == 'a':
        cz -= 2
    elif ch == 'd':
        cz += 2
    elif ch == 'w':
        cx += 2
    elif ch == 's':
        cx -= 2
    elif ch == 'y':
        cy += 2
    elif ch == 'Y':
        cy -= 2
    elif ch == 'o':
        if (anglePorta + 3 <= 90):
            anglePorta += 3
    elif ch == 'c':
        if (anglePorta - 3 >= 0):
            anglePorta -= 3
    elif ch == 'j':
        if (angleJanela+2 <= 90):
            angleJanela += 2
    elif ch == 'J':
        if (angleJanela-2 >= 0):
            angleJanela -= 2
    elif ch == 't':
        isDay = not isDay
    elif ch == 'e':
        turnLampPc = not turnLampPc
    elif ch == 'q':
        turnLampRoof[0]['state'] = not turnLampRoof[0]['state']


    glutPostRedisplay()

def montar_monitores():
    global turnOnPc
    # base dos monitores do lado direito
    x_max, x_min, y_max, y_min, z_max, z_min = 6.5, 6.35,  0.815, 0.8001,  4.235,  3.985
    while(x_min > 0):
        z_max, z_min = 4.235, 3.985
        while(z_max < 6.4):
            glPushMatrix()
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)
            glPopMatrix()
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71

    # parte 2 da base dos monitores lado direito
    x_max, x_min, y_max, y_min, z_max, z_min = 6.48, 6.45, 1.115, 0.815, 4.135,4.085
    while(x_min > 0):
        z_max, z_min = 4.135, 4.085
        while(z_max < 6.4):
            glPushMatrix()
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
            glPopMatrix()
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # monitores do lado direito
    x_max, x_min, y_max, y_min, z_max, z_min = 6.455, 6.445, 1.165, 0.915, 4.4, 3.82
    while(x_min > 0):
        z_max, z_min = 4.4, 3.82
        while(z_max < 6.4):
            glPushMatrix()
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0, 0, 0)
            glPopMatrix()
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # gabinetes do lado direito
    x_max, x_min, y_max, y_min = 6.75, 6.25, 1.2, 0.8001
    while(x_min > 0):
        z_max, z_min = 4.58, 4.43
        while(z_max < 6.4):
            glPushMatrix()
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.1, 0.1, 0.1)
            glPopMatrix()
            z_max+=0.9
            z_min+= 0.9
        x_max-=1.71
        x_min-= 1.71
    
    # # botão power do lado direito
    x_max, x_min, y_max, y_min = 6.25001, 6.245, 0.91, 0.9

    while(x_min > 0):
        z_max, z_min = 4.51, 4.49
        while(z_max < 6.4):
            glPushMatrix()
            turnOnPc.append({'x_max': x_max, 'x_min': (x_min), 'y_max': y_max, 'y_min': y_min, 'z_max': z_max, 'z_min': z_min, 'state': False})
            modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.35, 0.35, 0.35)
            glPopMatrix()
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
    x_max, x_min, y_max, y_min = 6.25001, 6.245, 0.91, 0.9
    while(x_min > 0):
        z_max, z_min = 1.9, 1.88
        while(z_max > 0):
            turnOnPc.append({'x_max': x_max, 'x_min': (x_min), 'y_max': y_max, 'y_min': y_min, 'z_max': z_max, 'z_min': z_min, 'state': False})
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
    glPushMatrix()
    glTranslatef(8*medida, -8.1495*medida, 0)
    glRotatef(90, 0, 0, 1)
    montar_textura(x_max, x_min, y_max, y_min+8.3, z_max, z_min, texture_floor)
    glPopMatrix()

    #teto
    x_max, x_min, y_max, y_min, z_max, z_min = 8.15, -0.15, 3.15, 3, 6.55, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.5, 0.5, 0.5)

    # parede direita inferior
    x_max, x_min, y_max, y_min, z_max, z_min = 7, -0.15, 2.5, 0, 6.55, 6.4
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    # pilastra parede direita
    x_max, x_min, y_max, y_min, z_max, z_min = 5.8, 5.5, 3, 0, 6.55, 6.35
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    # parede direita, lado esquerdo
    x_max, x_min, y_max, y_min, z_max, z_min = 6.85, 6.8, 3, 2.5, 6.55, 6.4
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    # parede direita, lado direito
    x_max, x_min, y_max, y_min, z_max, z_min = 0.5, 0, 3, 2.5, 6.55, 6.4
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    #parede menor a direita, lado da porta
    x_max, x_min, y_max, y_min, z_max, z_min = 7, 6.85, 3, 0, 6.55, 5.55
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    #parede esquerda inferior
    x_max, x_min, y_max, y_min, z_max, z_min = 8.15, -0.15, 1.25, 0, 0, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    # parede esquerda superior
    x_max, x_min, y_max, y_min, z_max, z_min = 8.15, -0.15, 3, 2.95, 0, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    # parede esquerda, lateral esquerda
    x_max, x_min, y_max, y_min, z_max, z_min = 0.5, -0.15, 2.95, 1.25, 0, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    # parede esquerda, lateral direita
    x_max, x_min, y_max, y_min, z_max, z_min = 8.15, 7.8, 2.95, 1.25, 0, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    # pilastra parede esquerda
    x_max, x_min, y_max, y_min, z_max, z_min = 5.8, 5.5, 3, 0, 0.05, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    #parede do fundo
    x_max, x_min, y_max, y_min, z_max, z_min = 0, -0.15, 3, 0, 6.55, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

    #parede da frente, no quadro
    x_max, x_min, y_max, y_min, z_max, z_min = 8.15, 8, 3, 0, 6.55, -0.15
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.75, 0.75, 0.75)

def montar_textura(x_max, x_min,  y_max, y_min, z_max, z_min, texture ):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    glColor3f(1, 1, 1)
    
    if(x_min == 0):
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(x_max*medida, y_max*medida, z_max*medida)
        glTexCoord2f(1, 0)
        glVertex3f(x_max*medida, y_max*medida, z_min*medida)
        glTexCoord2f(1, 1)
        glVertex3f(x_max*medida, y_min*medida, z_min*medida)
        glTexCoord2f(0, 1)
        glVertex3f(x_max*medida, y_min*medida, z_max*medida)
        glEnd()
    else:
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(x_max*medida, y_max*medida, z_max*medida)
        glTexCoord2f(1, 0)
        glVertex3f(x_max*medida, y_max*medida, z_min*medida)
        glTexCoord2f(1, 1)
        glVertex3f(x_max*medida, y_min*medida, z_min*medida)
        glTexCoord2f(0, 1)
        glVertex3f(x_max*medida, y_min*medida, z_max*medida)
        glEnd()
        

    glDisable(GL_TEXTURE_2D)

def montar_quadro():
    global texture_board
    x_max, x_min, y_max, y_min, z_max, z_min = 8, 7.98, 2.44, 0.71, 4, 1.55
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.87, 0.87, 0.87)
    montar_textura(7.97995, 0, y_max, y_min, z_max, z_min, texture_board)
    

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
    global texture_fan
    #ventilador 1
    x_max, x_min, y_max, y_min, z_max, z_min = -0.5, 0.5, 0, 0, 0.05, -0.05
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)
    glPushMatrix()
    glRotatef(-90, 0, 0, 1)
    montar_textura(x_max+0.51, x_min, y_max+0.5, y_min-0.5, z_max, z_min, texture_fan)
    glPopMatrix()

    x_max, x_min, y_max, y_min, z_max, z_min = 0.05, -0.05, 0, 0,-0.5, 0.5
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)
    glPushMatrix()
    glTranslatef(0, 0.045*medida, 0)
    glRotatef(-90, 0, 0, 1)
    montar_textura(x_max, x_min, y_max+0.05, y_min-0.05, z_max, z_min, texture_fan)
    glPopMatrix()


def montar_teclado():
    # lado lideiro
    x, y, z = 6.2, 0.81, 4.05
    for linha in range(4):
        for coluna in range(3):
            glPushMatrix()
            glColor(1, 1, 1)
            glTranslatef(x*medida, y*medida, z*medida)
            glScale(0.4, 0.55, 0.35)
            glRotatef(-90, 0, 1, 0)
            glCallList(objTeclado.gl_list)
            glPopMatrix()
            z+=0.9
        x-=1.71
        z = 4.05

    # lado esquerdo
    x, y, z = 6.2, 0.81, 2.25
    for linha in range(4):
        for coluna in range(3):
            glPushMatrix()
            glTranslatef(x*medida, y*medida, z*medida)
            glScale(0.4, 0.55, 0.4)
            glRotatef(-90, 0, 1, 0)
            glCallList(objTeclado.gl_list)
            glPopMatrix()
            z-=0.9
        x-=1.71
        z = 2.25

def montar_janela_lado_direito():
    global medida

    vertices = [
        [7.98, 7.18, 3, 2.22, 5.5575],
        [7.16, 7.02, 3, 2.22, 5.5575],
        [7.16, 7.02, 2.2, 0, 5.5575],
    ]

    for janela in vertices:
        glBegin(GL_QUADS)
        glColor4f(0.75,0.75,0.75, 0.5) 
        glVertex3f(janela[0] * medida, janela[3] * medida, janela[4] * medida)
        glVertex3f(janela[0] * medida, janela[2] * medida, janela[4] * medida)
        glVertex3f(janela[1] * medida, janela[2] * medida, janela[4] * medida)
        glVertex3f(janela[1] * medida, janela[3] * medida, janela[4] * medida)
        glEnd()
    
    x_center, y_center, z_center = 6.05, 2.75, 6.475
    for i in range(2):
        glPushMatrix()
        glTranslatef(x_center*medida, y_center*medida, z_center*medida)
        glRotatef(angleJanela, 0, 1, 0)
        montar_janela_de_movimento(0.5, 0.5)
        glPopMatrix()
        x_center+=0.5

    x_center, y_center, z_center = 0.75, 2.75, 6.475
    for i in range(10):
        glPushMatrix()
        glTranslatef(x_center*medida, y_center*medida, z_center*medida)
        glRotatef(angleJanela, 0, 1, 0)
        montar_janela_de_movimento(0.5, 0.5)
        glPopMatrix()
        x_center+=0.5
    
def ligar_monitor():
    global turnOnPc
    for pc in turnOnPc:
        if(pc['state'] and pc['z_max'] < 3.2):
            # lado esquerdo
            glPushMatrix()
            glColor3f(1, 1, 1)
            glTranslatef((pc['x_min']+0.2)*medida, (pc['y_max']+0.13) *medida, (pc['z_min']+0.41) *medida)
            glScale(0.37, 0.84, 0.54)
            glRotatef(90, 0, 1, 0)
            glRotatef(-90, 1, 0, 0)
            glCallList(objMonitorOn.gl_list)
            glPopMatrix()
        elif(pc['state'] and pc['z_max'] > 3.2):
            # lado direito
            glPushMatrix()
            glColor3f(1, 1, 1)
            glTranslatef((pc['x_min']+0.2)*medida, (pc['y_max']+0.13) *medida, (pc['z_min']-0.38) *medida)
            glScale(0.37, 0.84, 0.54)
            glRotatef(90, 0, 1, 0)
            glRotatef(-90, 1, 0, 0)
            glCallList(objMonitorOn.gl_list)
            glPopMatrix()

def ligar_pc():
    global turnOnPc

    for pc in turnOnPc:
        if(pc['state']):
            glPushMatrix()
            modelar_objeto(pc['x_max'], pc['x_min'], pc['y_max'], pc['y_min'], pc['z_max'], pc['z_min'], 0, 1, 0)
            glPopMatrix()

def setup_lamp():
    x_max, x_min, y_max, y_min, z_max, z_min = 7.99, 7.985, 1.445, 1.425, 5.02, 4.98
    turnLampRoof.append({'x_max': x_max, 'x_min': x_min, 'y_max': y_max, 'y_min': y_min, 'z_max': z_max, 'z_min': z_min, 'state': False})

def montar_tomada():
    global turnSwitch, turnLamp
    x_max, x_min, y_max, y_min, z_max, z_min = 8, 7.99, 1.55, 1.35, 5.03, 4.97
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.93,0.90,0.66)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.99, 7.985, 1.485, 1.465, 5.02, 4.98
    turnSwitch.append({'x_max': x_max, 'x_min': x_min, 'y_max': y_max, 'y_min': y_min, 'z_max': z_max, 'z_min': z_min, 'state': False})
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.87,0.72,0.52)

    x_max, x_min, y_max, y_min, z_max, z_min = 7.99, 7.985, 1.445, 1.425, 5.02, 4.98
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.87,0.72,0.52)

def loop():
    global angleVent, turnSwitch

    if turnSwitch[0]['state']:
        angleVent += 15
        if(angleVent >= 360):
            angleVent = 0
    
    if isDay:
        glClearColor(0.73, 0.95, 0.97, 1)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.5, 0.5, 0.5, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0, 0, 0, 1])
    else:
        glClearColor(0, 0, 0.1, 1)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.15, 0.15, 0.15, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0, 0, 0, 1])
    glutPostRedisplay()

def montar_janela_de_movimento(tam_x, tam_y):
    global medida
    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    x_max, x_min, y_max, y_min, z_max, z_min = -0.035 + (tam_x/2), 0.035 - (tam_x/2), -0.035 + (tam_y/2), 0.035 - (tam_y/2), 0.005, -0.005
    glBegin(GL_QUADS)
    glColor4f(0.75,0.75,0.75, 0.5) 
    glVertex3f(x_max * medida, y_min * medida, 0 * medida)
    glVertex3f(x_max * medida, y_max * medida, 0 * medida)
    glVertex3f(x_min * medida, y_max * medida, 0 * medida)
    glVertex3f(x_min * medida, y_min * medida, 0 * medida)
    glEnd()
    glPopMatrix()

    # parte esquerda da janela
    x_max, x_min, y_max, y_min, z_max, z_min = 0.035 - (tam_x/2), 0.005 - (tam_x/2), (tam_y/2), -(tam_y/2), 0.005, -0.005
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)

    # parte direita da janela
    x_max, x_min, y_max, y_min, z_max, z_min = -0.005 + (tam_x/2), -0.035 + (tam_x/2), (tam_y/2), -(tam_y/2), 0.005, -0.005
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)

    # parte de cima da janela
    x_max, x_min, y_max, y_min, z_max, z_min = -0.035 + (tam_x/2), 0.035 - (tam_x/2), (tam_y/2), -0.035 + (tam_y/2), 0.005, -0.005
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)

    # parte de baixo da janela
    x_max, x_min, y_max, y_min, z_max, z_min = -0.035 + (tam_x/2), 0.035 - (tam_x/2), 0.035 - (tam_y/2), -(tam_y/2), 0.005, -0.005
    modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)

def habilitar_spot():
    if turnLampPc:
        glEnable(GL_LIGHT1)
        luz(6.34, 1.45, 4.125, GL_LIGHT1, 90, 0.2)

        glEnable(GL_LIGHT2)
        luz(6.34, 1.45, 5.025, GL_LIGHT2, 90 , 0.2)
        
        glEnable(GL_LIGHT3)
        luz(6.34, 1.45, 5.925, GL_LIGHT3, 90, 0.2)

        glEnable(GL_LIGHT4)
        luz(6.34, 1.45, 2.305, GL_LIGHT4, 90, 0.2)

        glEnable(GL_LIGHT5)
        luz(6.34, 1.45, 1.405, GL_LIGHT5, 90, 0.2)
        
        glEnable(GL_LIGHT6)
        luz(6.34, 1.45, 0.505, GL_LIGHT6, 90, 0.2)
    
    if turnLampRoof[0]['state']:
        glEnable(GL_LIGHT7)
        luz(2.5, 3, 3.2, GL_LIGHT7, 180, 0.005)
        if not isDay:
            glLightfv(GL_LIGHT7, GL_AMBIENT, [0.25, 0.25, 0.25, 1])
        else:
            glLightfv(GL_LIGHT7, GL_AMBIENT, [0.05, 0.05, 0.05, 1])
        

def desabilitar_spot():
    if not turnLampPc:
        glDisable(GL_LIGHT1)
        glDisable(GL_LIGHT2)
        glDisable(GL_LIGHT3)
        glDisable(GL_LIGHT4)
        glDisable(GL_LIGHT5)
        glDisable(GL_LIGHT6)
    if not turnLampRoof[0]['state']:
        glDisable(GL_LIGHT7)

def montar_lampadas(colorR, colorG, colorB):
    x, y, z = 5, 2.95, 4.8
    for lado_direiro in range(3):
        # apoio da lampada
        x_max, x_min, y_max, y_min, z_max, z_min = x, x-0.1, 3, 2.88, z+0.1, z-0.05
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)

        x_max, x_min, y_max, y_min, z_max, z_min = x+1.1, x+1, 3, 2.88, z+0.1, z-0.05
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)

        for par in range(2):
            glPushMatrix()
            glTranslatef(x*medida, y*medida, z*medida) # Define a posição do cilindro
            glRotatef(90, 0, 1, 0) # Rotaciona o cilindro
            glColor3f(colorR, colorG, colorB) # Define a cor do cilindro
            quad = gluNewQuadric() # Cria um novo objeto quadric
            gluQuadricDrawStyle(quad, GLU_FILL) # Define o estilo de desenho
            gluCylinder(quad, 0.15, 0.15, 1*medida, 32, 32) # Desenha o cilindro
            glPopMatrix()
            z+=0.05
        
        x-=2
        z = 4.8

    x, y, z = 5, 2.95, 1.6
    for lado_esquerdo in range(3):
        # apoio da lampada
        x_max, x_min, y_max, y_min, z_max, z_min = x, x-0.1, 3, 2.88, z+0.1, z-0.05
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)

        x_max, x_min, y_max, y_min, z_max, z_min = x+1.1, x+1, 3, 2.88, z+0.1, z-0.05
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0,0,0)

        for par in range(2):
            glPushMatrix()
            glTranslatef(x*medida, y*medida, z*medida) # Define a posição do cilindro
            glRotatef(90, 0, 1, 0) # Rotaciona o cilindro
            glColor3f(colorR, colorG, colorB) # Define a cor do cilindro
            quad = gluNewQuadric() # Cria um novo objeto quadric
            gluQuadricDrawStyle(quad, GLU_FILL) # Define o estilo de desenho
            gluCylinder(quad, 0.15, 0.15, 1*medida, 32, 32) # Desenha o cilindro
            glPopMatrix()
            z+=0.05
        
        x-=2
        z = 1.6


def luz(x, y, z, type_luz, angle, clarity):
    glLightfv(type_luz, GL_POSITION, [x * medida, y*medida, z*medida, 1])
    glLightfv(type_luz, GL_SPOT_DIRECTION, [0.0, -1.0, 0.0])
    glLightfv(type_luz, GL_DIFFUSE, [1, 1, 1, 1])
    glLightfv(type_luz, GL_SPECULAR, [0.5, 0.5, 0.5, 1])
    glLightf(type_luz, GL_SPOT_CUTOFF, angle)
    glLightf(type_luz, GL_SPOT_EXPONENT, 1)
    
    glLightf(type_luz, GL_CONSTANT_ATTENUATION, 1)
    glLightf(type_luz, GL_LINEAR_ATTENUATION, 0.01)
    glLightf(type_luz, GL_QUADRATIC_ATTENUATION, clarity)

def montar_luminaria(r, g, b):
    #  lado direito
    x_max, x_min, y_max, y_min, z_max, z_min = 6.58, 6.56, 1.515, 0.815, 4.135,4.115
    while(z_max < 6.4):
        glPushMatrix()
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
        glPopMatrix()
        z_max+=0.9
        z_min+= 0.9
    
    x_max, x_min, y_max, y_min, z_max, z_min = 6.58, 6.35, 1.53, 1.515, 4.135,4.115
    while(z_max < 6.4):
        glPushMatrix()
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
        glPopMatrix()
        z_max+=0.9
        z_min+= 0.9

    x_max, x_min, y_max, y_min, z_max, z_min = 6.35, 6.33, 1.53, 1.45, 4.135,4.115
    while(z_max < 6.4):
        glPushMatrix()
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
        glPopMatrix()
        z_max+=0.9
        z_min+= 0.9
    
    x_max, x_min, y_max, y_min, z_max, z_min = 6.37, 6.31, 1.48, 1.42, 4.155,4.095
    while(z_max < 6.4):
        glPushMatrix()
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(((x_max+x_min)/2)*medida, y_min*medida, ((z_max+z_min)/2)*medida)
        glColor3f(r, g, b)
        glutSolidSphere(0.15, 50, 50)
        glPopMatrix()
        z_max+=0.9
        z_min+= 0.9

    # lado esquerdo
    x_max, x_min, y_max, y_min, z_max, z_min = 6.58, 6.56, 1.515, 0.815, 2.315, 2.295
    while(z_max > 0):
        glPushMatrix()
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
        glPopMatrix()
        z_max-=0.9
        z_min-= 0.9
    
    x_max, x_min, y_max, y_min, z_max, z_min = 6.58, 6.35, 1.53, 1.515, 2.315, 2.295
    while(z_max > 0):
        glPushMatrix()
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
        glPopMatrix()
        z_max-=0.9
        z_min-= 0.9

    x_max, x_min, y_max, y_min, z_max, z_min = 6.35, 6.33, 1.53, 1.45, 2.315, 2.295
    while(z_max > 0):
        glPushMatrix()
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
        glPopMatrix()
        z_max-=0.9
        z_min-= 0.9
    
    x_max, x_min, y_max, y_min, z_max, z_min = 6.37, 6.31, 1.48, 1.42, 2.335, 2.275
    while(z_max > 0):
        glPushMatrix()
        modelar_objeto(x_max, x_min, y_max, y_min, z_max, z_min, 0.2, 0.2, 0.2)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(((x_max+x_min)/2)*medida, y_min*medida, ((z_max+z_min)/2)*medida)
        glColor3f(r, g, b)
        glutSolidSphere(0.15, 50, 50)
        glPopMatrix()
        z_max-=0.9
        z_min-= 0.9

def load_texture(filename):
    image = Image.open(filename)
    width, height = image.size
    image_data = image.tobytes()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)

    return texture_id

def Draw():
    setup_lamp()
    global medida, cx, cy, cz, fx, fy, fz, ux, uy, uz, anglePorta, angleVent, objTeclado, turnLamp
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMaterialfv(GL_FRONT, GL_AMBIENT, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.1, 0.1, 0.1, 1])
    glMaterialfv(GL_FRONT, GL_SHININESS, 10.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(cx, cy, cz, cx + fx, cy + fy, cz + fz, ux, uy, uz)

    glPushMatrix()
    ligar_monitor()
    glPopMatrix()

    glPushMatrix()
    montar_teclado()
    glPopMatrix()


    glPushMatrix()
    if not turnLampPc:
        montar_luminaria(0.4, 0.4, 0.4)
    else:
        montar_luminaria(1, 1, 1)
        
    if turnLampRoof[0]['state']:
        montar_lampadas(1, 1, 1)
    else:
        montar_lampadas(0.3, 0.3, 0.3)
    habilitar_spot()
    desabilitar_spot()
    glPopMatrix()

    glPushMatrix()
    montar_tomada()
    glPopMatrix()

    glPushMatrix()
    ligar_pc()
    glPopMatrix()

    glPushMatrix()
    montar_paredes()
    montar_mesas()
    montar_monitores()
    montar_quadro()
    montar_estruturas_da_porta()
    glPopMatrix()
    
    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    montar_janela_lado_direito()
    glPopMatrix()

    glPushMatrix()
    x_center, y_center, z_center = 0.75, 2.1, -0.075
    for i in range(10):
        glPushMatrix()
        glTranslatef(x_center*medida, y_center*medida, z_center*medida)
        glRotatef(angleJanela, 0, 1, 0)
        montar_janela_de_movimento(0.5, 1.7)
        glPopMatrix()
        x_center+=0.5

    x_center, y_center, z_center = 6.05, 2.1, -0.075
    for i in range(4):
        glPushMatrix()
        glTranslatef(x_center*medida, y_center*medida, z_center*medida)
        glRotatef(angleJanela, 0, 1, 0)
        montar_janela_de_movimento(0.5, 1.7)
        glPopMatrix()
        x_center+=0.5
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
    glPopMatrix()

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

    glutSwapBuffers()

def myInit():
    glClearColor(0.73, 0.95, 0.97, 1)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def gerenciaMouse(button,state, x, y):
    global antigo_x, antigo_y

    vport = glGetIntegerv(GL_VIEWPORT)
    depth = glReadPixels(x, vport[3] - y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)

    vport      = glGetIntegerv(GL_VIEWPORT)
    mvmatrix   = glGetDoublev(GL_MODELVIEW_MATRIX)
    projmatrix = glGetDoublev(GL_PROJECTION_MATRIX)

    worldCoordinate1 = gluUnProject(x, vport[3] - y, depth, mvmatrix, projmatrix, vport)

    if state == 1:
        for pc in turnOnPc:
            if pc['x_max']*medida >= worldCoordinate1[0] >= ((pc['x_min']*medida) - 0.2) and pc['y_max']*medida >= worldCoordinate1[1] >= pc['y_min']*medida and pc['z_max']*medida >= worldCoordinate1[2] >= pc['z_min']*medida:
                if pc['state']:
                    pc['state'] = False
                    break
                else:
                    pc['state'] = True
                    break

        for switch in turnSwitch:
            if switch['x_max']*medida >= worldCoordinate1[0] >= ((switch['x_min']*medida) - 0.2) and switch['y_max']*medida >= worldCoordinate1[1] >= switch['y_min']*medida and switch['z_max']*medida >= worldCoordinate1[2] >= switch['z_min']*medida:
                if switch['state']:
                    switch['state'] = False
                    break
                else:
                    switch['state'] = True
                    break

        for lamp in turnLampRoof:
            if lamp['x_max']*medida >= worldCoordinate1[0] >= ((lamp['x_min']*medida) - 0.2) and lamp['y_max']*medida >= worldCoordinate1[1] >= lamp['y_min']*medida and lamp['z_max']*medida >= worldCoordinate1[2] >= lamp['z_min']*medida:
                if lamp['state']:
                    lamp['state'] = False
                    break
                else:
                    lamp['state'] = True
                    break

    antigo_x = x
    antigo_y = y
    glutPostRedisplay()

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


def setup_lighting():
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)

    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT7)

    # luz no pc
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT3)
    glEnable(GL_LIGHT4)
    glEnable(GL_LIGHT5)
    glEnable(GL_LIGHT6)



    glShadeModel(GL_SMOOTH)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)


def main():
    global objTeclado, objMonitorOn, texture_board, texture_fan, texture_floor

    glutInit()
    glutInitWindowSize(1600, 1000)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutCreateWindow("lab 2")
    glEnable(GL_MULTISAMPLE)
    myInit()
    texture_board = load_texture("texture/board.jpg")
    texture_fan = load_texture("texture/fan.jpg")
    texture_floor = load_texture("texture/floor.jpeg")
    objTeclado = OBJ('ObjBlender/teclado.obj')
    objMonitorOn = OBJ('ObjBlender/monitor.obj')
    setup_lighting()
    glutDisplayFunc(Draw)
    glutIdleFunc(loop)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(gerenciaMouse)
    glutMotionFunc(mouse_camera)
    glutMainLoop()

if __name__ == '__main__':
    main()