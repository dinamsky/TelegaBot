from datetime import datetime as dt
import time

fatto = 0
Notte = '11:24:00'
oraNotte = dt.strptime(Notte, '%H:%M:%S').time()

while fatto == 0:
    ora = dt.now()
    if ora.isoweekday() == 3 and ora.time().replace(second=0, microsecond=0) == oraNotte:
        fatto = 1
        print('Tic')
    else:
        print('Nah')
    time.sleep(10)
