from django.core.management.base import BaseCommand
from frontend.models import Liked_Disliked  

##Function to populate Liked_Disliked model with initial data
class Command(BaseCommand):
    help = 'Populate Liked_Disliked model with initial data'

    def handle(self, *args, **kwargs):
        Liked_Disliked_Data = [
            {'appid': '1', 'title': 'LikedGame 1', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'},
            {'appid': '2', 'title': 'LikedGame 2', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'},
            {'appid': '3', 'title': 'LikedGame 3', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'},
            {'appid': '4', 'title': 'LikedGame 4', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'},
            {'appid': '5', 'title': 'LikedGame 5', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Like'}, 
            {'appid': '6', 'title': 'dislikedGame 1', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
            {'appid': '7', 'title': 'dislikedGame 2', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
            {'appid': '8', 'title': 'dislikedGame 3', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
            {'appid': '9', 'title': 'dislikedGame 4', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
            {'appid': '10', 'title': 'dislikedGame 5', 'IMG': 'https://cdn.akamai.steamstatic.com/steam/apps/655370/header.jpg?t=1617500526', 'action': 'Dislike'},
        ]

        for data in Liked_Disliked_Data:
            Liked_Disliked.objects.create(
                app_id=data['appid'],
                title=data['title'],
                header_image=data['IMG'],
                action=data['action']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Liked_Disliked model.'))