# ChatBot 6 : Local LLM Chatbot (TinyLlama)

## Features

- **Local LLM Inference:** Runs the TinyLlama language model locally using the Hugging Face Transformers library instead of relying on cloud-based APIs like OpenAI or Gemini.
- **No API Key Required:** Once the model is downloaded, the chatbot works without requiring an API key or internet connection.
- **Automatic Tokenization:** Uses `AutoTokenizer` to convert user prompts into tokens that can be processed by the language model.
- **Automatic Model Loading:** Uses `AutoModelForCausalLM` to download and load the TinyLlama chat model from Hugging Face.
- **GPU Acceleration:** Automatically loads the model onto the GPU if available using `device_map="auto"`; otherwise, it runs on the CPU.
- **Manual Conversation History:** Stores previous user and assistant messages in a Python list and manually builds the prompt before every generation.
- **Text Generation:** Generates responses using the model's `generate()` method with configurable generation parameters such as `temperature` and `max_new_tokens`.

---

## How this Chatbot Works

```text
          User Message
                │
                ▼
      Build Prompt from
   Conversation History
                │
                ▼
        AutoTokenizer
 (Convert Text → Tokens)
                │
                ▼
     TinyLlama Language Model
      (Local Inference)
                │
                ▼
      Generate Output Tokens
                │
                ▼
       Decode Tokens to Text
                │
                ▼
       Assistant Response
                │
                ▼
 Update Conversation History
```

---

## Improvements

- Runs Completely Offline
- No API Key Required
- Hugging Face Transformers
- Automatic Tokenization
- Local Model Inference
- GPU Acceleration Support
- Manual Conversation History
- Configurable Text Generation
- Lower Cost (No API Usage)

---

## Limitations

- Runs slower than cloud-hosted LLMs on CPU
- Model quality depends on the selected local model
- Manual prompt construction
- No LangChain integration
- No memory abstraction
- No streaming responses
- No vector database or RAG
- No tool/function calling
- Requires downloading the model before first use
