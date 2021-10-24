# Digital Tranformation Leaders

---

##### Task #10: News recommender system for www.mos.ru users


The repo is about to be born soon... In-depth description will be provided by neonate.

#### Startup manual

1. Step one - make sure your pip is pip, then hit:
    ```pip install -r requirements.txt```
2. Step two - let's generate history from 2 files to speed up response from server
    ```python save_history.py```
3. Step three - start up local server with:
    ```uvicorn main:app --reload```
4. Proceed to http://127.0.0.1:8000/
5. Run task update model and choose "auto_markup" to generate required files. This task needs some time (~10 min). So, relax and don't hurry!
6. Now push get / post
7. Repeat
8. Good evening

#### Start with docker-compose

- Command for jupyter:
```docker-compose up jupyter``` 
Use host and port http://127.0.0.1:8089/
- Command for web-service:
```docker-compose up web```
Use host and port http://127.0.0.1:8090/
