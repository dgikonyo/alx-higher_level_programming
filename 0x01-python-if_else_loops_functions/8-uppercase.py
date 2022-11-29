#!/usr/bin/python3
# Author - Gikonyo Kimani

def uppercase(str):
    for c in str:
        if ord(c) >= 65 and ord(c) <=90:
            return True
        else:
            return False
