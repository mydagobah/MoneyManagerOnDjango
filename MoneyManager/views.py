from django.shortcuts import render
from django.utils import timezone
from django.http import Http404, HttpResponse
from MoneyManager.models import SpenseForm
from decimal import Decimal
import dao
import json

chart_cols = [{"id": 'A', "label": 'Category', "type": 'string'},
              {"id": 'B', "label": 'Spending', "type": 'string'}]

# index view controller
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

# return json data
def getMonthlyData(request):
    dataByCategory = dao.getMonthlyData()
    m_json = {}
    m_json['cols'] = chart_cols
    m_json['rows'] = []

    for c in dataByCategory.keys():
	row = {}
	row['c'] = [{'v': c}, {'v': dataByCategory[c]}]
        m_json['rows'].append(row)

    return HttpResponse(json.dumps(m_json, cls=DecimalEncoder), content_type='application/json')

# return json data
def getYearlyData(request):
    dataByCategory = dao.getYearlyData()
    y_json = {}
    y_json['cols'] = chart_cols
    y_json['rows'] = []

    for c in dataByCategory.keys():
	row = {}
	row['c'] = [{'v': c}, {'v': dataByCategory[c]}]
        y_json['rows'].append(row)

    return HttpResponse(json.dumps(y_json, cls=DecimalEncoder), content_type='application/json')


# serialize python Decimal to json number
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

#----------------------------------------------
# import data from xls/cvs files
# def import(request):
#     category_list = Category.objects.all()
#     context = {'category_list': category_list}
#     return render(request, 'MoneyManager/index.html', context)
# 
# # 
# def income(request):
#     category_list = Category.objects.all()
#     context = {'category_list': category_list}
#     return render(request, 'MoneyManager/index.html', context)
