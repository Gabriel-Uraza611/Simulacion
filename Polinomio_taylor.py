import tkinter as tk
from tkinter import messagebox
from sympy import symbols, sympify, diff, factorial, simplify, lambdify


def ventana_taylor():
    x = symbols('x')

    def calcular_taylor():
        funcion_str = entrada_funcion.get()
        grado_str = entrada_grado.get()
        x0_str = entrada_x0.get()
        valor_str = entrada_valor.get()

        try:
            f = sympify(funcion_str)
            grado = int(grado_str)
            x0 = float(x0_str)

            # Calcular el polinomio de Taylor
            taylor = 0
            for n in range(grado + 1):
                derivada = diff(f, x, n)
                derivada_en_x0 = derivada.subs(x, x0)
                termino = (derivada_en_x0 * (x - x0)**n) / factorial(n)
                taylor += termino

            taylor_simplificado = simplify(taylor)

            resultado = f"Polinomio de Taylor:\n{taylor_simplificado}"

            # Si se ingresó un valor para evaluar
            if valor_str.strip():
                valor = float(valor_str)
                f_func = lambdify(x, f)
                taylor_func = lambdify(x, taylor_simplificado)

                valor_f = f_func(valor)
                valor_taylor = taylor_func(valor)
                error_absoluto = abs(valor_f - valor_taylor)

                resultado += (
                    f"\n\nf({valor}) = {valor_f:.6f}"
                    f"\nTaylor({valor}) = {valor_taylor:.6f}"
                    f"\nError absoluto = {error_absoluto:.6e}"
                )

            salida_resultado.config(text=resultado)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error")

    # Interfaz con tkinter
    ventana = tk.Tk()
    ventana.title("Polinomio de Taylor")
    ventana.geometry("420x400")
    ventana.configure(bg="#1e1e1e")

    tk.Label(ventana, text="Función f(x):", fg="white", bg="#1e1e1e").pack()
    entrada_funcion = tk.Entry(ventana, width=40)
    entrada_funcion.pack()

    tk.Label(ventana, text="Grado del polinomio:", fg="white", bg="#1e1e1e").pack()
    entrada_grado = tk.Entry(ventana, width=10)
    entrada_grado.pack()

    tk.Label(ventana, text="Punto x0:", fg="white", bg="#1e1e1e").pack()
    entrada_x0 = tk.Entry(ventana, width=10)
    entrada_x0.pack()

    tk.Label(ventana, text="Valor x a evaluar (opcional):", fg="white", bg="#1e1e1e").pack()
    entrada_valor = tk.Entry(ventana, width=10)
    entrada_valor.pack()

    tk.Button(ventana, text="Calcular Polinomio de Taylor", command=calcular_taylor, bg="#4CAF50", fg="white").pack(pady=10)

    salida_resultado = tk.Label(ventana, text="", fg="white", bg="#1e1e1e", wraplength=380, justify="center")
    salida_resultado.pack(pady=10)

    ventana.mainloop()
