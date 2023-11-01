import csv
import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# Create a table to store the CSV data with 39 columns
c.execute('''CREATE TABLE IF NOT EXISTS Game
             (AppID TEXT, Name TEXT, Release_date TEXT, Estimated_owners TEXT, Peak_CCU TEXT, 
          Required_age TEXT, Price TEXT, DLC_count TEXT, About_the_game TEXT, Supported_languages TEXT,
           Full_audio_languages TEXT, Reviews TEXT, Header_image TEXT, Website TEXT, Support_url TEXT, 
          Support_email TEXT, Windows TEXT, Mac TEXT, Linux TEXT, Metacritic_score TEXT, Metacritic_url TEXT,
           User_score TEXT, Positive TEXT, Negative TEXT, Score_rank TEXT, Achievements TEXT, 
          Recommendations TEXT, Notes TEXT, Average_playtime_forever TEXT, Average_playtime_two_weeks TEXT, 
          Median_playtime_forever TEXT, Median_playtime_two_weeks TEXT, Developers TEXT, Publishers TEXT, 
          Categories TEXT, Genres TEXT, Tags TEXT, Screenshots TEXT, Movies TEXT)''')

# Read the CSV file and insert its data into the database
with open('games.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row if it exists
    for row in reader:
        c.execute("INSERT INTO Game VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)

print("Imported CSV data into database")

conn.commit()
conn.close()

