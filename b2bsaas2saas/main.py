from openai import OpenAI
import os

# load environment variabkes
import dotenv
dotenv.load_dotenv()


def get_random_saas_idea():

    prompt = """
    Generate a B2B SaaS idea and describe it with 6-8 sentences. It should be as hype as possible, I don't really care 
    if it's technically very straightforward to do (e.g. a chatgpt wrapper). However, it should claim to solve a specific problem
    and be coherent enough to understand. The idea should have as many of the following qualities/keywords as possible to attract
    that sweet venture capital money (NOT necessarily ordered by importance):
    
    artificial intelligence (AI), machine learning (ML), deep learning (DL), natural language processing (NLP), 
    retrieval augmented generation (RAG), large language models (LLMs), foundational models, agentic AI, generative AI,
    multimodal AI, disruptive innovation, possibility to create shareholder value, context engineering
    """

    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an expert at B2B SaaS ideation."},
        {"role": "user", "content": prompt}
    ],
    temperature=1.2
    )

    print(completion.choices[0].message.content)

if __name__ == "__main__":
    a = get_random_saas_idea()