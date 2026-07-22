from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents= [ 
  "Virat Kohli is one of the greatest batsmen in international cricket.",

"Rohit Sharma is known as the Hitman for his explosive batting.",

"KL Rahul is a versatile Indian batsman and wicketkeeper.",

"Jasprit Bumrah is famous for his deadly yorkers and unique bowling action."
]
query="Which Indian cricketer is known as versatile Indian batsman and wicketkeeper?"

doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding],doc_embeddings)[0]
index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:",score)