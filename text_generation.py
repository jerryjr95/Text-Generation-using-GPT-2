# text_generation.py

from transformers import pipeline

# Load GPT-2 Text Generation Pipeline
generator = pipeline("text-generation", model="gpt2-medium", framework="pt")

def generate_gpt2_text(prompt):
    """
    Generate text using GPT-2 model based on input prompt.
    
    Args:
        prompt (str): Starting input text.
    
    Returns:
        str: Generated continuation text.
    """
    if not prompt.strip():
        return "⚠️ Please enter meaningful starting text."

    result = generator(
        prompt,
        max_length=250,
        num_return_sequences=1,
        temperature=0.5,
        top_p=0.9,
        do_sample=True,
        early_stopping=True
    )

    return result[0]['generated_text']
