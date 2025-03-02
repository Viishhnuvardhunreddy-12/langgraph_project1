from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

generation_prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are with Twitter techy influencer assistant tasked with writing excellent Twitter posts."
            "Generate the best Twitter post possible for the user's request."
            "If the user provides critique, respond with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

reflection_prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral Twitter influencer creating a tweet.Generate critic and recommendations for the user tweet."
            "Always provide the detailed recommendations, including request for the length, virality, style, etc."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_chain=generation_prompt | llm
reflection_chain=reflection_prompt | llm