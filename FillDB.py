from CreateDB import app,db,Temperatuur,actielog,Afstand
from translate import translate
from random import uniform,randint,choice
def genrandomtime(x):
    tijd=translate()
    datum=int(tijd.split(" ")[0])+x//10
    maand=tijd.split(" ")[1]
    jaar=tijd.split(" ")[2]
    uren=randint(1,12)
    if uren<10:
        uren=f"0{uren}"
    minuten=randint(0,60)
    if minuten<10:
        minuten=f"0{minuten}"
    tijd=f"{datum} {maand} {jaar} {uren}:{minuten}"
    return tijd

def genid(Database):
    with app.app_context():
        '''Temperatuur'''
        if Database.query.all()==[]:
            id=1
        else:
            highestid = Database.query.all()
            id=(highestid[-1].id+1)
        return id

def randomfill(amount=1):
    for x in range(amount):
        with app.app_context():
            '''Temperatuur'''
            id=genid(Temperatuur)
            tijd=genrandomtime(x)
            data= round(uniform(25,35),2)
            db.session.add_all([Temperatuur(id,tijd, data)])

            '''Afstand'''
            id=genid(Afstand)
            tijd=genrandomtime(x)
            diepte=round(uniform(2,4),1)
            nap=round(uniform(-1,1),1)
            db.session.add_all([Afstand(id,tijd, diepte,nap)])

            '''Log'''
            id=genid(actielog)
            data=genrandomtime(x)
            actie=choice(['Noodstop','Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd', 'Ingelogd'])
            db.session.add_all([actielog(id,data,actie)])
            db.session.commit()


if __name__=="__main__":
    randomfill(100)