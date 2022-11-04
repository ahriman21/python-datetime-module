1-
# to make a DateType variable :
from datetime import date
my_birthday = date(2003,9,1) ## year,month,day

2-
# get current date:
toay = date.today()
  ## print("todate",today)
  ## print("Current year:", today.year)
  ## print("Current month:", today.month)
  ## print("Current day:", today.day)

3-
# convert date to str :
today = date.today()
str_date = date.isoformat(today)

4-
# make Time Variable :
Time = time(hour=2,minute=22,second=00)

5-
# Converting Time object to string
Time = time(12,24,36,1212)
Str_time = Time.isoformat()

6-
# calling date and time using datetime from datetime module  :
from datetime import datetime
today = datetime.now()
print("Current date and time is", today)
