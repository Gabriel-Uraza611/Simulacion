import tkinter as tk
from tkinter import messagebox
from m_biseccion import ventana_biseccion
from int_Newton import ventana_interpolacion
from Polinomio_taylor import ventana_taylor
from m_newton_raphson import ventana_raphson
from int_lagrange import ventana_lagrange
from minimos_cuad import ventana_ajuste



# Interfaz gráfica
window = tk.Tk()
window.title("Simulación Numérica ")
window.geometry("300x300")
window.configure(bg="skyblue")

tk.Label(window, text="¿Qué quieres calcular hoy?", fg="black", bg="#f0e9e9", font=("Arial", 14, "bold")).pack()
tk.Button(window, text="Polinomio de taylor", command=ventana_taylor, bg="#F3213A", fg="white").pack(pady=10)
tk.Button(window, text="Método de bisección", command=ventana_biseccion, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(window, text="Interpolación de Newton", command=ventana_interpolacion, bg="#2196F3", fg="white").pack(pady=10)
tk.Button(window, text="Metodo Newton Raphson", command=ventana_raphson, bg="#0051FF", fg="white").pack(pady=10)
tk.Button(window, text="Ajuste de curvas", command=ventana_ajuste, bg="#A31A68", fg="white").pack(pady=10)





window.mainloop()
