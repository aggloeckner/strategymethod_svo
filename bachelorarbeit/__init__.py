from otree.api import *
from string import digits

c = Currency

doc = """
Bachelorarbeit Léon Bartosch
"""


class Constants(BaseConstants):
    name_in_url = 'bachelorarbeit'
    players_per_group = None
    num_rounds = 1
    endowment = cu(200)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_end = models.StringField()
    consentGiven = models.BooleanField()
    compr_check_pass = models.BooleanField(
        initial = False
    )
    srsn_check_pass = models.BooleanField(
        initial = False
    )
    study_started = models.BooleanField(
        initial = False
    )
    study_completed = models.BooleanField(
        initial = False
    )
    compr_check_1st_1 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    compr_check_1st_2 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    compr_check_2nd_1 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    compr_check_2nd_2 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        blank=True
    )
    compr_check_3rd_1 = models.CurrencyField(
        min = 0,
        max = Constants.endowment,
        blank = True
    )
    compr_check_3rd_2 = models.CurrencyField(
        min = 0,
        max = Constants.endowment,
        blank = True
    )
    contribution = models.CurrencyField(
        min=0,
        max=Constants.endowment
    )
    cond_coop_0 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '0 Cent'
    )
    cond_coop_10 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '10 Cent'
    )
    cond_coop_20 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '20 Cent'
    )
    cond_coop_30 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '30 Cent'
    )
    cond_coop_40 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '40 Cent'
    )
    cond_coop_50 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '50 Cent'
    )
    cond_coop_60 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '60 Cent'
    )
    cond_coop_70 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '70 Cent'
    )
    cond_coop_80 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '80 Cent'
    )
    cond_coop_90 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '90 Cent'
    )
    cond_coop_100 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '100 Cent'
    )
    cond_coop_110 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '110 Cent'
    )
    cond_coop_120 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '120 Cent'
    )
    cond_coop_130 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '130 Cent'
    )
    cond_coop_140 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '140 Cent'
    )
    cond_coop_150 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '150 Cent'
    )
    cond_coop_160 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '160 Cent'
    )
    cond_coop_170 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '170 Cent'
    )
    cond_coop_180 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '180 Cent'
    )
    cond_coop_190 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '190 Cent'
    )
    cond_coop_200 = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label = '200 Cent'
    )
    reasons = models.LongStringField(
        label = ''
    )
    fear_exploited = models.IntegerField(
        choices=[
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
        ],
        widget=widgets.RadioSelectHorizontal,
        label = 'Befürchteten Sie, dass Ihre Gruppenmitglieder Sie ausbeuten könnten?',
        blank = True
    )
    effort = models.IntegerField(
        choices=[
            [1, 'fast keine'],
            [2, 'sehr wenig'],
            [3, 'etwas'],
            [4, 'ziemlich viel'],
            [5, 'sehr viel'],
        ],
        widget=widgets.RadioSelect
    )
    attention = models.IntegerField(
        choices=[
            [1, 'fast keine'],
            [2, 'sehr wenig meiner'],
            [3, 'etwas meiner'],
            [4, 'die meiste meiner'],
            [5, 'meine volle'],
        ],
        widget=widgets.RadioSelect
    )
    use_data = models.BooleanField(
        choices=[
            [True, 'Ja'],
            [False, 'Nein'],
        ]
    )
    comments = models.LongStringField(
        label = '',
        blank = True
    )

def condition(p):
#    if p.participant.label != "1234555":
    if p.study_started:
        return True
    else:
        return False

# ADMINPAGE
def vars_for_admin_report(subsession):
    with open('LabIds/CountParticipation.txt', 'r') as file:
        count_participants_condition = int(file.read())

    count_participants_all = sum([int(p.study_completed) for p in filter(condition, subsession.get_players())])

    count_participants_started = sum([int(p.study_started) for p in subsession.get_players()])

    if count_participants_started > 0:
        payoffs = sum([p.payoff for p in filter(condition, subsession.get_players())]).to_real_world_currency(subsession.session)
    else:
        payoffs = 0

    missing_subjects = subsession.session.config['max_number_participants'] - count_participants_condition

    if count_participants_condition > 0:
        predicted_costs = (payoffs / count_participants_all) * subsession.session.config['max_number_participants'] * count_participants_started / count_participants_condition
    else:
        predicted_costs = "-"

    return dict(
        count_participants_condition = count_participants_condition,
        count_participants_all = count_participants_all,
        count_participants_started = count_participants_started,
        payoffs = payoffs,
        missing_subjects = missing_subjects,
        predicted_costs = predicted_costs
    )


# PAGES
class Introduction(Page):
    def is_displayed(player):
        player.study_started = True
        player.payoff = player.session.config['participation_fee'] / player.session.config['real_world_currency_per_point']
        return True
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['consentGiven']

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        with open('LabIds/Participated.txt', 'a') as file:
            if(player.participant.label != "1234555"):
                file.write('\n')
                file.write(player.participant.label)

class Instructions(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class ComprehensionCheck(Page):
    form_model = 'player'
    form_fields = ['compr_check_1st_1','compr_check_1st_2']

    def error_message(player, values):
        if values['compr_check_1st_1'] is None or values["compr_check_1st_2"] is None:
            return 'Bitte füllen Sie alle Felder aus.'

    def before_next_page(player, timeout_happened):
        if player.compr_check_1st_1 == 200 and player.compr_check_1st_2 == 0:
            player.compr_check_pass = True
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class ComprehensionCheck2(Page):
    form_model = 'player'
    form_fields = ['compr_check_2nd_1','compr_check_2nd_2']

    def is_displayed(player):
        return player.compr_check_1st_1 != 200 or player.compr_check_1st_2 != 0

    def error_message(player, values):
        if (values['compr_check_2nd_1'] is None and player.compr_check_1st_1 != 200) or (values["compr_check_2nd_2"] is None and player.compr_check_1st_2 != 0):
            return 'Bitte füllen Sie alle Felder aus.'

    def before_next_page(player, timeout_happened):
        if (player.compr_check_1st_1 == 200 or player.compr_check_2nd_1 == 200) and (player.compr_check_1st_2 == 0 or player.compr_check_2nd_2 == 0):
            player.compr_check_pass = True
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class ComprehensionCheck3(Page):
    form_model = 'player'
    form_fields = ['compr_check_3rd_1','compr_check_3rd_2']

    def is_displayed(player):
        return (player.compr_check_1st_1 != 200 and player.compr_check_2nd_1 != 200) or (player.compr_check_1st_2 != 0 and player.compr_check_2nd_2 != 0)

    def error_message(player, values):
        if (values['compr_check_3rd_1'] is None and player.compr_check_1st_1 != 200 and player.compr_check_2nd_1 != 200) or (values["compr_check_3rd_2"] is None and player.compr_check_1st_2 != 0 and player.compr_check_2nd_2 != 0):
            return 'Bitte füllen Sie alle Felder aus.'

    def before_next_page(player, timeout_happened):
        if (player.compr_check_1st_1 == 200 or player.compr_check_2nd_1 == 200 or player.compr_check_3rd_1 == 200) and (player.compr_check_1st_2 == 0 or player.compr_check_2nd_2 == 0 or player.compr_check_3rd_2 == 0):
            player.compr_check_pass = True
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def error_message(player, values):
        if values['contribution'] % 2 != 0:
            return 'Bitte geben Sie einen geraden Betrag ein.'

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class StrategyMethod(Page):
    form_model = 'player'
    form_fields = ['cond_coop_0','cond_coop_10','cond_coop_20','cond_coop_30','cond_coop_40','cond_coop_50','cond_coop_60','cond_coop_70','cond_coop_80','cond_coop_90','cond_coop_100','cond_coop_110','cond_coop_120','cond_coop_130','cond_coop_140','cond_coop_150','cond_coop_160','cond_coop_170','cond_coop_180','cond_coop_190','cond_coop_200']

    def error_message(player, values):
        for i in values:
            if values[i] % 2 != 0:
                return 'Bitte geben Sie nur gerade Beträge ein.'

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Explain(Page):
    form_model = 'player'
    form_fields = ['reasons']

class Exploited(Page):
    form_model = 'player'
    form_fields = ['fear_exploited']

    def error_message(player, values):
        for i in values:
            if values[i] is None:
                return 'Wählen Sie eine der Optionen aus.'

class SeriousnessCheck(Page):
    form_model = 'player'
    form_fields = ['effort','attention','use_data']

    def before_next_page(player, timeout_happened):
        player.study_completed = True
        player.payoff += player.contribution * 2

        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        if player.effort == 5 and player.attention == 5 and player.use_data:
            player.srsn_check_pass = True

        with open('LabIds/CountParticipation.txt', 'r') as file:
            txt = int(file.read())
            txt += 1
        if(player.participant.label != "1234555"):
            if player.compr_check_pass & player.use_data:
                with open('LabIds/CountParticipation.txt', 'w') as file:
                    file.write(str(txt))

class Debriefing(Page):
    form_model = 'player'
    form_fields = ['comments']

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Finish(Page):
    pass

page_sequence = [
    Introduction,
    InformedConsent,
    Instructions,
    ComprehensionCheck,
    ComprehensionCheck2,
    ComprehensionCheck3,
    Contribute,
    StrategyMethod,
    Explain,
    Exploited,
    SeriousnessCheck,
    Debriefing,
    Finish
]
