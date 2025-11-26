#  InnDine Assistant — Hotel & Restaurant AI Assistant

A desktop application built using **Python Tkinter**, **Machine Learning (LSTM/ML classifier)**, and backend Python services for **hotel room booking**, **restaurant food ordering**, and **chat-based assistance**.

---

## 📌 **Project Overview**

**InnDine Assistant** is an AI-powered desktop application designed to manage hotel room bookings, food ordering, and provide smart responses based on user intent.

It includes:

* 🤖 **AI Chat Assistant** (Intent classification using ML model)
* 🏨 **Room Booking System**
* 🍽 **Food Ordering System**
* 🎨 **Modern Purple UI Theme**
* 💬 Live Chat Window with user/bot message formatting
* 📦 Modular architecture (`ai_model.py`, `hotel_services.py`, `restaurant_services.py`)

---

## 🧠 **Features**

### 💬 Smart Chat Assistant

The chat detects user intent such as:

* Check room availability
* Book a room
* Order food
* Greetings / Goodbye
* Unknown commands

```python
intent = predict_intent(user_input)
```

### 🏨 Hotel Room Booking

* Select Room ID
* Enter customer details
* Choose check-in & check-out dates
* Backend Python function handles database / logic

```python
book_room(name, email, room_id, checkin, checkout)
```

### 🍴 Food Ordering

* Choose food item
* Enter quantity
* Enter customer details

```python
order_food(name, email, food, quantity)
```

---

## 📁 **Project Structure**

```
InnDine-Assistant/
│── ai_model.py
│── hotel_services.py
│── restaurant_services.py
│── main.py  (your Tkinter GUI code)
│── README.md
│── requirements.txt
```

---

## ▶️ **How to Run the Project**

### **1. Install Dependencies**

Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

Common requirements include:

```
tk
tensorflow / sklearn  (depending on your model)
mysql-connector-python (if you use MySQL)
```

---

### **2. Run the Application**

```bash
python main.py
```

The Tkinter window will launch with:

* Chat Section
* Room Booking Section
* Food Ordering Section

---

## 🧩 **How Intent Detection Works**

Your `ai_model.py` contains:

* A trained model (LSTM / Naive Bayes)
* `predict_intent(text)` returns one of:

```
check_availability
book_room
order_food
greeting
goodbye
unknown
```

---

## 🏗 **Backend Service Files**

### **hotel_services.py**

Handles:

* Checking room availability
* Booking rooms
* Database interactions if added

### **restaurant_services.py**

Handles:

* Food ordering logic
* Storing orders in database or variables

---

## 🎨 UI / UX — Purple Theme

The interface uses:

* Custom color palette
* Rounded cards
* Styled Combobox
* Emoji-based user experience
* Auto-scroll chat

---

## 🛠 Tech Stack

| Component           | Technology           |
| ------------------- | -------------------- |
| GUI                 | Tkinter              |
| ML / NLP            | TensorFlow / Sklearn |
| Backend             | Python               |
| Database (optional) | MySQL / SQLite       |
| Styling             | Custom theme         |

---

## 📌 Future Improvements

* Add live database support
* Add payment integration
* Add speech-to-text chat
* Improve LSTM training dataset
* Add admin dashboard

---

## 👤 Author

**Developer:** Sanjana Tasnim Prome
**Project:** InnDine Assistant (AI-powered hotel & restaurant bot)

---

## 📜 License

This project is open-source. You may modify and distribute.

---

**Enjoy building AI-powered hotel and restaurant management systems! 💜**
