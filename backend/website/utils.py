MESSAGES = [
    {
        "body": """Hi there 👋! Welcome to NextGenVoice!
        A social platform to share your thoughts, drive change and earn rewards along the way!""",
        "chatgpt_reply": False,
        "function": None,
        "response_required": False,
        "responses": [],
    },
    {
        "body": "Before we get started, here's a short video on what to expect!",
        "chatgpt_reply": False,
        "function": None,
        "response_required": False,
        "responses": [],
    },
    {
        "body": "test_video.mp4",
        "chatgpt_reply": True,
        "function": None,
        "response_required": True,
        "responses": ["I've finished the video, let's continue!"],
    },
    {
        "body": "First things first, we need to get to know you so we can provide you with the best experience!",
        "chatgpt_reply": False,
        "function": None,
        "response_required": False,
        "responses": [],
    },
    {
        "body": "What's your name?",
        "chatgpt_reply": False,
        "function": "updateName",
        "response_required": True,
        "responses": [],
    },
    {
        "body": "Awesome[name]!Let's select your avatar - please choose one that you resonate with the most",
        "chatgpt_reply": False,
        "function": "updateGender",
        "response_required": True,
        "responses": [
            "👨",
            "👩",
            "Prefer not to say",
        ],
    },
]

CHATBOT_MESSAGES = [
    {
        "id": i,
        "sender": "bot",
        "body": MESSAGES[i]["body"],
        "timestamp": None,
        "chatgpt_reply": MESSAGES[i]["chatgpt_reply"],
        "function": MESSAGES[i]["function"],
        "response_required": MESSAGES[i]["response_required"],
        "responses": MESSAGES[i]["responses"],
    }
    for i in range(len(MESSAGES))
]
