import pdb
from models.league import League
from models.wrestler import Wrestler
from models.match import Visit


import repositories.league_repo as league_repo
import wrestler_repo as wrestler_repo
import repositories.match_repo as match_repo

wrestler1 = Wrestler("Stone Cold Steve Austin", 0)
wrestler_repo.save(wrestler1)

wrestler2 = Wrestler("Jon Moxley", 0)
wrestler_repo.save(wrestler2)

wrestler3 = Wrestler("Sting", 0)
wrestler_repo.save(wrestler3)

wrestler4 = Wrestler("Kenny Omega", 0)
wrestler_repo.save(wrestler4)

match1 = Match("singles match", wrestler4, wrestler3, wrestler3 )
match_repo.save(match1)

match2 = Match("singles match", wrestler2, wrestler1, wrestler1)

pdb.trace()