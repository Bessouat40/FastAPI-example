# FastAPI use

## FastAPI

It's a tool to build RestAPI with python. It's an easy library to deploy API for your webapp for example.

## Usage

* First you need to install python dependencies :

```bash
python -m pip install -r requirements.txt
```

* Then you need to run your API :

```bash
python main.py
```

Now your API is running at `http://localhost:8000`.

If you want to test your API, you can run call.py :

```bash
python call.py
```

## API calls

If you want to access this API :

```python
import requests

data = {'number' : 1}

response = requests.post('http://localhost:8000/soustraction', data = data)
```
