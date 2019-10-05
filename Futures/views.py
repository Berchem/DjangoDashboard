import datetime as dt

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from Futures.models import HModel
from Futures.models import TestKLineData
from Futures.models import TestQuoteData


@login_required
def futures(request):
    title = "Futures"
    tsea_today_close = TestKLineData.objects.\
        filter(item_code='TSEA').\
        order_by('-index')[0]

    today = dt.datetime.today()
    close = today.replace(hour=13, minute=30, second=0, microsecond=0)
    today = close if today > close else close - dt.timedelta(days=1)

    tsea_quote = TestQuoteData.objects.\
        filter(item_code='TSEA'). \
        order_by('-datetime')[0]
        # filter(datetime__startswith=today.strftime("%Y/%m/%d %H:%M")).\
        # order_by('-datetime')[0]

    mtx_current_quote = TestQuoteData.objects.\
        filter(item_code='MTX00').\
        order_by('-datetime')[0]

    mtx_next_quote = TestQuoteData.objects. \
        filter(item_code='MTX%02d' % (today.month + 1)). \
        order_by('-datetime')[0]
    return render(request, 'futures.html', locals())


def get_quote(request):
    tsea_today_close = TestKLineData.objects. \
        filter(item_code='TSEA'). \
        order_by('-index')[0]

    today = dt.datetime.today()
    close = today.replace(hour=13, minute=30, second=0, microsecond=0)
    today = close if today > close else close - dt.timedelta(days=1)

    mtx_current = TestKLineData.objects. \
        filter(item_code='MTX00'). \
        filter(datetime__startswith=today.strftime("%Y/%m/%d %H:%M")). \
        order_by('-datetime')[0]
    mtx_current = {'item_code': mtx_current.item_code}

    mtx_next = TestKLineData.objects. \
        filter(item_code='MTX%02d' % (today.month + 1)). \
        filter(datetime__startswith=today.strftime("%Y/%m/%d %H:%M")). \
        order_by('-datetime')[0]

    mtx_current_quote = TestQuoteData.objects. \
        filter(item_code='MTX00'). \
        order_by('-datetime')[0]

    mtx_next_quote = TestQuoteData.objects. \
        filter(item_code='MTX%02d' % (today.month + 1)). \
        order_by('-datetime')[0]
    return

def get_data(request):
    data = []
    for record in HModel.objects.all():
        row = dict()
        row["id"] = record.id
        row["date"] = record.date
        row["weighted_index"] = float(record.weighted_index)
        row["volume"] = float(record.volume)
        row["current_price"] = int(record.current_price)
        row["next_price"] = int(record.next_price)
        data += [row]
    return JsonResponse(data, safe=False)
