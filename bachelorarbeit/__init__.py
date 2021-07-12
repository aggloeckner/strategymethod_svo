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
    costs = models.CurrencyField(
        initial = 0
    )
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
        choices = [
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
        ],
        widget = widgets.RadioSelectHorizontal,
        label = 'Meine Befürchtung in Teil A der Studie war, dass meine Gruppenmitglieder mich ausbeuten würden.',
        blank = True
    )
    reciprocity = models.IntegerField(
        choices = [
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
        ],
        widget = widgets.RadioSelectHorizontal,
        label = 'Mit meinem Entscheidungsverhalten in Teil B wollte ich das Verhalten meiner Mitspieler erwidern („Prinzip der Gegenseitigkeit”).',
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

def started(p):
#    if p.participant.label != "1234555":
    if p.study_started:
        return True
    else:
        return False

def finished(p):
#    if p.participant.label != "1234555":
    if p.study_completed and p.use_data and p.compr_check_pass:
        return True
    else:
        return False

# ADMINPAGE
def vars_for_admin_report(subsession):
    with open('LabIds/CountParticipation.txt', 'r') as file:
        count_participants_condition = int(file.read())

    count_participants_all = sum([int(p.study_completed) for p in filter(started, subsession.get_players())])

    count_participants_finished = sum([int(p.study_completed) for p in filter(finished, subsession.get_players())])

    count_participants_started = sum([int(p.study_started) for p in subsession.get_players()])

    if count_participants_started > 0:
        total_costs = sum([p.costs for p in filter(started, subsession.get_players())]).to_real_world_currency(subsession.session)
    else:
        total_costs = cu(0).to_real_world_currency(subsession.session)

    missing_subjects = subsession.session.config['max_number_participants'] - count_participants_condition

    if count_participants_condition > 0:
        predicted_costs = (total_costs / count_participants_all) * subsession.session.config['max_number_participants'] * count_participants_started / count_participants_condition
    else:
        predicted_costs = "-"


    if count_participants_all > 0:
        average_contribution = sum([p.contribution for p in filter(finished, subsession.get_players())]).to_real_world_currency(subsession.session) / count_participants_finished
        contribution_0 = sum([p.cond_coop_0 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_1 = sum([p.cond_coop_10 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_2 = sum([p.cond_coop_20 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_3 = sum([p.cond_coop_30 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_4 = sum([p.cond_coop_40 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_5 = sum([p.cond_coop_50 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_6 = sum([p.cond_coop_60 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_7 = sum([p.cond_coop_70 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_8 = sum([p.cond_coop_80 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_9 = sum([p.cond_coop_90 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_10 = sum([p.cond_coop_100 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_11 = sum([p.cond_coop_110 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_12 = sum([p.cond_coop_120 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_13 = sum([p.cond_coop_130 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_14 = sum([p.cond_coop_140 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_15 = sum([p.cond_coop_150 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_16 = sum([p.cond_coop_160 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_17 = sum([p.cond_coop_170 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_18 = sum([p.cond_coop_180 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_19 = sum([p.cond_coop_190 for p in filter(finished, subsession.get_players())]) / count_participants_finished
        contribution_20 = sum([p.cond_coop_200 for p in filter(finished, subsession.get_players())]) / count_participants_finished
    else:
        average_contribution = "-"
        contribution_0 = 0
        contribution_1 = 0
        contribution_2 = 0
        contribution_3 = 0
        contribution_4 = 0
        contribution_5 = 0
        contribution_6 = 0
        contribution_7 = 0
        contribution_8 = 0
        contribution_9 = 0
        contribution_10 = 0
        contribution_11 = 0
        contribution_12 = 0
        contribution_13 = 0
        contribution_14 = 0
        contribution_15 = 0
        contribution_16 = 0
        contribution_17 = 0
        contribution_18 = 0
        contribution_19 = 0
        contribution_20 = 0


    return dict(
        count_participants_condition = count_participants_condition,
        count_participants_all = count_participants_all,
        count_participants_started = count_participants_started,
        total_costs = total_costs,
        missing_subjects = missing_subjects,
        predicted_costs = predicted_costs,
        average_contribution = average_contribution,
        contribution_0 = contribution_0,
        contribution_1 = contribution_1,
        contribution_2 = contribution_2,
        contribution_3 = contribution_3,
        contribution_4 = contribution_4,
        contribution_5 = contribution_5,
        contribution_6 = contribution_6,
        contribution_7 = contribution_7,
        contribution_8 = contribution_8,
        contribution_9 = contribution_9,
        contribution_10 = contribution_10,
        contribution_11 = contribution_11,
        contribution_12 = contribution_12,
        contribution_13 = contribution_13,
        contribution_14 = contribution_14,
        contribution_15 = contribution_15,
        contribution_16 = contribution_16,
        contribution_17 = contribution_17,
        contribution_18 = contribution_18,
        contribution_19 = contribution_19,
        contribution_20 = contribution_20
    )


# PAGES
class Introduction(Page):
    def is_displayed(player):
        player.study_started = True
        player.costs = player.session.config['participation_fee'] / player.session.config['real_world_currency_per_point']
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

class Szenario1(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Szenario2(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Szenario3(Page):
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

class PartA(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def error_message(player, values):
        if values['contribution'] % 2 != 0:
            return 'Bitte geben Sie einen geraden Betrag ein.'

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class PartB(Page):
    form_model = 'player'
    form_fields = ['cond_coop_0','cond_coop_10','cond_coop_20','cond_coop_30','cond_coop_40','cond_coop_50','cond_coop_60','cond_coop_70','cond_coop_80','cond_coop_90','cond_coop_100','cond_coop_110','cond_coop_120','cond_coop_130','cond_coop_140','cond_coop_150','cond_coop_160','cond_coop_170','cond_coop_180','cond_coop_190','cond_coop_200']

    def error_message(player, values):
        for i in values:
            if values[i] % 2 != 0:
                return 'Bitte geben Sie nur gerade Beträge ein.'

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Reasons(Page):
    form_model = 'player'
    form_fields = ['reasons']

class Motives(Page):
    form_model = 'player'
    form_fields = ['fear_exploited','reciprocity']

    def error_message(player, values):
        for i in values:
            if values[i] is None:
                return 'Wählen Sie eine der Optionen aus.'

class SeriousnessCheck(Page):
    form_model = 'player'
    form_fields = ['effort','attention','use_data']

    def before_next_page(player, timeout_happened):
        player.study_completed = True
        player.costs += player.contribution + Constants.endowment

        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        if player.effort == 5 and player.attention == 5 and player.use_data:
            player.srsn_check_pass = True

        with open('LabIds/CountParticipation.txt', 'r') as file:
            txt = int(file.read())
            print(txt)
            txt += 1
            print(txt)
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
    Szenario1,
    Szenario2,
    Szenario3,
    ComprehensionCheck,
    ComprehensionCheck2,
    ComprehensionCheck3,
    PartA,
    PartB,
    Reasons,
    Motives,
    SeriousnessCheck,
    Debriefing,
    Finish
]
