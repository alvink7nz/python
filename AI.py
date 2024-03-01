import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

def semantic_search(query, documents):
    response = openai.Engine("davinci").search(
        documents=documents,
        query=query
    )
    return response['data']

# Example usage
query = "How does DNA work?"
documents = [
    "DNA is a molecule that carries the genetic instructions for growth, development, functioning, and reproduction in all known living organisms.",
    "The structure of DNA is a double helix, consisting of two long chains of nucleotides twisted around each other.",
    "DNA replication is the process by which DNA makes a copy of itself during cell division.",
    "DNA mutations can lead to changes in an organism's traits and can be inherited by offspring.",
    "Genes are segments of DNA that contain the instructions for building proteins, which perform various functions in the body."
]

results = semantic_search(query, documents)
for result in results:
    print("Document:", result['document'])
    print("Score:", result['score'])
    print()