# import openai

# openai.api_key = "key"

# messages=[]
# question= input("ask a question: ")
# messages.append({"role":"system", "content":question})

# print("your new assistant is ready!")
# while input != "quit()":
#     message = input()
#     messages.append({"role":"user", "content":message})
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages)
#     reply= response["choices"][0]["message"]["content"]
#     messages.append({"role": "assistant", "content": reply})
#     print("\nBOT:" + reply +"\n")


import openai
import gradio

openai.api_key = "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"

messages=[]

def CustomChatGpt(user_input):
    messages.append({"role":"system", "content":user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    chatgpt_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chatgpt_reply})
    return chatgpt_reply

demo = gradio.Interface(fn=CustomChatGpt, inputs="text", outputs="text", title="Chatbot")
demo.launch(share=True)