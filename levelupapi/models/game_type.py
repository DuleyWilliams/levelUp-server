from unittest.util import _MAX_LENGTH
from django.db import models


class GameType(models.Model):

    label = models.CharField(max_length=50)
