from email_service import send_email


test_receiver = "sanjanatasnim18@gmail.com"

subject = " Email Test from HotelChatbot"
message = (
    "Hello!\n\n"
    "This is a test email from your HotelChatbot system.\n"
    "If you received this, your email setup works perfectly! 🎉\n\n"
    "Best,\nHotelChatbot AI"
)


result = send_email(test_receiver, subject, message)
print(result)
