import gradio as gr
import tiktoken
from tokenizer import CustomTokenizer

# Initialize tokenizers
custom_tokenizer = CustomTokenizer("bpe_tok.model")
tiktoken_encoder = tiktoken.get_encoding("gpt2")

def encode_text(text):
    # Get encodings from both tokenizers
    custom_tokens = custom_tokenizer.encode(text, allowed_special={"<|endoftext|>"})
    tiktoken_tokens = tiktoken_encoder.encode(text)
    
    # Format output
    custom_output = f"Token count: {len(custom_tokens)}\nTokens: {custom_tokens}"
    tiktoken_output = f"Token count: {len(tiktoken_tokens)}\nTokens: {tiktoken_tokens}"
    
    return custom_output, tiktoken_output

# Create Gradio interface
iface = gr.Interface(
    fn=encode_text,
    inputs=gr.Textbox(lines=5, label="Enter text to tokenize"),
    outputs=[
        gr.Textbox(label="Custom Tokenizer Output", lines=4),
        gr.Textbox(label="Tiktoken Output", lines=4)
    ],
    title="Tokenizer Comparison",
    description="Compare custom BPE tokenizer with Tiktoken GPT-2 tokenizer",
    examples=[
        ["आज तो बहुत थक गया हूँ, ಸ್ವಲ್ಪ विश्रಾಂತಿ ಬೇಕು।"],
        ["मौसम कितना अच्छा है! ನೀವೂ ಹೊರಗೆ ಬನ್ನಿ, let's enjoy together."],
        ["My name is Jeff Bezos, and I'm the owner of Amazon.<|endoftext|>"]
    ]
)

if __name__ == "__main__":
    iface.launch() 