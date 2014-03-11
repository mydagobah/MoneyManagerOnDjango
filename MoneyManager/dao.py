from MoneyManager.models import Category, Spense
from django.utils import timezone

def getMonthlyData():
    currmonth   = timezone.now().month
    monthlyData = Spense.objects.filter(issue_date__month = currmonth)
    spenseByCategory = {}
    for e in monthlyData:
	if e.category.name in spenseByCategory:
    	    spenseByCategory[e.category.name] += e.amount
	else:
    	    spenseByCategory[e.category.name] = e.amount

    return spenseByCategory

def getYearlyData():
    curryear   = timezone.now().year
    yearlyData = Spense.objects.filter(issue_date__year = curryear)
    spenseByCategory = {}
    for e in yearlyData:
	if e.category.name in spenseByCategory:
    	    spenseByCategory[e.category.name] += e.amount
	else:
    	    spenseByCategory[e.category.name] = e.amount

    return spenseByCategory

