import requests
from django.core.management.base import BaseCommand
from calendar_event_app.models import Events, Tag
from decouple import config
from django.views.decorators.debug import sensitive_variables

API_URL = "https://rekrutacja.teamwsuws.pl/events"
DETAIL_API_URL = "https://rekrutacja.teamwsuws.pl/events/{id}"
API_KEY = config('API_KEY')
headers = {
     'api-key': API_KEY 
}

#__init__.py files in this and the previous folder are necessary to make sure that Python treats the directories as packages
class Command(BaseCommand):
    help = 'Fetch data from the external API and populate the database'

    def handle(self, *args, **kwargs):
        # First API call to get the list of events
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            events_data = response.json()

            for event_data in events_data:
                event_id = event_data['id']
        
                # Make the second API call to get detailed information for each event
                detailed_response = requests.get(DETAIL_API_URL.format(id=event_id), headers=headers)
                if detailed_response.status_code == 200:
                    detailed_event_data = detailed_response.json()

                    # Create or update the Event instance
                    event, created = Events.objects.update_or_create(
                        id=event_id,  # Use the ID from the API
                        defaults={
                            'name': event_data['name'],
                            'start_time': event_data['start_time'],
                            'duration': event_data['duration'],
                            'image_url': event_data['image_url'],
                            'short_description': event_data['short_description'],
                            'location': detailed_event_data.get('location', ''),  # From second API
                            'registration_link': detailed_event_data.get('registration_link', ''),  # From second API
                            'long_description': detailed_event_data.get('long_description', ''),  # From second API
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Created event: {event.name}"))
                    else:
                        self.stdout.write(self.style.SUCCESS(f"Updated event: {event.name}"))

                    # Now that the event is saved, handle the tags
                    event.tags.clear()  # Clear existing tags
                    for tag_data in event_data.get('tags', []):
                        tag_name = tag_data['name']
                        tag, _ = Tag.objects.get_or_create(name=tag_name)
                        event.tags.add(tag)

                    event.save()  # Save the event after adding tags

            self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from the API'))