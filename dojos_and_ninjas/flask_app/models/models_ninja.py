from flask_app.config.mysqlconnection import connectToMySQL
db = 'dojos_and_ninjas'

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Setup query to add ninja
    @classmethod
    def add_ninja(cls,data):
        query = """
                INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
                VALUES (%(fname)s, %(lname)s, %(age)s, %(dojo_id)s, NOW(), NOW())
                """
        return connectToMySQL(db).query_db(query,data)

    # Display one ninja
    @classmethod
    def get_one_ninja(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query,data)

    # Setup query to update ninja
    @classmethod
    def update_ninja(cls,data):
        query = """
                UPDATE ninjas
                SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,data)

    # Setup query to delete ninja
    @classmethod
    def delete_ninja(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)