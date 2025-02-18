import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

response = client.chat.completions.create(model='gpt-4o',
                                          messages=[
                                              {'role': 'user', 'content': '안녕하세요!'}
                                          ]
                                          )

print(response.choices[0].message.content)