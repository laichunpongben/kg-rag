# RAG System

Welcome to the RAG (Retrieval-Augmented Generation) system! This repository contains the code for a basic RAG system that integrates various tools to provide an interactive chat experience with retrieval-based context. This README will guide you through setting up and using the RAG system.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Starting the Application](#starting-the-application)
  - [API Endpoints](#api-endpoints)
  - [Testing the System](#testing-the-system)
- [Project Structure](#project-structure)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Overview

The RAG system is a chat application that enhances user interaction by incorporating retrieval-augmented generation. It uses a combination of FastAPI for serving the chat interface and Qdrant for vector storage to efficiently retrieve and synthesize responses based on the input queries.

## Features

- **Consolidating Data**: Integrates multiple data sources, retrieving relevant documents to create comprehensive responses.
- **Context-Aware Responses**: Uses a vector store to retrieve and incorporate relevant documents into responses, ensuring detailed and informed answers.
- **Chat Interface**: Interactive chat endpoint to handle user queries, providing a user-friendly way to access information.

## Architecture

The RAG system is built on a microservice architecture using the following components:

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs.
- **Qdrant**: A vector database for storing and querying embeddings.
- **Llama Index**: Used for indexing and retrieval of documents based on vector similarity.
- **Hugging Face Embeddings & Gemini**: Models used for embedding and language generation.

## Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.8+ (Tested with Python 3.12.3)
- pip (Python package installer)
- `qdrant-client` for interacting with Qdrant

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/laichunpongben/kg-rag.git
cd kg-rag
pip install -r requirements.txt
```

### Configuration
Set up the configuration files:

rag/configs/secret.py: Create this file and add your Qdrant API key and host details.
```
QDRANT_HOST = "your-qdrant-host"
QDRANT_API_KEY = "your-qdrant-api-key"
QDRANT_COLLECTION_NAME = "your-collection-name"
GOOGLE_API_KEY = "your-google-api-key"
```

## Usage
### Starting the Application
Start the FastAPI application using uvicorn:
```
uvicorn app:app --reload
```
The application will be available at http://127.0.0.1:8000.


### API Endpoints

Chat Endpoint: 
POST /chat: Sends a message and receives a response.

Request:
```
{
  "message": "Your query here"
}
```
Response:
```
{
  "utterance": "Response from the chat system"
}
```
Reset Endpoint: 
POST /reset: Resets the chat state.

Response:
```
{
  "status": true
}
```

### Testing the System
You can test the chat functionality directly within the Python environment:

```
from rag.rag import RAG
import asyncio

async def test_chat():
    rag = RAG()
    response = await rag.chat("Hello!")
    print(response)
    await rag.reset()

asyncio.run(test_chat())
```

## Project Structure
```
project_root/
│
├── app.py                      # FastAPI application
├── rag/
│   ├── rag.py                  # Core RAG logic
│   ├── settings.py             # Configuration settings
│   ├── prompt_template.py      # Prompt templates for chat and QA
│   └── indexer.py              # Document indexing script
├── log_conf.yaml               # Logging configuration
├── requirements.txt            # Python dependencies
└── README.md                   # This README file
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to adhere to the existing code style and include tests where appropriate.

## License
This project is licensed under the MIT License. See the LICENSE file for details.