# imaginehack_speedbuild

---

## Technologies we're going to use?

---

### Server-side
1. python flask
   1. server routing
   2. user cookie handling
   3. user database handling
   4. API hosting
2. MySQL

### Client-side
1. reactjs
2. PixiJS https://www.pixijs.com/
   1. the game engine
3. Bootstrap

---

## Topic

---
### United Nation's Goal no.4 
> Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all

Webapp idea originated from: forest https://www.forestapp.cc/

### website function:
1. play a game to earn coins
2. those coins can be exchanged for a funding in quality education

---

## Current status

---

### Running the web app

Make sure mysql is installed (assuming you're on ubuntu 18.04)


### Running at 1st time
```bash
git clone https://github.com/MonkOnMars/imaginehack_speedbuild

cd imaginehack_speedbuild
python3 -m venv .
cd server
source bin/activate
pip install -r requirements.txt

mysql -u root -p < sql_script.sql

python3 main.py
```

### Running at 2nd time and onwards
```bash
python3 main.py
```

### Windows
Make sure MySQL-server 8.0 and MySQL-shell is installed.
https://dev.mysql.com/downloads/installer/

```pwsh
git clone https://github.com/MonkOnMars/imaginehack_speedbuild

cd imaginehack_speedbuild
py -m venv .
cd server
.\Scripts\activate
pip install -r requirements.txt

mysqlsh -u root -p --file .\sql_script.sql

py main.py
```

---

### Routes
1. /
2. /login
3. /register
4. /game
5. /market
6. /api


---
### Databases
1. game

### Tables

| user |          |       |          |
| ---- | -------- | ----- | -------- |
| id   | username | email | password |


| user_data |          |                 |               |               |
| --------- | -------- | --------------- | ------------- | ------------- |
| id        | username | available_coins | highest_level | funding_count |

| market_data |             |               |                         |                      |
| ----------- | ----------- | ------------- | ----------------------- | -------------------- |
| id          | course_name | currency(MYR) | current_available_funds | funding_people_count |
