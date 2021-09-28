from db.run_sql import run_sql
from models.wrestler import Wrestler
from models.match import Match
import repositories.wrestler_repo as wrestler_repo
import pdb


def get_results(winner, loser, match_type):
    if winner == Wrestler.name:
        Wrestler.points += 2
    return f"{winner} defeats {loser}"





def save(match):
    sql = "INSERT INTO matches ( wrestler1_id, wrestler2_id, result ) VALUES (%s, %s, %s) RETURNING id"
    # import pdb
    # pdb.set_trace()
    values = [match.wrestler1.id, match.wrestler2.id, match.result.id]
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
        
        wrestler1 = wrestler_repo.select(row['wrestler1_id'])
        wrestler2 = wrestler_repo.select(row['wrestler2_id'])
        result = wrestler_repo.select(row['result'])
        # pdb.set_trace()
        match = Match(wrestler1, wrestler2, result)
        matches.append(match)
    return matches

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql)

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)
