# Problem to solve
Refer to [instructions](https://github.com/ijc-90/api-merger/blob/main/instructions.md)

# Installation
```
. venv/bin/activate
pip install Flask
```

# Run server
```
. venv/bin/activate
cd src
flask run
```
Server will be running on http://127.0.0.1:5000/
# Run tests
```
python -m pytest -s tests
```
# Endpoints

 - /health_check
 - /merge_api_calls?member_id=<member_id>

