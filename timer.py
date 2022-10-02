import time
import sys
import os

def countdown(minute):
    for j in range(minute-1,-1,-1):
        for i in range(59,-1,-1):
            if i <= 9:
                sys.stdout.write \
                (f'\rDuration: {j} Minutes 0{i} Seconds to go')
            else:
                sys.stdout.write \
                (f'\rDuration: {j} Minutes {i} Seconds to go')

            time.sleep(1)
            sys.stdout.flush()

countdown(1)
