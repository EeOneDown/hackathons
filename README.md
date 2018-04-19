# HACKATHONS

## DEPLOY
1. create mysql database (e.g. `hacks_db`)
2. git clone
3. create venv and activate it (`pip install virtualenv`, `virtualenv venv -p python3`, `sourse venv/bin/activate`)
4. `pip install -r requirements.txt`
5. change app/config.py
6. `export FLASK_APP=flask_app.py` (or `set ..` in Windows) 
7. `flask db migrate -m "init db"`
8. `flask db upgrade`
