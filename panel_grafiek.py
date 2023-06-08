# pip install pandas matplotlib sqlalchemy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from databasevuller import app, Afstand

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def run(dag=0):
    distlist = []
    
    with app.app_context(): 
        for x in Afstand.query.all():
            combined_value = x.afstand + x.nap
            distlist.append((x.tijd, combined_value))
    
    return distlist

def animate(i):
    ax1.clear()  # Clear the previous plot
    data = run()
    if data:
        xs = [x[0] for x in data]
        ys = [x[1] for x in data]
        ax1.clear()
        ax1.plot(xs, ys)
        ax1.set_ylabel('Afstand + Nap')

ax1.set_xlabel('Tijd')

ani = animation.FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
plt.show()