from odoo.addons.google_account.models.google_service import TIMEOUT
from odoo.addons.google_calendar.utils.google_calendar import GoogleCalendarService

_original_get_events = GoogleCalendarService.get_events


def new_get_events(self, sync_token=None, token=None, timeout=TIMEOUT):
    # add
    # custom
    # logic
    # here
    return _original_get_events(self, sync_token=sync_token, token=token, timeout=timeout)

def post_load_hook():
    GoogleCalendarService.get_events = new_get_events
