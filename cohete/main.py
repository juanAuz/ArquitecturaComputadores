import argparse
from utils.projectile_functions import dSdt
from utils.projectile_functions import resolverEDO

def main(resAire,velInicial,tiempoVuelo,angulos):
    #resAire = B
    #velInicial = V
    #tiempoVuelo = t
    #angulos = angulos 





    # --- PRUEBA DE QUE LOS ARGS LLEGAN BIEN ---
    print("\n" + "="*40)
    print("¡DATOS RECIBIDOS CORRECTAMENTE EN EL MAIN!")
    print("="*40)
    print(f"Resistencia del aire (B): {resAire} (Tipo: {type(resAire).__name__})")
    print(f"Velocidad inicial (V):    {velInicial} (Tipo: {type(velInicial).__name__})")
    print(f"Tiempo de vuelo (t):      {tiempoVuelo} (Tipo: {type(tiempoVuelo).__name__})")
    print(f"Lista de ángulos:         {angulos} (Tipo: {type(angulos).__name__})")
    print("="*40 + "\n")




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
