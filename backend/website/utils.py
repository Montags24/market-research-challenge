MESSAGES = [
    {
        "body": "Hi there 👋! Welcome to NextGenVoice! A platform to share your thoughts, drive change and win prizes along the way!",
        "responses": [],
    },
    {
        "body": "Before we get started, here's a short video on what to expect!",
        "responses": [],
    },
    {
        "body": "test_video.mp4",
        "responses": ["I've finished the video, let's continue!"],
    },
    {
        "body": "What's your favorite way to unwind after a long day?",
        "responses": [
            "Taking a hot bath",
            "Going for a walk",
            "Reading a book",
            "Watching TV shows",
            "Listening to podcasts",
            "Meditating",
        ],
    },
    {
        "body": "It was great getting to know you! Based on your responses, we'd love to get your thoughts on the following:",
        "responses": [],
    },
]

CHATBOT_MESSAGES = [
    {
        "id": i,
        "sender": "bot",
        "body": MESSAGES[i]["body"],
        "timestamp": None,
        "responses": MESSAGES[i]["responses"],
    }
    for i in range(len(MESSAGES))
]
