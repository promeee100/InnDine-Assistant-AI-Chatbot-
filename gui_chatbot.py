from tkinter import *
from tkinter import ttk
from ai_model import predict_intent
from hotel_services import check_availability, book_room
from restaurant_services import order_food



BG_MAIN = "#F3EFFF"
CARD_BG = "#FFFFFF"
ACCENT = "#7A3EF2"
ACCENT2 = "#8C52FF"
BORDER = "#D3C7F5"
DARK_TEXT = "#1F102C"

def create_card(parent):
    frame = Frame(
        parent, bg=CARD_BG, bd=1, relief=RIDGE,
        highlightthickness=1, highlightbackground=BORDER
    )
    frame.pack(padx=20, pady=15, fill=BOTH, expand=True)
    return frame

def send_message():
    user_input = entry.get().strip()
    if user_input == "":
        return

    chat_log.config(state=NORMAL)
    chat_log.insert(END, f"🧑 You: {user_input}\n", "user")
    entry.delete(0, END)

    intent = predict_intent(user_input)

    if intent == "check_availability":
        response = check_availability()
    elif intent == "book_room":
        response = "📅 Please fill the booking section below to book a room."
    elif intent == "order_food":
        response = "🍽 Please choose food in the Order Section."
    elif intent == "greeting":
        response = "💜 Hello! How can I assist you today?"
    elif intent == "goodbye":
        response = "💟 Goodbye! Hope to see you again!"
    else:
        response = "😕 Sorry, I didn’t understand that."

    chat_log.insert(END, f"🤖 Bot: {response}\n\n", "bot")
    chat_log.config(state=DISABLED)
    chat_log.yview(END)


def book_room_gui():
    if not all([room_var.get(), name_var.get(), email_var.get(), checkin_var.get(), checkout_var.get()]):
        result_var.set("⚠️ All booking fields are required.")
        return

    try:
        response = book_room(name_var.get(), email_var.get(), room_var.get(), checkin_var.get(), checkout_var.get())
        result_var.set(response)
    except Exception as e:
        result_var.set(f"❌ Error: {e}")


def order_food_gui():
    if not all([food_var.get(), quantity_var.get(), name_var.get(), email_var.get()]):
        result_var.set("⚠️ All order fields are required.")
        return
    try:
        q = int(quantity_var.get())
        response = order_food(name_var.get(), email_var.get(), food_var.get(), q)
        result_var.set(response)
    except:
        result_var.set("❌ Quantity must be a number.")


root = Tk()
root.title("💜 InnDine Assistant — Purple Edition")
root.geometry("840x850")
root.minsize(760, 700)
root.configure(bg=BG_MAIN)

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", padding=5, font=("Segoe UI", 10))
style.configure("TLabel", background=CARD_BG)


chat_card = create_card(root)
Label(chat_card, text="💬 Chat Assistant", bg=CARD_BG,
      font=("Segoe UI", 14, "bold"), fg=ACCENT).pack(pady=5)

chat_log = Text(
    chat_card, state=DISABLED, height=14,
    bg="#FBF8FF", fg=DARK_TEXT, relief=FLAT, wrap=WORD,
    font=("Segoe UI", 10)
)
chat_log.pack(padx=15, pady=10, fill=BOTH, expand=True)

chat_log.tag_config("user", foreground="#6D28D9", font=("Segoe UI", 10, "bold"))
chat_log.tag_config("bot", foreground="#9D4EDD", font=("Segoe UI", 10, "italic"))

entry_frame = Frame(chat_card, bg=CARD_BG)
entry_frame.pack(fill=X, padx=10, pady=8)

entry = Entry(
    entry_frame, font=("Segoe UI", 10),
    bg="#F7F4FF", relief=FLAT, highlightbackground=BORDER,
    highlightthickness=1
)
entry.pack(side=LEFT, fill=X, expand=True, ipady=7)

send_button = Button(
    entry_frame, text="💜 Send", command=send_message,
    bg=ACCENT2, fg="white", relief=FLAT,
    font=("Segoe UI", 10, "bold"), padx=14, pady=6
)
send_button.pack(side=LEFT, padx=(10, 0))


book_card = create_card(root)
Label(book_card, text="🏨 Book a Room", bg=CARD_BG,
      font=("Segoe UI", 14, "bold"), fg=ACCENT).grid(row=0, column=0, columnspan=4, pady=10)

room_var = StringVar()
Label(book_card, text="Room ID:").grid(row=1, column=0, sticky=W, padx=10)
ttk.Combobox(book_card, textvariable=room_var, values=["1", "2", "3"], width=10).grid(row=1, column=1)

name_var = StringVar()
Label(book_card, text="Name:").grid(row=1, column=2, sticky=W, padx=10)
Entry(book_card, textvariable=name_var, width=20).grid(row=1, column=3)

email_var = StringVar()
Label(book_card, text="Email:").grid(row=2, column=0, sticky=W, padx=10)
Entry(book_card, textvariable=email_var, width=22).grid(row=2, column=1)

checkin_var = StringVar()
Label(book_card, text="Check-in:").grid(row=2, column=2, sticky=W)
Entry(book_card, textvariable=checkin_var, width=18).grid(row=2, column=3)

checkout_var = StringVar()
Label(book_card, text="Check-out:").grid(row=3, column=0, sticky=W, padx=10)
Entry(book_card, textvariable=checkout_var, width=18).grid(row=3, column=1)

Button(
    book_card, text="💟 Confirm Booking", command=book_room_gui,
    bg=ACCENT, fg="white", relief=FLAT,
    font=("Segoe UI", 10, "bold"), padx=12
).grid(row=3, column=3, pady=10)


order_card = create_card(root)
Label(order_card, text="🍴 Order Food", bg=CARD_BG,
      font=("Segoe UI", 14, "bold"), fg=ACCENT).grid(row=0, column=0, columnspan=4, pady=10)

food_var = StringVar()
Label(order_card, text="Food Item:").grid(row=1, column=0, sticky=W, padx=10)
ttk.Combobox(order_card, textvariable=food_var,
             values=["Pizza", "Burger", "Pasta", "Sandwich"], width=17).grid(row=1, column=1)

quantity_var = StringVar()
Label(order_card, text="Quantity:").grid(row=1, column=2, sticky=W)
Entry(order_card, textvariable=quantity_var, width=10).grid(row=1, column=3)

Button(
    order_card, text="💜 Place Order", command=order_food_gui,
    bg=ACCENT2, fg="white", relief=FLAT,
    font=("Segoe UI", 10, "bold")
).grid(row=2, column=3, pady=10)


result_frame = Frame(root, bg=BG_MAIN)
result_frame.pack(fill=X, pady=20, padx=20)

result_var = StringVar()
result_label = Label(
    result_frame,
    textvariable=result_var,
    bg=BG_MAIN,
    fg=DARK_TEXT,
    font=("Segoe UI", 12, "bold"),
    wraplength=760,
    justify=LEFT,
    padx=10,
    pady=10
)
result_label.pack(fill=X, expand=True)


bottom_space = Frame(root, height=30, bg=BG_MAIN)
bottom_space.pack()

root.mainloop()