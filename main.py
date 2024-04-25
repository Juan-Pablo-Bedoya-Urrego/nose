#coneccion con SQLserver
import pyodbc

# Definir los parámetros de conexión
usuario = "Juan"
password = "123"
bd = "Pruebas_BD"
ip = "localhost"
puerto = "1433"

# Construir la cadena de conexión
cadena_conexion = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={ip},{puerto};"
    f"DATABASE={bd};"
    f"UID={usuario};"
    f"PWD={password};"
)

codigo = 1
marca = "Nose me lo invento"
nombre = "menos que se"
descrip = "la buena"
categoria = "Chupe"
ubicacion = "alla"
cantidad = 10 
precio = 1.000

try:
    conn = pyodbc.connect(cadena_conexion)
    cursor = conn.cursor()

    sql = "INSERT INTO Productos VALUES (?,?,?,?,?,?,?,?)"

    cursor.execute(sql,(codigo,marca,nombre,descrip,categoria,ubicacion,cantidad,precio))

    conn.commit()

    cursor.close()
    conn.close()

    print("Guardado")
except Exception as e:
    print("Error: ", e)
