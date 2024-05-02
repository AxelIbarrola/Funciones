def obtener_mejor_alumno(**alumnos):
    
    mayor_nota = 0
    mejores_alumnos = []
    
    for nota in alumnos.values():
        if nota >= mayor_nota:
            mayor_nota = nota
    
    for nombre, nota in alumnos.items():
        if nota == mayor_nota:
            mejores_alumnos.append(nombre.capitalize())
            
    
    if len(mejores_alumnos) == 1:
        print("El alumno con mejor nota es:")
        print(mejores_alumnos[0])
    else:
        print("Los alumnos con mejores notas son:")
        for alumno in mejores_alumnos:
            print(alumno, end= " | ")


obtener_mejor_alumno(axel = 4, angel = 10, jeremias = 9, ivan = 10, luis = 10, jorge = 7, tobias = 6, nico = 6, david = 4)