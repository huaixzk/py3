#!/usr/bin/env python

s = input("enter an integer :");
try :
    i = int(s);
    print("vaild integer entered:",i);
except ValueError as err:
    print(err);
