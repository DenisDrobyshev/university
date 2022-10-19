from math import pi

def deg_to_gms(deg):
    '''
    :param deg: Градусы в десятичном преставлении
    :return: Градусы, минуты, секунды по умолчанию в формате ГГ ММ СС
    '''
    grad = int(deg)
    minutes_ost = (deg - grad) * 60
    minutes = int(minutes_ost)
    second = (minutes_ost - minutes) * 60
    return f"{grad}° {minutes}` {second}"

def gms_to_deg(deg, minutes, seconds):
    '''
    :param deg: Десятичные градусы
    :param minutes: Минуты
    :param seconds: Секунды
    :return: Значение
    '''
    return int(deg) + (int(minutes) / 60) + (int(seconds) / 3600)

def deg_to_rad(deg):
    '''
    :param deg: Десятичные градусы
    :return: Перевод в радианы
    '''
    return (pi / 180) * deg

def rad_to_deg(rad):
    '''
    :param rad: Радианы
    :return: Перевод в градусы
    '''
    return (180 / pi) * rad

def main():

    print(deg_to_gms(39.97))
    print(gms_to_deg(39, 58, 12))
    print(deg_to_rad(39.97))
    print(rad_to_deg(deg_to_rad(39.97)))
    print(__name__)

if __name__ == "__main__":
    main()