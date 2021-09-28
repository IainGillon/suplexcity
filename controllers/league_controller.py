from flask import  Blueprint, Flask, render_template, request, redirect
import repositories.league_repo as league_repo

league_blueprint = Blueprint("League", __name__)


