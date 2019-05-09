class Employee:
  def __init__(self, name, workDays):
    self.name = name
    self.workDays = workDays
    self.__payment = 0

  def addPayment(self, value):
    self.__payment += value

  def getFullPayment(self):
    return str(self.__payment)

class WorkDay:
  def __init__(self, id, start, end):
    self.id = id
    self.start = start
    if end == 0:
      self.end = 24
    else:
      self.end = end

  def getHours(self):
    return self.end - self.start

class Schedule:
  def __init__(self, ids, ranges):
    self.ids = ids
    self.ranges = ranges

class PaymentRange:
  def __init__(self, value, start, end):
    self.value = value
    self.start = start
    self.end = end