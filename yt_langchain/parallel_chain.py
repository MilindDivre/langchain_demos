from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
load_dotenv()

# create prompt1
prompt1 = PromptTemplate(
    template="Summarize the topic {topic}", 
    input_variables=["topic"]
)
# create prompt2
prompt2 = PromptTemplate(
    template="generate 5 questions along with answers {topic}", 
    input_variables=["topic"]
)
# create prompt3
prompt3 = PromptTemplate(
    template="Merge the detailed report and generate quiz along with answers \n {report} \n {quiz}", 
    input_variables=["report", "quiz"]
)
# create a model
model = ChatOpenAI()

# parser for output parsing
parser = StrOutputParser()

# create a chain
parallel_chain = RunnableParallel(
    {
        'report': prompt1 | model | parser,  
        'quiz': prompt2 | model | parser
    }
)

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain
text = """Powered by type hints — with Pydantic, schema validation and serialization are controlled by type annotations; less to learn, less code to write, and integration with your IDE and static analysis tools. Learn more…
Speed — Pydantic's core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python. Learn more…
JSON Schema — Pydantic models can emit JSON Schema, allowing for easy integration with other tools. Learn more…
Strict and Lax mode — Pydantic can run in either strict mode (where data is not converted) or lax mode where Pydantic tries to coerce data to the correct type where appropriate. Learn more…
Dataclasses, TypedDicts and more — Pydantic supports validation of many standard library types including dataclass and TypedDict. Learn more…
Customisation — Pydantic allows custom validators and serializers to alter how data is processed in many powerful ways. Learn more…
Ecosystem — around 8,000 packages on PyPI use Pydantic, including massively popular libraries like FastAPI, huggingface, Django Ninja, SQLModel, & LangChain. Learn more…
Battle tested — Pydantic is downloaded over 70M times/month and is used by all FAANG companies and 20 of the 25 largest companies on NASDAQ. If you're trying to do something with Pydantic, someone else has probably already done it. Learn more…"""
result=chain.invoke({"topic": text})
print(result)