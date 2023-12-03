import json
from django.db import connection

config_file = "connectorConfig.json"


class LoadSearchProcedures:
    cursor = connection.cursor()

    @staticmethod
    def create_game_title_search_procedure():
        procedure_query = """
            CREATE PROCEDURE game_title_search(IN Title varchar(30))
            READS SQL DATA
            BEGIN
                -- SQLite
                -- Basic fuzzy title search
                SELECT AppID, Name
                FROM Game 
                WHERE Name LIKE CONCAT('%', Title, '%')
                ORDER BY Name;
            END;
        """
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Title Procedure created.")

    @staticmethod
    def create_language_search_procedure():
        procedure_query = """
            CREATE PROCEDURE language_search(IN Language varchar(30))
            READS SQL DATA
            BEGIN
                -- SQLite
                -- find games with support for given language
                SELECT g.AppID, Name, (Positive * 1.0)/(Positive + Negative) as Reception
                FROM Game g INNER JOIN GameLanguages l ON g.AppID = l.AppID
                WHERE l.language = Language
                ORDER BY Reception DESC;
            END;
            """
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Language Procedure created.")

    @staticmethod
    def create_devoloper_search_procedure():
        procedure_query = """
            CREATE PROCEDURE games_by_devoloper_search(IN Devoloper varchar(30))
            READS SQL DATA
            BEGIN
                -- SQLite
                -- find games by given developer
                SELECT g.AppID, Name, Release_date
                FROM Game g INNER JOIN GameDeveloper d ON g.AppID = d.AppID
                WHERE d.developer LIKE CONCAT('%', Devoloper, '%')
                ORDER BY Release_date DESC;
            END;
            """
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Developer Procedure created")

    @staticmethod
    def create_publisher_search_procedure():
        procedure_query = """
            CREATE PROCEDURE games_by_publisher_search(IN Publisher varchar(30))
            READS SQL DATA
            BEGIN
                -- SQLite
                -- find games from given publisher
                SELECT g.AppID, Name, Release_date
                FROM Game g INNER JOIN GamePublisher p ON g.AppID = p.AppID
                WHERE p.publisher LIKE CONCAT('%', Publisher, '%')
                ORDER BY Release_date DESC;
            END;
            """
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Publisher Procedure created")

    @staticmethod
    def create_reception_search_procedure():
        procedure_query = """
            CREATE PROCEDURE reception_search(IN User_Rating REAL)
            READS SQL DATA
            BEGIN
                -- SQLite
                -- find games above a given user rating
                SELECT AppID, Name, (Positive * 1.0)/(Positive + Negative) as Reception
                FROM Game
                WHERE Reception > User_Rating and Reception < 1;
            END;
            """
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Reception Procedure created")

    @staticmethod
    def create_age_rating_search_procedure():
        procedure_query = """
            CREATE PROCEDURE age_rating_search(IN User_Age REAL)
            READS SQL DATA
            BEGIN
                -- SQLite
                -- select games within an age rating
                SELECT *
                FROM Game
                WHERE Required_age >= 0 AND Required_age < User_Age;
            END;
            """
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Age Rating Procedure Created")

    @staticmethod
    def create_devolopers_by_reception_search_procedure():
        procedure_query = """
            CREATE PROCEDURE devolopers_by_reception()
            READS SQL DATA
            BEGIN
                -- SQLite
                -- list developers ranked by the average reception of their games
                SELECT Developer, round(avg(Reception), 4) as Dev_Reception, count(*) as Num_Games
                FROM GameDeveloper d INNER JOIN (
                SELECT AppID, (Positive * 1.0)/(Positive + Negative) as Reception
                FROM Game
                -- exclude non-game items
                WHERE AppID NOT IN (
                    SELECT AppID
                    FROM GameTag
                    WHERE tag = "Software"
                )
                ) g on d.AppID = g.AppID
                GROUP BY Developer
                HAVING Num_Games > 3 AND Dev_Reception < .9  -- minimum number of games developed and bound on reception
                ORDER BY Dev_Reception DESC, Num_Games DESC;
            END;
            """
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Developer by reception search created")
        
    @staticmethod
    def genre_search(genres_string):
        genres = genres_string.strip().split(" ")
        undesired_genres = tuple([s[1:] for s in genres if s.startswith('-')]) #TODO: fix for singletons
        desired_genres = tuple([s for s in genres if not s.startswith('-')])
        print(desired_genres)
        print(undesired_genres)
        query = f"""
            SELECT g.AppID, Name, (Positive * 1.0)/(Positive + Negative) as Reception
            FROM (SELECT AppID
                FROM Gamegenre
                WHERE genre IN {desired_genres}  -- desired genres
                AND AppID NOT IN (
                SELECT AppID
                FROM GameGenre
                WHERE genre IN {undesired_genres})   -- excluded genres
                ) Gen INNER JOIN Game g on Gen.AppID = g.AppID
            GROUP BY g.AppID
            HAVING count(g.AppID) > {int(len(genres) * .2)}
            ORDER BY count(g.AppID) DESC, Reception DESC"""
        print(query)
        LoadSearchProcedures.cursor.execute(query)
        return dictfetchall(LoadSearchProcedures.cursor)
        
    def tag_search(tags_string):
        tags = tags_string.strip.split(" ")
        undesired_tags = (s[1:] for s in tags if s.startswith('-'))
        desired_tags = (s for s in tags if not s.startswith('-'))
        query = f"""
            SELECT g.AppID, Name, (Positive * 1.0)/(Positive + Negative) as Reception
            FROM (SELECT AppID
                FROM Gametag
                WHERE tag IN {desired_tags}  -- desired tags
                AND AppID NOT IN (
                SELECT AppID
                FROM Gametag
                WHERE tag IN {undesired_tags})   -- excluded tags
                ) Gen INNER JOIN Game g on Gen.AppID = g.AppID
            GROUP BY g.AppID
            HAVING count(g.AppID) > {int(tags.len() * .2)}  -- limit to more relevant titles
            ORDER BY count(g.AppID) DESC, Reception DESC"""
        LoadSearchProcedures.cursor.execute(query)
        return dictfetchall(LoadSearchProcedures.cursor)
        
    def category_search(cats_string):
        cats = cats_string.strip.split(" ")
        undesired_cats = (s[1:] for s in cats if s.startswith('-'))
        desired_cats = (s for s in cats if not s.startswith('-'))
        query = f"""
            SELECT g.AppID, Name, (Positive * 1.0)/(Positive + Negative) as Reception
            FROM (SELECT AppID
                FROM Gamecategory
                WHERE category IN {desired_cats}  -- desired categorys
                AND AppID NOT IN (
                SELECT AppID
                FROM Gamecategory
                WHERE category IN {undesired_cats})   -- excluded categorys
                ) Gen INNER JOIN Game g on Gen.AppID = g.AppID
            GROUP BY g.AppID
            HAVING count(g.AppID) > 2  -- limit to more relevant titles
            ORDER BY count(g.AppID) DESC, Reception DESC;"""
        LoadSearchProcedures.cursor.execute(query)
        return dictfetchall(LoadSearchProcedures.cursor)

    def recomendation_search(req_string):
        reqs = tuple(req_string.strip.split(" "))
        query = f"""SELECT G.AppID, G.Name, G.About_the_game, (G.Positive - G.Negative) as Reception
            FROM (SELECT GT.AppID, GT.tag
                FROM GameTag GT
                WHERE GT.tag IN   -- desired tags
            ) AS GT JOIN (SELECT GG.AppID, GG.genre
                FROM GameGenre GG
                WHERE GG.genre IN {reqs}  -- desired genres
            ) AS GG ON GG.AppID = GT.AppID JOIN (SELECT GC.AppID, GC.category
                FROM GameCategory GC
                WHERE GC.category IN {reqs}  -- desired categories
            ) AS Gen ON Gen.AppID = GG.AppID
            NATURAL JOIN Game as G
            GROUP BY G.AppID
            HAVING COUNT(G.AppID) > 3
            ORDER BY COUNT(G.AppID) DESC, Reception DESC;"""
        LoadSearchProcedures.cursor.execute(query)
        return dictfetchall(LoadSearchProcedures.cursor)
    
    @staticmethod
    def game_title_search(title):
        query = """CALL game_title_search(%s);"""
        LoadSearchProcedures.cursor.execute(query, (title,))
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def language_search(lang):
        query = """CALL language_search(%s);"""
        LoadSearchProcedures.cursor.execute(query, params=lang)
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def games_by_developer_search(dev):
        query = """CALL  games_by_devoloper_search(%s);"""
        LoadSearchProcedures.cursor.execute(query, params=dev)
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def games_by_publisher_search(pub):
        query = """CALL games_by_publisher_search(%s);"""
        LoadSearchProcedures.cursor.execute(query, params=pub)
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def reception_search(recep):
        query = """CALL reception_search(%s);"""
        LoadSearchProcedures.cursor.execute(query, params=recep)
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def age_rating_search(age):
        query = """CALL  age_rating_search(%s);"""
        LoadSearchProcedures.cursor.execute(query, params=age)
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def devolopers_by_reception_search(search_parameter):
        query = """CALL devolopers_by_reception();"""
        LoadSearchProcedures.cursor.execute(query)
        return dictfetchall(LoadSearchProcedures.cursor)


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

