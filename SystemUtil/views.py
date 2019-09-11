import time
import psutil

from django.shortcuts import render
from django.http import JsonResponse

max_network_speed = 0


# Create your views here.
def get_cpu_percent(requests):
    cpu_percent = psutil.cpu_percent()
    return JsonResponse({"cpu_percent": cpu_percent}, safe=False)


def get_memory_percent(requests):
    memory = psutil.virtual_memory()
    percent = memory.percent
    return JsonResponse({"memory_percent": percent}, safe=False)


def get_recv_speed(requests):
    global max_network_speed

    bytes_recv_0 = psutil.net_io_counters().bytes_recv
    t0 = time.perf_counter()

    bytes_recv_1 = psutil.net_io_counters().bytes_recv
    t1 = time.perf_counter()

    recv_speed = float(bytes_recv_1 - bytes_recv_0) / (t1 - t0) / (1024 * 1024)
    max_network_speed = recv_speed if recv_speed > max_network_speed else max_network_speed

    avg_speed = (recv_speed + max_network_speed) / 2
    avg_rate = avg_speed / max_network_speed * 100

    return JsonResponse({"recv_speed": "%.4f" % avg_speed, "recv_rate": avg_rate}, safe=False)


def get_battery_level(requests):
    battery = psutil.sensors_battery()
    percent = battery.percent
    return JsonResponse({"battery_status": percent}, safe=False)

