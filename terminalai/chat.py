import google.generativeai as genai
from term_ai.config import API_KEY

genai.configure(api_key=API_KEY)


def get_response(input: str) -> str:
    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    model = genai.GenerativeModel(
        model_name="gemini-pro", generation_config=generation_config
    )

    prompt_parts = [
        f"You are linux shell assistant be less verbose, skip printing the command explanation.\nExample:\nquestion: Change directory\nanswer: cd \nquestion: List files\nanswer: ls\nquestion: Show file content\n answer: cat\nquestion: Get docker image \nanswer: docker pull\nquestion: {input} \nanswer:",
    ]
    response = model.generate_content(prompt_parts)
    return response.text


def read_input():
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    elif len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return " "
