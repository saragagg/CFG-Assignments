import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    pass
def create_db_connection():
    try:
        #establishing the connection using mysql.connector
        conn = mysql.connector.connect(host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE)

        return conn

    except Exception:
        print(f'Sorry, there has been a error trying to connect to the database')


def get_all_classes():
    try:
        db_connection = create_db_connection()
        cursor = db_connection.cursor()

        query = """
        SELECT c.id as class_number, c.class_name, c.schedule as scheduled_for, c.description, c.available_spots, i.first_name as instructor_name, i.last_name as instructor_surname 
        FROM classes as c 
        JOIN instructors as i 
        ON c.instructor_id = i.id;
        """

        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return result

    except Exception:
        raise DbConnectionError("Sorry, failed to read data from the database")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def register_to_class(class_id):
    try:
        db_connection = create_db_connection()
        cursor = db_connection.cursor()
        # decreasing available_spots of class when a student registers
        query = f"""
        UPDATE classes
        SET available_spots = available_spots - 1
        WHERE classes.id = {class_id};
        """

        cursor.execute(query)

        db_connection.commit()
        cursor.close()

    except Exception:
        raise DbConnectionError("Failed to post data to DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def register_student(first_name, last_name, email_address, phone_number, disability_requirements):

    try:
        db_connection = create_db_connection()
        cursor = db_connection.cursor()

        query = """
                INSERT INTO students 
                (first_name, last_name, email_address, phone_number, disability_requirements)
                VALUES 
                (%s, %s, %s, %s, %s)
                """
        student_details = (first_name, last_name, email_address, phone_number, disability_requirements)

        cursor.execute(query, student_details)

        db_connection.commit()
        cursor.close()

    except Exception:
        raise DbConnectionError("Failed to post data to DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
