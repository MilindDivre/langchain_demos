from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from load_dotenv import load_dotenv
load_dotenv()

loader = WebBaseLoader("https://playwright.dev/python/")
docs=loader.load()
# print(docs[0])
# print(docs[0].page_content)


model= ChatOpenAI()

prompt = PromptTemplate(
    template="Generate a summary of the following text: {text}", 
    input_variables=["text"]
)
parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({"text": docs[0].page_content})
print("#################")
print(res)