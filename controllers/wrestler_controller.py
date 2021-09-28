from flask import  Blueprint, Flask, render_template, request, redirect
from models.match import Match
from models.wrestler import Wrestler
import repositories.league_repo as league_repo
import repositories.match_repo as match_repo
import repositories.wrestler_repo as wrestler_repo

wrestler_blueprint = Blueprint("match", __name__)

@wrestler_blueprint.route("/wrestlers")
def show_all_wrestlers():
    wrestlers = wrestler_repo.select_all()
    return render_template("index.html", title=wrestlers, wrestlers=wrestlers)

@wrestler_blueprint.route("/wrestlers/<id>")
def show_wrestler(id):
    wrestler = wrestler_repo.select(id)
    return render_template("index.html", title=wrestler, wrestler=wrestler)