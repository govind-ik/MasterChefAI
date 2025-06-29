from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from decouple import config
from langchain_core.messages import SystemMessage,HumanMessage

def func(data):
    gem_ai=config('GEM_API_KEY')
    llm=ChatGoogleGenerativeAI(google_api_key=gem_ai,model="gemini-1.5-flash",max_token=300)
    systemmsgprom=SystemMessagePromptTemplate.from_template("Your are a master chef and have to give recipe of the dish asked, try to be as concise as much and try to give response in minimum words and in case question is not related to food simply reply i don't know nothing else")
    hummsgprom=HumanMessagePromptTemplate.from_template('{asked_dish}')

    chatpromt=ChatPromptTemplate.from_messages([systemmsgprom,hummsgprom])

    format_chat=chatpromt.format_messages(
        asked_dish=data
    )
    response=llm.invoke(format_chat)

    return response.content


