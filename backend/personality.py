personality = {
    "tone": "supportive",
    "style": "concise"
}

def get_personality_prompt():
    return f"You are an AI assistant with a {personality['tone']} tone and {personality['style']} style."