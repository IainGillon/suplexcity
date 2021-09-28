from db.run_sql import run_sql
from models.wrestler import Wrestler
from models.match import Match

def save(wrestler):
    sql = "INSERT INTO wrestlers ( name ) VALUES (%s) RETURNING ID"
    values = [wrestler.name]
    results = run_sql(sql, values)
    wrestler.id = results[0]['id']
    return wrestler

def select(id):
    sql = 'SELECT FROM wrestlers WHERE id = %s'
    values = [id]
    run_sql(sql)

def select_all():
    wrestlers = []

    sql = "SELECT * FROM wrestlers"

    results = run_sql(sql)

    for row in results:
        wrestler = Wrestler(row["name"], row["points"], row["id"])
        wrestlers.append(wrestler)
    return wrestlers

def delete(id):
    sql = "DELETE FROM wrestlers WHERE id = %s"
    values = [id]
    run_sql(sql)

def delete_all():
    sql = "DELETE FROM wrestlers"
    run_sql(sql)





