import random
from datetime import datetime, timedelta
from faker import Faker

from product_name import build_product_name

fake = Faker()

def generate_logistics_data(num_records):
    logistics_data = []
    i = 0

    for _ in range(num_records):
        quantity = fake.random_int(min=1, max=5)
        marge = fake.random_int(min=500, max=3000) / 100
        unit_seller_price = fake.random_int(min=1, max=5000) * 100
        
        p_price = (unit_seller_price + unit_seller_price * marge / 100)
        price = p_price * quantity
        price_seller = quantity * unit_seller_price

        list_price = p_price 
        day = fake.random_int(min=1, max=20)

        logistics_entry = {
            # "id": int(datetime.now().timestamp()) + random.randint(1, 1000),
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
            "timestart": (datetime.now() - timedelta(hours=fake.random_int(min=0, max=230*2)) - timedelta(minutes=fake.random_int(min=1, max=60))).isoformat(),
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
            "discount": int(fake.random_int(min=0, max=10)/5),
            "offer_id": fake.random_int(min=1, max=5),
            "bundle": None,
            "time_end": None,
            "supercat_name": build_product_name(["adjective", "other"]),
            "CAT_NAME": build_product_name(["verb"]),
            "tag": build_product_name(["adjective", "noun"]),
            "subcat_name": build_product_name(["other"]),
            "inventory_stock": int(fake.random_int(min=0, max=100)/5),
            "platform_name": fake.word(),
            "firstorders": str(fake.boolean(chance_of_getting_true=30)).lower(),
            "reason_id": None,
            "reason_name": None,
            "mmk_fault": str(fake.boolean(chance_of_getting_true=10)).lower()
        }
        # 20% chance for timedelivered to be set to timestart + 2 hours
        if random.random() < 0.2:
            logistics_entry["timedelivered"] = (datetime.fromisoformat(logistics_entry["timestart"]) + timedelta(hours=2)).isoformat()
        else:
            # 80% chance for timedelivered to be randomly set between timestart + 2 hours and timestart + 5*24 hours
            random_hours = random.uniform(2, 5 * 24)
            logistics_entry["timedelivered"] = (datetime.fromisoformat(logistics_entry["timestart"]) + timedelta(hours=random_hours)).isoformat()
            logistics_entry["updated_at"] = logistics_entry["timedelivered"]
    
        logistics_data.append(logistics_entry)
        
    return logistics_data