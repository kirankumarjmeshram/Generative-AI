from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"     # Automatically puts model on GPU if available
)

print("Chatbot is ready!\n")

def chat():
    history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Bye!")
            break

        # Build a very simple prompt
        prompt = ""
        for turn in history:
            prompt += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n"

        prompt += f"User: {user_input}\nAssistant:"

        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        output = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
        )

        response = tokenizer.decode(output[0], skip_special_tokens=True)

        # Extract only the last assistant message
        assistant_reply = response.split("Assistant:")[-1].strip()

        print(f"Chatbot: {assistant_reply}\n")

        history.append({"user": user_input, "assistant": assistant_reply})


# Start chat
chat()
