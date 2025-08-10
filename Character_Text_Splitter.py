from langchain.text_splitter import CharacterTextSplitter 
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"F:\projects for job\Generative AI\Text_Splitter\Psychophysiology 8.2 Electrocortical measures.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=''
)

result = splitter.split_documents(docs)

print(result[6].page_content)
print(result[6].metadata)
