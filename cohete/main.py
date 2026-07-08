import argparse
from utils.projectile_functions import dSdt
from utils.projectile_functions import resolverEDO
import matplotlib.pyplot as plt

def main(resAire,velInicial,tiempoVuelo,angulos):
    #resAire = B
    #velInicial = V
    #tiempoVuelo = t
    #angulos = angulos 

    # Resolver la trayectoria para cada ángulo y graficarla
    for angulo in angulos:
        solucion = resolverEDO(resAire, velInicial, tiempoVuelo, angulo)

        plt.plot(
            solucion.y[0],
            solucion.y[2],
            label=fr'$\theta_0={angulo}^\circ$'
        )

    plt.ylim(bottom=0)
    plt.xlabel("$x/g$", fontsize=14)
    plt.ylabel("$y/g$", fontsize=14)
    plt.title("Trayectoria del cohete")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lanzamiento de un cohete')
    parser.add_argument('-B', '--resAire',type = float, default = 0.1, help = "Se declara la variable para la resistencia del aire, ej. 0.1"
                        )
    parser.add_argument('-V','--velInicial',type=float, default = 1, help = "Se declara la variable para la velocidad inicial del lanzamiento"
                        )
    parser.add_argument('-t','--tiempoVuelo' ,type=float,default = 2, help = "tiempo de vuelo"
                        )
    parser.add_argument('-a', '--angulos',type=float,nargs='+', default = [40,45,50,60], help = "Se declaran n angulos de lanzamiento para el cohete"
                        )
    args = parser.parse_args()
    main(args.resAire, args.velInicial, args.tiempoVuelo, args.angulos)
