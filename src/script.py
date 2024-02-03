import random
import mysql.connector
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

def create_logistics_table(connection):
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS logistics_entries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        reference VARCHAR(255),
        seller_name VARCHAR(255),
        seller_id INT,
        address VARCHAR(255),
        price FLOAT,
        user_firstName VARCHAR(255),
        user_lastName VARCHAR(255),
        persona VARCHAR(255),
        seller_ref VARCHAR(255),
        price_seller FLOAT,
        marge_commerciale FLOAT,
        marge VARCHAR(255),
        unit_seller_price FLOAT,
        apt_interval VARCHAR(255),
        apt_date DATETIME,
        commentary TEXT,
        timestart DATETIME,
        p_price FLOAT,
        list_price FLOAT,
        timedelivered DATETIME,
        updated_at DATETIME,
        status VARCHAR(255),
        delivery_address VARCHAR(255),
        listings_id INT,
        quantity INT,
        rating FLOAT,
        list_title VARCHAR(255),
        list_subtitle VARCHAR(255),
        list_description TEXT,
        list_img VARCHAR(255),
        list_of_images TEXT,
        discount FLOAT,
        offer_id INT,
        bundle VARCHAR(255),
        time_end DATETIME,
        supercat_name VARCHAR(255),
        CAT_NAME VARCHAR(255),
        tag VARCHAR(255),
        subcat_name VARCHAR(255),
        inventory_stock INT,
        platform_name VARCHAR(255),
        firstorders VARCHAR(5),
        reason_id INT,
        reason_name VARCHAR(255),
        mmk_fault VARCHAR(5)
    );
    """
    cursor.execute(create_table_query)

    connection.commit()
    cursor.close()

def generate_logistics_data(num_records):
    logistics_data = []

    for _ in range(num_records):
        quantity = fake.random_int(min=1, max=5)
        marge = fake.random_int(min=5, max=30)
        unit_seller_price = fake.random_int(min=1, max=5000) * 100
        
        p_price = (unit_seller_price + unit_seller_price * marge) / 100
        price = p_price * quantity
        price_seller = quantity * unit_seller_price

        list_price = p_price 
        day = fake.random_int(min=1, max=20)

        logistics_entry = {
            "id": int(datetime.now().timestamp()) + random.randint(1, 1000),
            "reference": fake.uuid4(),
            "seller_name": fake.company(),
            "seller_id": fake.random_int(min=50, max=100),
            "address": fake.address(),
            "price": price,
            "user_firstName": fake.first_name(),
            "user_lastName": fake.last_name(),
            "persona": fake.word(),
            "seller_ref": fake.uuid4(),
            "price_seller": price_seller,
            "marge_commerciale": price - price_seller,
            "marge": f"{marge}%",  # Format the percentage
            "unit_seller_price": unit_seller_price,
            "apt_interval": f"{fake.random_int(min=1, max=12)}e mois {day}/{day+fake.random_int(min=0, max=3)} {fake.random_int(min=1, max=24)}h-{fake.random_int(min=1, max=24)}h",
            "apt_date": (datetime.now() + timedelta(days=fake.random_int(min=1, max=30))).isoformat(),
            "commentary": fake.sentence() if fake.boolean(chance_of_getting_true=30) else None,
            "timestart": (datetime.now() - timedelta(minutes=fake.random_int(min=1, max=60))).isoformat(),
            "p_price": p_price,
            "list_price": list_price,
            "timedelivered": None,
            "updated_at": datetime.now().isoformat(),
            "status": fake.random_element(elements=("PRÉPARATION", "EN COURS", "LIVRÉ")),
            "delivery_address": fake.address(),
            "listings_id": fake.random_int(min=4000, max=5000),
            "quantity": quantity,
            "rating": float(fake.random_int(min=0, max=5)),
            "list_title": fake.word(),
            "list_subtitle": fake.word(),
            "list_description": fake.paragraph(),
            "list_img": fake.image_url(),
            "list_of_images": None,
            "discount": fake.pyfloat(left_digits=2, right_digits=1),
            "offer_id": fake.random_int(min=1, max=5),
            "bundle": None,
            "time_end": None,
            "supercat_name": fake.word(),
            "CAT_NAME": fake.word(),
            "tag": fake.word(),
            "subcat_name": fake.word(),
            "inventory_stock": fake.random_int(min=0, max=100),
            "platform_name": fake.word(),
            "firstorders": str(fake.boolean(chance_of_getting_true=50)).lower(),
            "reason_id": None,
            "reason_name": None,
            "mmk_fault": str(fake.boolean(chance_of_getting_true=10)).lower()
        }
        logistics_data.append(logistics_entry)

    return logistics_data

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

if __name__ == "__main__":
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fdata"
    )

    # Create logistics_entries table if not exists
    create_logistics_table(db_connection)

    # Generate data
    num_records_to_generate = 5
    logistics_data_generated = generate_logistics_data(num_records_to_generate)

    # Execute SQL INSERT statements
    execute_sql_statements(generate_sql_insert_statements(logistics_data_generated), db_connection)

    # Execute SQL UPDATE statement
    execute_sql_update(db_connection)

    # Close the database connection
    db_connection.close()