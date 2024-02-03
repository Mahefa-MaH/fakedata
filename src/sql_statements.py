def generate_sql_insert_statements(data):
    statements = []

    for entry in data:
        columns = ', '.join(entry.keys())
        values = ', '.join([repr(value) if value is not None else 'NULL' for value in entry.values()])
        statement = f"INSERT INTO logistics_entries ({columns}) VALUES ({values});"
        statements.append(statement)

    return statements

def execute_sql_statements(sql_statements, connection):
    cursor = connection.cursor()

    for statement in sql_statements:
        cursor.execute(statement)

    connection.commit()
    cursor.close()

def execute_sql_update(connection):
    cursor = connection.cursor()

    # Example: Update all prices to a new value
    update_query = "UPDATE logistics_entries SET price = price * 1.1;"
    cursor.execute(update_query)

    connection.commit()
    cursor.close()
