import openai

openai.api_key = "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"


text = input("What's the course? ")

process = openai.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content": f"generate a 25 token peanut sized prayer point about {text}, it must ne no more than 25 tokens! make it simple, short heartfelt and direct. Emphhasis on simplicity"}])

output = process.choices[0].message.content

print(output)
