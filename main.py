import sys

def clean_value(value):
    ##Quitar espacios y solo permitir los digitos correctos
    value = value.strip()
    valid_chars= '.-0123456789'
    result=''
    ##Recorremos la cadena y si el digito es correcto lo guardamos
    for char in value:
        if char in valid_chars:
            result +=char
    return result


def convert_int (texto):
    ##Si esta vacio entonces devuelve 0
    if texto == "":
        return 0
    ##Se intenta convertir el texto a un numero y si no se puede entonces se devuelve 0
    try:
        number=float(texto)
        return int(number)
    except ValueError:
        return 0