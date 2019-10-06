import datetime as dt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from Jobs.models import TestRequestJob
from Jobs.models import TestRequestJobDaily


status_bg = {
    'NEW': 'bg-primary',
    'RUNNING': 'bg-info',
    'KILL': 'bg-warning',
    'FINISH': 'bg-success',
}

status_icon = {
    'NEW': 'arrow-right',
    'RUNNING': 'play-circle',
    'KILL': 'ban',
    'FINISH': 'check-circle',
}


@login_required
@staff_member_required
def jobs(request):
    title = 'Jobs'

    daily_jobs = TestRequestJobDaily.objects.all()

    request_jobs = get_request_jobs(request)

    return render(request, 'jobs.html', locals())


def get_request_jobs(request):
    obj_request_jobs = TestRequestJob.objects.\
        filter(username=request.user.username).\
        order_by('-submit_time')
    request_jobs = [{
        'index': record.index,
        'username': record.username,
        'submit_time': record.submit_time,
        'status': record.status,
        'status_icon': status_icon[record.status],
        'status_bg': status_bg[record.status],
        'program': record.program,
        'process': record.process,
        'item_code': record.item_code,
        'duration': dt.datetime.now().replace(second=0, microsecond=0) - dt.datetime.strptime(record.submit_time, '%Y/%m/%d %H:%M:%S'),
        'page': record.page,
        'k_line_type': record.k_line_type,
        'output_format': record.output_format,
        'trade_session': record.trade_session,
    } for record in obj_request_jobs]
    return request_jobs


def kill(request, index):
    print(index, type(index))
    job = TestRequestJob.objects.get(pk=index)
    job.status = "KILL"
    job.save()
    record = TestRequestJob.objects.get(pk=index)
    return JsonResponse({'index': record.index,
                         'username': record.username,
                         'submit_time': record.submit_time,
                         'status': record.status,
                         'status_icon': status_icon[record.status],
                         'status_bg': status_bg[record.status],
                         'program': record.program,
                         'process': record.process,
                         'item_code': record.item_code,
                         'duration': str(dt.datetime.now().replace(second=0, microsecond=0) - dt.datetime.strptime(record.submit_time, '%Y/%m/%d %H:%M:%S')),
                         'page': record.page,
                         'k_line_type': record.k_line_type,
                         'output_format': record.output_format,
                         'trade_session': record.trade_session, }, safe=False)
