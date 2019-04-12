import threading, time, random

counter = 0


def worker():
    global counter
    counter += 1
    print("The count is {}".format(counter))
    print("----------")


print("starting up\n")
for i in range(10):
    threading.Thread(target=worker).start()
print("finished the work")

