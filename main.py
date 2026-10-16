import zahl
from libs import zahl2

print (zahl.gibZahl()) # aus zahl.py

print(zahl2.gibZahl2()) # aus libs/zahl2.py

with open("demofile.txt", "a") as f:
  f.write("Das ist ein Test!")

with open("demofile.txt") as f:
  print(f.read())