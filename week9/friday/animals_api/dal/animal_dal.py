from database import get_connection

class Animal_DAL:

    def create_animal(self, name, animal_type, age):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
        insert into animals(name, animal_type, age)
        values(%s, %s, %s)

            """,
            (name, animal_type, age)
                       )
        connection.commit()
        connection.close()


    def get_all_animals(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            select * from animals
            """
        )

        result = cursor.fetchall()

        connection.close()
        return result
    

    def get_animal_by_id(self, animal_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            select * from animals where id = %s
            """,
            (animal_id,)
        )

        result = cursor.fetchall()

        connection.close()
        return result
    

    def update_animal(self, animal_id, name, animal_type, age):
        connection = get_connection()
        cursor =connection.cursor()

        cursor.execute(
            """
        update animals
        set name = %s,
        animal_type = %s,
        age = %s
        where id = %s

            """,
            (name, animal_type, age, animal_id)
        )

        connection.commit()
        connection.close()



    def delete_animal(self, animal_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            delete from animals where id = %s

            """,
            (animal_id)
        )

        connection.commit()
        connection.close()