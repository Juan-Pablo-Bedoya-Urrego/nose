#conexion Postgres
import psycopg2

# Definir los parámetros de conexión
conexion = {
    'user': 'postgres',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'PruebaConeccion'
}

id = 1
nombre = "Juan"

try:
    # Conectar a la base de datos
    conn = psycopg2.connect(**conexion)
    cursor = conn.cursor()

    # Preparar la sentencia SQL
    sql = "INSERT INTO Ejemplo VALUES (%s, %s)"

    # Ejecutar la sentencia SQL
    cursor.execute(sql, (id, nombre))

    # Confirmar la transacción
    conn.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    print("Guardado")
except Exception as e:
    print("Error: ", e)

