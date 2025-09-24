#Comenzaremos realizando una calculadora
def decimal_binario():
     resto = [] 
     num = int(input('Ingrese el número decimal que desea convertir a binario: '))    
  
     while num >= 2:  #mientras que el numero sea mayor que 2 debo seguir dividiendo e ir guardando el residuo.
         if num % 2 == 0:
            resto.append(0)
         else:
            resto.append(1)
         num = num // 2 
     resto.append(num)
     print(' número binario es:', "".join(map(str, resto[::-1])))

    #Pasaremos de números binario a decimal

def binario_decimal():
     num = str(input('Ingrese el numero binario que desea conertir en decimal: '))
     num = num[::-1]

     valor  = 1
     suma = 0
     pasos = []
     for pos in range(len(num)):
        suma = suma + (int(num[pos]) * valor)
        valor = valor * 2
  
     print('El numero decimal equivalente es: ', suma) 


     #Desde aca intentaremos realizar la suma binaria
    
    
def suma_binaria():
     bin1 = input('Ingrese el primer número binario: ') # 10 en decimal
     bin2 = input('Ingrese el segundo número binario: ')   # 13 en decimal

# Convertir binario a decimal, sumar, y volver a binario
     suma_decimal = int(bin1, 2) + int(bin2, 2)
     suma_binaria = bin(suma_decimal)  # bin() devuelve una cadena como '0b10111'

# Imprimir el resultado sin el prefijo '0b'
     print(suma_binaria[2:])

def resta_binaria():
#Desde aca intentaremos realizar la resta binaria
     bin1 = input('Ingrese el primer número binario: ') # 10 en decimal
     bin2 = input('Ingrese el segundo número binario: ')   # 13 en decimal

# Convertir binario a decimal, sumar, y volver a binario
     resta_decimal = int(bin1, 2) - int(bin2, 2)
     resta_binaria = bin(resta_decimal)  # bin() devuelve una cadena como '0b10111'

# Imprimir el resultado sin el prefijo '0b'
     print(resta_binaria[2:])

while True:
    print("1. Convertir un número decimal a binario.")
    print("2. Convertir un número binario a decimal.")
    print("3. Sumar dos números binarios.")
    print("4. Restar dos número binario.")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        decimal_binario()
    elif opcion == "2":
        binario_decimal()
    elif opcion == "3":
        suma_binaria()
    elif opcion == "4":
        resta_binaria()
    elif opcion == "5":
        print('Hasta luego!')
    else:
        print("La opció ingresada no es váalida" )
