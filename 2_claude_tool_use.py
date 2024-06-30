"""
Demo script to show how to use Claude with tools. We've created the tools in tools.py and loaded the tool schema in this script. We'll use the tools to save and load files in the local filesystem. The demo itself will create some new Python files, load them, and create a simple test case for them files.
"""

import anthropic
from tools import TOOLS_SCHEMA, use_tool

client = anthropic.Anthropic()


def send_message(new_message: str, messages_history: list[dict] = []):
    new_message_block = {
        "role": "user",
        "content": [{"type": "text", "text": new_message}],
    }
    return send_message_block(
        new_message_block=new_message_block, messages_history=messages_history
    )


def send_message_block(new_message_block: dict, messages_history: list[dict] = []):
    messages = messages_history.copy()
    messages.append(new_message_block)
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        system="You are a coding assistant. Help the user by working closely with the code artifacts (saving new files, loading existing files, etc.).Before answering, explain your reasoning step-by-step in tags.",
        tools=TOOLS_SCHEMA,
        messages=messages,
    )

    # Print the response.
    response_text = response.content[0].text
    print(f"\n✨ System Response: {response_text}\n")

    # Append the message to the history.
    response_block = {
        "role": "assistant",
        "content": response.content,
    }
    messages.append(response_block)

    if response.stop_reason == "tool_use":
        tool_use_content = next(
            block for block in response.content if block.type == "tool_use"
        )
        tool_output = use_tool(tool_use_content)
        tool_response = {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use_content.id,
                    "content": tool_output,
                }
            ],
        }
        print(f"\n✅ Using Tool [{tool_use_content.name}]: {tool_output}\n")
        messages = send_message_block(
            new_message_block=tool_response, messages_history=messages
        )

    return messages


if __name__ == "__main__":
    send_message(
        "Write a Python program that adds two numbers together, and save it as 'add.py'",
    )
    send_message(
        "Write a simple, happy-case unit test (pytest) every .py file in the artifacts. Save them as 'test_[name].py'",
    )
