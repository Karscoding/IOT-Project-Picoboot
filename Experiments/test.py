import time
run = False
if __name__ == '__main__':
    run = True

f = open('temp.txt', 'w')
f.write('Working')
f.close()

x = 0.0

while run:
    x += 1.1
    f = open('temp.txt', 'w')
    f.write(str(x))
    f.close()
    time.sleep(2)