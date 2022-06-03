#DDI CLASS
print("Irving Hernández Carlos-9°A-DDI-03/06")

""" proyecto python mas mysql
1. Abrir el asistente
2. loggin y registro
3. si elegimos registro agregra un ususario
4. si elegimos iniciar sesion identificara al usuario y preguntara
5. crear notas mostrar y editar
 """
#para importar de otra lases
from usuarios import acciones
#import usuarios.acciones

print("""
Acciones disponibles:
    -registro
    -login
""")

hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer? ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
