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

