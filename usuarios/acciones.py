import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("Ser realizara tu registro en el sistema...")

        nombre = input("¿Cual es tu nombre? ")
        apellidos = input("¿Cuales son tus apellidos? ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre}, te haz registrado con el email {registro[1].email}")
        else:
            print("\nNo te haz registrado correctamnete !!!")


    def login(self):
        print("Identificate en el sistema")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado {login[5]} en el sistema")
                self.proximasAcciones(login)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print("\n Login incorrecto intentalo mas tarde ")
        
    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles

            -crear nota (nota)
            -Mostrar nota (mostrar)
            -eliminar nota (eliminar)
            -salir (salir)
        """)
        
        accion = input("¿Que quieres hacer? ")
        hasEl = notas.acciones.Acciones()

        if accion == "crear":
            #print("vamos a crear nota")
            hasEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            #print("vamos a mostrar")
            hasEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            #print("vamos a eliminar")
            hasEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            exit()    
