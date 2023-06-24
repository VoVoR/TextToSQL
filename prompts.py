from constants import few_shot, select, schema
from sentence_transformers import SentenceTransformer
from faiss import IndexFlatL2


def gen_prompt_question(question):
    """Question-based intuitive prompting

    Example: https://arxiv.org/pdf/2204.00498.pdf (Appendix C)
    Args:
        question (str): initial user's query
    """

    prompt = f"-- Using valid SQL, answer the following questions. \n-- {question} \n SELECT"
    return prompt


def gen_prompt_API_Docs(question, docs):
    """API Docs-based prompt (if you have such)

    Example: https://arxiv.org/pdf/2204.00498.pdf (Appendix C)
    Args:
        question (str): initial user's query
        docs (str): short description of DB's properties
    """
    prompt = f"### Clickhouse DB tables, with their properties:\
            {docs} \
            ### {question}\
            SELECT "
    return prompt


def gen_prompt_select(question, k, db=None):
    """Prompt with k rows for each table with example data

    Example: https://arxiv.org/pdf/2204.00498.pdf (Appendix C)
    Args:
        question (str): initial user's query
        k (int): n_rows of tables examples to append in prompt (considering input_len limits)
        db (clickhouse_connect.driver.httpclient.HttpClient): db's connection or instance for gathering k rows of each table
    """
    prompt = f"/*\n{k} example rows from table agency_data:\nSELECT TOP {k} * FROM agency_data;\nTable: agency_data\n"
    prompt += "\n".join(select[0:k+1])
    prompt += "\n*/\n\n"
    prompt += f"-- Using valid SQL, answer the following questions.\n-- {question}\nSELECT"
    return prompt


def gen_prompt_Create_Table(question, schema):
    """Prompt starting with tables schemas 

    Example: https://arxiv.org/pdf/2204.00498.pdf (Appendix C)
    Args:
        question (str): initial user's query
        schema (str): SQL commands that create all tables
    """
    prompt = ""
    prompt += schema
    prompt += f"\n-- Using valid SQL, answer the following questions for the tables provided above.\n-- {question}\nSELECT"
    return prompt


def gen_prompt_select_create_table_few(question, k, schema, n, db=None, few=None):
    """ Prompt for few-shot(n). It starts with the schema and k example rows per database

    Example: https://arxiv.org/pdf/2204.00498.pdf (Appendix C)
    Args:
        question (str): initial user's query
        k (int): n_rows of tables examples to append in prompt (considering input_len limits)
        db (clickhouse_connect.driver.httpclient.HttpClient): db's connection or instance for gathering k rows of each table
        schema (str): SQL commands that create all tables
        n (int): number of example for few-shot prompting. Ideally with COT (chain-of-thoughts) explanation
    """
    prompt = ""
    prompt += schema
    prompt += f"\n/*\n{k} example rows from table agency_data:\nSELECT TOP {k} * FROM agency_data;\nTable: agency_data\n"
    prompt += "\n".join(select[0:k+1])
    prompt += "\n*/\n\n"
    if few:
        prompt += few
    else:
        prompt += "".join(few_shot[:n])

    prompt += f"-- {question} \n SELECT"
    return prompt


def gen_prompt_API_Docs_qdecomp(question, docs):
    """API Docs-based prompt (if you have such) with question decomposition (QDecomp) and InterCOL

    Example: https://arxiv.org/pdf/2305.14215.pdf (Appendix A)
    Args:
        question (str): initial user's query
        docs (str): short description of DB's properties
    """
    # TODO: QDecomp with InterCOL implementation
    prompt = f"### Clickhouse DB tables, with their properties:\
            {docs} \
            ### {question}\
            SELECT "
    return prompt


def retrive_few_shot(question, index, n):
    """Search for the most semantically similar queries in cache file

    Args:
        question (str): initial user's query
        index (faiss.index): faiss index instance
        n (int): number of example for few-shot prompting. Ideally with COT (chain-of-thoughts) explanation
    """
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L12-v2")
    embedding = model.encode(question)
    neighbours = index.search(embedding, n)
    # TODO: Create storage for queries and final result
    return neighbours
