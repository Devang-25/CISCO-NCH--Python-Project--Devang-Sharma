# Solution Submitted By: DEVANG SHARMA
# Email: devangsharma419@gmail.com
# Alternate Email: devangsharma25398@gmail.com
# T: +91-9953027469


# Code Starts Here


import calendar
import datetime
from IPython.display import display,HTML

def function(num):
    
    # Entered Value Must Lie Between -12 and 12
    if num>12 or num<-12:
        print("Enter a Number between -12 to +12")
    
    else:
        now = datetime.datetime.now()
        yy=now.year
        mm=now.month+num
        
        if mm>12:
            yy=yy+1
            mm=mm%12
        
        if mm<1:
            yy=yy-1
            mm=mm+12
        
        # create HTML Calendar month
        cal = calendar.HTMLCalendar(calendar.SUNDAY)
        s= cal.formatmonth (yy,mm)
        
        # add cell's backgroundcolor, bold and underling html tags 
        # around today's date
        ss = s.replace('>%i<'%t.day, ' bgcolor="#66ff66"><b><u>%i</u></b><'%t.day)
        display(HTML(ss))

print("Enter Value: ", end="")
val=int(input())
function(val)
