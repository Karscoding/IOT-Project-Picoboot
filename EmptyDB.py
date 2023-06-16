from CreateDB import app,Temperatuur,actielog,Afstand,db

def delete():
    with app.app_context():
        for x in Temperatuur.query.all():
            db.session.delete(x)
        for x in Afstand.query.all():
            db.session.delete(x)
        for x in actielog.query.all():
            db.session.delete(x)
        db.session.commit()

if __name__=="__main__":
    delete()
    
