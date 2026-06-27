"""
ConvoForge Conversation Manager
"""


class ConversationManager:

    def get_reply(self, message):
        text = message.lower()

        if text == "hello":
            return "Hello! Welcome to ConvoForge."

        if text == "help":
            return "How can I assist you today?"

        if text == "bye":
            return "Goodbye! Have a great day."

        return "I didn't understand that message."
