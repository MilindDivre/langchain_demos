from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch,RunnableLambda

load_dotenv()

# create a model
model = ChatOpenAI()
parser = StrOutputParser()



# now you want the res should always be positive or negative
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="The sentiment of the feedback.")
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# create a template
prompt = PromptTemplate(
    template="Generate a senitimate for the given feedback {feedback} \n {format_instructions}", 
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

# create a chain
classifier_chain = prompt | model | parser2
# res=classifier_chain.invoke({"feedback": "This is a slow movie"})
# print(res)

prompt2 = PromptTemplate(
    template="write an appropriate response for the positive feedback {feedback} ",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="write an appropriate response for the negative feedback {feedback} ",
    input_variables=["feedback"]
)
# creat a branch chain
branch_chain = RunnableBranch(
    # (condition,chain)
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "No feedback"),
)

# invoke the chain  
chain = classifier_chain | branch_chain
res = chain.invoke({"feedback": "This is a slow movie"})
print(res)

