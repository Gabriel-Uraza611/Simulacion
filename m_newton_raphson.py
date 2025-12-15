import tkinter as tk
from tkinter import messagebox
from sympy import symbols, sympify, lambdify

x = symbols('x')

def newton_raphson(func_expr, deriv_expr, x0, tol=1e-6, max_iter=100):
    f = lambdify(x, func_expr, 'math')
    f_prime = lambdify(x, deriv_expr, 'math')
    
    for i in range(max_iter):
        try:
            fx = f(x0)
            dfx = f_prime(x0)
            if dfx == 0:
                return None, f"Derivada cero en iteración {i}, no se puede continuar."
            x1 = x0 - fx / dfx
            if abs(x1 - x0) < tol:
                return x1, f"Convergió en {i+1} iteraciones."
            x0 = x1
        except Exception as e:
            return None, f"Error en la iteración {i}: {e}"
    
    return None, "No convergió después del número máximo de iteraciones."

def ventana_raphson():
    def calcular_raiz():
        try:
            f_input = entrada_funcion.get()
            df_input = entrada_derivada.get()
            x0 = float(entrada_x0.get())

            func_expr = sympify(f_input)
            deriv_expr = sympify(df_input)

            raiz, mensaje = newton_raphson(func_expr, deriv_expr, x0)

            if raiz is not None:
                resultado.set(f"Raíz: {raiz:.6f}\n{mensaje}")
            else:
                resultado.set(f"Error: {mensaje}")

        except Exception as e:
            resultado.set(f"Entrada inválida: {e}")

    # Crear nueva ventana
    ventana = tk.Toplevel()
    ventana.title("Método de Newton-Raphson")
    ventana.geometry("400x350")

    # Widgets de entrada
    tk.Label(ventana, text="f(x):").pack()
    entrada_funcion = tk.Entry(ventana, width=40)
    entrada_funcion.pack()

    tk.Label(ventana, text="f'(x):").pack()
    entrada_derivada = tk.Entry(ventana, width=40)
    entrada_derivada.pack()

    tk.Label(ventana, text="Valor inicial x₀:").pack()
    entrada_x0 = tk.Entry(ventana, width=20)
    entrada_x0.pack()

    tk.Button(ventana, text="Calcular raíz", command=calcular_raiz).pack(pady=10)

    # Resultado
    resultado = tk.StringVar()
    label_resultado = tk.Label(ventana, textvariable=resultado, fg="blue", wraplength=350, justify="left")
    label_resultado.pack(pady=10)