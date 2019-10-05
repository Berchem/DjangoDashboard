import datetime as dt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from Jobs.models import TestRequestJob
from Jobs.models import TestRequestJobDaily


@login_required
@staff_member_required
def jobs(request):
    title = 'Jobs'
    return render(request, 'jobs.html', locals())


