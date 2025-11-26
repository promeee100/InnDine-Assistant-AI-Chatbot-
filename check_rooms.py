from database import get_db_connection

def show_available_rooms():
    db, cursor = get_db_connection()
    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()
    db.close()

    if not rooms:
        print("No rooms found in database.")
        return

    print("Rooms in Database:")
    for r in rooms:
        status = "Available" if r['is_available'] else "Booked"
        print(f"Room {r['room_id']}: {r['room_type']} - ${r['price_per_night']}/night | {status}")

if __name__ == "__main__":
    show_available_rooms()
