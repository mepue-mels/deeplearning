from transformers import T5ForConditionalGeneration, T5Tokenizer
from preprocessors import format_outline

model_name = './outline_model'

model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

inputs = input()
input_ids = tokenizer(inputs, return_tensors="pt", truncation=True, max_length=1024).input_ids

outputs = model.generate(input_ids, max_length=256, do_sample=True, top_p=0.95, temperature=0.7)
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)


print(format_outline(answer))

