import csv
import json
import os
from datetime import datetime

import pymysql
import pymysql.cursors

config_file = "connectorConfig.json"
with open(config_file, 'r', encoding="utf-8") as f:
    config = json.load(f)

con = pymysql.connect(**config["MySQL"])
cur = con.cursor()

games_table_description = """CREATE TABLE IF NOT EXISTS Game(
        AppID INTEGER PRIMARY KEY,
        Name TEXT,
        Release_date TEXT,
        Required_age INTEGER,
        Price REAL,
        About_the_game TEXT,
        Metacritic_score INTEGER,
        Positive INTEGER,
        Negative INTEGER,
        Header_image TEXT
    );"""

genre_table_description = """CREATE TABLE IF NOT EXISTS GameGenre(
        AppID INTEGER,
        genre TEXT
    );"""

tag_table_description = """CREATE TABLE IF NOT EXISTS GameTag(
        AppID INTEGER,
        tag TEXT
    );"""

cat_table_description = """CREATE TABLE IF NOT EXISTS GameCategory(
        AppID INTEGER,
        category TEXT
    );"""

dev_table_description = """CREATE TABLE IF NOT EXISTS GameDeveloper(
        AppID INTEGER,
        developer TEXT
    );"""

pub_table_description = """CREATE TABLE IF NOT EXISTS GamePublisher(
        AppID INTEGER,
        Publisher TEXT
    );"""

lang_table_description = """CREATE TABLE IF NOT EXISTS GameLanguages(
        AppID INTEGER,
        language TEXT
    );"""

plat_table_description = """CREATE TABLE IF NOT EXISTS GamePlatform(
        AppID INTEGER,
        Windows INTEGER,
        MAC INTEGER,
        Linux INTEGER
    );"""

table_descriptors = [
    games_table_description,
    genre_table_description,
    tag_table_description,
    cat_table_description,
    dev_table_description,
    pub_table_description,
    lang_table_description,
    plat_table_description,
]


def main():
    create_tables(*table_descriptors)
    insert_table("games.csv")
    con.commit()
    cur.close()


def create_tables(*descriptors):
    for table in descriptors:
        cur.execute(table)


def insert_table(file_path):
    dic_tuples_game = {}
    dic_tuples_genres = {}
    dic_tuples_tags = {}
    dic_tuples_cats = {}
    dic_tuples_devs = {}
    dic_tuples_pubs = {}
    dic_tuples_langs = {}
    dic_tuples_platform = {}

    (
        dic_tuples_game,
        dic_tuples_genres,
        dic_tuples_tags,
        dic_tuples_cats,
        dic_tuples_devs,
        dic_tuples_pubs,
        dic_tuples_langs,
        dic_tuples_platform,
    ) = read_csv(
        file_path,
        dic_tuples_game,
        dic_tuples_genres,
        dic_tuples_tags,
        dic_tuples_cats,
        dic_tuples_devs,
        dic_tuples_pubs,
        dic_tuples_langs,
        dic_tuples_platform,
    )

    for game_id in dic_tuples_game:
        cur.execute(f"INSERT INTO Game VALUES {dic_tuples_game[game_id]}")

        for genre_tuple in dic_tuples_genres[game_id]:
            cur.execute(f"INSERT INTO GameGenre VALUES {genre_tuple}")

        for tag_tuple in dic_tuples_tags[game_id]:
            cur.execute(f"INSERT INTO GameTag VALUES {tag_tuple}")

        for cat_tuple in dic_tuples_cats[game_id]:
            cur.execute(f"INSERT INTO GameCategory VALUES {cat_tuple}")

        for dev_tuple in dic_tuples_devs[game_id]:
            cur.execute(f"INSERT INTO GameDeveloper VALUES {dev_tuple}")

        for pub_tuple in dic_tuples_pubs[game_id]:
            cur.execute(f"INSERT INTO GamePublisher VALUES {pub_tuple}")

        for lang_tuple in dic_tuples_langs[game_id]:
            cur.execute(f"INSERT INTO GameLanguages VALUES {lang_tuple}")

        cur.execute(f"INSERT INTO GamePlatform VALUES {dic_tuples_platform[game_id]}")


def read_csv(
    file_path,
    dic_tuples_game,
    dic_tuples_genres,
    dic_tuples_tags,
    dic_tuples_cats,
    dic_tuples_devs,
    dic_tuples_pubs,
    dic_tuples_langs,
    dic_tuples_platform,
):
    with open(file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')
        next(csv_reader)

        for row in csv_reader:
            app_id = row[0]
            name = row[1]
            # convert dates to ISO8601 strings
            release_date = process_realse_date(row[2])
            req_age = row[5]
            price = row[6]
            game_desc = row[8]
            img_link = row[12]
            mete_score = row[19]
            pos_score = row[22]
            neg_score = row[23]

            categories = process_string_list(row[34])
            genres = process_string_list(row[35])
            tags = process_string_list(row[36])
            developers = process_string_list(row[32])
            publishers = process_string_list(row[33])
            supported_langs = process_langs(row[9])
            platforms = (1 if s == "TRUE" else 0 for s in (row[16], row[17], row[18]))  # windows, mac, linux bools

            dic_tuples_game[app_id] = (
                app_id,
                name,
                release_date,
                req_age,
                price,
                game_desc,
                mete_score,
                pos_score,
                neg_score,
                img_link,
            )

            dic_tuples_genres[app_id] = [(app_id, g) for g in genres]
            dic_tuples_tags[app_id] = [(app_id, t) for t in tags]
            dic_tuples_cats[app_id] = [(app_id, c) for c in categories]
            dic_tuples_devs[app_id] = [(app_id, d) for d in developers]
            dic_tuples_pubs[app_id] = [(app_id, p) for p in publishers]
            dic_tuples_langs[app_id] = [(app_id, l) for l in supported_langs]
            dic_tuples_platform[app_id] = (app_id, *platforms)

    return (
        dic_tuples_game,
        dic_tuples_genres,
        dic_tuples_tags,
        dic_tuples_cats,
        dic_tuples_devs,
        dic_tuples_pubs,
        dic_tuples_langs,
        dic_tuples_platform,
    )


def process_realse_date(release_date) -> str:
    try:
        return datetime.strptime(release_date, "%b %d, %Y").strftime("%Y-%m-%d")
    except ValueError:
        return datetime.strptime(release_date, "%b %Y").strftime("%Y-%m")


def process_string_list(genre_string):
    return genre_string.split(",")


def process_langs(genre_string):
    return genre_string[2:-2].split("', '")


if __name__ == "__main__":
    main()
