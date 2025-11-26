from database import get_db_connection
from email_service import send_email

def check_availability():
    db, cursor = get_db_connection()
    try:
        cursor.execute("SELECT * FROM rooms WHERE is_available=1")
        rooms = cursor.fetchall()
        if rooms:
            return "\n".join([f"Room {r['room_id']}: {r['room_type']} - tk{r['price_per_night']}/night" for r in rooms])
        return "Sorry, no rooms available."
    finally:
        db.close()

def book_room(customer_name, email, room_id, check_in, check_out):
    if not all([customer_name, email, room_id, check_in, check_out]):
        return "All booking fields are required."

    db, cursor = get_db_connection()
    try:
        room_id = int(room_id)  # ensure integer
        # Check room availability
        cursor.execute("SELECT * FROM rooms WHERE room_id=%s AND is_available=1", (room_id,))
        room = cursor.fetchone()
        if not room:
            return "Room not available."


        cursor.execute(
            "INSERT INTO bookings (customer_name, email, room_id, check_in, check_out) VALUES (%s, %s, %s, %s, %s)",
            (customer_name, email, room_id, check_in, check_out)
        )

        cursor.execute("UPDATE rooms SET is_available=0 WHERE room_id=%s", (room_id,))
        db.commit()


        subject = "Hotel Room Booking Confirmation 🏨"
        message = (
            f"Dear {customer_name},\n\n"
            f"Your booking for Room {room_id} has been confirmed!\n"
            f"Check-in Date: {check_in}\n"
            f"Check-out Date: {check_out}\n\n"
            "We look forward to hosting you!\n"
            "Best regards,\nHotel Management Team"
        )
        send_email(email, subject, message)

        return f"Room {room_id} booked successfully! A confirmation email has been sent to {email}."
    finally:
        db.close()
