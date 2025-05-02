import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from config.config_loader import load_config


class ModelLoader:
    """
    Utility class to load embedding models and LLM models
    """

    def __init__(self):
        load_dotenv()
        self._validate_env()
        self.config= load_config()

    def _validate_env(self):
       """Validate Necessage environment variables"""
       required_vars = ["GOOGLE_API_KEY"]

       missing_vars = [var for var in required_vars if not os.getenv(var)]
       if missing_vars:
           raise EnvironmentError(f"Missing Environment variables : {missing_vars}")
       
    def load_embeddings(self):
        """Loads the embedding model"""
        print("Loading Embedding Model...")
        embedding_model = self.config["embedding_model"]["model_name"]
        return GoogleGenerativeAIEmbeddings(model=embedding_model)
    
    def load_llm(self):
        """Loads the LLM Model"""
        print("Loading LLM Model...")
        model_name = self.config["llm"]["model_name"]
        gemini_model = ChatGoogleGenerativeAI(model=model_name)
        return gemini_model