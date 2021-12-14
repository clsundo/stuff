import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)

delay_print("hello world !\n")
input("appuyez sur entrer pour sortir")
