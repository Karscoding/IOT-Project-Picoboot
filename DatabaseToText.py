from CreateDB import app, Temperatuur, Afstand,actielog
from translate import translate

def getdata():
    '''Haalt alle gegevens uit de database'''
    with app.app_context():

        '''Temperatuur'''
        temp=[]
        if Temperatuur.query.all()==[]:
            temp=("geen temperatuur opnames")
        else:
            for x in (Temperatuur.query.all()):
                temp.append((x.tijd,x.temperatuur))

        '''Afstand'''
        afst=[]
        if Afstand.query.all()==[]:
            afst="geen afstand opnames"
        else:
            for x in (Afstand.query.all()):
                if len(str(x.afstand))==1:
                    string=str(x.afstand)
                    string+='.0'
                    afst.append((x.tijd,string,x.nap))
                else:
                    afst.append((x.tijd,x.afstand,x.nap))

        '''Acties''' 
        acties=[]
        if actielog.query.all()==[]:
            acties="geen log opnames"
        else:
            for x in (actielog.query.all()):
                acties.append((x.tijd,x.actions))
    return temp,afst,acties

def makeup(list):
    '''Formatteerd alle gegevens'''
    if type(list)==str:
        return list
    try:
        string=""
        for x in list:
            string+=f"{x[0]}    {x[1]}    {x[2]}\n"
        return string
    except IndexError:
        string=""
        for x in list:
            string+=f"{x[0]}    {x[1]}\n"
        return string
    

def writetotext(alledata):
    '''Schrijft alle gegevens naar een tekstbestand'''
    temperaturen=alledata[0]
    afstanden=alledata[1]
    loggen=alledata[2]

    mooitemp=makeup(temperaturen)
    mooiafst=makeup(afstanden)
    mooilog=makeup(loggen)

    string="       Tijd       Temperatuur\n"
    string+=mooitemp

    string+="\n\n       Tijd        Afstand    NAP\n"
    string+=mooiafst

    string+="\n\n       Tijd        Actie\n"
    string+=mooilog

    with open(f"{translate().split()[0]}{translate().split()[1]}.txt","a") as f:
        f.write(string)


writetotext(getdata())
