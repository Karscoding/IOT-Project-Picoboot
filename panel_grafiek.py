import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os
from databasevuller import app, Afstand

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def run(dag=0):
    distlist = []
    
    with app.app_context(): 
        for x in Afstand.query.all():
            distlist.append((x.afstand, x.nap))
    
    return distlist

def animate(i):
    data = run()
    if data:
        xs = [x[0] for x in data]
        ys = [x[1] for x in data]
        ax1.clear()
        ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()