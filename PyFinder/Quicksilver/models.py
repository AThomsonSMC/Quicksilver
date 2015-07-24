from django.db import models
from django.contrib.auth.models import User
from random_primary import RandomPrimaryIdModel
import random

FULL_ALIGNMENT_GRID = [('LG', 'Lawful Good'), ('LN', 'Lawful Neutral'), ('LE', 'Lawful Evil'),
                       ('NG', 'Neutral Good'), ('TN', 'True Neutral'), ('NE', 'Neutral Evil'),
                       ('CG', 'Chaotic Good'), ('CN', 'Chaotic Neutral'), ('CE', 'Chaotic Evil')]

ALIGNMENT_CHOICES = FULL_ALIGNMENT_GRID + \
                    [('LG,NG,CG,LN,TN,CN,LE,NE,CE', 'Any'),
                     ('LG,NG,CG', 'Good'),
                     ('NG,TN,NE,LN,CN', 'Neutral'),
                     ('LE,NE,CE', 'Evil'),
                     ('LG,LN,LE', 'Lawful'),
                     ('CG,CN,CE', 'Chaotic')]

SIZE_CHOICES = [('f', 'Fine'), ('d', 'Diminutive'), ('t', 'Tiny'), ('s', 'Small'), ('m', 'Medium'), ('l', 'Large'), ('h', 'Huge'), ('g', 'Gargantuan'), ('c', 'Colossal')]

GENDER_OPTIONS = [('m','Male'), ('f','Female'), ('n','None'), ('o','Other')]

ABILITY_CHOICES = [('str', 'STRength'), ('dex', 'DEXterity'), ('con', 'CONstitution'),
                   ('int', 'INTelligence'), ('wis', 'WISdom'), ('cha', 'CHArisma')]

STATICS = {
    'align':FULL_ALIGNMENT_GRID,
    'align_choices': ALIGNMENT_CHOICES,
    'size':SIZE_CHOICES,
    'gender':GENDER_OPTIONS,
    'abil':ABILITY_CHOICES
}

class Class(RandomPrimaryIdModel):
    def __str__(self):
        return self.name

    HIT_DIE_CHOICES = [('4','d4'), ('6','d6'), ('8','d8'), ('10','d10'), ('12','d12')]

    CASTER_CHOICES = [('','Non-caster'), ('arcane','Arcane'), ('divine','Divine')]

    WEAPON_PROFS = [('','None'), ('simple', 'Simple'), ('martial', 'Martial'), ('exotic','Exotic'),
                    ('simple,martial', 'Simple + Martial'),
                    ('simple,exotic', 'Simple + Exotic'),
                    ('martial,exotic', 'Martial + Exotic'),
                    ('simple,martial,exotic', 'All')]

    ARMOR_PROFS = [('','No Armor'), ('light','Light'), ('medium', 'Medium'), ('heavy', 'Heavy')]

    SHIELD_PROFS = [('', 'No Shield'), ('shield', 'Shield'), ('tower', 'Tower Shield')]

    name = models.CharField(max_length=24)
    detail = models.TextField()
    alignment = models.CharField(max_length=40, choices=ALIGNMENT_CHOICES)
    hit_die = models.CharField(max_length=8, choices=HIT_DIE_CHOICES)
    skill_ranks = models.PositiveSmallIntegerField(default=0)
    caster = models.CharField(max_length=10, choices=CASTER_CHOICES, blank=True)
    weapon_prof = models.CharField(max_length=50, choices=WEAPON_PROFS, blank=True)
    armor_prof = models.CharField(max_length=50, choices=ARMOR_PROFS, blank=True)
    shield_prof = models.CharField(max_length=50, choices=SHIELD_PROFS, blank=True)

    def caster_type(self):
        return self.caster

    def can_equip(self, type, prof_needed):
        """
        :param type: either 'weapon', 'armor', or 'shield'
        :param prof_needed: value to check for
        :return: bool
        """
        if type == 'weapon':
            return bool(prof_needed in self.weapon_prof)
        elif type == 'armor':
            return bool(prof_needed in self.armor_prof)
        elif type == 'shield':
            return bool(prof_needed in self.shield_prof)

    def roll_health(self):
        return random.randrange(1,self.hit_die)

    def check_align(self, align):
        return bool(align in self.alignment)


class SpellsPerDay(RandomPrimaryIdModel):
    def __str__(self):
        return self.id

    lvl1 = models.TextField(null=True)
    lvl2 = models.TextField(null=True)
    lvl3 = models.TextField(null=True)
    lvl4 = models.TextField(null=True)
    lvl5 = models.TextField(null=True)
    lvl6 = models.TextField(null=True)
    lvl7 = models.TextField(null=True)
    lvl8 = models.TextField(null=True)
    lvl9 = models.TextField(null=True)
    lvl10 = models.TextField(null=True)
    lvl11 = models.TextField(null=True)
    lvl12 = models.TextField(null=True)
    lvl13 = models.TextField(null=True)
    lvl14 = models.TextField(null=True)
    lvl15 = models.TextField(null=True)
    lvl16 = models.TextField(null=True)
    lvl17 = models.TextField(null=True)
    lvl18 = models.TextField(null=True)
    lvl19 = models.TextField(null=True)
    lvl20 = models.TextField(null=True)


class ClassStats(RandomPrimaryIdModel):
    def __str__(self):
        return self.name

    BAB_CHOICES = [('slow', 'Slow (*.5)'), ('med', 'Normal (*.75)'), ('fast', 'Fast (*1.0)')]
    SAVE_CHOICES = [('slow', 'Slow'), ('fast', 'Fast')]

    name = models.OneToOneField(Class)
    bab = models.CharField(max_length=4, choices=BAB_CHOICES)
    fort = models.CharField(max_length=4, choices=SAVE_CHOICES)
    ref = models.CharField(max_length=4, choices=SAVE_CHOICES)
    will = models.CharField(max_length=4, choices=SAVE_CHOICES)
    skill_training = models.TextField()
    prereqs = models.TextField()
    spell_abil = models.CharField(max_length=3, choices=ABILITY_CHOICES)
    spells_per_day = models.OneToOneField(SpellsPerDay)


class Race(RandomPrimaryIdModel):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=24)
    detail = models.TextField()
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)


class VisionStats(RandomPrimaryIdModel):
    def __str__(self):
        return str(self.get_vision_rules())

    dark = models.IntegerField(default=0)
    dark_color = models.BooleanField(default=False)
    sense = models.IntegerField(default=0)
    special = models.TextField(blank=True)

    def get_vision_rules(self):
        return [self.dark, self.dark_color, self.sense, self.special]


class SpeedStats(RandomPrimaryIdModel):
    def __str__(self):
        return '%s ft.' % self.base

    base = models.IntegerField(default=0)
    run = models.IntegerField(default=0)
    charge = models.IntegerField(default=0)
    fly = models.IntegerField(default=0)
    climb = models.IntegerField(default=0)
    swim = models.IntegerField(default=0)
    burrow = models.IntegerField(default=0)


class AbilitySet(RandomPrimaryIdModel):
    def __str__(self):
        return 'STR:%s DEX:%s CON:%s INT:%s WIS:%s CHA:%s' % (self.str_score, self.dex_score, self.con_score,
                                                              self.int_score, self.wis_score, self.cha_score)

    str_score = models.IntegerField()
    dex_score = models.IntegerField()
    con_score = models.IntegerField()
    int_score = models.IntegerField()
    wis_score = models.IntegerField()
    cha_score = models.IntegerField()

    def get_mod(self, stat):
        try:
            score = getattr(self, stat + '_score')
            return (score - 10)/2
        except:
            return 0

    def check_abil(self, stat, needed):
        """
        :param stat: String in ['str','dex','con','int','wis','cha']
        :param needed: Score being checked
        :return: bool
        """
        score = getattr(self, stat + '_score')
        return (score > needed)

class Equipment(RandomPrimaryIdModel):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    detail = models.TextField()
    use_effect = models.TextField()
    damage = models.CharField(max_length=24)
    armor = models.IntegerField()
    placement = models.CharField(max_length=24)


class KnowledgeSet(RandomPrimaryIdModel):
    arcana_ranks = models.IntegerField(default=0, blank=True)
    arcana_mods = models.IntegerField(default=0, blank=True)
    dungeon_ranks = models.IntegerField(default=0, blank=True)
    dungeon_mods = models.IntegerField(default=0, blank=True)
    engineer_ranks = models.IntegerField(default=0, blank=True)
    engineer_mods = models.IntegerField(default=0, blank=True)
    geo_ranks = models.IntegerField(default=0, blank=True)
    geo_mods = models.IntegerField(default=0, blank=True)
    history_ranks = models.IntegerField(default=0, blank=True)
    history_mods = models.IntegerField(default=0, blank=True)
    local_ranks = models.IntegerField(default=0, blank=True)
    local_mods = models.IntegerField(default=0, blank=True)
    nature_ranks = models.IntegerField(default=0, blank=True)
    nature_mods = models.IntegerField(default=0, blank=True)
    noble_ranks = models.IntegerField(default=0, blank=True)
    noble_mods = models.IntegerField(default=0, blank=True)
    planes_ranks = models.IntegerField(default=0, blank=True)
    planes_mods = models.IntegerField(default=0, blank=True)
    religion_ranks = models.IntegerField(default=0, blank=True)
    religion_mods = models.IntegerField(default=0, blank=True)

    def get_knowledge(self):
        """
        :return: Tuple(ranks, mods)
        """
        ranks = {}
        mods = {}
        for field in dir(self):
            name = field[:field.index('_')]
            if self.field != 0:
                if 'ranks' in field:
                    ranks[name] = self.field
                elif 'mods' in field:
                    mods[name] = self.field
        return (ranks, mods)


class SkillSet(RandomPrimaryIdModel):
    acro_ranks = models.IntegerField(default=0, blank=True)
    acro_mods = models.IntegerField(default=0, blank=True)
    appr_ranks = models.IntegerField(default=0, blank=True)
    appr_mods = models.IntegerField(default=0, blank=True)
    bluff_ranks = models.IntegerField(default=0, blank=True)
    bluff_mods = models.IntegerField(default=0, blank=True)
    craft1_name = models.CharField(max_length=24, blank=True)
    craft1_ranks = models.IntegerField(default=0, blank=True)
    craft1_mods = models.IntegerField(default=0, blank=True)
    craft2_name = models.CharField(max_length=24, blank=True)
    craft2_ranks = models.IntegerField(default=0, blank=True)
    craft2_mods = models.IntegerField(default=0, blank=True)
    craft3_name = models.CharField(max_length=24, blank=True)
    craft3_ranks = models.IntegerField(default=0, blank=True)
    craft3_mods = models.IntegerField(default=0, blank=True)
    diplo_ranks = models.IntegerField(default=0, blank=True)
    diplo_mods = models.IntegerField(default=0, blank=True)
    disable_ranks = models.IntegerField(default=0, blank=True)
    disable_mods = models.IntegerField(default=0, blank=True)
    disguise_ranks = models.IntegerField(default=0, blank=True)
    disguise_mods = models.IntegerField(default=0, blank=True)
    escape_ranks = models.IntegerField(default=0, blank=True)
    escape_mods = models.IntegerField(default=0, blank=True)
    fly_ranks = models.IntegerField(default=0, blank=True)
    fly_mods = models.IntegerField(default=0, blank=True)
    handle_ranks = models.IntegerField(default=0, blank=True)
    handle_mods = models.IntegerField(default=0, blank=True)
    heal_ranks = models.IntegerField(default=0, blank=True)
    heal_mods = models.IntegerField(default=0, blank=True)
    intimidate_ranks = models.IntegerField(default=0, blank=True)
    intimidate_mods = models.IntegerField(default=0, blank=True)
    knowledges = models.OneToOneField(KnowledgeSet)
    linguist_ranks = models.IntegerField(default=0, blank=True)
    linguist_mods = models.IntegerField(default=0, blank=True)
    percep_ranks = models.IntegerField(default=0, blank=True)
    percep_mods = models.IntegerField(default=0, blank=True)
    perform1_name = models.CharField(max_length=24, blank=True)
    perform1_ranks = models.IntegerField(default=0, blank=True)
    perform1_mods = models.IntegerField(default=0, blank=True)
    perform2_name = models.CharField(max_length=24, blank=True)
    perform2_ranks = models.IntegerField(default=0, blank=True)
    perform2_mods = models.IntegerField(default=0, blank=True)
    profes1_name = models.CharField(max_length=24, blank=True)
    profes1_ranks = models.IntegerField(default=0, blank=True)
    profes1_mods = models.IntegerField(default=0, blank=True)
    profes2_name = models.CharField(max_length=24, blank=True)
    profes2_ranks = models.IntegerField(default=0, blank=True)
    profes2_mods = models.IntegerField(default=0, blank=True)
    ride_ranks = models.IntegerField(default=0, blank=True)
    ride_mods = models.IntegerField(default=0, blank=True)
    motive_ranks = models.IntegerField(default=0, blank=True)
    motive_mods = models.IntegerField(default=0, blank=True)
    sleight_ranks = models.IntegerField(default=0, blank=True)
    sleight_mods = models.IntegerField(default=0, blank=True)
    spellcraft_ranks = models.IntegerField(default=0, blank=True)
    spellcraft_mods = models.IntegerField(default=0, blank=True)
    stealth_ranks = models.IntegerField(default=0, blank=True)
    stealth_mods = models.IntegerField(default=0, blank=True)
    survival_ranks = models.IntegerField(default=0, blank=True)
    survival_mods = models.IntegerField(default=0, blank=True)
    swim_ranks = models.IntegerField(default=0, blank=True)
    swim_mods = models.IntegerField(default=0, blank=True)
    magic_device_ranks = models.IntegerField(default=0, blank=True)
    magic_device_mods = models.IntegerField(default=0, blank=True)

    def get_skills(self):
        """
        :return: Tuple(ranks, mods)
        """
        ranks = {}
        mods = {}
        for field in dir(self):
            if 'ranks' in field or 'mods':
                if self.field != 0:
                    if 'craft' in field:
                        craft = getattr(self, 'craft' + field[(field.indexOf('_'-1)):(field.indexOf('_'))] + '_name')
                        if 'ranks' in field:
                            ranks['Craft: %s'%craft] = self.field
                        elif 'mods' in field:
                            mods['Craft: %s'%craft] = self.field
                    elif 'profes' in field:
                        profes = getattr(self, 'profes' + field[(field.indexOf('_'-1)):(field.indexOf('_'))] + '_name')
                        if 'ranks' in field:
                            ranks['Profession: %s'%profes] = self.field
                        elif 'mods' in field:
                            mods['Professsion: %s'%profes] = self.field
                    elif 'perform' in field:
                        perform = getattr(self, 'perform' + field[(field.indexOf('_'-1)):(field.indexOf('_'))] + '_name')
                        if 'ranks' in field:
                            ranks['Perform: %s'%perform] = self.field
                        elif 'mods' in field:
                            mods['Perform :%s'%perform] = self.field
            elif field == 'knowledges':
                know_stats = self.knowledges.get_knowledge()
                try:
                    for key, val in know_stats[0]:
                        ranks['Knowledge: %s'%key] = val
                    for key, val in know_stats[1]:
                        mods['Knowledge: %s'%key] = val
                except:
                    print 'ERROR GETTING KNOWLEDGE'

        return (ranks, mods)

class Feat(RandomPrimaryIdModel):
    """
    prereq_abil: String rep of ability requirement.  Format: 'str14,wis07,...'
    prereq_skill: String rep of skill requirement.  Format: '8:appraise,10:knowledge-arcana'
    prereq_feat: List of Feat requirements as objects.  Format: [Feat, Feat, ...]
    prereq_class: Tuple(Class.name, level required). Format: ('warrior',4)
    prereq_bab: Int of required Base Attack Bonus
    """
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    detail = models.TextField()
    prereq_abil = models.CharField(max_length=24, blank=True)
    prereq_skill = models.CharField(max_length=50, blank=True)
    prereq_feat = models.ForeignKey('self', blank=True, null=True)
    prereq_class = models.CharField(max_length=25, blank=True)
    prereq_bab = models.SmallIntegerField(blank=True, default=0)


class Character(RandomPrimaryIdModel):
    name = models.CharField(max_length=50)
    alignment = models.CharField(max_length=40, choices=FULL_ALIGNMENT_GRID)
    player = models.ForeignKey(User)
    class1 = models.ForeignKey(Class, related_name='player_class1')
    class1_lvl = models.PositiveSmallIntegerField()
    class2 = models.ForeignKey(Class, related_name='player_class2', blank=True, null=True)
    class2_lvl = models.PositiveSmallIntegerField(default=0, blank=True)
    class3 = models.ForeignKey(Class, related_name='player_class3', blank=True, null=True)
    class3_lvl = models.PositiveSmallIntegerField(default=0, blank=True)
    deity = models.CharField(max_length=50, blank=True)
    home = models.CharField(max_length=50, blank=True)
    race = models.ForeignKey(Race)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    age = models.IntegerField(default=0, blank=True)
    height = models.IntegerField(default=0, blank=True)
    weight = models.IntegerField(default=0, blank=True)
    hair_color = models.CharField(max_length=20, blank=True, null=True)
    hair_style = models.CharField(max_length=20, blank=True, null=True)
    hair_length = models.CharField(max_length=20, blank=True, null=True)
    skin_tone = models.CharField(max_length=20, blank=True, null=True)
    eyes = models.CharField(max_length=20, blank=True)
    vision = models.OneToOneField(VisionStats)
    ability_scores = models.OneToOneField(AbilitySet)
    hit_points = models.IntegerField(default=0)
    speed = models.OneToOneField(SpeedStats)
    inventory = models.ManyToManyField(Equipment)
    skills = models.OneToOneField(SkillSet)
    feats = models.ManyToManyField(Feat)
    languages = models.TextField(blank=True)

    @property
    def disp_height(self):
        try:
            ft = str(int(self.height)/12) + "'"
            inch = str(int(self.height)%12) + '"'
            return ft + inch
        except:
            return 'ERR'

    @property
    def armor_class(self):
        try:
            ac = 10
            scores = self.ability_scores
            ac += (scores.get_mod('dex'))
            #ac += self.nat_armor
            #ac += self.armor
            #ac += self.shield
            #ac += self.size
            #ac += self.get_misc('armor')
            return ac
        except:
            return 'ERR'

    @property
    def flat_footed(self):
        try:
            ac = self.armor_class
            ac -= (self.ability_scores.get_mod('dex'))
            return ac
        except:
            return 'ERR'

    @property
    def touch_ac(self):
        try:
            ac = self.armor_class
            #ac -= self.nat_armor
            #ac -= self.armor
            #ac -= self.shield
            return ac
        except:
            return 'ERR'

    @property
    def initiative(self):
        try:
            init_mod = 0
            init_mod += self.ability_scores.get_mod('dex')
            #init_mod += self.get_misc('initiative')
            return init_mod
        except:
            return 'ERR'

    @property
    def saves(self):
        try:
            fort, ref, will = 0, 0, 0
            #fort += self.class.fort
            #fort += self.get_misc('fort')
            fort += self.ability_scores.get_mod('con')
            #ref += self.class.ref
            #ref += self.get_misc('ref')
            ref += self.ability_scores.get_mod('dex')
            #will += self.class.will
            #will += self.get_misc('will')
            will += self.ability_scores.get_mod('wis')
            return 'fort:+%s;ref:+%s;will:+%s' %(str(fort), str(ref), str(will))
        except:
            return 'fort:ERR;ref:ERR;will:ERR'

    @property
    def spell_res(self):
        try:
            sr = 0
            #sr += self.get_misc('sr')
            return str(sr)
        except:
            return 'Err'

    @property
    def bab(self):
        try:
            bab = 0
            #bab += self.class.bab
            return "+"+str(bab)
        except:
            return 'Err'

    @property
    def cmb(self):
        try:
            cmb = 0
            cmb += int(self.bab)
            cmb += self.ability_scores.get_mod('str')
            #cmb += self.size_mod
            #cmb += self.class.cmb
            return "+"+str(cmb)
        except:
            return 'Err'

    @property
    def cmd(self):
        try:
            cmd = 10
            cmd += int(self.cmb)
            cmd += self.ability_scores.get_mod('dex')
            return str(cmd)
        except:
            return 'Err'

    @property
    def total_level(self):
        try:
            tot = self.class1_lvl
            if self.class2:
                tot += self.class2_lvl
            if self.class3:
                tot += self.class3_lvl
            return tot
        except:
            return -1