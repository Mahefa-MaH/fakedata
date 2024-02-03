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