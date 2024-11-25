'''import transformers
from transformers import pipeline

## Translator spanish to english ##
model_name = 'Helsinki-NLP/opus-mt-es-en'
input_text = "Este curso sobre LLMs se está poniendo muy interesante"

# Define pipeline for Spanish-to-English translation
translator = pipeline("translation_es_to_en", model=model_name)

# Translate the input text
translations = translator(input_text)

# Access the output to print the translated text in English
print(translations[0]['translation_text'])


## Response generation ##
generator = pipeline(task="text-generation", model="gpt2")
response = "Dear valued customer, I am glad to hear you had a good stay with us."

# Complete the prompt
prompt = f"Customer review:\n{text}\n\nHotel reponse to the customer:\n{response}"

# Pass the prompt to the model pipeline
outputs = generator(prompt, max_length=150, pad_token_id=generator.tokenizer.eos_token_id)

# Print the generated text
print(outputs[0]['generated_text'])'''


