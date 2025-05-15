from calculos import menu_calcular_propina, dividir_cuenta

def main():
    while True:
        print("="*200)
        print (f"\n                 --- SIMULADOR DE PROPINA DEL RESTAURANTE DE DUKO PA' ---                    \n".center(50))
        print("="*200)
        opcion = input("\n1. Calcular propina y total a pagar. \n2. Calcular total a pagar dividido entre personas.\n3. SALIR. \nPor favor, digite una opcion (1-3): ")
        
        if opcion == "1":
            print("="*200)
            print("\n                 --- CALCULAR PROPINA ---                    \n")
            print("="*200)
            menu_calcular_propina ()
        elif opcion == "2":
            print("="*200)
            print("\n                   --- DIVIDIR CUENTA ENTRE VARIAS PERSONAS ---                    \n")
            print("="*200)
            dividir_cuenta()
        else:
            print ("Gracias por usar el simulador de propina del restaurante de Duko Pa' ")
            break
        
main ()
