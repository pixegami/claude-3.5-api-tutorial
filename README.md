# Claude 3.5 Sonnet API Tutorial

## Overview

This project serves as a comprehensive tutorial on how to use the Claude 3.5 Sonnet API. It demonstrates three distinct use cases:

1. Quick Start: Basic API call
2. Tool Use: Creating and utilizing custom tools
3. Image Analysis: Loading and analyzing images

Each use case is implemented in a separate Python script, providing practical examples of interacting with the Claude 3.5 Sonnet API.

## Setting Up

### Environment and Requirements

1. Ensure you have Python 3.7 or later installed on your system.
2. Clone this repository to your local machine.
3. Install the required packages by running:

```sh
pip install -r requirements.txt
```

The `requirements.txt` file includes:

- `anthropic`: The official Anthropic Python client
- `pytest`: For running unit tests (used in the tool use example)

### Setting up the API Key

To use the Claude 3.5 Sonnet API, you need to set up your API key:

1. Sign up for an account at [https://www.anthropic.com](https://www.anthropic.com) if you haven't already.
2. Obtain your API key from the Anthropic dashboard.
3. Set the API key as an environment variable:

```
export ANTHROPIC_API_KEY='your_api_key_here'
```

Alternatively, you can set the API key in your Python script:

```python
import anthropic
client = anthropic.Anthropic(api_key='your_api_key_here')
```

## 1. Quick Start

The `1_claude_quickstart.py` script demonstrates how to make a basic API call to Claude 3.5 Sonnet.

Key points:

- Imports the `anthropic` library
- Creates an `Anthropic` client
- Sends a message to the API with specific parameters
- Prints the response

To run:

```
python 1_claude_quickstart.py
```

This script sets Claude as a world-class poet and asks it to explain why the ocean is salty in the form of a short poem.

## 2. Tool Use

The `2_claude_tool_use.py` script showcases how to create and use custom tools with Claude 3.5 Sonnet.

### Creating Tool Functions

Tool functions are defined in `tools.py`:

- `list_artifacts()`: Lists all files in the `./artifacts/` directory
- `save_artifact(content, filename)`: Saves content to a file in the `./artifacts/` directory
- `load_artifact(filename)`: Loads content from a file in the `./artifacts/` directory

### Defining Tool Schemas

Tool schemas are JSON files in the `tool_schema/` directory:

- `list-artifacts.json`
- `save-artifact.json`
- `load-artifact.json`

These schemas define the input and output structure for each tool.

### Using Tools with Claude

The script demonstrates how to:

1. Load tool schemas
2. Create a message with tool use capabilities
3. Handle tool use responses
4. Process tool outputs

To run:

```sh
python 2_claude_tool_use.py
```

This script uses Claude to write a Python program that adds two numbers and creates a unit test for it, demonstrating file creation and manipulation through custom tools.

You should find the files being generated into the `./artifacts` folder. You can even run the test with:

```sh
pytest
```

## 3. Image Analysis

The `3_claude_vision.py` script shows how to load a local image and send it to the Claude API for analysis.

Key steps:

1. Load and encode an image file to base64
2. Create a message with both text and image content
3. Send the message to the Claude API
4. Process and display the response

To run:

```sh
python 3_claude_vision.py
```

This script loads an image of an AWS Lambda pricing table and asks Claude to generate a markdown table of the pricing information and model the cost for different numbers of users.
