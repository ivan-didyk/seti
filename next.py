
class take:
  def __init__(self, value):
    self.value = value
  
  def then(self, fn, *args, **kvargs):
    return take(fn(self.value, *args, **kvargs))
  
  def do(self, fn, *args, **kvargs):
    fn(self.value, *args, **kvargs)
    return self
  
  def doEach(self, fn, *args, **kvargs):
    for i in self.value:
      fn(self.value, *args, **kvargs)
    return self
  
  def each(self, fn, *args, **kvargs):
    res = []
    for i in self.value:
      res.append(fn(i, *args, **kvargs))
    return take(res)