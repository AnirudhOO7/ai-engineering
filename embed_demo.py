from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "How do I reset my password?",
    "I forgot my login credentials",
    "Best pizza in Rome",
    "How do I reset my watch?",
    "The spy whispered the password to enter the secret club"
]

vectors = model.encode(sentences)
print("Vector length:", len(vectors[0]))

print("pw vs login:", util.cos_sim(vectors[0], vectors[1]).item())
print("pw vs watch:", util.cos_sim(vectors[0], vectors[3]).item())
print("pw vs spy:", util.cos_sim(vectors[0], vectors[4]).item())