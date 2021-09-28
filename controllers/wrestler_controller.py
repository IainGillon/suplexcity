from flask import  Blueprint, Flask, render_template, request, redirect
from models.match import Match
from models.wrestler import Wrestler
import repositories.league_repo as league_repo
import repositories.match_repo as match_repo
import repositories.wrestler_repo as wrestler_repo
import pdb

wrestler_blueprint = Blueprint("wrestler", __name__)

@wrestler_blueprint.route("/wrestlers")
def show_all_wrestlers():
    wrestlers = wrestler_repo.select_all()
    # pdb.set_trace()
    return render_template("/wrestlers/index.html", title=wrestlers, wrestlers=wrestlers)

@wrestler_blueprint.route("/wrestlers/<id>")
def show_wrestler(id):
    wrestler = wrestler_repo.select(id)
    return render_template("index.html", title=wrestler, wrestler=wrestler)

@wrestler_blueprint.route("/wrestlers/new")
def add_wrestler():
    return render_template("wrestlers/new.html")

@wrestler_blueprint.route("/wrestlers", methods=["POST"])
def create_wrestler():
    name = request.form["name"]
    new_wrestler = Wrestler(name)
    wrestler_repo.save(new_wrestler)
    return redirect("/wrestlers")

@wrestler_blueprint.route("/wrestlers/<id>/edit")
def edit_wrestler(id):
    wrestler = wrestler_repo.select(id)
    return render_template('wrestlers/update.html', wrestler=wrestler)

@wrestler_blueprint.route("/wrestlers/<id>/delete", methods=["POST"])
def delete_wrestler(id):
    human_repository.delete(id)
    return redirect("/wrestlers")
