import openai
openai.api_key = ""  # Replace with your actual key

def generate_code(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-instruct",
                
            prompt=prompt,
            temperature=0.7,
            max_tokens=200
        )
        generated_code = response.choices[0].text.strip()
        return generated_code
    except Exception as e:
        return str(e)

def main():
    print("Welcome to the Text-based Code Generation AI!")
    print("Enter your prompts. Type 'exit' to quit.")

    while True:
        user_input = input("Enter your prompt: ")
        if user_input.lower() == 'exit':
            break
        generated_code = generate_code(user_input)
        print("Generated Code:")
        print(generated_code)
        print()

if __name__ == "__main__":
    main()
    

