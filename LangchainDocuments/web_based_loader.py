from langchain_community.document_loaders import WebBaseLoader


url = "https://www.flipkart.com/mobile-phones-store"

loader = WebBaseLoader(url)

docs = loader.load()
print(docs)