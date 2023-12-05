"""Functions for creating procedures, triggers, and facilitating queries."""
import json
from django.db import connection

config_file = "connectorConfig.json"


class LoadSearchProcedures:
    cursor = connection.cursor()

    @staticmethod
    def create_game_title_search_procedure():
        """creates a procedure for searching by game title."""
        drop_procedure = """DROP PROCEDURE IF EXISTS game_title_search;"""
        procedure_query = """
            CREATE PROCEDURE game_title_search(IN Title varchar(30))
            READS SQL DATA
            BEGIN
                -- Basic fuzzy title search
            	SELECT Game.AppID, Name, GROUP_CONCAT(DISTINCT Developer SEPARATOR ", ") as Developer,
                        GROUP_CONCAT(DISTINCT Publisher SEPARATOR ", ") as Publisher, Price
            	FROM Game 
            		JOIN Gamedeveloper d on d.AppID = Game.AppID
            		JOIN Gamepublisher p on p.AppID = Game.AppID
            	WHERE Name LIKE CONCAT('%', Title, '%')
                GROUP BY AppID
            	ORDER BY Name;
            END;
        """
        LoadSearchProcedures.cursor.execute(drop_procedure)
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Title Procedure created.")

    @staticmethod
    def create_language_search_procedure():
        """creates a procedure for searching by supported language."""
        drop_procedure = """DROP PROCEDURE IF EXISTS language_search;"""
        procedure_query = """
            CREATE PROCEDURE language_search(IN Language varchar(30))
            READS SQL DATA
            BEGIN
                -- find games with support for given language
                SELECT Game.AppID, Name, GROUP_CONCAT(DISTINCT Developer SEPARATOR ", ") as Developer,
                        GROUP_CONCAT(DISTINCT Publisher SEPARATOR ", ") as Publisher, Price,
                        (Positive * 1.0)/(Positive + Negative) as Reception
                FROM Game INNER JOIN GameLanguages l ON Game.AppID = l.AppID
                    JOIN Gamedeveloper d on d.AppID = Game.AppID
            		JOIN Gamepublisher p on p.AppID = Game.AppID
                WHERE l.language LIKE CONCAT('%', Language, '%')
                GROUP BY AppID
                ORDER BY Reception DESC;
            END;
            """
        LoadSearchProcedures.cursor.execute(drop_procedure)
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Language Procedure created.")

    @staticmethod
    def create_developer_search_procedure():
        """creates a procedure for searching by game developer."""
        drop_procedure = """DROP PROCEDURE IF EXISTS games_by_developer_search;"""
        procedure_query = """
            CREATE PROCEDURE games_by_developer_search(IN devoloper varchar(30))
            READS SQL DATA
            BEGIN
                -- find games by given developer
                SELECT Game.AppID, Name, GROUP_CONCAT(DISTINCT d.developer SEPARATOR ", ") as Developer,
                        GROUP_CONCAT(DISTINCT p.publisher SEPARATOR ", ") as Publisher, Price, Release_date
                FROM Game INNER JOIN GameDeveloper d ON Game.AppID = d.AppID
            		JOIN Gamepublisher p on p.AppID = Game.AppID
                WHERE d.Developer LIKE CONCAT('%', Devoloper, '%')
                GROUP BY AppID
                ORDER BY Release_date DESC;
            END;
            """
        LoadSearchProcedures.cursor.execute(drop_procedure)
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Developer Procedure created")

    @staticmethod
    def create_publisher_search_procedure():
        """creates a procedure for searching by game publisher."""
        drop_procedure = """DROP PROCEDURE IF EXISTS games_by_publisher_search;"""
        procedure_query = """
            CREATE PROCEDURE games_by_publisher_search(IN publisher varchar(30))
            READS SQL DATA
            BEGIN
                -- find games from given publisher
                SELECT Game.AppID, Name, GROUP_CONCAT(DISTINCT d.developer SEPARATOR ", ") as Developer,
                        GROUP_CONCAT(DISTINCT p.publisher SEPARATOR ", ") as Publisher, Price, Release_date
                FROM Game INNER JOIN GamePublisher p ON Game.AppID = p.AppID
                    JOIN Gamedeveloper d on d.AppID = Game.AppID
                WHERE p.Publisher LIKE CONCAT('%', Publisher, '%')
                GROUP BY AppID
                ORDER BY Release_date DESC;
            END;
            """ #TODO: publisher column is null for some reason??
        LoadSearchProcedures.cursor.execute(drop_procedure)
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Publisher Procedure created")

    @staticmethod
    def create_reception_search_procedure():
        """creates a procedure for searching by game reception."""
        drop_procedure = """DROP PROCEDURE IF EXISTS reception_search;"""
        procedure_query = """
            CREATE PROCEDURE reception_search(IN User_Rating REAL)
            READS SQL DATA
            BEGIN
                -- find games above a given user rating
                SELECT G.AppID, Name, GROUP_CONCAT(DISTINCT Developer SEPARATOR ", ") as Developer,
			            GROUP_CONCAT(DISTINCT Publisher SEPARATOR ", ") as Publisher, Price, Reception
                FROM (SELECT AppID, Name, Price, (Positive * 1.0)/(Positive + Negative) as Reception
                    FROM Game) G
                    JOIN Gamedeveloper d on d.AppID = G.AppID
                    JOIN Gamepublisher p on p.AppID = G.AppID
                WHERE Reception > User_Rating and Reception < 1
                GROUP BY AppID
                ORDER BY Reception;
            END;
            """
        LoadSearchProcedures.cursor.execute(drop_procedure)
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Reception Procedure created")

    @staticmethod
    def create_age_rating_search_procedure():
        """creates a procedues for searching by game age rating."""
        drop_procedure = """DROP PROCEDURE IF EXISTS age_rating_search;"""
        procedure_query = """
            CREATE PROCEDURE age_rating_search(IN User_Age REAL)
            READS SQL DATA
            BEGIN
                -- select games within an age rating
                SELECT Game.AppID, Name, GROUP_CONCAT(DISTINCT Developer SEPARATOR ", ") as Developer,
                        GROUP_CONCAT(DISTINCT Publisher SEPARATOR ", ") as Publisher, Price
                FROM Game
                    JOIN Gamedeveloper d on d.AppID = Game.AppID
            		JOIN Gamepublisher p on p.AppID = Game.AppID
                WHERE Required_age > 0 AND Required_age < User_Age
                GROUP BY AppID;
            END;
            """
        LoadSearchProcedures.cursor.execute(drop_procedure)
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Age Rating Procedure Created")

    @staticmethod
    def create_developers_by_reception_search_procedure():
        """creates a procedues for getting developers ordered by the reception
        of their games."""
        drop_procedure = """DROP PROCEDURE IF EXISTS developers_by_reception;"""
        procedure_query = """
            CREATE PROCEDURE developers_by_reception()
            READS SQL DATA
            BEGIN
                -- list developers ranked by the average reception of their games
                SELECT Developer, round(avg(Reception), 4) as Dev_Reception,
                        count(*) as Num_Games
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
        LoadSearchProcedures.cursor.execute(drop_procedure)
        LoadSearchProcedures.cursor.execute(procedure_query)
        print("Developer by reception search created")
        
    @staticmethod
    def create_delete_trigger():
        """creates a trigger to remove entries from junction tables when their
        associated game is deleted."""
        drop_trigger = """DROP TRIGGER IF EXISTS del_game;"""
        trigger_query = """
            CREATE TRIGGER del_game BEFORE DELETE ON Game
            FOR EACH ROW
            BEGIN
                DELETE FROM Gamecategory where AppID = OLD.AppID;
                DELETE FROM Gamedeveloper where AppID = OLD.AppID;
                DELETE FROM Gamegenre where AppID = OLD.AppID;
                DELETE FROM Gamelanguages where AppID = OLD.AppID;
                DELETE FROM Gameplatform where AppID = OLD.AppID;
                DELETE FROM Gamepublisher where AppID = OLD.AppID;
                DELETE FROM Gametag where AppID = OLD.AppID;
            END;"""
        LoadSearchProcedures.cursor.execute(drop_trigger)
        LoadSearchProcedures.cursor.execute(trigger_query)


    @staticmethod
    def genre_search(genres_string):
        """query by genre"""
        # Tuples are broken up if singletons or empty
        genres = genres_string.strip().split(" ")
        undesired = tuple([s[1:] for s in genres if s.startswith('-')])
        if len(undesired) == 1: undesired = f"('{undesired[0]}')"
        elif len(undesired) == 0: undesired = "('')"
        desired = tuple([s for s in genres if not s.startswith('-')])
        if len(desired) == 1: desired = f"('{desired[0]}')"
        elif len(desired) == 0: desired = "('')"
        query = f"""
            SELECT G.AppID, Name, GROUP_CONCAT(DISTINCT Developer SEPARATOR ", ") as Developer,
			            GROUP_CONCAT(DISTINCT Publisher SEPARATOR ", ") as Publisher, Price,
                        (G.Positive * 1.0)/(G.Positive + G.Negative) as Reception
            FROM (SELECT AppID
                FROM GameGenre
                WHERE genre IN {desired}  -- desired genres
                AND AppID NOT IN (
                SELECT AppID
                FROM GameGenre
                WHERE genre IN {undesired})   -- excluded genres
                ) Gen INNER JOIN Game as G on Gen.AppID = g.AppID
            JOIN GameDeveloper as GD on G.AppID = GD.AppID
            JOIN GamePublisher as GP on GD.AppID = GP.AppID 
            GROUP BY G.AppID
            HAVING count(G.AppID) > {int(len(genres) * .2)}
            ORDER BY count(G.AppID) DESC, Reception DESC"""
        print(query)
        LoadSearchProcedures.cursor.execute(query)
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod    
    def tag_search(tags_string):
        """query by tag"""
        #tuples are broken up if singletons or empty
        tags = tags_string.strip().split(" ")
        undesired = tuple([s[1:] for s in tags if s.startswith('-')]) #TODO: fix for singletons
        if len(undesired) == 1: undesired = f"('{undesired[0]}')"
        elif len(undesired) == 0: undesired = "('')"
        desired = tuple([s for s in tags if not s.startswith('-')])
        if len(desired) == 1: desired = f"('{desired[0]}')"
        elif len(desired) == 0: desired = "('')"
        query = f"""
            SELECT G.AppID, Name, GROUP_CONCAT(DISTINCT Developer SEPARATOR ", ") as Developer,
			            GROUP_CONCAT(DISTINCT Publisher SEPARATOR ", ") as Publisher, Price,
                        (G.Positive * 1.0)/(G.Positive + G.Negative) as Reception
            FROM (SELECT AppID
                FROM Gametag
                WHERE tag IN {desired}  -- desired tags
                AND AppID NOT IN (
                SELECT AppID
                FROM Gametag
                WHERE tag IN {undesired})   -- excluded tags
                ) Gen INNER JOIN Game G on Gen.AppID = g.AppID
                INNER JOIN gamepublisher p on g.AppID = p.AppID
                INNER JOIN Gamedeveloper d on p.AppID = d.AppID
            GROUP BY G.AppID
            HAVING count(g.AppID) > {int(len(tags) * .2)}  -- limit to more relevant titles
            ORDER BY count(g.AppID) DESC, Reception DESC"""
        LoadSearchProcedures.cursor.execute(query)
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod  
    def category_search(cats_string):
        """query by cetegory"""
        #tuples are broken up if singletons or empty
        cats = cats_string.strip().split(" ")
        undesired = tuple([s[1:] for s in cats if s.startswith('-')]) #TODO: fix for singletons
        if len(undesired) == 1: undesired = f"('{undesired[0]}')"
        elif len(undesired) == 0: undesired = "('')"
        desired = tuple([s for s in cats if not s.startswith('-')])
        if len(desired) == 1: desired = f"('{desired[0]}')"
        elif len(desired) == 0: desired = "('')"
        query = f"""
            SELECT G.AppID, Name, GROUP_CONCAT(DISTINCT Developer SEPARATOR ", ") as Developer,
			            GROUP_CONCAT(DISTINCT Publisher SEPARATOR ", ") as Publisher, Price,
                        (G.Positive * 1.0)/(G.Positive + G.Negative) as Reception
            FROM (SELECT AppID
                FROM Gamecategory
                WHERE category IN {desired}  -- desired categorys
                AND AppID NOT IN (
                SELECT AppID
                FROM Gamecategory
                WHERE category IN {undesired})   -- excluded categorys
                ) Gen INNER JOIN Game as G on Gen.AppID = G.AppID
            JOIN GameDeveloper as GD on G.AppID = GD.AppID
            JOIN GamePublisher as GP on GD.AppID = GP.AppID
            GROUP BY G.AppID
            HAVING count(G.AppID) > 2  -- limit to more relevant titles
            ORDER BY count(G.AppID) DESC, Reception DESC;"""
        LoadSearchProcedures.cursor.execute(query)
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def recomendation_search(req_string):
        """aggregate search across tag, genre, and category."""
        reqs = tuple(req_string.strip().split(" "))
        query = f"""
            SELECT G.AppID, Name, GROUP_CONCAT(DISTINCT Developer SEPARATOR ", ") as Developer,
			            GROUP_CONCAT(DISTINCT Publisher SEPARATOR ", ") as Publisher, Price,
                        (G.Positive * 1.0)/(G.Positive + G.Negative) as Reception
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
            JOIN GameDeveloper as GD on G.AppID = GD.AppID
            JOIN GamePublisher as GP on GD.AppID = GP.AppID
            GROUP BY G.AppID
            HAVING COUNT(G.AppID) > 3
            ORDER BY COUNT(G.AppID) DESC, Reception DESC;"""
        LoadSearchProcedures.cursor.execute(query)
        return dictfetchall(LoadSearchProcedures.cursor)
    
    @staticmethod
    def game_title_search(title):
        LoadSearchProcedures.cursor.callproc("game_title_search", [title])
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def language_search(lang):
        LoadSearchProcedures.cursor.callproc("language_search", [lang])
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def games_by_developer_search(dev):
        LoadSearchProcedures.cursor.callproc("games_by_developer_search", [dev])
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def games_by_publisher_search(pub):
        LoadSearchProcedures.cursor.callproc("games_by_publisher_search", [pub])
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def reception_search(recep):
        LoadSearchProcedures.cursor.callproc("reception_search", [recep])
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def age_rating_search(age):
        LoadSearchProcedures.cursor.callproc("age_rating_search", [age])
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def developers_by_reception_search(search_parameter):
        LoadSearchProcedures.cursor.callproc("developers_by_reception")
        return dictfetchall(LoadSearchProcedures.cursor)

    @staticmethod
    def delete_game(AppID):
        """deletes a game from the database"""
        query = f"""
            START TRANSACTION;
            SET SQL_SAFE_UPDATES = 0;
            delete from game where AppID = {AppID}; 
            SET SQL_SAFE_UPDATES = 1;
            COMMIT;
        """
        #TODO: confirm this rolls back when needed
        LoadSearchProcedures.cursor.execute(query)


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

