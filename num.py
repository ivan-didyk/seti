import string
__digs = string.digits + string.ascii_letters

def basen(x : int, base : int, upprcase=False):
  """
  Переводим `x` из десятичной в какую-то ещё
  :param upprcase: В каком регистры буквы - `C0FFE` или `c0ffe`
  """
  if base <= 0:
    raise AttributeError('Основание системы счисления должна быть больше нуля, а тут ' + str(base))
  if base > 36:
    raise AttributeError('Слишком большое основание системы счисления, максимум 36')

  if x == 0:
    return __digs[0]

  r = ''
  if x < 0:
    r += '-'
    x = -x
  
  arr = []
  while x:
    arr.append(__digs[x % base])
    x = x // base
  arr.reverse()
  r += ((''.join(arr).upper()) if upprcase else (''.join(arr).lower()))

  return r

def pad(x : int, width : int):
  """
  Дописать нули в начало строки до ширины `width`
  """
  return str(x).zfill(width)