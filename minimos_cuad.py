import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt


def ventana_ajuste():
    def agregar_punto():
        def guardar():
            try:
                x = float(x_entry.get())
                y = float(y_entry.get())
                tree.insert('', 'end', values=(x, y))
                top.destroy()
            except ValueError:
                messagebox.showerror("Error", "Coordenadas inválidas")

        top = tk.Toplevel(root)
        top.title("Nuevo punto")

        tk.Label(top, text="X:").grid(row=0, column=0)
        x_entry = tk.Entry(top)
        x_entry.grid(row=0, column=1)

        tk.Label(top, text="Y:").grid(row=1, column=0)
        y_entry = tk.Entry(top)
        y_entry.grid(row=1, column=1)

        tk.Button(top, text="Guardar", command=guardar).grid(row=2, column=0, columnspan=2, pady=5)

    def eliminar_punto():
        for item in tree.selection():
            tree.delete(item)

    def mostrar_resultado(tabla_texto, graficar_func, titulo):
        ventana = tk.Toplevel(root)
        ventana.title(titulo)

        text = tk.Text(ventana, width=80, height=30)
        text.pack(padx=10, pady=10)
        text.insert(tk.END, tabla_texto)

        graficar_func()

    def calcular_ajuste():
        items = tree.get_children()
        if len(items) < 2:
            messagebox.showerror("Error", "Se necesitan al menos 2 puntos.")
            return

        x_vals, y_vals = [], []
        for item in items:
            x, y = tree.item(item)['values']
            x_vals.append(float(x))
            y_vals.append(float(y))

        ajuste_lineal(x_vals, y_vals)

    def ajuste_lineal(x, y):
        x = np.array(x)
        y = np.array(y)
        n = len(x)

        x2 = x**2
        xy = x * y

        Sx = np.sum(x)
        Sy = np.sum(y)
        Sx2 = np.sum(x2)
        Sxy = np.sum(xy)

        A = np.array([[n, Sx], [Sx, Sx2]])
        B = np.array([Sy, Sxy])
        a0, a1 = np.linalg.solve(A, B)

        tabla = "TABLA:\n"
        tabla += f"{'x':>5} {'y':>8} {'x²':>8} {'xy':>10}\n"
        for xi, yi, x2i, xyi in zip(x, y, x2, xy):
            tabla += f"{xi:>5.2f} {yi:>8.2f} {x2i:>8.2f} {xyi:>10.2f}\n"

        tabla += "\nSUMATORIAS:\n"
        tabla += f"Σx = {Sx:.4f}\nΣy = {Sy:.4f}\nΣx² = {Sx2:.4f}\nΣxy = {Sxy:.4f}\n"

        tabla += "\nSISTEMA NORMAL:\n"
        tabla += f"{n}·a0 + {Sx:.4f}·a1 = {Sy:.4f}\n"
        tabla += f"{Sx:.4f}·a0 + {Sx2:.4f}·a1 = {Sxy:.4f}\n"

        tabla += f"\nSOLUCIÓN:\na0 = {a0:.4f}\na1 = {a1:.4f}\n"
        tabla += f"Modelo ajustado: y = {a0:.4f} + {a1:.4f}·x\n"

        def graficar():
            y_pred = a0 + a1 * x
            plt.scatter(x, y, label="Datos")
            plt.plot(x, y_pred, color='red', label='Ajuste')
            plt.title(f"Ajuste Lineal: y = {a0:.4f} + {a1:.4f}x")
            plt.grid()
            plt.legend()
            plt.show()

        mostrar_resultado(tabla, graficar, "Ajuste Lineal")

    # Crear interfaz principal
    root = tk.Tk()
    root.title("Ajuste Lineal por Mínimos Cuadrados - Método Manual")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    tree = ttk.Treeview(frame, columns=("x", "y"), show='headings', height=6)
    tree.heading("x", text="X")
    tree.heading("y", text="Y")
    tree.pack()

    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    tk.Button(btn_frame, text="Agregar punto", command=agregar_punto).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Eliminar punto", command=eliminar_punto).grid(row=0, column=1, padx=5)

    tk.Button(root, text="Calcular ajuste lineal", command=calcular_ajuste).pack(pady=10)

    # Ejecutar la app
    root.mainloop()
