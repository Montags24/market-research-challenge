import uuid


class Question:
    def __init__(
        self,
        body,
        chatgpt_reply=False,
        function=None,
        response_required=False,
        responses=None,
    ):
        self.id = uuid.uuid4()
        self.body = body
        self.chatgpt_reply = chatgpt_reply
        self.function = function
        self.response_required = response_required
        self.responses = responses or []

    def to_dict(self):
        return {
            "id": self.id,
            "body": self.body,
            "chatgpt_reply": self.chatgpt_reply,
            "function": self.function,
            "response_required": self.response_required,
            "responses": self.responses,
        }


class QuestionBank:
    def __init__(self, questions):
        self.questions = questions

    def to_list(self):
        return [question.to_dict() for question in self.questions]


WELCOME_QUESTIONS = [
    Question(
        """Hi there 👋! Welcome to NextGenVoice!
        A social platform to share your thoughts, drive change and earn rewards along the way!"""
    ),
    Question(
        """Please sign in, we don't want to lose your progress!""",
    ),
    Question(
        """Once you're done, send a reply :)""",
        response_required=True,
        responses=["All done, let's go!"],
    ),
]

INITIAL_SURVEY_QUESTIONS = [
    Question(
        "Nice one! Before we get started, here's a short video on what to expect!"
    ),
    Question(
        "test_video.mp4",
        chatgpt_reply=True,
        response_required=True,
        responses=["I've finished the video, let's continue!"],
    ),
    Question(
        """To recap:\n🔥 earns you rewards!\n Your multiplier increases over time, meaning you earn rewards faster!""",
        response_required=True,
        responses=["Sounds good!"],
    ),
    Question(
        "First a bit of admin - we need to get to know you so we can provide you with the best experience!"
    ),
    Question(
        "What's your gender?",
        response_required=True,
        responses=["Female", "Male", "Another gender", "Prefer not to say"],
    ),
    Question(
        "And how old are you?",
        response_required=True,
        responses=["16-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    ),
    Question(
        "That's it for the admin, let's get started!",
    ),
]

AGE_GROUP_16_24 = [
    Question(
        """Based on a YouGov poll, the most important issues facing 16-24yr olds are the economy 💰,
        health 💉 and housing 🏠.Fancy delving deeper into one of these topics?""",
        chatgpt_reply=True,
        response_required=True,
        responses=["Economy", "Health", "Housing", "I'd like some more options"],
    ),
]

ECONOMY_SURVEY_QUESTIONS = []


QUESTION_BANK = {
    "welcome_question_bank": QuestionBank(WELCOME_QUESTIONS).to_list(),
    "initial_survey_question_bank": QuestionBank(INITIAL_SURVEY_QUESTIONS).to_list(),
}
