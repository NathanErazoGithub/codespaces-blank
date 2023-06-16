print('¡Bienvenido a la clase de 1ºBACHILLER B!')
horario = {
    "Matematicas": ["Lunes 8h", "Jueves 8:55h", "Viernes 8h"],
    "Historia": ["Lunes 11,05h", "Miércoles 13:15h", "Jueves 8h"],
    "TIC": ["Lunes 12h", "Miercoles 11,05h", "Viernes 11,05h"],
    "Castellano": ["Martes 8h", "Miércoles 8,55h", "Viernes 13,15h"],
    "Catalan": ["Martes 13,15h", "Miércoles 8h", "Jueves 11,05h"],
    "Ed Fisica": ["Lunes 13,15h", "Miércoles 12h", "Jueves 12h"],
    "Filosofia": ["Martes 12h", "Jueves  14,10h", "Viernes 12h"],
    "Economia": ["Martes 11,05h", "Jueves 13,15h", "Viernes 10,10h"],
    "Religión": ["Martes 9h", "Jueves 10,10h"],
  "Ingles": ["Martes 10,10h", "Miércoles 10,10h", "Viernes 8,55h"],
  "Trabajo de Investigación": ["Lunes 9h","Lunes 10,10h"],  

}

asignatura = input("Introduce el nombre de la asignatura para obtener su horario, las asignaturas que puedes elegir son las siguientes: Matematicas, Economia, Tic, Historia, Trabajo de Investigacion, Religion, Ed.Fisica, Filosofia, Ingles, Castellano y Catalan :")

while asignatura not in horario:
    print("La asignatura no existe. Inténtalo de nuevo.")
    asignatura = input("Introduce una asignatura: ")

horarios = horario[asignatura]

print("Horarios de", asignatura + ":")

x = 0
while x < len(horarios):
    print(horarios[x])
    x += 1

print("¡Gracias por utilizar el programa de horario escolar!")