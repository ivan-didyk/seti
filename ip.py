"""
Класс для махинаций с IP
"""
class ip:
  def __init__(self, a : int, b : int, c : int, d : int):
    """
    Делаем IP из квадрантов
    """
    self.__addr = (a, b, c, d)
  
  @staticmethod
  def fromSring(text : str):
    """
    Получаем IP из строчки вида 1.2.3.4
    """
    a, b, c, d = map(int, text.split('.'))
    return ip(a, b, c, d)
  