from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from config import OPENAI_API_KEY
import openai


class CVGenerator:
    def __init__(self, api_key: str = OPENAI_API_KEY):
        """
        Initializes the CVGenerator class with OpenAI API key and sets up LangChain components.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

        # Define the prompt template to create a one-page CV
        self.cv_prompt_template = """
        You are a skilled resume writer. Create a one-page CV based on the provided information. 
        The CV should be concise and formatted in a professional way, with sections like 'Name', 
        'Experience', 'Education', and 'Skills'. Ensure that the CV is well-organized and highlights 
        the most important details.

        Here is the information in plain text:
        {content}

        Output the CV in a readable format that would fit a single page.
        """

        self.llm = OpenAI()
        self.prompt = PromptTemplate(input_variables=["content"], template=self.cv_prompt_template)
        self.cv_chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def generate_cv(self, content: str) -> str:
        """
        Generates a CV from the provided content using LangChain.

        Args:
        content (str): The plain text content from the markdown file.

        Returns:
        str: The generated CV in plain text.
        """
        return self.cv_chain.run(content)
