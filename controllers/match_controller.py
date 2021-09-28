from flask import  Blueprint, Flask, render_template, request, redirect
from models.match import Match
import repositories.league_repo as league_repo
import repositories.match_repo as match_repo
import pdb

match_blueprint = Blueprint("match", __name__)
 
@match_blueprint.route("/matches")
def show_all_matches():
    
    matches = match_repo.select_all()
    return render_template("/matches/index.html", title="match", matches=matches)

 
# @match_blueprint.route("/matches")
# def show_match(id):
#     match = match_repo.select(id)
#     return render_template(index.html, title=match, match=match)

    
