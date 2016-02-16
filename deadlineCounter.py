import datetime
currentDate = datetime.date.today()
deadline = input ("What is the deadline of the project? (mm/dd/yyyy) ")
#strftime convert a string to a date
remainingTime = \
datetime.datetime.strptime(deadline, "%m/%d/%Y").date()
#why did we list datetime twice?
#because we are calling strptime function
#which is part of a datetime class
#which is in the datetime module

daysTillPayment = remainingTime - currentDate
print ("Days till your deadline: ")
print (daysTillPayment.days)

#Divide deadline into weeks and days 
totalWeeks = daysTillPayment.days/7
totalDays = daysTillPayment.days%7
print ("You have %d weeks " %totalWeeks + " and %d days " %totalDays +" left")