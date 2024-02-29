import openai

# Set up your OpenAI API key
api_key = 'alvin'
openai.api_key = api_key

def generate_text(prompt, max_tokens=50, temperature=0.7):
    """
    Generate text based on the given prompt using OpenAI's GPT model.
    
    Parameters:
        prompt (str): The input prompt for text generation.
        max_tokens (int): Maximum number of tokens to generate.
        temperature (float): Controls the randomness of the generated text.
            Higher values make the text more diverse, lower values make it more conservative.
    
    Returns:
        str: Generated text.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose a different engine if desired
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()

# Example usage:
prompt = "Python is a versatile programming language used in many applications."
generated_text = generate_text(prompt)
print(generated_text)