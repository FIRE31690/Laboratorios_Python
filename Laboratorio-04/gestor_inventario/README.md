# Gestor de inventario persistente

Solución de la práctica integradora 4.5. Utiliza exclusivamente la biblioteca estándar de Python.

## Ejecutar

Desde esta carpeta:

```bash
python main.py
```

El JSON se guarda en `datos/productos.json`; el CSV se exporta a `reportes/inventario.csv`. Las rutas se resuelven con relación al módulo, no al directorio desde el que se invoca Python.

## Diseño

- `producto.py`: valida productos, actualiza existencias y serializa los cinco campos.
- `inventario.py`: mantiene productos por código y ofrece operaciones, consultas y resumen.
- `almacenamiento.py`: carga en una instancia temporal y escribe el JSON mediante reemplazo atómico.
- `reportes.py`: exporta columnas tabulares y calcula precio por cantidad.
- `main.py`: interacción de consola, conversiones y coordinación.

Si el JSON existente no se puede interpretar o contiene datos inválidos, la aplicación informa el error y termina sin sobrescribirlo. Las modificaciones aceptadas se guardan inmediatamente; también existe una opción de guardado manual.

## Pruebas

Desde esta carpeta:

```bash
python -m unittest discover -s tests -v
```

Se prueban validaciones, duplicados, protección del JSON dañado, recuperación, totales y CSV. Para probar manualmente, registra los productos del informe, cierra y reinicia la aplicación.