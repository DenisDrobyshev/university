def gms_to_deg(deg: int, minutes: int, seconds: int) -> float:
    '''
    :param deg: Десятичные градусы
    :param minutes: Минуты
    :param seconds: Секунды
    :return: Значение
    '''
    return int(deg) + (int(minutes) / 60) + (int(seconds) / 3600)
