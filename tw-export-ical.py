import os
import datetime
import icalendar
import tasklib

tw = tasklib.TaskWarrior()
tasks = tw.tasks.filter('due.not:')

def export_to_ical(task):
    calendar = icalendar.Calendar()
    calendar.add('prodid', '-//Taskwarrior exporter//Version 1//EN')
    calendar.add('version', '2.0')
    
    event = icalendar.Event()
    event['summary'] = task['description']
    event.add('dtstart', task['due'])
    event.add('dtend', task['due']+datetime.timedelta(seconds=1))
    event.add('dtstamp', task['entry'])
    event.add('uid', task['uuid'].upper())
    
    calendar.add_component(event)
    
    filename = '~/.calendars/tw/{0}.ics'.format(event['uid'])
    with open(os.path.expanduser(filename), 'w') as f:
        f.write(calendar.to_ical())

for task in tasks:
    export_to_ical(task)

