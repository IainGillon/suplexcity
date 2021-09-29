from flask import  Blueprint, Flask, render_template, request, redirect
from models.match import Match
import repositories.wrestler_repo as wrestler_repo
import repositories.league_repo as league_repo
import repositories.match_repo as match_repo
import pdb

match_blueprint = Blueprint("match", __name__)
 
@match_blueprint.route("/matches")
def show_all_matches():
    
    matches = match_repo.select_all()
    return render_template("/matches/index.html", title="match", matches=matches)

@match_blueprint.route("/matches/new.html")
def new_match():
    wrestlers=wrestler_repo.select_all()
    return render_template("/matches/new.html")
 
@match_blueprint.route("/matches", methods=["POST"])
def create_match():
    wrestler1 = request.form["wreslter 1"]
    wrestler2 = request.form["wrestler 2"]
    winner = request.form["Winner"]
    new_match = Wrestler(wrestler1, wrestler2, winner)
    match_repo.save(new_match)

    return redirect("/matches")


@match_blueprint.route("/matches/<id>/delete", methods=["POST"])
def delete_match(id):
    match_repo.delete(id)
    return redirect("/matches")
