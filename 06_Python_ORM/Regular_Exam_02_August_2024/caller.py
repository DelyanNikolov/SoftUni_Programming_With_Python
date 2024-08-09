import os
import django
from django.db.models import Q, Count, F, Avg, Subquery

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Mission, Spacecraft


# Create queries within functions
def get_astronauts(search_string=None) -> str:
    if search_string is None:
        return ""

    astronauts = Astronaut.objects.filter(
        Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    ).order_by('name')

    result = []
    for a in astronauts:
        status = "Active" if a.is_active else "Inactive"
        result.append(f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {status}")

    return "\n".join(result)


def get_top_astronaut() -> str:
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()
    if not top_astronaut or top_astronaut.missions_count == 0:
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.missions_count} missions."


def get_top_commander() -> str:
    top_commander = Astronaut.objects.annotate(
        num_of_missions=Count('mission_commander')
    ).order_by('-num_of_missions', 'phone_number').first()

    if not top_commander or top_commander.num_of_missions == 0:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.num_of_missions} commanded missions."


def get_last_completed_mission() -> str:
    last_completed_mission = (Mission.objects.select_related(
        'spacecraft', 'commander'
    ).prefetch_related(
        'astronauts'
    ).order_by(
        '-launch_date'
    ).filter(status='Completed').first())

    if not last_completed_mission:
        return "No data."

    commander_name = "TBA" if last_completed_mission.commander is None else last_completed_mission.commander.name
    astronauts_names = ', '.join(a.name for a in last_completed_mission.astronauts.all().order_by('name'))
    total_spacewalks = sum(a.spacewalks for a in last_completed_mission.astronauts.all())

    return (f"The last completed mission is: {last_completed_mission.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {astronauts_names}. Spacecraft: {last_completed_mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft() -> str:
    most_used_spacecraft = Spacecraft.objects.annotate(
        num_missions=Count('mission')
    ).order_by('-num_missions', 'name').first()

    unique_astronauts = Astronaut.objects.filter(
        mission_astronauts__spacecraft=most_used_spacecraft
    ).distinct().count()

    if not most_used_spacecraft or most_used_spacecraft.num_missions == 0:
        return "No data."

    return (f"The most used spacecraft is: {most_used_spacecraft.name},"
            f" manufactured by {most_used_spacecraft.manufacturer}, used in {most_used_spacecraft.num_missions} "
            f"missions, astronauts on missions: {unique_astronauts}.")


def decrease_spacecrafts_weight() -> str:

    spacecrafts_to_update = Spacecraft.objects.prefetch_related(
        "mission_set"
    ).filter(
        mission__status="Planned",
        weight__gte=200.0
    ).distinct()

    num_of_spacecrafts_affected = spacecrafts_to_update.count()

    if num_of_spacecrafts_affected == 0:
        return "No changes in weight."

    spacecrafts_to_update.update(weight=F('weight') - 200.0)

    avg_weight = Spacecraft.objects.all().aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (f"The weight of {num_of_spacecrafts_affected} "
            f"spacecrafts has been decreased. The new average weight of all spacecrafts is {avg_weight:.1f}kg")

