import datetime
import itertools

def friday_the_13th():
    today = datetime.date.today()

    todaymonth = today.month
    todayyear = today.year
    
    

    for year in itertools.count(start = todayyear, step = 1):
        
        if year == todayyear:
            startMonth = todaymonth
        else:
            startMonth = 1

        for i in range(startMonth,13):
            currDate = datetime.date(year,i,13)
            currDay = currDate.strftime("%A")

            if currDate < today:
                continue
            
            if(currDay == "Friday"):
                return str(currDate)

    
                
            
            
            
