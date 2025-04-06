from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# create a template1
prompt1 = PromptTemplate(
    template="Generate detailed report {topic}", 
    input_variables=["topic"]
)
# create  template2
prompt2 = PromptTemplate(
    template="Generate 5 pointer summary about {text}", 
    input_variables=["text"]
)
# create a model
model = ChatOpenAI()

# parser for output parsing
parser = StrOutputParser()

# create a chain
chain = prompt1 | model | parser | prompt2 | model | parser
res=chain.invoke({"topic": "unemployment in india"})
print(res)
chain.get_graph().print_ascii()