import json
import os

# Create artifacts directory if it doesn't exist.
if not os.path.exists("./artifacts"):
    os.makedirs("./artifacts")


def list_artifacts():
    artifacts_list = os.listdir("./artifacts/")
    return f"Artifacts: {artifacts_list}"


def save_artifact(content: str, filename: str):
    with open(f"./artifacts/{filename}", "w") as f:
        f.write(content)
        return f"File successfully saved as {filename}."


def load_artifact(filename: str):
    if os.path.exists(f"./artifacts/{filename}"):
        with open(f"./artifacts/{filename}", "r") as f:
            return f.read()
    else:
        return f"File {filename} not found."


def load_tool_schema(filename: str):
    with open(f"./tool_schema/{filename}", "r") as f:
        return json.load(f)


list_artifact_schema = load_tool_schema("list-artifacts.json")
save_artifact_schema = load_tool_schema("save-artifact.json")
load_artifact_schema = load_tool_schema("load-artifact.json")

TOOLS_SCHEMA = [list_artifact_schema, save_artifact_schema, load_artifact_schema]
TOOL_MAP = {
    "list_artifacts": list_artifacts,
    "save_artifact": save_artifact,
    "load_artifact": load_artifact,
}


def use_tool(tool_content):
    tool_func = TOOL_MAP[tool_content.name]
    tool_output = tool_func(**tool_content.input)
    return tool_output
