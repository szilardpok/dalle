import os
import openai

import os
import openai
import pprint
import tiktoken

tiktoken.get_encoding("cl100k_base")
tiktoken.encoding_for_model("gpt-3.5-turbo")

openai.api_key = "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"

role = "Egy 20 év tapasztalattal rendelkező RENDKÍVÜL INNOVATÍV ÉS KREATÍV IT szakember vagy. " \
       "Hatékonyan tervezel meg projekteket, kreatív ötleteket találsz ki, " \
       "az architektúrákat közel tökéletesen tervezed, és a megvalósítás is jól megy."

messages_ = [
    {"role": "system", "content": role}
]

messages_strings = [
    role
]


def num_tokens_from_string(string, encoding_name='cl100k_base'):
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def chat(message):
    messages_.append({"role": "user", "content": message})
    messages_strings.append(message)
    new_string = ''
    for item in messages_strings:
        new_string = '\n'.join(item)
    if num_tokens_from_string(new_string) > 4000:
        messages_.clear()
        messages_.append({"role": "system", "content": role})
        messages_strings.append(role)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_
    )
    messages_.append({"role": "assistant", "content": response["choices"][0]["message"].content})
    return response.choices[0]["message"].get('content')


print('************* KAPCSOLAT LÉTREHOZVA *************')
print('Jöhetnek a promptok.')

__exit__ = 0
while __exit__ == 0:
    u_message = input('')

    if u_message == '__exit__':
        __exit__ = 1
        break
    else:
        pprint.pprint((chat(u_message)))



