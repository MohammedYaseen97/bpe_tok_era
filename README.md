# Multilingual Tokenizer Comparison

A web application to compare tokenization between a custom multilingual BPE tokenizer and OpenAI's GPT-4 tokenizer.

## Live Demo

Try it out: [Huggingface Spaces Demo](https://huggingface.co/spaces/ace-1/bpe_tok)

## Features

- Supports multiple scripts:
  - Latin (English)
  - Devanagari (Hindi)
  - Kannada
- Shows token counts and IDs for both tokenizers
- Interactive web interface
- Example texts for comparison

## Tokenizer Details

### Overview

The custom tokenizer was developed using Byte Pair Encoding (BPE) with a custom regex pattern designed specifically for multilingual text. The development process included:

1. **Custom Regex for BPE Tokenization**: 
   - A specialized regex pattern that handles English, Hindi, and Kannada scripts
   - Carefully designed to preserve linguistic units in each script

2. **Training Corpus Composition**:
   - English (60%): From `HuggingFaceFW/fineweb-edu` dataset
   - Hindi (20%): From `ai4bharat/sangraha` dataset (Devanagari script)
   - Kannada (20%): From `ai4bharat/sangraha` dataset (Kannada script)
   - This distribution aligns with token distribution patterns observed in models like GPT-4

3. **Vocabulary Details**:
   - Total Size: 3257 tokens
   - Composition:
     - 256 byte-level tokens
     - 3000 merge operations
     - 1 special `<|endoftext|>` token
   - Achieves approximately 4.07x compression ratio

### Technical Implementation

The tokenizer implementation includes:
- Custom regex patterns for multilingual text segmentation
- BPE training with controlled merge operations
- Special token handling
- Efficient encoding/decoding mechanisms

## Installation

```bash
# Clone the repository
git clone https://github.com/MohammedYaseen97/bpe_tok_era.git
cd bpe_tok_era

# Install dependencies
pip install -r requirements.txt

# Run the app locally
python app.py
```

## Project Structure

```
├── app.py # Gradio web interface
├── tokenizer.py # Custom tokenizer implementation
├── bpe_tok.model # Trained tokenizer model
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```


## Development Process

The tokenizer development involved several key steps:

1. **Dataset Preparation**:
   - Careful selection of multilingual datasets
   - Balanced sampling to maintain script representation
   - Text cleaning and preprocessing

2. **Tokenizer Training**:
   - Custom regex pattern development
   - BPE training with controlled vocabulary growth
   - Optimization for multilingual support

3. **Performance Metrics**:
   - Compression ratio: 4.07x
   - Balanced token distribution across scripts
   - Efficient handling of mixed-script text

## Usage Examples

The tokenizer effectively handles various text combinations:
- Pure English text
- Pure Hindi text
- Pure Kannada text
- Mixed script text
- Special tokens and control characters

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request