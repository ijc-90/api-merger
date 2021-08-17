from flask import Flask, request
from json_merger import JsonMerger
from external_integration import call_external_api

app = Flask(__name__)
apis_to_call = [
    'https://api1.com',
    'https://api2.com',
    'https://api3.com',
]

@app.route("/health_check")
def health_check():
    return "success"


@app.route("/merge_api_calls")
def merge_api_calls():
    member_id = request.args.get('member_id')
    json_merger = JsonMerger()
    for api in apis_to_call:
        json_merger.add_element(call_external_api(api, int(member_id)))
    return json_merger.get_result()