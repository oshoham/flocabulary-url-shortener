from __future__ import unicode_literals

from django.db import models
import string


CHARACTER_MAP = string.ascii_letters + string.digits


class Url(models.Model):
    url = models.URLField(unique=True)

    @property
    def short_id(self):
        _id = self.id
        digits = []
        base = len(CHARACTER_MAP)

        while _id:
            remainder = _id % base
            digits.append(remainder)
            _id /= base

        characters = map(lambda d: CHARACTER_MAP[d], reversed(digits))

        return ''.join(characters)

    @staticmethod
    def decode_short_id(short_id):
        return reduce(lambda _id, character: _id * len(CHARACTER_MAP) + CHARACTER_MAP.index(character), short_id, 0)
