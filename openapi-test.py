from openai import OpenAI

#from text_2_Speech import text_2_Speech


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a sports reporter, who talks like an english premier league comentator like Robbie Mustoe. "},
    {"role": "user", "content": "Re-word the following in your words shortening it where possible and make it sound like spoken news report about the game. Dont include anything else in your response apart from the summary itself of the following: " + game_text}
  ]
)

print(completion.choices[0].message)