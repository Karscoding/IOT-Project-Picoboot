def translate(string):
    # days = {
    #     'Monday': 'Maandag',
    #     'Tuesday': 'Dinsdag',
    #     'Wednesday': 'Woensdag',
    #     'Thursday': 'Donderdag',
    #     'Friday': 'Vrijdag',
    #     'Saturday': 'Zaterdag',
    #     'Sunday': 'Zondag'
    # }

    # for day, dutch_day in days.items():
    #     if day in string:
    #         string = string.replace(day, dutch_day)

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



    # splitalles=string.split(',')
    # dag=splitalles[0]
    # helft=splitalles[1].split(' ')
    helft=string.split(' ')
    maand=helft[0]
    datum=helft[1]
    jaar=helft[2]
    tijd=helft[3]
    # return str(f"{dag} {datum} {maand} {jaar} {tijd}")
    return str(f"{datum} {maand} {jaar} {tijd}")
