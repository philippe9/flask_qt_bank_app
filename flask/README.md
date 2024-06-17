# Bank app documentation

## Setup app and test

Build requirements.txt after package update.

Inside flask directory type : `pip install -r requirements.txt`

You should have a mysql database up with a database named banque and a user having all privileges on it

Create .env file at the root. Example content :

DATABASE_USERNAME="user"
DATABASE_PASSWORD="user_pass"
DATABASE_HOST="192.168.1.10"
DATABASE_PORT=3306
DATABASE_TABLE="banque"
DATABASE_CERT_FILE="ca-certificate.crt"
Import sample database in the repository sample.sql

Create the folder logs to record the logs created by the app

Run app graphical app with python3 main.py 

Features :
- Login
- List users
- List trxs
- Trx b/n users