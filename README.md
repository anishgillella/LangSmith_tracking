# LangSmith_tracking

# Langchain and Langsmith Python Examples

This repository contains two Python scripts demonstrating the usage of the Langchain and Langsmith libraries for handling and evaluating language models.

## Overview

The repository includes two main files:
- `langchain_example.py`: This file shows how to use Langchain to interact with OpenAI's language model, specifically for processing and responding to user input based on a given context.
- `langsmith_evaluation.py`: This script demonstrates how to use Langsmith for setting up a simple evaluation experiment for language models.

## Setup

Before running the scripts, you need to install the required libraries and set up the necessary environment variables.

### Requirements
- Python 3.x
- `langchain-openai`
- `langsmith`
- `python-dotenv`

You can install the necessary Python packages using pip:

```bash
pip install langchain-openai langsmith python-dotenv
```

### Environment Variables

Both scripts require certain environment variables to be set. Create a `.env` file in the root of this repository with the following variables:

```plaintext
OPENAI_API_KEY='your_openai_api_key_here'
LANGCHAIN_API_KEY='your_langchain_api_key_here'
```

## Files Description

### `langchain_example.py`

This script sets up a prompt using `ChatPromptTemplate` and processes it through the OpenAI model configured with Langchain tracking enabled. It outputs the model's response to a predefined question and context.

#### Running the Script

To run the script, use the following command:

```bash
python langchain_example.py
```

### `langsmith_evaluation.py`

This file demonstrates how to set up and run a simple evaluation using Langsmith. It creates a dataset, defines a basic evaluation function, and evaluates a hardcoded AI system based on exact match criteria.

#### Running the Script

To run the evaluation script, use the following command:

```bash
python langsmith_evaluation.py
```

## Contributing

Feel free to fork this repository and contribute by submitting pull requests or creating issues for bugs and feature requests.
