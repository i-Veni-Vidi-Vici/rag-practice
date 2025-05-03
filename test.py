from langchain_core.prompts import load_prompt

prompt = load_prompt("prompts/general.yaml", "utf-8")
print(prompt)
