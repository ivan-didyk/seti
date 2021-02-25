"""
Хемминг, он самый
"""
from math import ceil, log2

def encode(byteStr):
  """
  Закодировать хемминга
  Возвращает строку битов
  """
  strg = ''
  idx = 0
  got = 0
  while got < len(byteStr):
    if not (idx & (idx+1)):
      strg += '.'
    else:
      strg += byteStr[got]
      got += 1
    idx += 1
  
  mstr = list(strg)
  
  for i in range(len(strg)):
    if strg[i] == '.':
      arr = list(map(list, [strg[j:j+i+1] for j in range(i, len(strg), i*2+2)]))
      arr = sum(arr, [])
      mstr[i] = ('1' if arr.count('1') % 2 == 1 else '0')
  
  mstr = ''.join(mstr)
  return mstr;

def decode(byteStr):
  mstr = list(byteStr)
  ctrl = [2**i-1 for i in range(ceil(log2(len(byteStr))))]
  where = -1
  has = False

  for i in ctrl:
    arr = list(map(list, [byteStr[j:j+i+1] for j in range(i, len(byteStr), i*2+2)]))
    arr = sum(arr, [])
    sm = arr.count('1') % 2
    where += sm * (i + 1)
    has |= sm
  
  if has:
    mstr[where] = ('0' if mstr[where] == '1' else '1')
  
  res = ''
  for i in range(len(mstr)):
    if i in ctrl:
      ...
    else:
      res += mstr[i]
  
  return res



