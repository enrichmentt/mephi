### venv
```python -m venv .venv```

### requirements
```pip install -r requirements.txt```

### run server uwsgi
```uwsgi -H .venv --http :5000 --module server:app```
