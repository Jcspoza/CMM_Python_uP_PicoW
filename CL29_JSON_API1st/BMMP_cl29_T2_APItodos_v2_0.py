# Taller Programación y Robótica en CMM BML – 2023 - Clase 29
# Resumen: Usar los API´s que normlmente vienen como JSON - Ejemplo de consulta de API´s todos
# Topicos nuevos: libreria json
# Ref Tutorial JSON completo : https://realpython.com/python-json/#deserializing-json
# Fecha inicio 2024 03 11
# Licencia : CC BY-NC-SA 4.0
# Version 2.0 more comments & names more clear

# IMPORTAR modulo que maneja JSON
import json
import requests

# Informative block - start
p_topic = "Working with JSON"
p_project = "A Real World Example (sort of)"
p_ref = "https://realpython.com/python-json/"
p_version = "2.0"
p_keyLib = "json"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 1- Consultar una API de ejemplos aplicacion de tareas y extraer una lista de todos
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# 2 - Ver aspecto de los datos con los 3 primeros de ellos, si se ha volcado como  lista
if type(todos) is list:
    print(f'Los datos JSON se han volcado como una lista de {len(todos)} elementos')
    print(f'Cada elemento de la lista es un {type(todos[0])} con las claves {todos[0].keys()}')
    print('Se muestran los 3 primeros')
    todos3_JSON = json.dumps(todos[:3], indent=4)
    print(todos3_JSON)
    
# 3- Extraemos la info de todos los 'todos' para determinar los usuarios con el maximo numero de tareas completadas
# 3.1 Map of userId to number of complete TODOs for that user
Done_todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            Done_todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            Done_todos_by_user[todo["userId"]] = 1
      
print("Done 'todo's by user")
print(Done_todos_by_user)

# # 3.2 Create a sorted list of (userId, num_complete) dictionary pairs.
# Ordered_users = sorted(Done_todos_by_user.items(), 
#                    key=lambda x: x[1], reverse=True)
# 
# # 3.3 Get the maximum number of complete TODOs.
# max_complete = Ordered_users[0][1]
# 
# # 3.4 Create a list of all users who have completed
# # the maximum number of TODOs y lo muestra
# users = []
# for user, num_complete in Ordered_users: # recorre la lista y asigna cada elemento de la tupla
#     # (usuario, num completados) en orden a user y num_complete
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# 
# max_users = " and ".join(users)
# s = "s" if len(users) > 1 else ""
# print(f"user{s} {max_users} completed {max_complete} TODOs")
# 
# # 3.5 Define a function to filter out completed TODOs 
# # of users with max completed TODOS.
# def keep(todo):
#     is_complete = todo["completed"]
#     has_max_count = str(todo["userId"]) in users
#     return is_complete and has_max_count
# 
# # 3.6 Write filtered TODOs to file.
# with open("filtered_data_file.json", "w") as data_file:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, data_file, indent=2)
#     
# # 4- Abrimos el fichero resultado sin tocaer nada 
# with open("filtered_data_file.json") as f:
#     datosResult = f.read()
#     
# print('==== Fichero Resultado ====')
# print(datosResult)
