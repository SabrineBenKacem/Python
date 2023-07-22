from mysqlconnection import connectToMySQL
from pprint import pprint
class User :

    def __init__(self,data_dict):
        self.id  = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
    
    # EVERY QUERY MUST BE CLASSMETHOD CURD 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        all_users = []
        # print("🔥"*10,results,"🔥"*10)
        for row in results:
            user = cls(row)
            all_users.append(user)
        # print("🎈"*10, all_artists,"🎈"*10)
        return all_users
    

    @classmethod
    def create_user(cls,data_dict):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        result = connectToMySQL("users_schema").query_db(query, data_dict)
        return result
    