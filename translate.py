import datetime
def translate():
    now = datetime.datetime.now()
    string=(now.strftime("%A %B %d %Y %H:%M:%S"))

    months = {
        'January': 'Januari',
        'February': 'Februari',
        'March': 'Maart',
        'April': 'April',
        'May': 'Mei',
        'June': 'Juni',
        'July': 'Juli',
        'August': 'Augustus',
        'September': 'September',
        'October': 'Oktober',
        'November': 'November',
        'December': 'December'
    }

    for month, dutch_month in months.items():
        if month in string:
            string = string.replace(month, dutch_month)



    splitalles=string.split(' ')
    maand=splitalles[1]
    datum=splitalles[2]
    jaar=splitalles[3]
    tijd=str(splitalles[4].split(':')[0])+ ":" + str(splitalles[4].split(':')[1])
    return f"{datum} {maand} {jaar} {tijd}"
