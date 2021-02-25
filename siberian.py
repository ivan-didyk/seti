def __siberianSnake(arr, ln):
  """
  Змеим строку из таблицы
  """
  x = 0
  y = 0
  diag = False
  top = True
  strn = ''
  for i in range(ln):
    strn += arr[y][x]
    if y == 0 and not diag:
      x += 1
      diag = True
      top = False
    elif x == 0 and not diag:
      y += 1
      diag = True
      top = True
    else:
      diag = False
      if top:
        x += 1
        y -= 1
      else:
        y += 1
        x -= 1
  return strn


def __siberianArray(ln):
  """
  Получаем массив трасположения букв
  Например
  ```
  1 1 1
  1 1 0
  1 0 0
  ```
  """
  # Мне лень лезть в математику, так что массив чуть больше
  arr = [ [ False for i in range(ln//2) ] for i in range(ln//2) ]
  x = 0
  y = 0
  diag = False
  top = True
  strn = ''
  for i in range(ln):
    arr[y][x] = True
    if y == 0 and not diag:
      x += 1
      diag = True
      top = False
    elif x == 0 and not diag:
      y += 1
      diag = True
      top = True
    else:
      diag = False
      if top:
        x += 1
        y -= 1
      else:
        y += 1
        x -= 1
  
  # print('\n'.join(map(lambda x : ' '.join(map(lambda n : '{:3}'.format(n), x)), arr)))
  return arr

def __siberianHardBase(text):
  """
  Сибирский Хард, только без удаления пробелов
  """
  arr = __siberianArray(len(text))
  x = 0
  y = 0
  fin = [ '' for i in range(len(arr)) ]
  for i in text:
    fin[y] += i
    x += 1
    if not arr[y][x]:
      y += 1
      x = 0
  
  # print('\n'.join(fin))

  return __siberianSnake(fin, len(text))

def siberian(text):
  """
  Раскодируем сибирский
  Где вся инфа в интернете? Кошмар!
  Возвращает текст без пробелов... Ставьте их сами.
  """
  ln = len(text.replace(' ', ''))
  text = text.split(' ')
  return __siberianSnake(text, ln)

def siberianHard(text):
  """
  `СибирскийХард`
  """
  text = text.replace(' ', '')
  return __siberianHardBase(text)

def siberianHardPlus(text, chunklength=4):
  """
  `СибирскийХард+`, по сути то же самое
  `chunklength` обозначает длинну групп, в `Этиш тоол кс!с оомр п` оно `4`
  Обратно совместим с `siberianHard`, но лучше так не делать
  """
  # Считаем с пробелом
  chunks = [text[i:i+chunklength+1] for i in range(0, len(text), chunklength+1)]
  last = chunks[-1] # С последним не надо
  chunks = list(map(lambda x : x[:-1], chunks)) # Убираем пробелы
  chunks[-1] = last
  txt = ''.join(chunks)
  return __siberianHardBase(txt)



if __name__ == "__main__":
  siberians = [
    'Побу пое рм .. .',
    'Чтал оаг? зом рт и',
    'Чтумрир! оанпда зиоум ктмш эао лК ?',

    'Знлгабол ааороге яр,тог иманч ттме ьа н',
    'Глоетивы аннстк впуьу рпнб оой до н',
    'Умощчтелся еяу,отьтнм нщепапеае еирвради неаовнн пдсеаа отдмд озиа иэз тм и'
  ]

  for i in siberians:
    print(siberian(i))
  
  print('--------')

  hardSiberians = [
    'Этиш тоол кс!с оомр п',
    'Тоне ал!ж м,ми еепу уирд снил еонж',
    'Маза яоыэ нем, бнбб тепа ееро ишлр матм ьаит чалв !н,н оиио ьблг яииз кмоо ми',
  ]

  for i in hardSiberians:
    print(siberianHard(i))

  print('--------')

  extraSiberians = [
    'Крди муоо ле к  сг- во л !оав',
    'Гоь  сну  твше ов-о увйо  б , лву  о .а где  укхв о',
    # Последний пример я никак не могу списать
  ]

  for i in extraSiberians:
    print(siberianHardPlus(i))



# 0 0

# 1 0
# 0 1

# 2 0
# 1 1
# 0 2

# 3 0
# 2 1
# 1 2
# 0 3

# 4 0
# 3 1