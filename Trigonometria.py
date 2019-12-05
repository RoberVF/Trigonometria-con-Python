import math
import os

while True:
    os.system("cls")
    print("1. Razones trigonometricas")
    print("2. Teorema de pitagoras")
    print("3. Cambio de variable")
    print("4. Puntos de la 'Y' en Eje de Coordenadas")
    print("\n Establece un valor: ")
    variable= int(input())

    if variable==1:
        os.system("cls")
        print("\t*Razones trigonometricas*\n")
        print("Declara un lado")
        a= float (input())
        print("Declara el otro lado")
        b= float (input())
        print("Declara la altura")
        h= float (input())
        seno= round(a/h, 3)
        coseno= round(b/h, 3)
        tangente= round(a/b, 3)
        print("Sen= ", seno)
        print("Cos= ", coseno)
        print("Tan= ", tangente)
        os.system("pause")

    if variable==2:
        os.system("cls")
        print("\t*Teorema de pitagoras*\n")
        print("Declara el cateto 1")
        cateto1= float(input())
        print("Declara el cateto 2")
        cateto2= float(input())
        altura= cateto1**2 + cateto2**2
        
        print("La altura es: ", round(math.sqrt(altura), 2))
        os.system("pause")

    if variable==3:
        os.system("cls")
        print("\t*Cambio de unidades*")
        print("\n1. Cambio de radianes a grados (Tengo radianes quiero grados)")
        print("2. Cambio de grados a radianes (Tengo grados y quiero radianes)")
        eleccion= float(input())
        if eleccion==1:
            print("Establece los radianes")
            r= float(input())
            resultadoR= round(r*180 / 3.1416, 2)
            print(r, "radianes equivalen a", resultadoR, "grados")
            os.system("pause")

        if eleccion==2:
            print("Establece los grados")
            g= float(input())
            resultadoG= round(g*3.1416 / 180, 2)
            print(g, "grados equivalen a", resultadoG, "radianes")
            os.system("pause")

        else:
            pass

    if variable==4:
        os.system("cls")
        print("*\tValores de la y*\n")
        print("1. Valor predeterminado de la X")
        print("2. Valor personalizado de la X")
        valor= int(input())
        if valor==1:
            os.system("cls")
            print("\tValor predeterminado\n")
            print("""
    Coseno de alfa     Seno de alfa    Tangente de alfa

        X  |  Y           X  |  Y          X  |  Y
      -----------       -----------      ----------
      -180 | -1         -180 |  0        -180 |  0
      -90  |  0         -90  | -1        -45  | -1
        0  |  1           0  |  0          0  |  0
       90  |  0          90  |  1         45  |  1
       180 | -1          180 |  0         180 |  0
            """)
            os.system("pause")
        if valor==2:
            os.system("cls")
            print("\tValor personalizado\n")
            print("Establece parametros para las X en radianes:")
            subindice= str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
            print("X1=".translate(subindice))
            x1= float(input())
            print("X2=".translate(subindice))
            x2= float(input())
            print("X3=".translate(subindice))
            x3= float(input())
            print("X4=".translate(subindice))
            x4= float(input())
            print("X5=".translate(subindice))
            x5= float(input())
            
            #Coseno
            resultado1cos= round(math.cos(x1), 2)
            resultado2cos= round(math.cos(x2), 2)
            resultado3cos= round(math.cos(x3), 2)
            resultado4cos= round(math.cos(x4), 2)
            resultado5cos= round(math.cos(x5), 2)

            print("\n  Coseno  \n")
            print("   X   |   Y   ")
            print("---------------")
            print(x1,   "  | ", resultado1cos)
            print(x2,   "  | ", resultado2cos)
            print(x3,   "  | ", resultado3cos)
            print(x4,   "  | ", resultado4cos)
            print(x5,   "  | ", resultado5cos)

            #Seno
            resultado1sin= round(math.sin(x1), 2)
            resultado2sin= round(math.sin(x2), 2)
            resultado3sin= round(math.sin(x3), 2)
            resultado4sin= round(math.sin(x4), 2)
            resultado5sin= round(math.sin(x5), 2)

            print("\n   Seno   \n")
            print("   X   |   Y   ")
            print("---------------")
            print(x1,   "  | ", resultado1sin)
            print(x2,   "  | ", resultado2sin)
            print(x3,   "  | ", resultado3sin)
            print(x4,   "  | ", resultado4sin)
            print(x5,   "  | ", resultado5sin)

            #Tangente
            resultado1tan= round(math.tan(x1), 2)
            resultado2tan= round(math.tan(x2), 2)
            resultado3tan= round(math.tan(x3), 2)
            resultado4tan= round(math.tan(x4), 2)
            resultado5tan= round(math.tan(x5), 2)

            print("\n  Tangente   \n")
            print("   X   |   Y   ")
            print("---------------")
            print(x1,   "  | ", resultado1tan)
            print(x2,   "  | ", resultado2tan)
            print(x3,   "  | ", resultado3tan)
            print(x4,   "  | ", resultado4tan)
            print(x5,   "  | ", resultado5tan)

            os.system("pause")

    else:
        pass



