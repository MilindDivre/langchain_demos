from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
# create a template
prompt = PromptTemplate(
    template="Generate 5 intresting facts about {topic}", 
    input_variables=["topic"]
)
# create a model
model = ChatOpenAI()

# parser for output parsing
parser = StrOutputParser()

# create a chain
chain = prompt | model | parser

# invoke the chain  
res = chain.invoke({"topic": "ice cream"})  
print(res)
