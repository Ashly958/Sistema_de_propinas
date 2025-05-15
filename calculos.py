
def menu_calcular_propina ():
    opcion = input ("Digite el porcentaje de propina que desea dejar:\n1. 10%. \n2. 15%. \n3. 20%.\n")
    
    if opcion == "1":
        print("El porcentaje de propina elegido es 10% ")
        calcular_propina()
    elif opcion == "2":
        print("El porcentaje de propina elegido es 15% ")
        calcular_propina()
    elif opcion == "3":
        print("El porcentaje de propina elegido es 20% ")
        calcular_propina()
    

def calcular_propina ():
    monto_total =float (input ("Ingrese el monto total de la cuenta: $ "))
    porcentaje_propina = int (input("Ingrese el porcentaje de propina que desea dejar: "))
    print (f"El porcentaje de propina elegido es: {porcentaje_propina}%")
    propina = monto_total * (porcentaje_propina / 100)
    total_a_pagar = monto_total + propina 
    print (f"El monto total a pagar es: ${total_a_pagar:.2f}")  
    return total_a_pagar

    
def dividir_cuenta ():    
    monto_total =float (input ("Ingrese el monto total de la cuenta: $ "))
    personas = int (input("Ingrese el numero de personas entre las que desea dividir la cuenta: "))
    monto_total = calcular_propina()
    division = monto_total / personas
    print ("El costo por persona es: $", division)
