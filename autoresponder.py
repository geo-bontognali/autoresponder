from mitmproxy import http

import json

# Load rules from a separate JSON file
with open("/home/geo/repos/autoresponder/rules.json", "r") as f:
    rules = json.load(f)

def request(flow: http.HTTPFlow) -> None:
    for rule in rules:
        if rule["url_part"] in flow.request.pretty_url:
            with open(rule["file_path"], 'rb') as f:
                file_content = f.read()

            flow.response = http.Response.make(
                status_code=200,
                content=file_content,
                headers={"Content-Type": "application/octet-stream"}
            )

