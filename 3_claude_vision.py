"""
Example of how to load a local image and send it to the Claude API.
We'll load an image AWS Lambda pricing table, then ask to generate a markdown table of the pricing information in the image.
We'll also ask to model the cost for 100, 1000, and 10000 users for a service that uses Lambda (with some assumptions).
"""

import anthropic
import base64

client = anthropic.Anthropic()


def load_image(path: str):
    # Read the image file and encode it to base64
    with open(path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")
        return image_data


image_type = "image/png"
image_data = load_image("images/lambda_pricing_image.png")
message = """
Generate a markdown table of the pricing information in this image.
Then, create a separate table to model the operating price for a service that uses Lambda with the following assumptions:
- Functions are 1GB in size.
- Functions run for 500ms on average.
- A single user makes 50 requests per month.
Create a table to model the cost for 100, 1000, and 10000 users.
"""

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_type,
                        "data": image_data,
                    },
                },
                {"type": "text", "text": message},
            ],
        }
    ],
)

response_text = message.content[0].text
print(response_text)
