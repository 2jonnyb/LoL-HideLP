import time

with open ("test1.txt","w") as f:
    f.write("dn")
time.sleep(2)
with open ("test2.txt","w") as f:
    f.write("dn")
