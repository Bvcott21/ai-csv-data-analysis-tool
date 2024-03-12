from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain.llms import OpenAI

def query_agent(data, query):
    #Parse the csv file and create a Pandas DataFrame from its contents.
    df = pd.read_csv(data)
    
    llm = OpenAI()
    
    # Create a Pandas DataFrame agent
    agent = create_pandas_dataframe_agent(llm, df, verbose = True)
    
    # Python REPL: A Python shell used to evaluating and executing Python cmds
    # It takes Python code as input and outputs the result. The input Python
    # code can be generated form another tool in the LangChain
    return agent.run(query)