# coding: utf-8

from models import *

SCHEDULE = [
  Schedule(
    ['MO', 'TU', 'WE', 'TH', 'FR'],
    [
      PaymentRange( 25, 0, 9 ),
      PaymentRange( 15, 9, 18 ),
      PaymentRange( 20, 18, 24 )
    ]
  ),
  Schedule(
    ['SA', 'SU'],
    [
      PaymentRange( 30, 0, 9 ),
      PaymentRange( 20, 9, 18 ),
      PaymentRange( 25, 18, 24 )
    ]
  )
]

days = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']

global employees
employees = []

def read_file(name):
    try:
        x = open(name, 'r')
        return x
    except:
        return('Something went wrong when reading to the file')
        x.close()

def get_day(token, index):
    day = token[0:2]
    if (day in days):
        return day
    else:
        raise Exception('Day does not exist! in line', index)

def get_start(token, index):
    hour = token[2:4]
    minute = token[5:7]
    time = 0
    try:
        if (hour.isdigit() and (int(hour) < 24 and int(hour) >= 0)):
            time = hour
            if (minute.isdigit() and int(minute) == 0):
                return int(time)
            else:
                raise Exception('hours should not have minutes! in line', index)
        else:
            raise Exception('Error in hours format! in line', index)
        raise Exception('Something went wrong! in line', index)
    except  Exception as inst:
        raise Exception(inst)

def get_end(token, index):
    hour = token[8:10]
    minute = token[11:13]
    time = 0
    try:
        if (hour.isdigit()):
            time = hour
            if (minute.isdigit() and int(minute) == 0):
                return int(time)
            else:
                raise Exception('Hours should not have minutes! in line', index)
        else:
            raise Exception('Error in hours format! in line', index)
        raise Exception('Something went wrong! in line', index)
    except  Exception as inst:
        raise Exception(inst)

def get_info(token, index):
    listDay = []
    days = token.split(',')
    try:
        for d in days:
            if (get_day(d, index)):
                info = WorkDay(
                    get_day(d, index),
                    get_start(d, index),
                    get_end(d, index)
                )
                listDay.append(info)
            else:
                raise Exception('Error days format!, in line ' + index)
                break
    except Exception as inst:
        raise Exception(inst)
    return listDay

def serialize_file():
    try:
        f = read_file('data.txt')
        index = 1
        for linea in f:
            if len(linea) > 1:
                register = linea.split('=', 1)
                dataSerialized = Employee(
                    register[0],
                    get_info(register[1], index)
                )
                employees.append(dataSerialized)
            index += 1
        f.close()
    except Exception as inst:
        raise Exception(inst)
    finally:
        f.close()

def calculate(employee):
  for schedule in SCHEDULE:
    for day in employee.workDays:
      if day.id in schedule.ids:
        matchDay = False
        for rank in schedule.ranges:
          if day.start > rank.start and day.end <= rank.end:
            hours = day.getHours()
            if hours <= 0:
              print('Hours not valid for ' + employee.name+ '\n')
              return
            matchDay = True
            employee.addPayment( hours * rank.value )
        if not matchDay:
          print('Hours not valid for ' + employee.name+ '\n')
          return
  print('The amount to pay ' + employee.name+ ' is: ' + employee.getFullPayment() + ' USD\n')

def main():
    try:
        serialize_file()
        for employee in employees:
		    calculate(employee)
    except Exception as inst:
        print(inst.args)
        print(inst)
main()

