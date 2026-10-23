# Respuestas de las secciones "Comprobación"

## Práctica 3.1
- **`print()` vs `return`:** `print()` muestra algo en pantalla (efecto visible) pero la función devuelve `None`; `return` entrega un valor al programa para guardarlo o usarlo después.
- **Parámetro vs argumento:** el parámetro es el nombre en la definición (`def saludar(nombre)`); el argumento es el valor concreto de la llamada (`saludar("Laura")`).
- **Modificar la lista recibida vs devolver una nueva:** la lista recibida es el mismo objeto que tiene quien llama, así que `append()` la cambia (efecto colateral). Si se hace `copia = lista.copy()` y se devuelve la copia, el original no cambia.

## Práctica 3.2
- **Qué archivo se ejecuta:** el que se pasa a `python` (normalmente `main.py`); los demás solo se ejecutan si se importan.
- **Importar:** Python ejecuta el módulo una vez y deja disponibles sus nombres.
- **`import modulo` vs `from modulo import funcion`:** el primero mantiene claro el origen (`modulo.funcion()`) y evita choques de nombres; el segundo permite llamar `funcion()` directamente, útil con pocas funciones.
- **`if __name__ == "__main__"`:** ejecuta código solo cuando el archivo se corre directamente, no cuando se importa.

## Práctica 3.3
- **`self`:** el objeto concreto que ejecuta el método; con él se accede a sus atributos.
- **`__init__`:** inicializa los atributos de un objeto recién creado.
- **`self.elementos = []`:** crea una lista distinta por objeto; una lista a nivel de clase es una sola, compartida por todas las instancias.

## Práctica 3.4
- **`Inventario` conserva objetos:** cada elemento es un `Producto` con sus datos y su comportamiento, no un diccionario suelto; el inventario administra la colección.
- **`_productos` es interno:** el guion bajo indica por convención que no debe tocarse desde fuera; se accede mediante métodos.
- **Asignación libre vs método con reglas:** `obj.cantidad = -5` se acepta sin revisar; `actualizar_existencias(-5)` comprueba la regla y rechaza el cambio.
