# LangChain Text Splitters Examples

This project demonstrates various ways to split large text/documents into smaller chunks using **LangChain**.  
It covers multiple splitting strategies, from simple length-based splitting to advanced semantic chunking.

## 📂 Project Overview

The project includes examples of the following splitters:

1. **Length-based Text Splitter**  
   - Splits text into fixed-size chunks based on character length.

2. **Recursive Character Text Splitter**  
   - Uses a list of separators and recursively splits text until it meets size constraints.

3. **Document-based Text Splitter**  
   - Works directly on `Document` objects loaded using LangChain document loaders.

4. **Recursive-based Text Split**  
   - Similar to recursive character splitting, but applied on structured data/documents.

5. **Semantic-based Splitter / Semantic Chunker**  
   - Uses embeddings to split text based on semantic meaning instead of fixed sizes.

---

## 📦 Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/yourusername/langchain-text-splitters.git
cd langchain-text-splitters
pip install -r requirements.txt
