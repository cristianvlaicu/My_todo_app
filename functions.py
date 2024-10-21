        # Creamos funciones para eliminar código repetitivo y que el Código General quede más ordenado.


FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):    #creamos función para abrir el archivo todos y extraerlo (es lo que devuelve en el return)  en forma de lista.
    """Read a text file and Return the list os
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local  # devuelve un instncia en formato lista.


def write_todos(todos_arg, filepath=FILEPATH):   # esta función es un procedimiento con dos parámetros locales y no devuelve nada, ya que se trata de sobreescribir una información sobre la otra anterior.
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':  # Esto se usa cuando no queremos que lo hay debajo se ejecute/vea desde el archivo "main" en este caso.
                            # Pero si lo ejecutamos el archivo "functions" (sería el archivo principal para "__name__") sí se vería/ejecutaría lo que hay debajo.
                            # Es muy útil cuando queremos hacer pruebas de funciones y dejarlas anotadas en el archivo aparte de "functions" en este caso.
    print("Hello, you can see this because it is executed in __name__ = '__main__' (functions)!.")
    print(get_todos())