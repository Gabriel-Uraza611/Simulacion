import tkinter as tk
from tkinter import messagebox, ttk
from sympy import sympify, Symbol, lambdify


# === FUNCIÓN DE BISECCIÓN QUE RETORNA LOS DATOS ===
def metodo_biseccion_datos(f_str, a, b, tol=1e-5, max_iter=100):
    pasos = []
    try:
        x = Symbol('x')
        exp = sympify(f_str)
        f = lambdify(x, exp, modules=['numpy'])
    except Exception as e:
        return None, [f"Error al procesar la función: {e}"]

    if f(a) * f(b) >= 0:
        return None, ["La función no cambia de signo en el intervalo dado."]

    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        pasos.append((i + 1, a, b, c, fc))

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c, pasos

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return None, pasos


# === VENTANA BISECCIÓN ===
def ventana_biseccion():
    window = tk.Tk()
    window.title("Simulación Numérica - Bisección")
    window.geometry("700x600")
    window.configure(bg="white")

    # Campos de entrada
    tk.Label(window, text="Método de Bisección", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(window, text="Ingrese la función f(x):").pack()
    campo_fuc = tk.Entry(window, width=50)
    campo_fuc.pack(pady=5)

    tk.Label(window, text="Valor de a:").pack()
    campo_a = tk.Entry(window)
    campo_a.pack(pady=5)

    tk.Label(window, text="Valor de b:").pack()
    campo_b = tk.Entry(window)
    campo_b.pack(pady=5)

    tk.Label(window, text="Tolerancia:").pack()
    campo_tol = tk.Entry(window)
    campo_tol.pack(pady=5)

    tk.Label(window, text="Máximo de iteraciones:").pack()
    campo_iter = tk.Entry(window)
    campo_iter.pack(pady=5)

    # Tabla: se crea una sola vez
    tabla = ttk.Treeview(window, columns=("Iter", "a", "b", "c", "f(c)"), show="headings", height=15)
    for col in ("Iter", "a", "b", "c", "f(c)"):
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor='center')
    tabla.pack(pady=10)

    # Función de cálculo
    def calcular_raiz():
        try:
            f_str = campo_fuc.get()
            a = float(campo_a.get())
            b = float(campo_b.get())
            tol = float(campo_tol.get())
            max_iter = int(campo_iter.get())

            if a >= b:
                messagebox.showerror("Error", "'a' debe ser menor que 'b'")
                return
            if tol <= 0:
                messagebox.showerror("Error", "La tolerancia debe ser positiva.")
                return

            resultado, pasos = metodo_biseccion_datos(f_str, a, b, tol, max_iter)

            # Limpiar tabla antes de actualizar
            for row in tabla.get_children():
                tabla.delete(row)

            if resultado is not None:
                messagebox.showinfo("Resultado", f"La raíz aproximada es: {round(resultado, 6)}")
            else:
                messagebox.showwarning("Resultado", pasos[-1])  # mensaje de error

            # Insertar pasos en la tabla
            for paso in pasos:
                fila = [round(v, 6) if isinstance(v, float) else v for v in paso]
                tabla.insert("", "end", values=fila)

        except ValueError:
            messagebox.showerror("Error", "Verifica que los valores numéricos sean correctos.")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")

    # Botón para calcular
    tk.Button(window, text="Calcular método de bisección", command=calcular_raiz, bg="#4CAF50", fg="white").pack(pady=10)

    window.mainloop()
