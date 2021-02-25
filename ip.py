from num import basen, pad

"""
Класс для махинаций с IP
"""
class ip:
  def __init__(self, a : int, b : int, c : int, d : int):
    """
    Делаем IP из квадрантов
    """
    if not ip.isValid(a, b, c, d):
      raise AttributeError('{}.{}.{}.{} - это не IP'.format(a, b, c, d))

    self.__addr = (a, b, c, d)
  
  @staticmethod
  def fromString(text : str, sep='.', base=10):
    # @todo Для разных квадрантов разные СС
    """
    Получаем IP из строчки вида 1.2.3.4
    :param sep: Разделитель, например для "1 2 3 4" это пробел
    :param base: Система счисления, иногда бывает двоичная
    """
    a, b, c, d = map(lambda x : int(x, base), text.split(sep))
    return ip(a, b, c, d)
  
  @staticmethod
  def fromNumber(num : str, base=10):
    # @todo
    pass
  
  @staticmethod
  def isValid(a: int, b : int, c : int, d : int):
    """
    Проверяем, может ли это считаться правильным IP
    Broadcast и Net ID тоже правильные IP
    """
    return (0 <= a <= 255) and (0 <= b <= 255) and (0 <= c <= 255) and (0 <= d <= 255)

  def toString(self, sep='.', base=10):
    # @todo Для разных квадрантов разные СС
    """
    Преобразуем IP в строку
    """
    return sep.join(map(lambda x : basen(x, base), self.__addr))
  
  def toClassicString(self, sep='.', base=10):
    """
    Классическая запись Ip с нулями, например 255.015.088.000
    """
    if not base in (2, 10, 16):
      raise AttributeError('Классической формы для основания ' + str(base) + ' пока не придумали')

    zzz = (8 if base == 2 else 3 if base == 10 else 2)
    return sep.join(map(lambda x : pad(basen(x, base), zzz), self.__addr))
  