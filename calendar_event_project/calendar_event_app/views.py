from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Events
from django.http import JsonResponse
import calendar
from datetime import datetime

def calendar_view(request, year=datetime.now().year, month=datetime.now().month):
    events = Events.objects.filter(start_time__year=year, start_time__month=month)
    cal = calendar.HTMLCalendar().formatmonth(year, month)

    events_by_day = {}
    for event in events:
        day = event.start_time.day
        if day not in events_by_day:
            events_by_day[day] = []
        events_by_day[day].append(event)

    for day, events_list in events_by_day.items():
        event_bubbles = ''.join(
            [f"<div class='event-bubble' data-event-id='{event.id}'>{event.name}</div>" for event in events_list]
        )
        day_html = f"<a href='#'>{day}</a>{event_bubbles}"
        cal = cal.replace(f'>{day}<', f'>{day_html}<')

    context = {
        'calendar': mark_safe(cal),
        'month': month,
        'year': year,
    }
    return render(request, 'calendar.html', context)

def event_detail_view(request, event_id):
    try:
        event = Events.objects.get(id=event_id)
        event_data = {
            'name': event.name,
            'location': event.location,
            'duration': event.duration,
            'long_description': event.long_description,
            'registration_link': event.registration_link,
        }
        return JsonResponse(event_data)
    except Events.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)
