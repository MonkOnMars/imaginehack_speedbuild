# imaginehack_speedbuild

---

## Technologies we're going to use?


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

### UN no.4 
### Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all

Idea originated from: forest https://www.forestapp.cc/

### website function:
1. play a game to earn coins
2. those coins can be exchanged for a funding in quality education



## Current status

Running the web app

Make sure mysql is installed (assuming you're on ubuntu 18.04)

```bash
git clone https://github.com/MonkOnMars/imaginehack_speedbuild

cd imaginehack_speedbuild
python3 -m venv .
cd server
pip install -r requirements.txt

mysql -u root -p < sql_script.sql

python3 main.py
```


### Routes
1. /
2. /login
3. /game
4. /api