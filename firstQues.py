from datetime import date

sunday=0
for year in range(1900,2001):
	for month in range(1,13):
		if date(year,month,1).weekday()==6:
			sunday+=1
print(sunday)
