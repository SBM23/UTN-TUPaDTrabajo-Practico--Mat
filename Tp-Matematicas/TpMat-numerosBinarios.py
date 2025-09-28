
#Comenzaremos realizando una calculadora
while True:
    print("1. Convertir un número decimal a binario.")
    print("2. Convertir un número binario a decimal.")
    print("3. Sumar dos números binarios.")
    print("4. Restar dos número binario.")
    print("5. Contador binario.")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print('Ha ingresado la opción 1')
        resto = [] 
        import time 
        num = int(input('Ingrese el número decimal que desea convertir a binario: '))    
  
        while num >= 2:  #mientras que el numero sea mayor que 2 debo seguir dividiendo e ir guardando el residuo.
          if num % 2 == 0:
         
            resto.append(0)
          else:
            resto.append(1)
        
          time.sleep(3)
          print(num, '/ 2 =', num // 2, ', residuo =', num % 2)

          num = num // 2 
        else:
            print(num) 
        resto.append(num)
        time.sleep(3)
        print(' Número binario es:', "".join(map(str, resto[::-1])))
        print(f"{num} es menor que 2, se agrega directamente.")
        input('Ingrese una tecla para continuar')
        print('-------------------------*********************--------------------------')
    elif opcion == "2":
        print('Ha ingresado la opción 2')
        num = str(input('Ingrese el numero binario que desea conertir en decimal: '))
        num = num[::-1]

        valor  = 1
        suma = 0
        pasos = []
        for pos in range(len(num)):
           print(num[pos], '*', valor, '=', int(num[pos]) * valor)
           if num [pos]== "1":
             suma = suma + valor
           valor = valor * 2
   
        print('El numero decimal equivalente es: ', suma) 

        print('-------------------------*********************--------------------------')
    elif opcion == "3":
        
        print('Ha ingresado la opción 3')
        bin1 = input('Ingrese el primer número binario: ') # 10 en decimal
        decimal_1 = int(bin1, 2)
        print(f"El numero ingresado de binario a decimal es: {decimal_1}")


        bin2 = input('Ingrese el segundo número binario: ')   # 13 en decimal
        decimal_2 = int(bin2, 2)
        print(f"El numero ingresado de binario a decimal es: {decimal_2}")

               # Convertir binario a decimal, sumar, y volver a binario
        suma_decimal = decimal_1 + decimal_2
        print(f"El resultado de la suma decimal es: {suma_decimal}")    
        suma_binaria = bin(suma_decimal)  # bin() devuelve una cadena como '0b10111'

            # Imprimir el resultado sin el prefijo '0b'
        
        print("El resultado de la suma es: ", suma_binaria[2:])

       

        print('-------------------------*********************--------------------------')
    elif opcion == "4":
        print('Ha ingresado la opción 4')
        #Desde aca intentaremos realizar la resta binaria
        bin1 = input('Ingrese el primer número binario: ') # 10 en decimal
        bin2 = input('Ingrese el segundo número binario: ')   # 13 en decimal

          # Convertir binario a decimal, sumar, y volver a binario
        resta_decimal = int(bin1, 2) - int(bin2, 2)
        resta_binaria = bin(resta_decimal)  # bin() devuelve una cadena como '0b10111'

          # Imprimir el resultado sin el prefijo '0b'
        print("El resultado de la resta es: ", resta_binaria[2:])
 
        print('-------------------------*********************--------------------------')
    elif opcion == "5":
        import time

        print('Ha ingresado la opción 5')
        
        for i in range(1,16):
            binario = ""
            n = i
            while n > 0:
                binario = str(n % 2) + binario
                n = n // 2
            print(binario)
            time.sleep(1)

    elif opcion == "6":
        print('Ha ingresado la opción 6.')
        print('Hasta luego!')
        break
    else:
        print("La opció ingresada no es válida" )
print('-------------------------*********************--------------------------')