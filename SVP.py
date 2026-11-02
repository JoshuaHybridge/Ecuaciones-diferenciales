#Selecciona una ecuación diferencial separable, resuélvela analíticamente 
# usando el método de separación de variables para obtener la solución 
# exacta. Luego, aplica el método de Euler para aproximar la solución en
# el intervalo t ∈ [0,1] y con un paso de h = 0.2
import sympy as sp
import numpy as np
import pandas as pd

#1.-Separación de variables
x, y = sp.symbols('x y')
C = sp.symbols('C')

# dy/dx = 2*x*y^2
print("Ecuació diferencial:")
sp.pprint(sp.Eq(sp.Symbol('dy/dx'), 2*x*y**2))


# Separar variables
# dy/y^2 = 2*x dx

print("\nSeparación de variables:")
print("dy/y^2 = 2*x dx")

#Imtegrar ambos lados

integral_izquierda = sp.integrate(y**(-2), y)
integral_derecha = sp.integrate(2*x, x)

#print("\nIntegrar:")
#print("Lado izquierdo:")
sp.pprint(integral_izquierda)

#print("Lado derecho:")
sp.pprint(integral_derecha)

#Igualar integrales

solucion_implicita = sp.Eq(
    integral_izquierda,
    integral_derecha + C
)

print("\nSolución implicita (Separación de variables):")
sp.pprint(solucion_implicita)

#Despejar y

solucion = sp.solve(solucion_implicita, y)

print("\nSolución exacta (Separación de variables):")
for s in solucion:
    sp.pprint(s)

#Solución constante

#print("\nSolución constante:")
#print("y(x) = 0")

# Solucion exacta particular
# (Python calcula valor exacto hay que evitar errores como t entre 0)

# No hay solución definida en t=1 por eso se añade el siguiente segmento
# y(t) = 1/(1-t^2)

def solucion_exacta(t):
    if t == 1:
        return np.nan
    return 1 / (1 - t**2)

#2.-Método de Euler

def f(t, y):
    return 2*t*y**2

t0 = 0
tf = 1
h = 0.2
y0 = 1

# puntos de intervalo
t = np.arange(t0, tf + h/2, h)

# Arreglo para aproximaciones
y_euler = np.zeros(len(t))

y_euler[0] = y0

# Método de Euler
for i in range(len(t)-1):
    y_euler[i+1] = (
        y_euler[i] + h*f(t[i], y_euler[i])
    )

# Comparación de euler con solución exacta el margen de error de ambas

exacta = np.array([
    solucion_exacta(valor) for valor in t
])

error = np.abs(exacta - y_euler)

#Tabla de resultados

tabla = pd.DataFrame({
    't': t,
    'Euler': y_euler,
    'Solucion exacta': exacta,
    'Error absoluto': error
})

print("\nResultados de Euler:")
print(tabla.to_string(index=False))
print("\nAproximación final de euler:")
print("y(1) =", y_euler[-1])

