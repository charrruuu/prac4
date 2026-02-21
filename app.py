from langchain.chat_models import init_chat_model
import os
os.environ['GOOGLE_API_KEY']=""
model = init_chat_model("gemini-2.5-flash-lite",model_provider="google_genai")
promptA="Suggest me a unique name for my cat"
promptB="give me one creative name for a white kitten"
responseA=model.invoke(promptA).content
responseB=model.invoke(promptB).content
print("Response A:", responseA)
print("Response B:",responseB)
