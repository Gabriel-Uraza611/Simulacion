import tkinter as tk
from tkinter import messagebox
import sympy

def polinomio_lagrange(x_puntos, y_puntos):
   
    x = sympy.symbols('x') #Definir 'x' como un símbolo matemático
    n = len(x_puntos)
    polinomio = 0 #Inicializar el polinomio final. Es la variable para la gran Sumatoria (Σ).

    #BUCLE PRINCIPAL (IMPLEMENTA LA SUMATORIA: Σ desde k=0 hasta n-1)
    for k in range(n):
        #Cada iteración construye un término completo: y_k * L_k(x)
        termino_Lk = 1 #Inicializar el polinomio base L_k(x). Es la variable para el Producto (Π).
        for j in range(n): #BUCLE ANIDADO (IMPLEMENTA EL PRODUCTO: Π desde j=0 hasta n-1, con j≠k). Construye cada fracción (x - x_j) / (x_k - x_j) y la multiplica.
            if j != k: #La condición j≠k es crucial para evitar la división por cero (x_k - x_k).
                termino_Lk *= (x - x_puntos[j]) / (x_puntos[k] - x_puntos[j])
        
        polinomio += y_puntos[k] * termino_Lk #Construir el término completo de la suma y añadirlo al polinomio total. Esto es: y_k * L_k(x)
    
    # Simplificar el polinomio para una mejor presentación
    polinomio_expandido = sympy.expand(polinomio)
    
    # Crear una función numérica para evaluar el polinomio
    funcion_evaluable = sympy.lambdify(x, polinomio_expandido, 'numpy')
    
    return polinomio_expandido, funcion_evaluable # Retornamos tanto el polinomio bonito para mostrar, como la función rápida para calcular.

def ventana_lagrange():
    # Crear la ventana secundaria
    top = tk.Toplevel()
    top.title("Interpolación de Lagrange")
    top.geometry("500x400")
    top.configure(bg="#f0f0f0")

    tk.Label(top, text="Interpolación de Lagrange", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    # Entradas de datos
    tk.Label(top, text="Valores de x (separados por comas):", bg="#f0f0f0").pack()
    entrada_x = tk.Entry(top, width=50)
    entrada_x.pack(pady=5)

    tk.Label(top, text="Valores de y (separados por comas):", bg="#f0f0f0").pack()
    entrada_y = tk.Entry(top, width=50)
    entrada_y.pack(pady=5)

    tk.Label(top, text="Valor de x a interpolar (opcional):", bg="#f0f0f0").pack()
    entrada_valor = tk.Entry(top, width=20)
    entrada_valor.pack(pady=5)
    
    # Etiqueta para mostrar los resultados
    resultado_texto = tk.StringVar()
    label_resultado = tk.Label(top, textvariable=resultado_texto, font=("Arial", 12), wraplength=450, justify="left", bg="white", relief="solid", borderwidth=1, padx=10, pady=10)
    label_resultado.pack(pady=15, fill="both", expand=True)

    def calcular_interpolacion():
        try:
            x_str = entrada_x.get()
            y_str = entrada_y.get()
            
            if not x_str or not y_str:
                messagebox.showerror("Error", "Los campos de 'x' e 'y' no pueden estar vacíos.")
                return

            x = list(map(float, x_str.split(",")))
            y = list(map(float, y_str.split(",")))
            
            if len(x) != len(y):
                messagebox.showerror("Error", "Las listas de 'x' e 'y' deben tener la misma longitud.")
                return

            polinomio_simbolico, funcion_evaluable = polinomio_lagrange(x, y)
            polinomio_str = str(polinomio_simbolico).replace('**', '^')
            texto_final = f"Polinomio de Lagrange P(x):\n{polinomio_str}"

            # Evaluar el polinomio si se proporcionó un valor
            valor_str = entrada_valor.get()
            if valor_str:
                valor = float(valor_str)
                resultado_evaluacion = funcion_evaluable(valor)
                texto_final += f"\n\nEvaluación en x = {valor}:\nP({valor}) ≈ {resultado_evaluacion:.6f}"
            
            resultado_texto.set(texto_final)

        except ValueError:
            messagebox.showerror("Error", "Verifica que los valores estén bien escritos y separados por comas.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Los valores de 'x' deben ser únicos (no puede haber puntos repetidos).")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")

    # Botón para ejecutar el cálculo
    tk.Button(top, text="Calcular", command=calcular_interpolacion, bg="#FF9800", fg="white", font=("Arial", 12, "bold")).pack(pady=10)