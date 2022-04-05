# timer
# User: should input a time 
# Program: will after the time is inputed count down then when at 0 play a sound.
# done by Samuel Chandler


import time

def countdown(t):
    while t:
        mins, sec = divmod(t,60)
        timer = '{:}'