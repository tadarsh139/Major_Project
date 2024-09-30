from django.shortcuts import render
from .utils import initialize_monitor, detect_modifications
import os

# Initialize the monitor at server start
initialize_monitor()

def monitor_files(request):
    modifications = detect_modifications()
    print(os.listdir)
    return render(request, 'C:/Users/HP/FileMonitor/monitor/templates/monitor/index.html', {'modifications': modifications})

# monitor_files("request")