import os
import django
from django.db.models import Q, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import TennisPlayer, Tournament, Match


# Create queries within functions

def get_tennis_players(search_name=None, search_country=None) -> str:
    if search_name is None and search_country is None:
        return ""

    if search_name is not None and search_country is not None:
        query = Q(Q(full_name__icontains=search_name) & Q(country__icontains=search_country))

    elif search_name is not None:
        query = Q(full_name__icontains=search_name)

    else:
        query = Q(country__icontains=search_country)

    tennis_players = TennisPlayer.objects.filter(query).order_by('ranking')

    if not tennis_players.exists():
        return ""

    result = []
    for tp in tennis_players:
        result.append(f"Tennis Player: {tp.full_name}, country: {tp.country}, ranking: {tp.ranking}")

    return "\n".join(result)


def get_top_tennis_player() -> str:
    top_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()
    if top_player is None:
        return ""

    return f"Top Tennis Player: {top_player.full_name} with {top_player.wins_count} wins."


def get_tennis_player_by_matches_count() -> str:
    player = TennisPlayer.objects.annotate(
        matches_count=Count('players_matches')
    ).order_by(
        '-matches_count', 'ranking'
    ).first()

    if player is None or player.matches_count == 0:
        return ""

    return f"Tennis Player: {player.full_name} with {player.matches_count} matches played."


def get_tournaments_by_surface_type(surface=None) -> str:
    if surface is None:
        return ""

    tournaments = Tournament.objects.prefetch_related('match_set').annotate(
        num_matches=Count('match')
    ).filter(
        surface_type__icontains=surface,
    ).order_by('-start_date')

    if not tournaments.exists():
        return ""

    result = []
    for t in tournaments:
        result.append(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}")

    return "\n".join(result)


def get_latest_match_info() -> str:
    last_match = Match.objects.select_related('tournament').prefetch_related('players').order_by('-date_played',
                                                                                                 '-id').first()

    if last_match is None:
        return ""

    winner = "TBA" if last_match.winner is None else last_match.winner.full_name
    players_names = ' vs '.join(p.full_name for p in last_match.players.all().order_by('full_name'))

    return (f"Latest match played on: {last_match.date_played}, "
            f"tournament: {last_match.tournament.name}, score: {last_match.score}, "
            f"players: {players_names}, "
            f"winner: {winner}, summary: {last_match.summary}")


def get_matches_by_tournament(tournament_name=None) -> str:
    if tournament_name is None:
        return "No matches found."

    tournament = Tournament.objects.filter(name__exact=tournament_name).first()

    if tournament is None:
        return "No matches found."

    matches = Match.objects.prefetch_related('players').select_related('winner').filter(tournament=tournament).order_by('-date_played')
    if not matches.exists():
        return "No matches found."

    result = []
    for m in matches:
        winner = "TBA" if m.winner is None else m.winner.full_name
        result.append(f"Match played on: {m.date_played}, score: {m.score}, winner: {winner}")

    return '\n'.join(result)
