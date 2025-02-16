# -*- coding: utf-8 -*-
"""T5 method.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M7ChmLYl5AHUbw9A3G_5J4emgf_ECepZ

**Run time type=TPU**
"""

!apt-get install tesseract-ocr -y
!pip install pytesseract

!pip install python-docx transformers

from google.colab import files
uploaded = files.upload()

#Extract the filename
file_name = list(uploaded.keys())[0]

import docx

# Function to extract text from a Word document
def read_word_file(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Specify the file path (this will be the uploaded file's name)
file_path = 'asal.docx'  # Replace with your actual filename
doc_content = read_word_file(file_path )

# Print the content (optional)
#print(doc_content)

""" **T5 (Text-to-Text Transfer Transformer)**







"""

from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the tokenizer and model for T5
tokenizer = T5Tokenizer.from_pretrained('t5-large')
model = T5ForConditionalGeneration.from_pretrained('t5-large')

# Define the question and the document content
question = "What is the main point of this paper?"
context = doc_content  # Ensure this is properly extracted from your document

# Format the input text for the model
input_text = f"question: {question} context: {context}"

# Tokenize the input
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

# Generate the output with a larger max_new_tokens (for a longer answer)
output_ids = model.generate(input_ids, max_new_tokens=1000)  # Adjust the token length

# Decode the output to a readable answer
answer = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Print the result
print(f"Answer: {answer}")