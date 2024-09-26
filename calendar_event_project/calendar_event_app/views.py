from django.shortcuts import render
from django.utils.safestring import mark_safe
#from .models import Event
import calendar
from datetime import datetime, timedelta

def calendar_view(request, year=datetime.now().year, month=datetime.now().month):
   # events = Event.objects.filter(date__year=year, date__month=month)
    cal = calendar.HTMLCalendar().formatmonth(year, month)
    
   # for event in events:
   #     day = event.date.day
   #     cal = cal.replace(f'>{day}<', f'><a href="/event/{event.slug}/">{day}</a><')

    context = {
        'calendar': mark_safe(cal),
        'month': month,
        'year': year,
    }
    return render(request, 'home.html', context)