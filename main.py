from constants import schema
from prompts import gen_prompt_select_create_table_few, gen_prompt_question, gen_prompt_select, gen_prompt_Create_Table
from texttosql import gen_sql, add_index_and_cache


if __name__ == "__main__":
    question = "Which platform had the highest CPC in 2022: Google or Bing?"
    # prompt = gen_prompt_question(question)
    # prompt = gen_prompt_select(question, 3, None)
    # prompt = gen_prompt_Create_Table(question, schema)
    prompt = gen_prompt_select_create_table_few(question, 3, schema, 3)
    print(prompt)

    # sql = gen_sql(prompt)
    # add_index_and_cache("cache.index", question, prompt, sql)
