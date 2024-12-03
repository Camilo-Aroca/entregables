alumnos = ["Jose", "sofia", "Luis"]
for alumno in alumnos:
    print(f"Alumno: {alumno}")

agenda = {
    "Jose": "juan@example.com",
    "sofia": "ana@example.com"
}
for nombre, correo in agenda.items():
    print(f"Nombre: {nombre}, Correo: {correo}")

nuevo_alumno = input("Introduce el nombre de un nuevo alumno: ")
alumnos.append(nuevo_alumno)
print("Lista actualizada de alumnos:", alumnos)

nuevo_nombre = input("Introduce un nombre para actualizar/agregar: ")
nuevo_email = input("Introduce el correo de este contacto: ")
agenda[nuevo_nombre] = nuevo_email
print("Agenda actualizada:", agenda)
