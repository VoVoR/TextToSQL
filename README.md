<h1 align="center">TextToSQL Task</h1>
<h3 align="center">
A simple approach for automated prompting for <br/>
text-to-sql in-context learning<br/>
</h3>
<br/>

## LLM

### Fine-tunung (FT):

I would use Codegen-16b or StarCoder and spider dev set for fine-tuning.
Perhaps the data annotation will be needed for (FT)

### In-Context Learning (ICL):

I used GPT-4 GUI mostly. For proper evaluation it would be some API without rate limiters or local inference server with open-sourced models:
* LLama-65b
* falcon-40b-instruct
* Bloom
* Dolly-2
* Etc

## Eval

* [Spider](https://github.com/taoyds/spider)
* [Bird](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/bird)

### Metricies 

* Percentage of predictions which are valid SQL (VA)
* Execution accuracy (EX)
* Component Matching (CM)

## Roadmap

* [x] Dummy datasset in Clickhouse
* [x] Prompts implementation
* [x] GPT-4 call
* [x] Caching placeholder
* [ ] Eval
* [ ] Different LLMs experiments
* [ ] Prompts automation for random DB
* [ ] DB for cached queries, prompts and SQL results
* [ ] QDecomp as a separate LLM call
