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
    def vars_for_template(player):
     
        fixed_payment = 2
        
        
        return dict(
            
            fixed_payment = fixed_payment,
          
        )

page_sequence = [Redirect]