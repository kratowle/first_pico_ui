# i am importing a script from a library within the python package in system dependancies
import time
import os


total_hours = 12
total_minutes = 60
total_seconds = 60

current_hour = 1
current_minute = 30
current_second = 0

# keeps everything happening below locked in a loop forever updating every /time.sleep()
while True:
    current_second = current_second + 1
    print(current_second)

    if (current_second == 4):
        print("were learning")
        break
        


    time.sleep(1)
    os.system("clear")

