from num import basen

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
  def fromSring(text : str, sep='.', base=10):
    """
    Получаем IP из строчки вида 1.2.3.4
    :param sep: Разделитель, например для "1 2 3 4" это пробел
    :param base: Система счисления, иногда бывает двоичная
    """
    a, b, c, d = map(lambda x : int(x, base), text.split(sep))
    return ip(a, b, c, d)
  
  @staticmethod
  def isValid(a: int, b : int, c : int, d : int):
    """
    Проверяем, может ли это считаться правильным IP
    Broadcast и Net ID тоже правильные IP
    """
    return (0 <= a <= 255) and (0 <= b <= 255) and (0 <= c <= 255) and (0 <= d <= 255)

  def toString(self, sep='.', base=10):
    """
    Преобразуем IP в строку
    """
    return sep.join(map(lambda x : basen(x, base), self.__addr))
  