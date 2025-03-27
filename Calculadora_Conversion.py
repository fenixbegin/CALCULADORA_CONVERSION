import tkinter as tk

def Mi_Calculadora():
    try:
        numero_inicial = entrada_numero.get()
        base_origen = int(entrada_base_origen.get())
        base_destino = int(entrada_base_destino.get())

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

        resultado_label.config(text=f"Resultado: {resultado}")

    except ValueError:
        resultado_label.config(text="Error: Ingrese valores válidos.")
    except Exception as e:
        resultado_label.config(text=f"Ocurrió un error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("MI CALCULADORA DE BASES NUMERCAS\n RECUERDA COLOCAR SOLO ENTEROS")
ventana.geometry("400x300")
# Crear etiquetas y entradas para los números y bases
tk.Label(ventana, text="Número:").grid(row=0, column=0)
entrada_numero = tk.Entry(ventana, width=30)
entrada_numero.grid(row=0, column=1, padx=30, pady=20)

tk.Label(ventana, text="Base Original:").grid(row=1, column=0)
entrada_base_origen = tk.Entry(ventana,width=30)
entrada_base_origen.grid(row=1, column=1, padx=30, pady=20)

tk.Label(ventana, text="Base Destino:").grid(row=2, column=0)
entrada_base_destino = tk.Entry(ventana,width=30)
entrada_base_destino.grid(row=2, column=1, padx=30, pady=20)

# Botón para resolver
resolver_boton = tk.Button(ventana, text="Resolver", command=Mi_Calculadora)
resolver_boton.grid(row=3, column=0, columnspan=2)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Resultado: ")
resultado_label.grid(row=4, column=0, columnspan=2)

ventana.mainloop()