# BPE Tokenization with Custom Regex

This notebook demonstrates the process of training a Byte Pair Encoding (BPE) tokenizer using a custom regex pattern. The tokenizer is designed to handle multilingual text, specifically English, Hindi, and Kannada. The notebook includes steps for tokenization, vocabulary building, and encoding/decoding of text.

## Overview

The notebook is structured into several key sections:

1. **Custom Regex for BPE Tokenization**: 
   - A custom regex pattern is defined to tokenize text in English, Hindi, and Kannada. This pattern is used to split text into tokens that are then processed by the BPE algorithm.

2. **Dataset Loading**:
   - Datasets from Hugging Face are loaded for English, Hindi (Devanagari script), and Kannada. These datasets are used to create a corpus for training the tokenizer.

3. **Corpus Preparation**:
   - Texts from the datasets are concatenated into a single corpus, which is then saved to a file. This corpus serves as the input for training the BPE tokenizer.

4. **Utility Functions**:
   - Functions are defined to handle control characters, visualize tokens, and manage token rendering.

5. **Training BPE**:
   - The BPE algorithm is trained on the prepared corpus. The process involves iteratively merging the most frequent pairs of tokens until the desired vocabulary size is reached.

6. **Vocabulary and Model Saving**:
   - The trained vocabulary and model are saved to disk for later use. The vocabulary consists of 3257 tokens, which includes:
     - 256 byte-level tokens
     - 3000 merge operations
     - 1 special `<|endoftext|>` token

7. **Encoding and Decoding**:
   - Functions are provided to encode text into token IDs and decode token IDs back into text. Special tokens are handled as part of this process.

8. **Testing**:
   - The tokenizer is tested on sample texts to verify its performance and compression ratio.

## Key Details

- **Vocabulary Size**: The final vocabulary size is set to 3257 tokens (256 byte tokens + 3000 merges + 1 `<|endoftext|>` token).
- **Tokenizer Training Corpus Composition**: The training corpus is constructed by combining texts from multiple datasets with the following distribution:
  - `HuggingFaceFW/fineweb-edu` (English): 60% of the corpus, aligning with the token distribution patterns observed in advanced language models like GPT-4, where English tokens constitute a significant majority
  - `ai4bharat/sangraha` (Hindi - Devanagari script): 20% of the corpus
  - `ai4bharat/sangraha` (Kannada - Kannada script): 20% of the corpus
- **Compression Ratio**: The compression ratio achieved by the BPE tokenizer is approximately 4.07x, indicating the efficiency of the tokenization process in reducing the size of the text representation.

## Usage

To use the tokenizer, load the saved model and vocabulary files, and utilize the provided encoding and decoding functions to process text. The tokenizer is capable of handling multilingual text and special tokens, making it suitable for diverse applications.

## Conclusion

This notebook provides a comprehensive guide to training a BPE tokenizer with custom regex patterns for multilingual text. The process includes dataset preparation, tokenization, vocabulary building, and model saving, offering a robust solution for text processing tasks.