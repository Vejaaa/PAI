import nltk
from nltk.chat.util import Chat, reflections
patterns = [
    (r'(.)Hi|hello(.)', ['How shall I assist you?']),
    (r'(.)admission|seats(.)', ['For admission inquiries, you can visit our website sahyadri.edu.in or contact the admission office.']),
    (r'(.)program|branches(.)', ['Our institution offers:\nAIML\nECE\nCSE\nISE\nMECHANICAL\nWhich program are you interested in?']),
    (r'(.)AIML(.)', ['Our institution offers AIML course for 180 students right now.']),
    (r'(.)ECE|EC(.)', ['Our institution offers ECE course for 120 students right now.']),
    (r'(.)CSE(.)', ['Our institution offers CSE course for 360 students right now.']),
    (r'(.)MECHANICAL(.)', ['Our institution offers Mechanical course for 60 students right now.']),
    (r'(.)ISE(.)', ['Our institution offers ISE course for 120 students right now.']),
    (r'(.)deadline|last date(.)', ['The admission deadline varies depending on the program. Please check our website for specific deadlines.']),
    (r'(.)contact|mail(.)', ['You can contact our admission office at admission@sahyadri.edu.in or call +918242277333.']),
    (r'(.)help(.)', ['How can I assist you further?']),
    (r'(.)(.)', ['I apologise. I am not able to understand what you want.']),
]
chatbot = Chat(patterns, reflections)
def admission_chat():
    print("Welcome to Sahyadri College Admission Chatbot. How can I assist you today?")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!Thank you for contacting us")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
admission_chat()