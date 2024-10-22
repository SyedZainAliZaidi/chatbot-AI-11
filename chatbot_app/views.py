from django.shortcuts import render




class Node:
    def __init__(self, question, response):
        self.question = question
        self.response = response
        self.left = None
        self.right = None

class Chatbot:
    def __init__(self):
        self.root = None
    
   
    def insert(self, question, response):
        if self.root is None:
            self.root = Node(question, response)
        else:
            self._insert(self.root, question, response)
    
    def _insert(self, current, question, response):
        if question < current.question:
            if current.left is None:
                current.left = Node(question, response)
            else:
                self._insert(current.left, question, response)
        elif question > current.question:
            if current.right is None:
                current.right = Node(question, response)
            else:
                self._insert(current.right, question, response)
    
    
    def get_response(self, question):
        return self._search(self.root, question)
    
    def _search(self, current, question):
        if current is None:
            return "Sorry, I don't understand that question."
        if question == current.question:
            return current.response
        elif question < current.question:
            return self._search(current.left, question)
        else:
            return self._search(current.right, question)


chatbot = Chatbot()
chatbot.insert("hello", "Hi there! How can I help you today?")
chatbot.insert("how are you", "I'm just a bot, but I'm doing great!")
chatbot.insert("what is your name", "I'm a simple chatbot!")
chatbot.insert("bye", "Goodbye! Have a great day!")


def chatbot_response(request):
    user_input = request.GET.get('message')  
    response = ""

    if user_input:  
        response = chatbot.get_response(user_input.lower())

    return render(request, 'chat.html', {'response': response})