# 📚 **BookCapsule**: *Unearth the Core of Knowledge in Minutes*

**BookCapsule** is an AI-driven book synopsis tool that distills complex text into its most essential insights and primary takeaways. With **BookCapsule**, you can quickly unpack the core of a book and save precious time without compromising comprehension.

## Key Features

- **Chapter-by-Chapter Summarization**: **BookCapsule** provides detailed summaries for each chapter, letting you concentrate on specific areas of interest.
- **Whole Book Synopsis**: In instances where the book doesn't have chapter divisions, **BookCapsule** condenses the entire text into a comprehensive overview.
- **Powered by Natural Language Processing (NLP)**: With cutting-edge NLP techniques at its core, **BookCapsule** intelligently processes the text, capturing the most pertinent and informative content.
- **Sleek User Interface**: **BookCapsule** features a clean and intuitive interface, making the summarization process smooth and user-friendly, regardless of technical proficiency.

## Workflow

**BookCapsule** exploits the `T5-small` pretrained model from HuggingFace Transformers to generate precise and readable summaries. The process unfolds as follows:

1. **Chunking**: The text of the book is segmented into chunks, either by chapter or as a whole.
2. **Tokenization**: The chunks are tokenized using the `T5Tokenizer` to be compatible with the `T5` model.
3. **Summary Generation**: The tokenized text is input into the `T5ForConditionalGeneration` model, which outputs summary token IDs.
4. **Decoding**: The summary token IDs are decoded back into intelligible text using the `T5Tokenizer`'s `decode()` function, resulting in the final summary.

## How to Begin

1. Clone the repository: `git clone https://github.com/DeanLJY/BookCapsule.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Launch the application: `python3 views.py`

For more detailed instructions and advanced usage, please refer to the source code.

## Contributing

We value contributions from the community! If you wish to contribute to **BookCapsule**, please feel free to submit a pull request or open an issue. Your feedback and support are greatly appreciated!

## License

**BookCapsule** is distributed under the [MIT License](https://github.com/FalloutOne/BookCapsule/blob/master/LICENSE).
