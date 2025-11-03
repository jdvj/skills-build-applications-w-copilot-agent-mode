from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Equipos
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Usuarios
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        wonderwoman = User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', is_superhero=True)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='Marvel', is_superhero=True)

        # Actividades
        Activity.objects.create(user='Iron Man', type='Run', duration=30, date='2025-11-01')
        Activity.objects.create(user='Batman', type='Swim', duration=45, date='2025-11-02')
        Activity.objects.create(user='Wonder Woman', type='Bike', duration=60, date='2025-11-03')
        Activity.objects.create(user='Spider-Man', type='Climb', duration=20, date='2025-11-04')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=150)
        Leaderboard.objects.create(team='DC', points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='Sprints', description='Run 5x100m sprints', difficulty='Medium')
        Workout.objects.create(name='Deadlift', description='Deadlift 100kg', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
