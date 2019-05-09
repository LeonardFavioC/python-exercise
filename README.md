# Exercise to calculate the value to pay according to hours worked in python

## Details

```Exercise written in python```

```The goal this exercise to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked.```

### Rules

```The following abbreviations will be used for entering data:```

`MO: Monday`

`TU: Tuesday`

`WE: Wednesday`

`TH: Thursday`

`FR: Friday`

`SA: Saturday`

`SU: Sunday`

`Hours format:` : **24:00**

`The hours must not contain minutes`

`Employees can not work at times with different value`

`One register for line in  file txt`

**The input values must strictly have this format:**

`RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00`

`The values to be paid are calculated according to the following table`

**Monday - Friday**

`00:01 - 09:00 25 USD`

`09:01 - 18:00 15 USD`

`18:01 - 00:00 20 USD`

**Saturday and Sunday**

`00:01 - 09:00 30 USD`

`09:01 - 18:00 20 USD`

`18:01 - 00:00 25 USD`

**For example:**

Case 1:

**INPUT**

`RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00`

**OUTPUT:**

`The amount to pay RENE is: 215 USD`

Case 2:

**INPUT**

`ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00`

**OUTPUT:**

`The amount to pay ASTRID is: 85 USD`

`To change inputs edit data.txt`

`To change values for hour change SCHEDULE in index.py`

## Usage

`Run in python 2 or 3 from terminal`

- Locate in folder

- Run

`python index.py`

**By: Leonardo Caraguay**
