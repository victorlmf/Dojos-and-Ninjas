from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_ninja import Ninja
db = 'dojos_and_ninjas'

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # Setup query to get all dojos
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    # Setup query to add dojo
    @classmethod
    def add_dojo(cls,data):
        query = """
                INSERT INTO dojos (name, created_at, updated_at)
                VALUES (%(name)s, NOW(), NOW());
                """
        return connectToMySQL(db).query_db(query,data)

    # Setup query to show one dojo
    @classmethod
    def get_one_dojo(cls,data):
        query = """
                SELECT * FROM dojos
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,data)

    # Setup query to show dojo and the associated ninjas
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = """
                SELECT * FROM dojos 
                LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
                WHERE dojos.id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query,data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo

    # Setup query to get dojo id and dojo name
    @classmethod
    def get_dojo_id_and_name(cls,data):
        query = """
                SELECT dojos.id, name FROM dojos
                JOIN ninjas ON ninjas.dojo_id = dojos.id
                WHERE ninjas.id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,data)