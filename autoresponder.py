from mitmproxy import http

import json

# Load rules from a separate JSON file
with open("/home/geo/repos/autoresponder/rules.json", "r") as f:
    rules = json.load(f)

def request(flow: http.HTTPFlow) -> None:
    # Check each rule
    for rule in rules:
        # Match the URL
        if rule["url_part"] in flow.request.pretty_url:
            # Read the content of the file
            with open(rule["file_path"], 'rb') as f:
                file_content = f.read()
            # Return the file content as the response
            flow.response = http.Response.make(
                status_code=200,
                content=file_content,
                headers={"Content-Type": "application/octet-stream"}
            )
            break  # Stop checking further rules if one is matched

    # For unmatched requests, let them be processed naturally without changes
