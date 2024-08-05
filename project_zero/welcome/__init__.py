from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'selection'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

class Welcome(Page):
    @staticmethod
    def vars_for_template(player):
        if player.id_in_group % 2 == 0:
            player.participant.vars['go_to_app'] = 'red'
            return { "custom_text": "There is anecdotal evidence suggesting that, when we use polite messages while interacting with conversational AI chatbots, it leads to better results. We ask you to try making your messages polite, while completing the tasks."}
        else:
            player.participant.vars['go_to_app'] = 'blue'
            return { "custom_text": "" }

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        return player.participant.vars.get('go_to_app')

page_sequence = [Welcome]
