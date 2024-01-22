from openai import OpenAI  

def text_2_comentary(game_text):
    client = OpenAI()
    print("attempting to summarise text: " + game_text)
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a sports reporter, who talks like an english premier league comentator like Robbie Mustoe. "},
        {"role": "user", "content": "Re-word the following in your words shortening it where possible and make it sound like spoken news report about the game. Dont include anything else in your response apart from the summary itself of the following: " + game_text}
    ]
    )

    return completion.choices[0].message