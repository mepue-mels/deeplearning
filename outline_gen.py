"""
File: outline_gen.py

Description: Mainline script for generating outlines from prompts using t5-base

Dependencies:
    1. outline_model (contains pre-trained and fine-tuned model)
    2. preprocessor.py (formatting function for outputs)

Usage:
    Parameter/s: course (string)
    Returns: null
    Outputs: .txt file containing outline (name is the course title)
"""

def create_outline(course): #main entry function; takes in course as an input
    #boilerplate stuff
    from transformers import T5ForConditionalGeneration, T5Tokenizer
    from preprocessors import format_outline

    outline_buffer = [] #declares buffer array for outputting outline

    model_dir = './models/outline_model' #change if necessary

    model = T5ForConditionalGeneration.from_pretrained(model_dir)
    tokenizer = T5Tokenizer.from_pretrained(model_dir)

    #start modifying here
    for week_num in range(1,13): #iterate over week 1 to 12
        inputs = f"Generate an outline for week {week_num} in {course}"
        input_ids = tokenizer(inputs, return_tensors="pt", truncation=True, max_length=1024).input_ids

        outputs = model.generate(input_ids, max_length=256, do_sample=True, top_p=0.95, temperature=0.7)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        outline_buffer.append(format_outline(answer)) #push to buffer
        print(f"{week_num}/12 done") #indicates status during output generation

    #outputs as file (change if necessary)
    with open(f"{course}.txt", "w") as file:
        for x in outline_buffer:
            file.write(x + "\n")

    print(f"Output written to {course}.txt")
