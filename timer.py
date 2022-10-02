import time
import sys
import os
import argparse

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.version = '1.0'
    parser.add_argument('minute',
                        action = 'store',
                        type = int,
                        choices = range(1, 60),
                        default = 25,
                        help = 'Set duration in minute')

    args = parser.parse_args()

    minute = args.minute
    os.system('cls')
    countdown(minute)
