# Depuración — errores provocados (sección 20)

Se provocaron sobre una copia del proyecto y se corrigieron uno por uno.

| # | Error provocado | Qué ocurre | Causa | Corrección |
|---|---|---|---|---|
| 1 | `_productos = []` en el cuerpo de la clase | No hay excepción: los inventarios se mezclan (el segundo "ve" lo que se registró en el primero). | Una lista mutable a nivel de clase es compartida por todas las instancias. | Crear `self._productos = []` dentro de `__init__`. |
| 2 | Consultar `producto.descuento` | `AttributeError: 'Producto' object has no attribute 'descuento'` | La propiedad o atributo no existe. | Usar un nombre existente (`precio`, `cantidad`, ...). |
| 3 | `def calcular_valor():` sin `self` | `TypeError: Producto.calcular_valor() takes 0 positional arguments but 1 was given` | Python pasa el objeto como primer argumento en los métodos de instancia. | Declarar `def calcular_valor(self):`. |
| 4 | Quitar la validación de cantidad en `__init__` | Se crea un producto con cantidad negativa sin error. | Las reglas deben aplicarse al crear el objeto, no solo al actualizarlo. | Validar con `_validar_cantidad()` en el constructor. |
| 5 | Borrar `from producto import Producto` en `inventario.py` | `NameError: name 'Producto' is not defined` | El nombre no está disponible en ese módulo. | Restaurar la importación. |
| 6 | Valor del inventario = suma de precios | Con los datos de prueba da 830000 en lugar de 1740000. | Se ignoran las cantidades. | `sum(p.calcular_valor() for p in self._productos)`. |
