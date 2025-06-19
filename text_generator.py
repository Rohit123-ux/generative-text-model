from transformers import pipeline, set_seed

# Create a text generation pipeline using GPT-2
generator = pipeline("text-generation", model="gpt2")
set_seed(42)  # Optional: Makes output repeatable

# Define your topic or prompt
prompt = "The impact of artificial intelligence on education"

# Generate text
result = generator(prompt, max_length=100, num_return_sequences=1)

# Print the result
print("\nGenerated Text:\n")
print(result[0]['generated_text'])
