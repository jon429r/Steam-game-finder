from django.core.management.base import BaseCommand
from frontend.models import Popular_Games

##Function to populate Liked_Disliked model with initial data
class Command(BaseCommand):
    help = 'Populate popular games model with initial data'

    def handle(self, *args, **kwargs):
        Resulting_Games_data = [
            {'appid': '1', 'title': 'popular game 1', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'},
            {'appid': '2', 'title': 'popular game 2', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'},
            {'appid': '3', 'title': 'popular game 3', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'},
            {'appid': '4', 'title': 'popular game 4', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'},
            {'appid': '5', 'title': 'popular game 5', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'}, 
            {'appid': '6', 'title': 'popular game 6', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
            {'appid': '7', 'title': 'popular game 7', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
            {'appid': '8', 'title': 'popular game 8', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
            {'appid': '9', 'title': 'popular game 9', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
            {'appid': '10', 'title': 'popular game 10', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
        ]

        for data in Resulting_Games_data:
            Popular_Games.objects.create(
                app_id=data['appid'],
                title=data['title'],
                header_image=data['IMG'],
                action=data['action']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Liked_Disliked model.'))