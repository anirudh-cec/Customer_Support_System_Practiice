from config.config_loader import load_config
config = load_config()
collection_name = config["astra_db"]["collection_name"]
embedding_model_name = config["embedding_model"]["model_name"]
top_k = config["retriever"]["top_k"]
print(f"Collection Name: {collection_name}")
print(f"Embedding Model Name: {embedding_model_name}")
print(f"Top K: {top_k}")
