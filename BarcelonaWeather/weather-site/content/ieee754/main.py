import ieee754_sum as IEEE754
def mostrarIEEE754(numero, resultado):
    """
    Muestra la información de un número en representación IEEE754
    """
    print("Representación del número ", numero, "en IEEE754")
    print("-"*50)
    print("Signo:",resultado["signo"])
    print("Exponente:",resultado["exponenteSesgado"])
    print("Mantisa:",resultado["mantisa"])
    print("IEEE754:",resultado["ieee754"])

def mostrarProcesoSuma(resultado):
    """
    Muestra paso a paso el proceso realizado para la suma IEEE754
    """
    print("\n1. Alineación de exponentes")
    print("-"*50)

    print("Exponente común:",resultado["exponenteComun"])

    print("Mantisa 1 alineada:",resultado["mantisa1Alineada"])

    print("Mantisa 2 alineada:",resultado["mantisa2Alineada"])

    print("\n2. Operación de mantisas")
    print("-"*50)

    print("Operación realizada:",resultado["operacion"])

    print("Signo del resultado:",resultado["signoFinal"])

    print("Mantisa mayor:",resultado["mantisaMayor"])

    print("Mantisa menor:",resultado["mantisaMenor"])

    print("Resultado de la operación:",resultado["mantisaResultado"])
    print("\n3. Normalización del resultado")
    print("-"*50)

    print("Mantisa normalizada:",
          resultado["mantisaNormalizada"])

    print("Exponente final:",
          resultado["exponenteFinal"])
    
    print("\n4. Ensamblaje IEEE754")
    print("-"*50)

    print("Representación final:")
    print(resultado["resultadoIEEE754"])
    print("Hexadecimal:")
    print(convertirHexadecimal(resultado["resultadoIEEE754"]))

def convertirHexadecimal(ieeeBinario):
    """
    Transforma un número binario IEEE754 a hexadecimal
    """
    decimal = int(ieeeBinario, 2)
    return hex(decimal).upper()
def main():
    print("*"*50)
    print("Suma de números en IEEE754")
    print("*"*50)

    #Ingreso de datos
    num1=float(input("Ingrese el primer número: "))
    num2=float(input("Ingrese el segundo número: "))

    #Conversión a IEEE754
    ieee1 = IEEE754.convertirIEEE754(num1)
    ieee2 = IEEE754.convertirIEEE754(num2)

    print("\nConversión a IEEE754 del primer número")
    mostrarIEEE754(num1, ieee1)

    print("\nConversión a IEEE754 del segundo número")
    mostrarIEEE754(num2, ieee2)

    #Suma
    print("\n")
    print("Suma IEEE754")
    print("="*50)

    resultado = IEEE754.sumarIEEE754(num1, num2)

    mostrarProcesoSuma(resultado)


if __name__ == "__main__":
    main()

