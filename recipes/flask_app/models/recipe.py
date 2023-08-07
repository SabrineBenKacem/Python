from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Recipe:

    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.instructions = data_dict['instructions']
        self.date_made = data_dict['date_made']
        self.under_30min = data_dict['under_30min']
        self.description = data_dict['description']
        self.user_id = data_dict['user_id']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.poster =""

    
    @classmethod
    def create(cls,data_dict):
        query = """INSERT INTO recipes 
                    (name,user_id, instructions, date_made, under_30min, description)
                    VALUES 
                    (%(name)s,%(user_id)s,%(instructions)s,%(date_made)s,%(under_30min)s,%(description)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict) 

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM recipes
                    JOIN users on recipes.user_id = users.id;"""
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes =[]
        for row in results:
            recipe = cls(row)
            recipe.poster = (row['first_name'])
            all_recipes.append(recipe)
        return all_recipes

    # @classmethod
    # def get_by_id(cls,data_dict):
    #     query = """SELECT * FROM recipes WHERE id=%(id)s;"""
    #     result = connectToMySQL(DATABASE).query_db(query, data_dict)
    #     recipe = cls(result[0])
    #     recipe.poster = (result[0]['first_name'])
    #     return recipe   
    @classmethod
    def get_by_id(cls,data_dict):
        query = """SELECT * FROM recipes JOIN users ON recipes.user_id = users.id
                    WHERE recipes.id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        
        recipe = cls(result[0])
        recipe.poster = f"{result[0]['first_name']}"
        return recipe
    

    @classmethod
    def update(cls,data_dict):
        query= """UPDATE recipes
                SET 
                name= %(name)s, instructions= %(instructions)s,
                under_30min= %(under_30min)s, date_made= %(date_made)s, 
                description= %(description)s
                WHERE id= %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data_dict)
    
    @classmethod
    def delete(cls,data_dict):
        query= """DELETE FROM recipes WHERE id= %(id)s; """
        return connectToMySQL(DATABASE).query_db(query,data_dict)


    @staticmethod
    def validate(data_dict):
        is_valid = True
        # date = datetime.strftime(data_dict["date"])
        
        if len(data_dict['name'])<2:
            is_valid =False
            flash("Name not valid", "name")

        if len(data_dict['instructions'])<2:
            is_valid =False
            flash("Instructions too short", "instructions")

        if len(data_dict["description"])<2:
            is_valid = False
            flash("Description too short", "description")
        if data_dict["date_made"] =="":
            is_valid = False
            flash("Date too short", "date_made")
        # elif date < datetime.now().date:
        #     is_valid = False
        #     flash("Date Already passed", "date")
        return is_valid   

