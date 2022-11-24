def deg_to_gms(deg: int) -> str:
    '''
    :param deg: Градусы в десятичном преставлении
    :return: Градусы, минуты, секунды по умолчанию в формате ГГ ММ СС
    '''
    grad = int(deg)
    minutes_ost = (deg - grad) * 60
    minutes = int(minutes_ost)
    second = (minutes_ost - minutes) * 60
    return f'{grad}° {minutes}` {round(second, 5)}"'
