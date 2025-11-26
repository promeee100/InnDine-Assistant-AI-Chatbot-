from database import get_db_connection
from email_service import send_email

def order_food(customer_name, email, food_item, quantity):
    if not all([customer_name, email, food_item, quantity]):
        return "All fields are required for food order."

    try:
        quantity = int(quantity)
    except ValueError:
        return "Quantity must be a number."

    db, cursor = get_db_connection()
    try:

        cursor.execute(
            "INSERT INTO food_orders (customer_name, email, food_item, quantity) VALUES (%s, %s, %s, %s)",
            (customer_name, email, food_item, quantity)
        )
        db.commit()


        subject = "Food Order Confirmation 🍕"
        message = (
            f"Dear {customer_name},\n\n"
            f"Your order for {quantity} x {food_item} has been received and is being prepared.\n"
            "We will notify you when it’s ready!\n\n"
            "Thank you for ordering with InnDine Assistant.\n"
            "Best regards,\nRestaurant Team"
        )
        send_email(email, subject, message)

        return f"Your order for {quantity} x {food_item} has been placed successfully! Confirmation email sent to {email}."
    finally:
        db.close()
