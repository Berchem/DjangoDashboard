import os
import time
import psutil

from django.shortcuts import render
from django.http import JsonResponse
from SystemUtil.models import ToDoList

max_receive_speed: float = 1e-6
max_sent_speed: float = 1e-6


def widgets(request):
    title = "Widgets"
    info_map = _system_status()
    to_do_list = ToDoList.objects.all()
    return render(request, 'widgets.html', locals())


def update_to_do_status(request, index):
    item = ToDoList.objects.get(pk=index)
    item.status = abs(item.status - 1)
    item.save()
    to_do_item = ToDoList.objects.get(pk=index)
    return JsonResponse({"index": to_do_item.index,
                         "item": to_do_item.item,
                         "status": to_do_item.status}, safe=False)


def delete_to_do_item(request, index):
    ToDoList.objects.get(pk=index).delete()
    return JsonResponse({"display": "none"})


def insert_to_do_list(request, item):
    ToDoList.objects.create(item=item, status=1)
    item = ToDoList.objects.filter(item=item).latest('index')
    print(item.index, item.item, item.status)
    list_item = """
    <li class="todo-list-item" id="todo-{{item.index}}">
        <div class="checkbox">
            <input type="checkbox" id="checkbox-{index}" onclick="update_to_do_status('checkbox-{index}')"/>
            <label for="checkbox-{index}">{item}</label>
        </div>
        <div class="pull-right action-buttons" onclick="delete_to_do_item('todo-{index}')"><a class="trash"><em class="fa fa-trash"></em></a></div>
    </li>""".format(index=item.index, item=item.item)
    return JsonResponse({"list_item": list_item})


def get_system_status(request):
    info_map = _system_status()

    if info_map["battery_low"]:
        os.system("shutdown -s")

    return JsonResponse(info_map, safe=False)


def _get_net_io_speed_rate(t_0, net_io_0, t_1, net_io_1):
    global max_receive_speed, max_sent_speed
    receive_speed = float(net_io_1.bytes_recv - net_io_0.bytes_recv) / (t_1 - t_0) / (1024 * 1024)
    max_receive_speed = receive_speed if receive_speed > max_receive_speed else max_receive_speed
    avg_receive_speed = (receive_speed + max_receive_speed) / 2

    sent_speed = float(net_io_1.bytes_sent - net_io_0.bytes_sent) / (t_1 - t_0) / (1024 * 1024)
    max_sent_speed = sent_speed if sent_speed > max_sent_speed else max_sent_speed
    avg_sent_speed = (sent_speed + max_sent_speed) / 2

    max_speed = max(max_receive_speed, max_sent_speed)
    avg_receive_rate = avg_receive_speed / max_speed * 100
    avg_sent_rate = avg_sent_speed / max_speed * 100
    return avg_receive_speed, avg_sent_speed, avg_receive_rate, avg_sent_rate


def _system_status():
    t_0, net_io_0 = time.perf_counter(), psutil.net_io_counters()
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    battery_percent = psutil.sensors_battery().percent
    battery_low = battery_percent < 10

    t_1, net_io_1 = time.perf_counter(), psutil.net_io_counters()

    avg_receive_speed, avg_sent_speed, avg_receive_rate, avg_sent_rate = _get_net_io_speed_rate(
        t_0, net_io_0, t_1, net_io_1)

    info_map = {"cpu_percent": cpu_percent,
                "memory_percent": memory_percent,
                "receive_speed": "%.4f" % avg_receive_speed,
                "receive_rate": avg_receive_rate,
                "sent_speed": "%.4f" % avg_sent_speed,
                "sent_rate": avg_sent_rate,
                "battery_status": battery_percent,
                "battery_low": battery_low}
    return info_map
