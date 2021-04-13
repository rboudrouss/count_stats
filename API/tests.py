from django.test import TestCase
from datetime import datetime

from .models import UserData, MessageData

# Create your tests here.


class ModelTesting(TestCase):
    def setUp(self):
        self.user = UserData.objects.create(
            user_id="1",
            avatar_url="https://rboud.ml/img/rboud-01.png",
            name="rboud",
            discriminator="1207",
            ghost=False,
            nb_msg=1,
            top=1
        )
        self.message = MessageData.objects.create(
            message_id="1",
            author_id="1",
            content="fromage",
            date=datetime.fromisoformat("2021-04-13T21:55:08.532862")
        )

    def test_post_model(self):
        self.assertTrue(isinstance(self.user, UserData))
        self.assertTrue(isinstance(self.message, MessageData))

    def test_repr_model(self):
        self.assertEqual(repr(self.user), "<User rboud#1207>")
        self.assertEqual(repr(self.message),
                         "<Message id=1 date=2021-04-13 21:55:08.532862>")
