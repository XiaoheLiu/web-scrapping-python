
## Setting Up Virtual Environment 

Initiate the virtual environment and activate it:
```bash
python3 -m venv scrapping
source scrapping/bin/activate
```

Install packages:
```bash
pip install requests
```

Generate/update requirements.txt file:
```bash
pip freeze > requirements.txt
```

To install the packages specified in requirements.txt:
```bash
 pip install -r requirements.txt
```