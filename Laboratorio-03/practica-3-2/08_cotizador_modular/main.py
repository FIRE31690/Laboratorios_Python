import calculos
import validaciones


def leer_numero(mensaje, convertir, es_valido, error):
    """Repite la pregunta hasta recibir un dato convertible y válido."""
    while True:
        try:
            valor = convertir(input(mensaje))
        except ValueError:
            print("Debes escribir un número válido.")
            continue

        if es_valido(valor):
            return valor
        print(error)


def formatear(valor):
    return int(valor) if valor == int(valor) else valor


def main():
    precio = leer_numero("Precio: ", float, validaciones.precio_valido,
                         "El precio debe ser mayor que cero.")
    cantidad = leer_numero("Cantidad: ", int, validaciones.cantidad_valida,
                           "La cantidad debe ser mayor que cero.")
    p_descuento = leer_numero("Descuento (%): ", float, validaciones.porcentaje_valido,
                              "El porcentaje debe estar entre 0 y 100.")
    p_impuesto = leer_numero("Impuesto (%): ", float, validaciones.porcentaje_valido,
                             "El porcentaje debe estar entre 0 y 100.")

    subtotal = calculos.calcular_subtotal(precio, cantidad)
    descuento = calculos.calcular_descuento(subtotal, p_descuento)
    base = subtotal - descuento
    impuesto = calculos.calcular_impuesto(base, p_impuesto)
    total = base + impuesto

    print()
    print("Subtotal:", formatear(subtotal))
    print("Descuento:", formatear(descuento))
    print("Base después del descuento:", formatear(base))
    print("Impuesto:", formatear(impuesto))
    print("Total:", formatear(total))


if __name__ == "__main__":
    main()
