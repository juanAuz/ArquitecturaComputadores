import numpy as np
from scipy.integrate import solve_ivp

def dSdt(t,S,B):
    """
    Use fd seguido de C-TAB para generar la funcion con docstrings
    Define el sistema de ecuaciones diferenciales para el movimien    to del proyectil
    con resistencia al aire
    Parametros:
        t (float): Tiempo
        S (list): Estado actual [x, vx, y, vy]
        B (float): Coeficiente de resistencia del aire. Varía desd        e 0.0 a 1.0
    Retorna:
        list: Derivadas [dx/dt, dvx/dt, dy/dt, dvy/dt]
    """
    x, vx, y, vy = S
    return [vx,
            -B*np.sqrt(vx**2+vy**2)*vx,
            vy,
            -1-B*np.sqrt(vx**2+vy**2)*vy]
def resolverEDO(B,V,t,angulo):
    """
    Esta función resuelve la EDO utilizando la libreria ivp
    param: recibe los parametros de B: resitencia del aire, V: velocidad , t: tiempo y angulo: angulo de lanzamiento

    retorna: la función retorna la solución lista para añadirla al gráfico
    """
    #transformamos el ángulo recibido de grados a radianes

    anguloRadianes = angulo*np.pi/180

    #usando la libreria ivp calculamos la solución de la EDO y la retornamos

    return solve_ivp(dSdt, [0, t],
                 y0=[0,V*np.cos(anguloRadianes),0,V*np.sin(anguloRadianes)],
                 t_eval=np.linspace(0,t,1000),
                 args=(B,)) #atol=1e-7, rtol=1e-4)


