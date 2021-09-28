from db.run_sql import run_sql
from models.wrestler import Wrestler
from models.match import Match


def get_results(winner, loser, match_type):
    if winner == Wrestler.name:
        Wrestler.points += 2
    return f"{winner} defeats {loser}"





def add(match):
    sql = "INSERT INTO matches ( wrestler1, wrestler2, match_type, result ) VALUES (%s, %s, %s, %s) RETURNING ID"
    values = [match.wrestler1, match.wrestler2, match.match_type, match.result]
    results = run_sql(sql, values)
    match.id = results[0]['id']
    return match

def select(id):
    sql = 'SELECT FROM matches WHERE id = %s'
    values = [id]
    run_sql(sql)

def select_all():
    matches = []

    sql = "SELECT * FROM matches"

    results = run_sql(sql)

    for row in results:
        match = Match(row["wrestler1"], row["wrestler2"], row["match_type"], row["result"])
        wrestlers.append(wrestler)
    return wrestlers

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql)

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)
