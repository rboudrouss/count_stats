
from django.test import TestCase
from .helpers import *
from .treatment import *


class HelpersTests(TestCase):
    def setUp(self):
        self.date = datetime(2002, 7, 12, 6, 45, 20)
        self.listdate: DateList = [2002, 7, 12, 6, 45, 20]
        self.message: MessageData = {
            "message_id": 2,
            "author_id" : 12,
            "content"   : "Yes",
            "date"      : self.listdate
        }

    def test_date_from_msg(self):
        self.assertEqual(
            self.date,
            date_from_msg(self.message)
        )
    
    def test_str_from_date(self):
        self.assertEqual(
            "12-7",
            str_from_date(self.date, False, False)
        )
        self.assertEqual(
            "12-7-6",
            str_from_date(self.date, True, False)
        )
        self.assertEqual(
            "12-7-6-45",
            str_from_date(self.date)
        )
    

class TreatmentTests(TestCase):
    def setUp():
        self.history: List[MessageData]=[
            {
                "message_id":1,
                "author_id" :1;
                "content"   :"Yes",
                "date":
            },
            {

            },
            {

            }
        ]