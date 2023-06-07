from otree.api import *
import random

doc = """
Gap Survey in English
"""



class C(BaseConstants):
    NAME_IN_URL = 'likert_items'
    PLAYERS_PER_GROUP = None
    TASKS = ['literacy', 'knowledge', 'strategie','closure','control','environment','pricecon','personal','buying','attention']
    NUM_ROUNDS = len(TASKS)

 
    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# FUNCTIONS

def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(C.TASKS, round_numbers))
            # print('player', p.id_in_subsession)
            # print('task_rounds is', task_rounds)
            p.participant.task_rounds = task_rounds
           
def make_field2(label):
    return models.IntegerField(
        choices = [1,2,3,4,5,6,7],
        label = label,
        widget = widgets.RadioSelect,
    )
    
class Player(BasePlayer):
    
  
    # strate Coping Strategies
    
    strat_1 = make_field2('I give up the attempt to get what I want.')
    strat_2 = make_field2('I just give up trying to reach my goal.')
    strat_3 = make_field2('I admit to myself that I can’t deal with it, and quit trying.')
    strat_4 = make_field2('I reduce the amount of effort I’m putting into solving the problem.')
    
    
    
    
   
    #Exp Insormation Avoidance
    exp_1 = make_field2('  I would rather not know the product information. ')    
    exp_2 = make_field2('I would avoid learning the product information.')    
    exp_3 = make_field2('Even if it will upset me, I want to know the product information.')    
    exp_4 = make_field2('When it comes to product information (sometimes) ignorance is bliss.')    
    exp_5 = make_field2('I want to know the product information.')    
    exp_6 = make_field2('I can think of situations in which I would rather not know the product information.')
    exp_7 = make_field2('It is important to know the product information of a product.')
    exp_8 = make_field2(' I want to know the product information immediately. ')
        
        
    
    # Sustainable Products
    
    lit_1 = make_field2('I intend to buy sustainable products.')
    
    lit_2 = make_field2('I will buy sustainable products.')
    
    lit_3 = make_field2('It is very likely that I will buy sustainable products.')
    
   
    clo_1 = make_field2('I do not like situations that are uncertain.')
    clo_2 = make_field2('I dislike questions which could be answered in many different ways.')
    clo_3 = make_field2('I find that a well ordered life with regular hours suits my temperament.')
    clo_4 = make_field2('I feel uncomfortable when I do not understand the reason why an event occurred in my life.')
    clo_5 = make_field2('I feel irritated when one person disagrees with what everyone else in a group believes.')
    clo_6 = make_field2('I do not like to go into a situation without knowing what I can expect from it.')
    clo_7 = make_field2('When I have made a decision, I feel relieved.')
    clo_8 = make_field2('When I am confronted with a problem, I’m dying to reach a solution very quickly.')
    clo_9 = make_field2('I would quickly become impatient and irritated if I would not find a solution to a problem immediately.')
    clo_10 = make_field2('I do not usually consult many different opinions before forming my own view.')
    clo_11 = make_field2('I dislike unpredictable situations.')
    clo_12 = make_field2('I find that establishing a consistent routine enables me to enjoy life more.')
    clo_13 = make_field2('I enjoy having a clear and structured mode of life.')
    clo_14 = make_field2('I dislike it when a persons statement could mean many different things.')
    clo_15 = make_field2('I don`t like to be with people who are capable of unexpected actions.')
        
    
    
    
    con_1 = make_field2('Chance determines what happens in my life.')
    con_2 = make_field2('I never plan in advance because things can always turn out differently than expected.')
    con_3 = make_field2('I am successful only because of my own efforts and involvement.')
    con_4 = make_field2('How many friends I have depends on me.')
    con_5 = make_field2('My life is largely determined by others.')
    con_6 = make_field2('Whether or not I can fulfill my plans depends on my own behavior.')
    con_7 = make_field2('I often feel that important decisions in my life are taken by others.')
    con_8 = make_field2('I’m my own boss.')
    con_9 = make_field2('Fate often gets in the way of my plans.')

    



    env_1 = make_field2('It is important to me that the products I use do not harm the environment.')
    env_2 = make_field2('I consider the potential environmental impact of my actions when making many of my decisions.')
    env_3 = make_field2('My purchase habits are affected by my concern for our environmnt.')
    env_4 = make_field2('I am concerned about wasting the resources of our planet.')
    env_5 = make_field2('I would describe myself as environmentally responsible.')
    env_6 = make_field2('I am willing to be inconvenienced in order to take actions that are more environmentally friendly.')
    
    
    price_1 = make_field2('I usually purchase the cheapest item.')
    price_2 = make_field2('I usually purchase items on sale only.')
    price_3 = make_field2('I often find myself checking prices.')
    price_4 = make_field2('A person can save a lot by shopping for bargains.')
    
    
    
    
    per_1 = make_field2('is reserved.')
    per_2 = make_field2('is generally trusting.')
    per_3 = make_field2('tends to be lazy.')
    per_4 = make_field2('is relaxed, handles stress well.')
    per_5 = make_field2('has few artistic interests.')
    per_6 = make_field2('is outgoing, sociable.')
    per_7 = make_field2('does a thorough job.')
    per_8 = make_field2('gets nervous easily.')
    per_9 = make_field2('has an active imagination.')

    


    buy_1 = make_field2('Clothes.')
    buy_2 = make_field2('Food')
    buy_3 = make_field2('Furniture')
    attention = make_field2('Check box number six')
    
    
class fin_lit(Page):
    form_model = 'player'
    get_form_fields = ['lit_1', 'lit_2', 'lit_3']
       
    def get_form_fields(self):        
        form_fields = ['lit_1', 'lit_2', 'lit_3']
        random.shuffle(form_fields)
        return form_fields
    
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['literacy']
    
class experience(Page):
    form_model = 'player'
    get_form_fields = ['exp_1', 'exp_2', 'exp_3', 'exp_4', 'exp_5', 'exp_6','exp_7','exp_8']

    def get_form_fields(self):        
        form_fields = ['exp_1', 'exp_2', 'exp_3', 'exp_4', 'exp_5',  'exp_6','exp_7','exp_8']
        random.shuffle(form_fields)
        return form_fields
    
    
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['knowledge']
    
    
    
    
    
    
class inv_strat(Page):
    form_model = 'player'
    get_form_fields = ['strat_1', 'strat_2', 'strat_3','strat_4']
           
    def get_form_fields(self):        
            form_fields = ['strat_1', 'strat_2', 'strat_3','strat_4']
            random.shuffle(form_fields)
            return form_fields
        
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['strategie']
    
    
    
class clos(Page):
    form_model = 'player'
    get_form_fields = ['clo_1','clo_2','clo_3','clo_4','clo_5','clo_6','clo_7','clo_8','clo_9','clo_10','clo_11','clo_12','clo_13','clo_14','clo_15']

    def get_form_fields(self):        
        form_fields = ['clo_1','clo_2','clo_3','clo_4','clo_5','clo_6','clo_7','clo_8','clo_9','clo_10','clo_11','clo_12','clo_13','clo_14','clo_15']
        random.shuffle(form_fields)
        return form_fields
    
    
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['closure']    
    
class env(Page):
    form_model = 'player'
    get_form_fields = ['env_1', 'env_2', 'env_3', 'env_4', 'env_5', 'env_6']

    def get_form_fields(self):        
            form_fields = ['env_1', 'env_2', 'env_3', 'env_4', 'env_5', 'env_6']
            random.shuffle(form_fields)
            return form_fields
        

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['environment']        
        
        

        
class con(Page):
    form_model = 'player'
    get_form_fields = ['con_1', 'con_2', 'con_3', 'con_4', 'con_5', 'con_6','con_7','con_8','con_9']

    def get_form_fields(self):        
        form_fields = ['con_1', 'con_2', 'con_3', 'con_4', 'con_5', 'con_6','con_7','con_8','con_9']
        random.shuffle(form_fields)
        return form_fields
   
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['control']
            
            
            
            
            
class price(Page):
    form_model = 'player'
    get_form_fields = ['price_1', 'price_2', 'price_3', 'price_4']

    def get_form_fields(self):        
        form_fields = ['price_1', 'price_2', 'price_3', 'price_4']
        random.shuffle(form_fields)
        return form_fields
                
                
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['pricecon']
                
class pers(Page):
    form_model = 'player'
    get_form_fields = ['per_1', 'per_2', 'per_3', 'per_4', 'per_5', 'per_6','per_7','per_8','per_9']

    def get_form_fields(self):        
     form_fields = ['per_1', 'per_2', 'per_3', 'per_4', 'per_5', 'per_6','per_7','per_8','per_9']
     random.shuffle(form_fields)
     return form_fields
                    
                    
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['personal']
    
class buy(Page):
    form_model = 'player'
    get_form_fields = ['buy_1', 'buy_2', 'buy_3']
               
    def get_form_fields(self):        
                form_fields = ['buy_1', 'buy_2', 'buy_3']
                random.shuffle(form_fields)
                return form_fields
            
    @staticmethod
    def is_displayed(player: Player):
            participant = player.participant
            return player.round_number == participant.task_rounds['buying']
        
        
class att(Page):
    form_model = 'player'
    get_form_fields = ['attention']
                   
    def get_form_fields(self):        
                    form_fields = ['attention']
                    random.shuffle(form_fields)
                    return form_fields
                
    @staticmethod
    def is_displayed(player: Player):
                participant = player.participant
                return player.round_number == participant.task_rounds['attention']
        

page_sequence = [
    fin_lit,
    experience,
    inv_strat,
    clos,
    con, 
    env,
    price,
    pers,
    buy,
    att
]