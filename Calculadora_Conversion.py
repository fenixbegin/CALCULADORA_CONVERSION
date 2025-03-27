def base_converter():
    try:
        numero_inicial = input("Ingrese el numero:")
        base_origen = int(input("Ingrese la base original del numero: "))
        base_destino = int(input("Ingrese la base a la que desea convertir: "))

        # Convertir a decimal (base 10)
        numero_decimal = int(numero_inicial, base_origen)

        # Convertir de decimal a la base destino
        if base_destino == 10:
            resultado = str(numero_decimal)
        else:
            if numero_decimal == 0:
                resultado = "0"
            else:
                digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                resultado = ""
                while numero_decimal > 0:
                    residuo = numero_decimal % base_destino
                    resultado = digitos[residuo] + resultado
                    numero_decimal //= base_destino

        print(f"El número {numero_inicial} en base {base_origen} es igual a {resultado} en base {base_destino}")

    except ValueError:
        print("Error: Ingrese valores válidos para el número y las bases.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    base_converter()