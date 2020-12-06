def str_calculate(a, b, operacja):
    if operacja == 'concat':
        return a + b

    if operacja == 'end':
        return a.endswith(b)

    if operacja  == 'contain':
        czy_zawiera = a.find(b)
        if czy_zawiera >= 0:
            return True
        return False

    if operacja == 'start':
        return a.startswith(b)
