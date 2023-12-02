import mysql.connector
import json

config_file = "connectorConfig.json"


class LoadSearchProcedures:
    @staticmethod
    def access_db(query, as_dictionary=False):
        with open(config_file, "r") as f:
            config = json.load(f)
        connection_config = config["mysql"]
        data_base = mysql.connector.connect(**connection_config)

        # Determine if tuple or dictionary format
        if as_dictionary:
            cursor_object = data_base.cursor(dictionary=True)
        else:
            cursor_object = data_base.cursor()

        cursor_object.execute(query)
        data_base.commit()  # Commit the transaction for procedure creation
        my_result = cursor_object.fetchall()

        return my_result

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
        LoadSearchProcedures.access_db(procedure_query)
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
        LoadSearchProcedures.access_db(procedure_query)
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
        LoadSearchProcedures.access_db(procedure_query)
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
        LoadSearchProcedures.access_db(procedure_query)
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
        LoadSearchProcedures.access_db(procedure_query)
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
        LoadSearchProcedures.access_db(procedure_query)
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
        LoadSearchProcedures.access_db(procedure_query)
        print("Developer by reception search created")


# Load all the procedures
LoadSearchProcedures.create_game_title_search_procedure()
LoadSearchProcedures.create_language_search_procedure()
LoadSearchProcedures.create_devoloper_search_procedure()
LoadSearchProcedures.create_publisher_search_procedure()
LoadSearchProcedures.create_reception_search_procedure()
LoadSearchProcedures.create_age_rating_search_procedure()
LoadSearchProcedures.create_devolopers_by_reception_search_procedure()
