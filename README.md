## Prerequisites

### Installing

Follow next steps:

```shell
git clone https://github.com/DmytroBondariev/API-listener-tg.git
```
```shell
cd <your catalog with project>
```
```shell
python3 -m venv venv
```
```shell
source venv/bin/activate
```
```shell
pip install -r requirements.txt
```
```shell
alembic init alembic
```

1. Open the `alembic.ini` file and update the `sqlalchemy.url` value:

    ```ini
    sqlalchemy.url = sqlite:///./message_catalog.db
    ```

2. Navigate to the `alembic/env.py` file and add the following imports at the top of the file:

    ```python
    from api_listener.models import *
    from database import Base
    ```

3. Still in the `alembic/env.py` file, update the `target_metadata` value:

    ```python
    target_metadata = [Base.metadata]
    ```
Make DB migration:
```shell
alembic revision --autogenerate -m 'Initial migration' 
```
```shell
alembic upgrade head     
```
Start the server:
```shell
uvicorn main:app --reload  
```

## Do not forget to start chat with your bot and/or add bot to your group chat!!!
## Tested POST requests via Postman https://www.postman.com/
