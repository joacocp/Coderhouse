
def dividir(a:int ,b: int) -> float| None:
    if b!=0:
        return a/b

print(dividir(14,32))


def dividir2(a: int, b: int) -> float | str:
    try:
        return a / b
    except (ZeroDivisionError,TypeError) as Err:
        print(Err)
    finally:
        print("Fin de la ejecucion")

print(dividir2(14, 0))