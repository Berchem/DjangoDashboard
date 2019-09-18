from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

from Configurations.models import CapitalAccount
from Configurations.models import CapitalFuturesCorp


@login_required
@staff_member_required
def configs(request):
    title = "Config"
    try:
        capital = CapitalAccount.objects.get(username=request.user.username)
    except ObjectDoesNotExist:
        CapitalAccount.objects.create(username=request.user.username)
        capital = CapitalAccount.objects.get(username=request.user.username)

    margin_accounts = CapitalFuturesCorp.objects.all()
    return render(request, 'configs.html', locals())


def check(request):
    update_capital_account(request)
    return redirect("/conf")


def update_capital_account(request):
    capital = CapitalAccount.objects.get(username=request.user.username)
    capital.account = request.POST["capital_account"]
    capital.password = request.POST["capital_password"]
    capital.id_number = request.POST["id_number"].upper()
    capital.deposit_code = request.POST["deposit_code"]
    capital.deposit_account = request.POST["deposit_account"].zfill(16)
    capital.save()
