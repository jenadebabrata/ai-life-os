from fastapi import FastAPI
from llm import generate_response
from memory import store_memory, retrieve_memory
from personality import get_personality_prompt

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Life OS running 🚀"}

@app.post("/chat")
def chat(user_input: str):
    memories = retrieve_memory(user_input)

    prompt = f"""
    {get_personality_prompt()}

    Relevant past memories:
    {memories}

    User: {user_input}
    """

    response = generate_response(prompt)

    store_memory(user_input + " " + response)

    return {"response": response}