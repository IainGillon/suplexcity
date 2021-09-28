import pdb
# from models.league import League
from models.wrestler import Wrestler
from models.match import Match


import repositories.league_repo as league_repo
import repositories.wrestler_repo as wrestler_repo
import repositories.match_repo as match_repo

wrestler1 = Wrestler("Stone Cold Steve Austin", 0)
wrestler_repo.save(wrestler1)

wrestler2 = Wrestler("Jon Moxley", 0)
wrestler_repo.save(wrestler2)

wrestler3 = Wrestler("Sting", 0)
wrestler_repo.save(wrestler3)

wrestler4 = Wrestler("Kenny Omega", 0)
wrestler_repo.save(wrestler4)

match1 = Match( wrestler1, wrestler2, wrestler1)
# match1 = Match("singles match", "Kenny Omego", "Jon Moxley", "Jon Moxley" )
match_repo.save(match1)

match2 = Match(wrestler1, wrestler3, wrestler3)
# match2 = Match("singles match", "Stone Cold Steve Austin", "Sting", "Sting")
match_repo.save(match2)

pdb.set_trace()