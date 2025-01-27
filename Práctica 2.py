class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre  
        self.horarios = []

    def agregar_horario(self, hora):
        self.horarios.append(hora)

class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = []
        self.conductores_asignados = []

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        self.horarios.append(horario)

    def asignar_conductor(self, conductor, horario):
        if horario not in conductor.horarios:
           conductor.agregar_horario(horario)
           self.conductores_asignados.append((conductor, horario))
        else:
            print("El conductor ya tiene asignado un bus en ese horario")

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, id_bus):
        bus = Bus(id_bus)
        self.buses.append(bus)

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)

    def asignar_bus_conductor(self, id_bus, nombre_conductor, horario):
        bus = self.buscar_bus(id_bus)
        conductor = self.buscar_conductor(nombre_conductor)
        if bus and conductor:
            bus.asignar_conductor(conductor, horario)
        else:
            if not bus:
                print(f"No se encontró un bus con ID {id_bus}.")
            if not conductor:
                print(f"No se encontró un conductor con nombre {nombre_conductor}.")

    def buscar_bus(self, id_bus):
        for bus in self.buses:
            if bus.id_bus == id_bus:
                return bus
        return None

    def buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        return None

    def menu(self):
        while True:
            print("\nMenú")
            print("1. Agregar bus")
            print("2. Agregar ruta a un bus")
            print("3. Registrar horario a un bus")
            print("4. Agregar conductor")
            print("5. Asignar bus a conductor")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_bus = input("Ingrese el ID del bus: ")
                if id_bus:
                    self.agregar_bus(id_bus)
                else:
                    print("El ID del bus no puede estar vacío.")

            elif opcion == "2":
                id_bus = input("Ingrese el ID del bus: ")
                if id_bus:
                    bus = self.buscar_bus(id_bus)
                    if bus:
                        ruta = input("Ingrese la ruta del bus: ")
                        bus.agregar_ruta(ruta)
                    else:
                        print("No se encontró un bus con ese ID.")
                else:
                    print("El ID del bus no puede estar vacío.")

            elif opcion == "3":
                id_bus = input("Ingrese el ID del bus: ")
                horario = input("Ingrese el horario del bus: ")
                if id_bus and horario:
                    bus = self.buscar_bus(id_bus)
                    if bus:
                        bus.registrar_horario(horario)
                    else:
                        print("No se encontró un bus con ese ID.")
                else:
                    print("El ID del bus y el horario no pueden estar vacíos.")

            elif opcion == "4":
                nombre_conductor = input("Ingrese el nombre del conductor: ")
                if nombre_conductor:
                    self.agregar_conductor(nombre_conductor)
                else:
                    print("El nombre del conductor no puede estar vacío.")

            elif opcion == "5":
                id_bus = input("Ingrese el ID del bus: ")
                nombre_conductor = input("Ingrese el nombre del conductor: ")
                horario = input("Ingrese el horario: ")
                if id_bus.nombre_conductor and horario:
                    self.asignar_bus_conductor(id_bus, nombre_conductor, horario)
                else:
                    print("El ID del bus, el nombre del conductor y el horario no pueden estar vacíos.")
            elif opcion == "6":
                break

            else:
                print("Opción inválida, por favor intente otra vez")

if __name__ == "__main__":
    admin = Admin()
    admin.menu()
