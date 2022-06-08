import notas.nota as modelo


class Acciones:
    def crear(self, usuario):
        print(f"OK{usuario[1]} !! Vamos a crear una nota")
        
        titulo = input("introduce titulo de la nota: ")
        descripcion = input("introduce la descripcion: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >= 1:
            print(f"\n Perfecto! has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se guardo tu nota: {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\n{usuario[1]}!! Estas son tus notas: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        #print(notas)
        for nota in notas:
            print("\n ***********")
            print(nota[2])
            print(nota[3])
            print("\n***********")

    def borrar(self, usuario):
        print(f"\n {usuario[1]} borrar tus notas")

        titulo = input("introduce el titulo de tu nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"se borrara la nota {nota.titulo}")
        else:
            print("no se elimino")
