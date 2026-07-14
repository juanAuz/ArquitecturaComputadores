def obtenerSigno(numero):
    """
    Devuelve el bit de signo según IEEE754
    """
    if numero<0:
        return 1
    else:
        return 0

def separarPartes(numero):
    """
    Separa un número en su parte entera y decimal, utilizando
    el valor absoluto del número
    """
    numero = abs(numero)
    entero = int(numero)
    decimal= numero - entero

    return entero, decimal

def convertirEnteroBinario (entero):
    """
    Devuelve la parte entera de un número en representación binaria
    Usa el método bin(), y quita la notación 0b
    """
    return bin(entero).replace("0b","")

def convertirDecimalBinario(decimal):
    """
    Devuelve la parte fraccionaria de un número en representación binaria, se utiliza el algoritmo aprendido en clase
    """
    bits = ""
    while decimal !=0 and len(bits) < 23:
        decimal = decimal*2
        if decimal>=1:
            bits +="1"
            decimal-=1
        else:
            bits += "0"

    if bits == "":
        return "0"

    return bits

def convertirBinario(numero):
    """
    Convierte un número en base decimal a un número binario, utiliza funciones que separan sus partes y las convierten a decimal.
    """
    entero, decimal = separarPartes(numero)
    return convertirEnteroBinario(entero)+"."+convertirDecimalBinario(decimal)

def normalizar(binario):
    """
    Normaliza un número binario al formato requerido para IEEE754
    Parámetro: binario de tipo string, un número binario
    Retorna la mantisa y el exponente.
    """
    entero, decimal = binario.split(".")

    #Primer caso: número mayor o igual a 1
    if entero != "0":
        exponente = len(entero)-1
        mantisa = entero [1:] + decimal
        return mantisa,exponente

    #Segundo caso: número entre 0 y 1
    indice = decimal.index("1")
    exponente = -(indice+1)
    mantisa = decimal[indice + 1:]
    return mantisa, exponente

def calcularExponente(exponente):
    """
    Calcula el exponente agregandole el sesgo, lo transforma a binario de 8 bits, para cumplir con la representación IEEE754
    """
    exponente = exponente + 127 #Sesgo 127
    binario = bin(exponente).replace("0b","")
    return binario.zfill(8)

def ajustarMantisa(mantisa):
    """
    Ajusta la mantisa para que tenga exactamente 23 bits
    """
    return mantisa.ljust(23, "0")

def convertirIEEE754(numero):
    """
    Convierte un número decimal a su representación IEEE754
    de 32 bits, retorna todas las partes del número separadas
    """
    if numero == 0:
        return {
            "signo": "0", "exponente":"00000000",
            "mantisa":"00000000000000000000000",
            "ieee754":"00000000000000000000000000000000"
        }

    signo = str(obtenerSigno(numero))
    binario = convertirBinario(numero)
    mantisa, exponente =normalizar(binario)
    exponenteIEEE = calcularExponente(exponente)
    mantisaIEEE = ajustarMantisa(mantisa)[:23]
    ieee754 = signo + exponenteIEEE + mantisaIEEE
    return {
        "signo":signo,
        "binario":binario,
        "exponenteReal": exponente,
        "exponenteSesgado":exponenteIEEE,
        "mantisa": mantisaIEEE,
        "ieee754":ieee754
    }

def alinearExponentes(exp1, mant1, exp2, mant2):
    """
    Alinea los exponentes desplazando a la mantisa del número
    con menor exponente
    """
    #Se recupera el 1 implícito
    mant1 ="1"+mant1
    mant2 = "1"+mant2

    while exp1 <exp2:
        mant1 ="0"+mant1[:-1]
        exp1 +=1

    while exp2 <exp1:
        mant2 = "0" + mant2[:-1]
        exp2 +=1

    return exp1, mant1, mant2

def determinarSignoYOrden(signo1, signo2, mant1, mant2):
    """
    Compara los signos para decidir si se suma o se resta. 
    Además, ordena las mantisas para que la resta sea siempre positiva,
    y determina cuál será el signo del resultado final.
    """
    val1 = int(mant1, 2)
    val2 = int(mant2, 2)
    
    if signo1 == signo2:
        return signo1, "suma", mant1, mant2
    else:
        # Si son signos distintos es una resta, el mayor define el signo final
        if val1 >= val2:
            return signo1, "resta", mant1, mant2
        else:
            return signo2, "resta", mant2, mant1

def operarMantisas(mantMayor, mantMenor, operacion):
    """
    Suma o resta mantisas binarias utilizando operaciones
    bit a bit.
    Retorna el resultado en binario.
    """
    while len(mantMayor) > len(mantMenor):
        mantMenor = "0" + mantMenor

    while len(mantMenor) > len(mantMayor):
        mantMayor = "0" + mantMayor

    if operacion == "suma":
        resultado = ""
        acarreo = 0

        # Se recorren las cadenas desde el bit menos significativo
        for i in range(len(mantMayor)-1, -1, -1):

            bit1 = int(mantMayor[i])
            bit2 = int(mantMenor[i])

            suma = bit1 + bit2 + acarreo

            if suma == 0:
                resultado = "0" + resultado
                acarreo = 0

            elif suma == 1:
                resultado = "1" + resultado
                acarreo = 0

            elif suma == 2:
                resultado = "0" + resultado
                acarreo = 1

            else:
                resultado = "1" + resultado
                acarreo = 1

        if acarreo == 1:
            resultado = "1" + resultado

        return resultado

    else:
        # Resta binaria
        resultado = ""
        prestamo = 0

        for i in range(len(mantMayor)-1, -1, -1):

            bit1 = int(mantMayor[i]) - prestamo
            bit2 = int(mantMenor[i])

            if bit1 < bit2:
                bit1 += 2
                prestamo = 1
            else:
                prestamo = 0

            diferencia = bit1 - bit2

            resultado = str(diferencia) + resultado

        return resultado

def normalizarResultado(mantResultado, expComun):

    if mantResultado == "0":
        return "0", 0

    exponente = expComun

    # Si hay acarreo, desplazar derecha
    if len(mantResultado) > 24:
        mantResultado = mantResultado[:-1]
        exponente += 1

    # Eliminar ceros iniciales
    while mantResultado[0] == "0":
        mantResultado = mantResultado[1:]
        exponente -= 1

    # quitar bit implícito
    mantisa = mantResultado[1:]

    return mantisa[:23], exponente

def ensamblarIEEE754(signo, exponenteReal, mantisa):
    """
    Construye la cadena final de 32 bits para su representación en IEEE754
    """
    if mantisa == "0" and exponenteReal == 0:
        return "00000000000000000000000000000000"
        
    exponenteIEEE = calcularExponente(exponenteReal)
    
    # Se ajusta la mantisa para que tenga exactamente 23 bits
    mantisaIEEE = ajustarMantisa(mantisa)[:23] 
    
    return signo + exponenteIEEE + mantisaIEEE

def sumarIEEE754(num1, num2):
    """
    Función principal integradora, usa todas las funciones anteriores
    para mostrar paso a paso el algoritmo propuesto.
    Retorna un diccionario con cada etapa del proceso.
    """

    # 1. Caso en el que uno de los números es 0
    if num1 == 0:
        return {
            "resultadoIEEE754": convertirIEEE754(num2)["ieee754"]
        }

    if num2 == 0:
        return {
            "resultadoIEEE754": convertirIEEE754(num1)["ieee754"]
        }

    # 2. Convertir y extraer partes
    ieee1 = convertirIEEE754(num1)
    ieee2 = convertirIEEE754(num2)

    # 3. Alinear exponentes
    expComun, mant1Alineada, mant2Alineada = alinearExponentes(
        ieee1["exponenteReal"], ieee1["mantisa"],
        ieee2["exponenteReal"], ieee2["mantisa"]
    )

    # 4. Analizar signos y orden
    signoFinal, operacion, mantMayor, mantMenor = determinarSignoYOrden(
        ieee1["signo"], ieee2["signo"],
        mant1Alineada, mant2Alineada
    )

    # 5. Operar aritméticamente
    mantResultado = operarMantisas(
        mantMayor,
        mantMenor,
        operacion
    )

    # 6. Normalizar el exponente y la mantisa tras operar
    mantNormalizada, expFinal = normalizarResultado(
        mantResultado,
        expComun
    )

    # 7. Ensamblar las 3 partes
    resultado = ensamblarIEEE754(
        signoFinal,
        expFinal,
        mantNormalizada
    )

    # 8. Retornar todos los pasos del algoritmo
    return {
        "exponenteComun": expComun,

        "mantisa1Alineada": mant1Alineada,
        "mantisa2Alineada": mant2Alineada,

        "signoFinal": signoFinal,
        "operacion": operacion,

        "mantisaMayor": mantMayor,
        "mantisaMenor": mantMenor,

        "mantisaResultado": mantResultado,

        "mantisaNormalizada": mantNormalizada,
        "exponenteFinal": expFinal,

        "resultadoIEEE754": resultado
    }
