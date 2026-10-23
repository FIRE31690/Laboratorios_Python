# Gestor de inventario (orientado a objetos)

Aplicación de consola que registra, lista, busca, actualiza y elimina
productos, y genera informes del inventario. Es la versión con clases del
gestor del Laboratorio 2 (que usaba diccionarios).

## Estructura

```text
gestor_inventario/
├── main.py                    # menú e interacción con el usuario
├── producto.py                # clase Producto
├── inventario.py              # clase Inventario
├── pruebas_independencia.py   # dos inventarios no comparten datos
├── pruebas_inventario.py      # pruebas obligatorias y comprobación numérica
├── depuracion.md              # errores provocados y su corrección
└── README.md
```

## Ejecución

```bash
python main.py                     # (o py main.py / python3 main.py)
python pruebas_inventario.py       # pruebas automáticas
python pruebas_independencia.py
```

No requiere instalar paquetes externos.

## Responsabilidad de cada clase

| Archivo | Responsabilidad |
|---|---|
| `producto.py` | `Producto`: guarda código, nombre, categoría, precio y cantidad; valida desde `__init__` (textos no vacíos, categoría autorizada, precio > 0, cantidad ≥ 0); expone propiedades de solo lectura (el código no se puede reasignar); `actualizar_existencias()` y `calcular_valor()`. |
| `inventario.py` | `Inventario`: conserva una lista propia de objetos `Producto`; registra (sin códigos duplicados), lista (devuelve una copia), busca, actualiza, elimina, consulta productos sin stock (comprensión de lista) y genera el resumen (comprensión de conjunto). |
| `main.py` | Único lugar con `input()` y `print()` de interacción: menú, lectura con reintentos, captura de `ValueError` y mensajes. |

### Respuestas a las preguntas previas

- Evita códigos repetidos: `Inventario`.
- Comprueba que la cantidad sea válida: `Producto`.
- Calcula el valor de un producto: `Producto`.
- `input()` se usa solo en `main.py`.
- Quien decide el mensaje mostrado tras una operación: `main.py`.

## Pruebas realizadas

| Caso | Resultado observado |
|---|---|
| Inventario vacío | Listado vacío y resumen en cero |
| Registrar P001 | Aceptado |
| Registrar P001 de nuevo | Rechazado |
| Código o nombre vacío (o solo espacios) | Rechazado (`ValueError` capturado en `main.py`) |
| Categoría no permitida | Rechazado |
| Precio cero o negativo | Rechazado por `Producto`; en el menú se vuelve a pedir el dato |
| Cantidad negativa | Rechazada; en el menú se vuelve a pedir el dato |
| Cantidad cero | Producto válido y sin existencias |
| Buscar P001 / P999 | Muestra el producto / informa que no existe |
| Actualizar a 10 | Cambia solo la cantidad |
| Actualizar a -3 | Rechazado, se conserva el dato anterior |
| Eliminar existente / inexistente | Elimina / informa sin fallar |
| Texto en campo numérico | Mensaje y nueva oportunidad |
| Resumen | 3 productos, 6 unidades, $1740000.0, 2 categorías, sin stock: Mouse |
| Tras actualizar P002 a 5 | 11 unidades, $1965000.0 |
| Dos inventarios | Primero: 1, Segundo: 0 |
| Salir (`0`) | Termina el ciclo |
