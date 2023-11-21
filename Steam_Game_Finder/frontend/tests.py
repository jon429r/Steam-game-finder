from django.test import TestCase
from django.urls import reverse
from .models import Game, Language, Developer, Publisher

class GameModelTests(TestCase):
    def test_create_game(self):
        # Create a sample Game instance for testing
        game = Game.objects.create(
            app_id=1,
            name='Test Game',
            release_date='2023-01-01',
            required_age=18,
            price=29.99,
            about_the_game='This is a test game.',
            supported_languages='English, Spanish',
            header_image='https://example.com/header_image.jpg',
            windows=True,
            mac=False,
            linux=True,
            metacritic_score=80,
            positive=100,
            negative=10,
            categories='Action, Adventure',
            genres='Shooter, RPG',
            tags='test, indie'
        )

        # Retrieve the created Game instance from the database
        test_game = Game.objects.get(app_id=1)

        # Check if the values match what we set
        self.assertEqual(test_game.name, 'Test Game')
        self.assertEqual(test_game.release_date, '2023-01-01')
        self.assertEqual(test_game.required_age, 18)
        self.assertEqual(test_game.price, 29.99)
        # Add more assertions for other fields

        # Check if the boolean fields are set correctly
        self.assertTrue(test_game.windows)
        self.assertFalse(test_game.mac)
        self.assertTrue(test_game.linux)

        # Check if the many-to-many fields are set correctly
        self.assertEqual(test_game.categories, 'Action, Adventure')
        self.assertEqual(test_game.genres, 'Shooter, RPG')
        self.assertEqual(test_game.tags, 'test, indie')

        
class Language_model_test(TestCase):
    def test_create_language(self):
        # Create a sample Language instance for testing
        language = Language.objects.create(
            app_id=1,
            language='English'
        )

        # Retrieve the created Language instance from the database
        test_language = Language.objects.get(app_id=1)

        # Check if the values match what we set
        self.assertEqual(test_language.language, 'English')
    
class Developer_model_test(TestCase):
    def test_create_developer(self):
        # Create a sample Developer instance for testing
        developer = Developer.objects.create(
            app_id=1,
            developer='Test Developer'
        )

        # Retrieve the created Developer instance from the database
        test_developer = Developer.objects.get(app_id=1)

        # Check if the values match what we set
        self.assertEqual(test_developer.developer, 'Test Developer')

class Publisher_model_test(TestCase):
    def test_create_publisher(self):
        # Create a sample Publisher instance for testing
        publisher = Publisher.objects.create(
            app_id=1,
            publisher='Test Publisher'
        )

        # Retrieve the created Publisher instance from the database
        test_publisher = Publisher.objects.get(app_id=1)

        # Check if the values match what we set
        self.assertEqual(test_publisher.publisher, 'Test Publisher')

class HomePageViewTests(TestCase):
    def test_home_page_view(self):
        # Issue a GET request to the homepage
        response = self.client.get('/Home_Page/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)


class QuizPageViewTests(TestCase):
    def test_quiz_page_view(self):
        # Issue a GET request to the homepage
        response = self.client.get('/Quiz_Page/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

class SearchPageViewTests(TestCase):
    def test_search_page_view(self):
        # Issue a GET request to the homepage
        response = self.client.get('/Search_Page/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

class DisplayGamesViewTests(TestCase):
    def test_display_games_view(self):
        # Issue a GET request to the homepage
        response = self.client.get('/display_games/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

class DisplayPopularGamesViewTests(TestCase):
    def test_display_popular_games_view(self):
        # Issue a GET request to the homepage
        response = self.client.get('/display_popular_games/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

class TestTemplates(TestCase):
    def test_home_page_template(self):
        # Issue a GET request to the homepage
        response = self.client.get('/Home_Page/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the correct template was used
        self.assertTemplateUsed(response, 'Home_Page.html')

    def test_quiz_page_template(self):
        # Issue a GET request to the homepage
        response = self.client.get('/Quiz_Page/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the correct template was used
        self.assertTemplateUsed(response, 'Quiz_Page.html')

    def test_search_page_template(self):
        # Issue a GET request to the homepage
        response = self.client.get('/Search_Page/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the correct template was used
        self.assertTemplateUsed(response, 'Search_Page.html')

    def test_display_games_template(self):
        # Issue a GET request to the homepage
        response = self.client.get('/display_games/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the correct template was used
        self.assertTemplateUsed(response, 'display_games.html')

    def test_display_popular_games_template(self):
        # Issue a GET request to the homepage
        response = self.client.get('/display_popular_games/')

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the correct template was used
        self.assertTemplateUsed(response, 'display_popular_games.html')

class Table_Tests(TestCase):
    def test_display_resulting_games(self):
        response = self.client.get(reverse('display_resulting_games'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Elder Scrolls V: Skyrim')
        self.assertContains(response, 'Game 2')

    def test_display_popular_games(self):
        response = self.client.get(reverse('display_popular_games'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Popular Game 1')
        self.assertContains(response, 'Popular Game 2')