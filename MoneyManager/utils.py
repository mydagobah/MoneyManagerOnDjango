import json
from decimal import Decimal

# column definition for category as x-axis
cols_category = [{"id": 'A', "label": 'Category', "type": 'string'},
                 {"id": 'B', "label": 'Spending', "type": 'string'}]

# column definition for month as x-axis
cols_month    = [{"id": 'A', "label": 'Month',    "type": 'string'},
                 {"id": 'B', "label": 'Spending', "type": "number"}]

# column definition for month as x-axis
cols_year     = [{"id": 'A', "label": 'Year',     "type": 'string'},
                 {"id": 'B', "label": 'Spending', "type": "number"}]

# map month number to English name
month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
	     7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

# initial year of use
# TODO read from config
INIT_YEAR = "2014"

# convert data to json format
# input - xname: string, x axis name of the chart
#       - data:  map, key-value pair
def toJson(xname, data):
    ret = {}
    ret['rows'] = []

    if (xname == 'Month'):
        ret['cols'] = cols_month
        for k, v in sorted(data.items()):
            row = {}
            row['c'] = [{'v': month_map[k]}, {'v': v}]
            ret['rows'].append(row)
    elif (xname == 'Year'):
        ret['cols'] = cols_year
        for k, v in sorted(data.items()):
            row = {}
            row['c'] = [{'v': str(k)}, {'v': v}]
            ret['rows'].append(row)
    else:
        ret['cols'] = cols_category
        for k, v in data.items():
            row = {}
            row['c'] = [{'v': k}, {'v': v}]
            ret['rows'].append(row)

    return ret

# serialize python Decimal to json number
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)
