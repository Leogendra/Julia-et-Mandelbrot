import math
import time

##############################################################
# fonctions sur les nombre complexes
def i_plus(z1,z2):
    return [z1[0]+z2[0],z1[1]+z2[1]]

def i_moins(z1,z2):
    return [z1[0]-z2[0],z1[1]-z2[1]]

def i_fois(z1,z2):
    a = z1[0]
    b = z1[1]
    c = z2[0]
    d = z2[1]
    return [a*c-b*d, a*d+b*c]

def i_carre(z):
    return i_fois(z,z)

##############################################################
# Fonction de dessin
def print_zone(z, axe):
    if axe:
        z = set_axis(z)
    for l in z:
        for c in l:
            print(c,end='')
        print()


def set_axis(z):
    x, y = get_dimensions(z)
    for i in range(2*y+1):
        for j in range(2*x+1):
            if i == y:
                if j == x:
                    if z[i][j] == ' ':
                        z[i][j] = '┼'
                    else:
                        z[i][j] = '╬'
                else:
                    if z[i][j] == ' ':
                        z[i][j] = '─'
                    else:
                        z[i][j] = '═'
            else:
                if j == x:
                    if z[i][j] == ' ':
                        z[i][j] = '│'
                    else:
                        z[i][j] = '║'
                    
    return z

def get_zone(maxx, maxy):
    zone = []
    lignes = 2*maxy + 1
    colonnes = 2*maxx + 1
    zero = [maxy+1,maxx+1]
    # zone de base
    for i in range(lignes):
        zone.append([" " for j in range(colonnes)])
    return zone


def get_dimensions(z):
    y = len(z) // 2
    x = len(z[0]) // 2
    return [x,y]


##############################################################
# Fonction pour les fractales
def z_carre_plus_c_boucle(z, c): # z² + c, avec c = a+ib
    cpt = 0
    while abs(z[0]+z[1]) < 10000 and cpt < 100:
        cpt += 1
        z = i_plus(i_carre(z), c)
    return cpt >= 100



def julia(zone, c): # z² + c
    x, y = get_dimensions(zone)
    for i in range(2*y+1):
        for j in range(2*x+1):
            if z_carre_plus_c_boucle([(j-x)/(x*0.6),-(i-y)/(y*0.8)],c):
                zone[i][j] = '#'
    return zone


def mandelbrot(zone):
    x, y = get_dimensions(zone)
    for i in range(2*y+1):
        for j in range(2*x+1):
            if z_carre_plus_c_boucle([0, 0], [(j-x)/(x*0.6), -(i-y)/(y*0.8)]):
                zone[i][j] = '#'
    return zone




# Fonction principale
def main():
    max_x = int(input("longueur : ")) // 2
    max_y = int(input("hauteur : ")) // 2
    axes = input("axes ? [0=Non, 1=Oui] : ") == "1"
    leave = "1"
    while leave != "0":
        plan = get_zone(max_x, max_y)
        ensemble = input("Julia, Mandelbrot, ou Julia Manuel [j/m/jm] ? ")
        if ensemble.lower() == "jm":
            print("Entrez a + ib (a,b inclus dans [-0.5; 0.5]).")
            a = float(input("a="))
            b = float(input("b="))
            print_zone(julia(plan, [a,b]), axes)

        elif ensemble.lower() == "m":
            print_zone(mandelbrot(plan), axes)
        else:
            for i in range(110,314*2):
                x = i/100
                a = math.cos(x)/1.5
                b = math.sin(x)/1.5
                print_zone(julia(plan, [a,b]), axes)
                print("c =",a,"+ i"+str(b),end='\r')
                time.sleep(0.1)

        leave = input("0 to exit ")


main()