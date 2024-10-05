from django.db import models
from django.db.models import QuerySet, Count


class TennisPlayerManager(models.Manager):
    def get_tennis_players_by_wins_count(self) -> QuerySet:
        players = self.annotate(wins_count=Count('winner_match')).order_by('-wins_count', 'full_name')

        return players

