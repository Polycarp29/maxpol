import random
import os 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOQRSTUVWXYZ"
numbers = "1234567890"
symbols ="/+_@#$%^&*()_+=[];'.><{}~`"
all = lower+upper+numbers+symbols
length = 25

password ="".join(random.sample(all,length))
point = (password)
print(password)
