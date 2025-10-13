import datetime
from typing import Dict
import logging

class Meeting_Calendar():
    def __init__(self, start_day: datetime.date, logger: logging.Logger):
        self.start_day = start_day
        self.logger = logger

    def Create_Calendar(self):
        self.calendar = {}

    def add_event (self, date : datetime, event_title: str, event_discription: str):
        if not isinstance(self.calendar[date.date()], Dict):
            self.calendar[date.date()] = {}
        if not isinstance(self.calendar[date.date()][date.time()], Dict):
            self.calendar[date.date()][date.time()] = {}
        self.calendar[date.date()][date.time()][event_title] = event_discription
        self.logger.log(f'Orchestrator ADDED event {event_title}')
    
    def alter_event (self, date: datetime, event_title: str, *reschedule_date: datetime):
        event_discription = self.calendar[date.date()][date.time()][event_title]
        self.calendar[date.date()][date.time()].pop(event_title)
        if reschedule_date:
            self.calendar[reschedule_date.date()][reschedule_date.time()][event_title] = event_discription
            self.logger.log(f'Orchestrator RESCHEDULED event {event_title}')
        else:
            self.logger.log(f'Orchestrator REMOVED event {event_title}')
    
    def get_event_for_day (self, date: datetime) -> Dict:
        return self.calendar[date.date()]
        
    