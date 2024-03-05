birtday = input("When is your birthday (DD/MM/YYYY)?" )
year = int(birtday[-4:])
day = int(birtday[0:2])
candel = str("i"*day)
print(f'''
       ___{candel}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~''')


if year % 4 == 0 and year % 100 != 0:
    print(f'''
       ___{candel}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~''')




