# Newbee-API
https://api-newbee.herokuapp.com/
#### API implementation using Flask and SQLite with 3 main endpoints for student and subject managements as well as a directory for college departments

---
## Student endpoint
https://api-newbee.herokuapp.com/student
  ##### GET method
 On a GET method this endpoint returns a JSON with all the registered students
  ##### POST method
On a POST method the API will insert a student object to the database following the models describe at the end of this file

https://api-newbee.herokuapp.com/student/matricula
 ##### GET method
 On a GET method this endpoint will return a JSON with all the details of the student object that has the specified "matricula" number.
 ##### PUT method
 On a PUT method the endpoint will update the specified student that matches the given "matricula".
 ##### DELETE method
 On a DELETE method this endpoint will delete from the database the student with the specified "matricula" and return the information from the deleted object.
  
 ---
## Materia endpoint
  https://api-newbee.herokuapp.com/materia
  
  ##### GET method
 On a GET method this endpoint returns a JSON with all the registered materias following the models describe at the end of this file
  ##### POST method
On a POST method the API will insert a materia object to the database following the models describe at the end of this file

https://api-newbee.herokuapp.com/materia/codigo
 ##### GET method
 On a GET method this endpoint will return a JSON with all the details of the materia object that has the specified "codigo".
 ##### PUT method
 On a PUT method the endpoint will update the specified materia that matches the given "codigo".
 ##### DELETE method
 On a DELETE method this endpoint will delete from the database the materia with the specified "codigo" and return the information from the deleted object.
 
   
 ---
## Directorio endpoint
  https://api-newbee.herokuapp.com/directorio
  
  ##### GET method
 On a GET method this endpoint returns a JSON with all the registered directorios following the models describe at the end of this file
  ##### POST method
On a POST method the API will insert a directorio object to the database following the models describe at the end of this file

https://api-newbee.herokuapp.com/directorio/area
 ##### GET method
 On a GET method this endpoint will return a JSON with all the directorios that have the specified "area".
 
 https://api-newbee.herokuapp.com/directorio/departamento
https://api-newbee.herokuapp.com/materia/codigo
 ##### GET method
 On a GET method this endpoint will return a JSON with all the details of the directorio with the specified "departamento"
 ##### PUT method
 On a PUT method the endpoint will update the specified directorio that matches the given "departamento".
 ##### DELETE method
 On a DELETE method this endpoint will delete from the database the directorio with the specified "departamento" and return the information from the deleted object.
 
 ---
# Models

### Student model

string **matricula**  MaxLength(7)
string **nombres** MaxLength(30)
string **apellidos** MaxLength(30)
string **password** MaxLength(50)
string **email** MaxLength(50)
bool  **active** --> True if student is active, otherwise false

### Materia model

string **nombre**  MaxLength(50)
string **codigo**  MaxLength(6)
int **seccion**
string **aula**  MaxLength(10)
string **horarioDias**  MaxLength(30)
string **horarioHoras**  MaxLength(30)
string **profesor**  MaxLength(50)

### Directorio model

string **area**  MaxLength(50)
string **departamento**  MaxLength(50)
string **encargado**  MaxLength(50)
string **telefono**  MaxLength(10)
string **edificio**  MaxLength(50)
string **descripcion**  MaxLength(100)

