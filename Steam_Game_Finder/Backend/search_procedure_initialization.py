import mysql.connector
import json
import timeit

config_file = "connectorConfig.json"

class load_search_functions:

    def access_db(query, as_dictionary=False):
        """
    Connect to database with mysql connector to execute queries or create procedures
    :param query: query to be preformed
    :param as_dictionary: whether results should be in dictionary form for ease of printing
    :return: results in dictionary or sql table form depending on as_dictionary
    """
        with open(config_file, "r") as f:
            config = json.load(f)
        connection_config = config["mysql"]
        data_base = mysql.connector.connect(**connection_config)

    # determine if tuple or dictionary format
        if as_dictionary:
            cursor_object = data_base.cursor(dictionary=True)
        else:
            cursor_object = data_base.cursor()

        cursor_object.execute(query)
        my_result = cursor_object.fetchall()

        return my_result
    
    def create_game_title_search_procedure():
        procedure_query = """
            CREATE PROCEDURE game_title_search(@Title varchar(30))
        READS SQL DATA
        BEGIN
            -- SQLite
            -- Basic fuzzy title search
            SELECT AppID, Name
            FROM Game 
            where Name like "%@Title%"
            ORDER BY Name;
            END;
        """
        load_search_functions.access_db(procedure_query)
        print("Title Procedure created.")
    
    def create_language_search_procedure():
        procedure_query = """
            CREATE PROCEDURE language_search(@Language (varchar(30))
        READS SQL DATA
        BEGIN
            -- SQLite
            -- find games with support for given language
            SELECT g.AppID, Name, (Positive * 1.0)/(Positive + Negative as Reception
            FROM Game g INNER JOIN GameLanguages l ON g.AppID = l.AppID
            where l.language = "@Language"
            ORDER BY Reception DESC
            END;
            """
        load_search_functions.access_db(procedure_query)
        print("Language Procedure created.")

    def create_devoloper_search_procedure():
        procedure_query = """
            CREATE PROCEDURE games_by_devoloper_search(@Devoloper (varchar(30))
        READS SQL DATA
        BEGIN
            -- SQLite
            -- find games by given developer
            SELECT g.AppID, Name, Release_date
            FROM Game g INNER JOIN GameDeveloper d ON g.AppID = d.AppID
            where d.developer Like "@Devoloper%"
            ORDER BY Release_date DESC
            END;
            """
        load_search_functions.access_db(procedure_query)
        print("Devoloper Procedure created")
    
    def create_publisher_search_procedure():
        procedure_query = """
            CREATE PROCEDURE games_by_publisher_search(@Publisher (varchar(30))
        READS SQL DATA
        BEGIN
            -- SQLite
            -- find games from given publisher
            SELECT g.AppID, Name, Release_date
            FROM Game g INNER JOIN GamePublisher p ON g.AppID = p.AppID
            where p.publisher Like "@Publisher%"
            ORDER BY Release_date DESC
            END;
            """
        load_search_functions(procedure_query)
        print("Publisher Procedure created")
    
    def create_reception_search_procedure():
        procedure_query = """
            CREATE PROCEDURE reception_search(IN User_Rating REAL)
        READS SQL DATA
        BEGIN
            -- SQLite
            -- find games above a given user rating
            SELECT AppID, Name, (Positive * 1.0)/(Positive + Negative) as Reception
            FROM Game
            WHERE Reception > User_Rating and Reception < 1
            END;     
            """
        load_search_functions(procedure_query)
        print("Reception Procedure created")
    

        
    

