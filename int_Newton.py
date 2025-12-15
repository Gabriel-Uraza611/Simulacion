from tkinter import messagebox
import tkinter as tk

def diferencias_divididas(x, y):
    n = len(x)
    coef = list(y)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

def evaluar_newton(x, coef, valor):
    n = len(coef)
    resultado = coef[-1]
    for i in range(n - 2, -1, -1):
        resultado = resultado * (valor - x[i]) + coef[i]
    return resultado

def ventana_interpolacion():
    top = tk.Toplevel()
    top.title("Interpolación de Newton")
    top.geometry("500x350")

    tk.Label(top, text="Valores de x (separados por comas):").pack()
    entrada_x = tk.Entry(top)
    entrada_x.pack(pady=5)

    tk.Label(top, text="Valores de y (separados por comas):").pack()
    entrada_y = tk.Entry(top)
    entrada_y.pack(pady=5)

    tk.Label(top, text="Valor de x a interpolar:").pack()
    entrada_valor = tk.Entry(top)
    entrada_valor.pack(pady=5)

    def calcular_interpolacion():
        try:
            x = list(map(float, entrada_x.get().split(",")))
            y = list(map(float, entrada_y.get().split(",")))
            valor = float(entrada_valor.get())

            if len(x) != len(y):
                messagebox.showerror("Error", "Las listas de x e y deben tener la misma longitud.")
                return

            coef = diferencias_divididas(x, y)
            resultado = evaluar_newton(x, coef, valor)
            messagebox.showinfo("Resultado", f"f({valor}) ≈ {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Verifica que los valores estén bien escritos y separados por comas.")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")

    tk.Button(top, text="Calcular", command=calcular_interpolacion).pack(pady=15)
