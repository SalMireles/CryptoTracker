# flask run uses this file to set configs (prod config overrites these)
FLASK_APP=app_run.py
FLASK_ENV=development
FLASK_DEBUG=true
# database format info for sqlalchemy *://username:password@host:port/database_name
# mysql-sqlalchemy local config (not using containers).
# uncomment to run MYSQL (not sqllite) in the local dev environment.
MYSQL_DATABASE_URL = mysql+pymysql://pyrate:iamyourcaptain@127.0.0.1:3306/pyrates