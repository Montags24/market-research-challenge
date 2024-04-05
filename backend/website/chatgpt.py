import os
from dotenv import load_dotenv
from openai import OpenAI

this_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(this_directory, "../.env"))

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def generate_chatgpt_response(
    user_reply: str, previous_question: str, user_name: str = None
) -> str:
    # Construct prompt with user's name if provided
    if user_name:
        prompt = f"{previous_question} User ({user_name}): {user_reply}\nAI:"
    else:
        prompt = f"{previous_question} User: {user_reply}\nAI:"

    # Call OpenAI API to generate response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"End with a statement. Respond to {user_name if user_name else 'the user'} and avoid asking questions.",
            },
            {
                "role": "assistant",
                "content": prompt,
            },
        ],
        max_tokens=50,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    previous_question = "What do you usually enjoy doing in your free time?"
    previous_answer = input("User: ")
    response = generate_chatgpt_response(previous_answer, previous_question)
    print("AI:", response)
