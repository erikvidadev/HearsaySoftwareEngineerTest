
**1. Crate Virtual Environment**

 ```bash
   python3.11 -m venv .ve
   ```

**2. Activate Virtual Environment**

 ```bash
   . .ve/bin/activate
   ```

**3. Install Requirements**

 ```bash
   pip install -r requirements.txt
   ```

**3. Install Dependencies**

 ```bash
   pip install -r requirements.txt
   ```

## Run FastAPI APP

**1. Run App Locally**

 ```bash
   python src/main.py
   ```

**2. Access The API**

 ```bash
   127.0.0.1:5000/docs
   ```

*Example Input*

 ```bash
   {
  "data": {
    "fruits": ["orange", "apple", "banana"],
    "animals": ["rabbit", "dog", "cat"],
    "cars": ["toyota", "audi", "opel"]
  },
  "sortKeys": {"keys": ["fruits", "cars"]}
}

   ```

## Docker

**Build the Docker Container**
 ```bash
docker build -t hearsay_software_engineer_test:latest .
   ```
**Run Docker Container**
 ```bash
docker run -p 5000:80 --name vidaerikhearsaytest hearsay_software_engineer_test:latest
   ```

**Stop Docker Container**
 ```bash
docker stop hearsay_software_engineer_test:latest
   ```

## Run Tests

**1. Run App Locally**
 ```bash
   pytest tests
   ```