from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'redirect'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    Redirect_Link = 'https://app.prolific.co/submissions/complete?cc=7B356C5D'
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Redirect(Page):
    pass

page_sequence = [Redirect]