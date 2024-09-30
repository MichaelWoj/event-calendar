# Event Calendar

An event calendar that takes events from an API and displays them and their relevant information on a calendar 

## Requirements
Make sure you have Python 3.8 or newer install

## Step by step guide

1. Download the project manually through GitHub or running the command 
```git clone https://github.com/MichaelWoj/event-calendar.git``` and enter it by ```cd event-calendar``` or under whatever path you placed it at. 

2. To make sure you have all the neccesarry libraries installed run the following command  
```pip install -r requirements.txt ```

3. Create a file name ".env" (without the quotes) in calendar_event_app. In that file write 
```API_KEY = your_api_key```

4. While in the "calendar_event_project" run the 
```python manage.py fetch_events```
 command to get the events from the API 

5. Run the application with the "python manage.py runserver" command.
