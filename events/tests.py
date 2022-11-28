from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Event
from django.core.files.uploadedfile import SimpleUploadedFile


class EventModelTests(TestCase):

    def test_valid_creation(self):
        start_date = timezone.now() + datetime.timedelta(days=1)
        end_date = timezone.now() + datetime.timedelta(days=10)
        event = Event(name="Test event 1", start_date=start_date, end_date=end_date)

    def test_name_must_not_be_empty(self):
        start_date = timezone.now() + datetime.timedelta(days=1)
        end_date = timezone.now() + datetime.timedelta(days=10)
        self.assertRaises(Exception, Event, start_date=start_date, end_date=end_date)

    def test_end_date_after_start_date(self):
        start_date = timezone.now() + datetime.timedelta(days=1)
        end_date = timezone.now() - datetime.timedelta(days=10)
        self.assertRaises(Exception, Event, name="Test event 2", start_date=start_date, end_date=end_date)


class EventsViewTest(TestCase):
    num_events = 3

    @classmethod
    def setUpTestData(cls):
        # Create num_events events
        start_date = timezone.now() + datetime.timedelta(days=1)
        end_date = timezone.now() + datetime.timedelta(days=10)
        small_gif = (
            b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04"
            b"\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02"
            b"\x02\x4c\x01\x00\x3b"
        )
        for event_id in range(EventsViewTest.num_events):
            Event.objects.create(name=f"Event {event_id}", start_date=start_date, end_date=end_date,
                                 image=SimpleUploadedFile("small.gif", small_gif, content_type="image/gif"))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['events']), EventsViewTest.num_events)
