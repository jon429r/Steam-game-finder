# Steam Game Finder

## Prepare to Run the App

1. **Install Dependencies:**
   - Run `pip install -r requirements.txt` to install our Python packages.

2. **Configure MySQL Database:**
   - Create a MySQL database named "databasefinder" with the password "Database-final1234".
   - See the Django DB connector in `Steam_Game_Finder/settings.py' to make sure info lines up (see line 75).
   - If you have a specific root password, enter it in `settings.py` (see around line 75).

3. **Apply Django Migrations:**
   - Navigate to `database-final/Steam_Game_Finder` in your terminal.
   - Run migrations with `python manage.py makemigrations` and `python manage.py migrate`.
   - These are Django specefic commands neccesary for some of our data objects

4. **Import CSV Data to Build the DB:**
   - Move the provided `games.csv` into the root project directory.
   - We could not provide it ourselves due to GitHub file size limits
   - Import data with `python manage.py import_csv` (ensure you are in the correct directory).

5. **Initialize Procedures:**
   - Run `python manage.py initialize_procedures` to set up procedures for MySQL.

## Run the App

Start our Django server by running:

`python manage.py runserver`

Then visit http://127.0.0.1:8000/ in your browser to access our frontend.

## Screen Shots

<img width="1310" alt="Screenshot 2023-12-29 at 3 57 52 PM" src="https://github.com/jon429r/Steam-game-finder/assets/103213920/3b130935-7b89-43b9-b658-233ebcd94b09">



<img width="1301" alt="Screenshot 2023-12-29 at 3 59 03 PM" src="https://github.com/jon429r/Steam-game-finder/assets/103213920/ef24cff4-1e2b-4286-9154-efa9e1cc31ee">
