from MoneyManager.models import Category, Spense
from django.utils import timezone
import datetime

# monthly summary by category
# input  - the query month, string
# output - spense: map, {category : monthly spense}
def getMDataByCategory(month, year):
    mnum = int(month)
    ynum = int(year)
    data = {}

    # fetch all spense of the month
    dataOfMonth = Spense.objects.filter(issue_date__year = ynum).filter(issue_date__month = mnum)

    for e in dataOfMonth:
	if e.category.name in data:
    	    data[e.category.name] += e.amount
	else:
    	    data[e.category.name] = e.amount

    return data

# yearly summary by category
# input  - year:   string, the year of query
# output - spense: map, {category : yearly spense}
def getYDataByCategory(year):
    ynum = int(year)
    data = {}

    dataOfYear = Spense.objects.filter(issue_date__year = ynum)

    for e in dataOfYear:
	if e.category.name in data:
    	    data[e.category.name] += e.amount
	else:
    	    data[e.category.name] = e.amount

    return data
# End of getYDataByCategory

# spense summary by month
# input  - month:  string, the last month of query
#          year:   string, the year of query
# output - spense: map, {month : monthly spense}
def getDataByMonth(month, year):
    mnum = int(month)
    ynum = int(year)
    data = {}

    # fetch all spense of the year
    dataOfYear = Spense.objects.filter(issue_date__year = ynum)

    # summarized by month
    for m in range(1, mnum + 1):
         dataOfMonth = dataOfYear.filter(issue_date__month = m)
         data[m] = 0
         for e in dataOfMonth:
             data[m] += e.amount

    return data
# End of getDataByMonth

# spense summary by year
# input  - init:   string, initial year
#          year:   string, the year of query
# output - spense: map, {year : monthly spense}
def getDataByYear(init, year):
    ybeg = int(init)
    yend = int(year)
    data = {}

    # fetch all spense of the year
    dataOfYears = Spense.objects.filter(issue_date__gte=datetime.date(ybeg,1,1), issue_date__lte=datetime.date(yend,12,31))

    # summarized by month
    for y in range(ybeg, yend + 1):
         dataOfYear = dataOfYears.filter(issue_date__year = y)
         data[y] = 0
         for e in dataOfYear:
             data[y] += e.amount

    return data
# End of getDataByYear


# monthly summary by category
# input  - the query month, string
# output - spense: map, {category : monthly spense}
def getCategoryData(year, month, category):
    mnum = int(month)
    ynum = int(year)
    ctgr = Category.objects.filter(name = category)

    # fetch all spense of the month
    dataOfMonth = Spense.objects.filter(issue_date__year = ynum).filter(issue_date__month = mnum).filter(category_id = ctgr[0].id)

    data = {}
    data['rows'] = []
    for d in dataOfMonth:
	row = {}
        row['category'] = d.category.name
        row['value']    = d.amount
	row['date']     = d.issue_date.strftime("%Y/%m/%d")
	row['comment']  = d.comment
        data['rows'].append(row)

    return data
