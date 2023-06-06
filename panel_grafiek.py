import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os
from databasevuller import app, Afstand

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def run(dag=0):
    distlist=[]
    
    with app.app_context(): 
        for x in Afstand.query.all():
            distlist.append((x.afstand,x.nap))
    print(distlist)

def animate(i):
    graph_data = 'dishlist'
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

    ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()