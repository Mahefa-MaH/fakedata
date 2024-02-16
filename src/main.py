import mysql.connector
from create_table import create_logistics_table
from generate_data import generate_logistics_data
from sql_statements import generate_sql_insert_statements, execute_sql_statements, execute_sql_update
from config import DATABASE_CONFIG

if __name__ == "__main__":
    # Connect to MySQL database
    db_connection = mysql.connector.connect(**DATABASE_CONFIG)

    # Create logistics_entries table if not exists
    create_logistics_table(db_connection)

    # Generate data
    num_records_to_generate = 200
    logistics_data_generated = generate_logistics_data(num_records_to_generate)

    # Execute SQL INSERT statements
    execute_sql_statements(generate_sql_insert_statements(logistics_data_generated), db_connection)

    # Execute SQL UPDATE statement
    execute_sql_update(db_connection)

    # Close the database connection
    db_connection.close()
