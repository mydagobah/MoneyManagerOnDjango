from django.shortcuts import render
from django.utils import timezone
from django.http import Http404, HttpResponse
import json

from MoneyManager.models import SpenseForm
import dao, utils

# display home page
# process add spense form
def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SpenseForm(request.POST)
        if form.is_valid():
	    obj = form.save(commit=False)
            obj.added_date = timezone.now()
	    obj.save()
	    form = SpenseForm()
    else:
        form = SpenseForm() # GET, return a empty form

    return render(request, 'MoneyManager/index.html', {'form': form})

# request:  monthly spense by category
#           month - string, the month, default to current month
#           year  - string, the year of the month, default to current year
# response: json formatted data
def getMDataByCategory(request):
    month = request.GET.get('month', str(timezone.now().month))
    year  = request.GET.get('year', str(timezone.now().year))
    dataByCategory = dao.getMDataByCategory(month, year)
    data = utils.toJson('Category', dataByCategory)

    return HttpResponse(json.dumps(data, cls=utils.DecimalEncoder), content_type='application/json')

# request:  yearly spense by category
#           year  - string, the year, default to current year
# response: json formatted data
def getYDataByCategory(request):
    year  = request.GET.get('year', str(timezone.now().month))
    dataByCategory = dao.getYDataByCategory(year)
    data = utils.toJson('Category', dataByCategory)

    return HttpResponse(json.dumps(data, cls=utils.DecimalEncoder), content_type='application/json')

# request:  monthly spense by month
#           month - string, the month, default to current month
#           year  - string, the year of the month, default to current year
# response: json formatted data
def getDataByMonth(request):
    month = request.GET.get('month', str(timezone.now().month))
    year  = request.GET.get('year',  str(timezone.now().year))
    dataByMonth = dao.getDataByMonth(month, year)
    # format jason data
    data = utils.toJson('Month', dataByMonth)

    return HttpResponse(json.dumps(data, cls=utils.DecimalEncoder), content_type='application/json')

# request:  yearly spense by year
#           year  - string, the year, default to current year
# response: json formatted data
def getDataByYear(request):
    year  = request.GET.get('year', str(timezone.now().year))
    dataByYear = dao.getDataByYear(utils.INIT_YEAR, year)
    # format jason data
    data = utils.toJson('Year', dataByYear)

    return HttpResponse(json.dumps(data, cls=utils.DecimalEncoder), content_type='application/json')



# request:  yearly spense by category
#           year  - string, the year, default to current year
# response: json formatted data
def getCategoryData(request):
    month = request.GET.get('month', str(timezone.now().month))
    year  = request.GET.get('year',  str(timezone.now().year))
    ctgr  = request.GET.get('category')
    data  = dao.getCategoryData(year, month, ctgr)

    return HttpResponse(json.dumps(data, cls=utils.DecimalEncoder), content_type='application/json')
