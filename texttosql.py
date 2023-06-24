import openai
import faiss
from sentence_transformers import SentenceTransformer


def gen_sql(prompt):
    answer = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # model="gpt-4"
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    return answer


def add_index_and_cache(index, question, prompt, sql):
    """Save correct 

    Args:
        index (_type_): _description_
        question (_type_): _description_
        prompt (_type_): _description_
        sql (_type_): _description_
    """
    # TODO: index read/write/update
    # write_index, read_index
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L12-v2")
    embedding = model.encode(question)
    index = faiss.read_index()
    index.add(embedding)
