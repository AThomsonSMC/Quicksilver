from django.db import models
from django.contrib.auth.models import User

import random

ALIGNMENT_CHOICES = [('LG,NG,CG,LN,TN,CN,LE,NE,CE', 'Any'),
                     ('LG,NG,CG', 'Good'),
                     ('NG,TN,NE,LN,CN', 'Neutral'),
                     ('LE,NE,CE', 'Evil'),
                     ('LG,LN,LE', 'Lawful'),
                     ('CG,CN,CE', 'Chaotic')]

FULL_ALIGNMENT_GRID = [('LG', 'Lawful Good'), ('LN', 'Lawful Neutral'), ('LE', 'Lawful Evil'),
                       ('NG', 'Neutral Good'), ('TN', 'True Neutral'), ('NE', 'Neutral Evil'),
                       ('CG', 'Chaotic Good'), ('CN', 'Chaotic Neutral'), ('CE', 'Chaotic Evil')]

SIZE_CHOICES = [('f', 'Fine'), ('d', 'Diminutive'), ('t', 'Tiny'), ('s', 'Small'), ('m', 'Medium'), ('l', 'Large'), ('h', 'Huge'), ('g', 'Gargantuan'), ('c', 'Colossal')]


class Class(models.Model):
    def __str__(self):
        return self.name

    HIT_DIE_CHOICES = [('4','d4'), ('6','d6'), ('8','d8'), ('10','d10'), ('12','d12')]

    CASTER_CHOICES = [('','Non-caster'), ('arcane','Arcane'), ('divine','Divine')]

    WEAPON_PROFS = [('','None'), ('simple', 'Simple'), ('martial', 'Martial'), ('exotic','Exotic'),
                    ('simple,martial', 'Simple + Martial'),
                    ('simple,exotic', 'Simple + Exotic'),
                    ('martial,exotic', 'Martial + Exotic'),
                    ('simple,martial,exotic', 'All')]

    ARMOR_PROFS = [('','None'), ('light','Light'), ('medium,light', 'Medium'), ('heavy,medium,light', 'Heavy')]

    SHIELD_PROFS = [('', 'None'), ('shield', 'Shield'), ('shield,tower', 'Tower Shield')]

    id = models.CharField(max_length=16, primary_key=True)
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


class Race(models.Model):
    def __str__(self):
        return self.name

    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=24)
    detail = models.TextField()
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)


class VisionStats(models.Model):
    def __str__(self):
        return str(self.get_vision_rules())

    id = models.CharField(max_length=16, primary_key=True)
    dark = models.IntegerField(default=0)
    dark_color = models.BooleanField(default=False)
    sense = models.IntegerField(default=0)
    special = models.TextField(blank=True)

    def get_vision_rules(self):
        return [self.dark, self.dark_color, self.sense, self.special]


class SpeedStats(models.Model):
    def __str__(self):
        return '%s ft.' % self.base

    id = models.CharField(max_length=16, primary_key=True)
    base = models.IntegerField(default=0)
    run = models.IntegerField(default=0)
    charge = models.IntegerField(default=0)
    fly = models.IntegerField(default=0)
    climb = models.IntegerField(default=0)
    swim = models.IntegerField(default=0)
    burrow = models.IntegerField(default=0)


class AbilitySet(models.Model):
    def __str__(self):
        return 'STR:%s DEX:%s CON:%s INT:%s WIS:%s CHA:%s' % (self.str_score, self.dex_score, self.con_score,
                                                              self.int_score, self.wis_score, self.cha_score)

    id = models.CharField(max_length=16, primary_key=True)
    str_score = models.IntegerField()
    dex_score = models.IntegerField()
    con_score = models.IntegerField()
    int_score = models.IntegerField()
    wis_score = models.IntegerField()
    cha_score = models.IntegerField()

    def check_abil(self, stat, needed):
        """
        :param stat: String in ['str','dex','con','int','wis','cha']
        :param needed: Score being checked
        :return: bool
        """
        score = getattr(self, stat + '_score')
        return (score > needed)

class Equipment(models.Model):
    def __str__(self):
        return self.name

    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=50)
    detail = models.TextField()
    use_effect = models.TextField()
    damage = models.CharField(max_length=24)
    armor = models.IntegerField()
    placement = models.CharField(max_length=24)


class KnowledgeSet(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
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


class SkillSet(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
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

class Feat(models.Model):
    """
    prereq_abil: String rep of ability requirement.  Format: 'str14,wis07,...'
    prereq_skill: String rep of skill requirement.  Format: '8:appraise,10:knowledge-arcana'
    prereq_feat: List of Feat requirements as objects.  Format: [Feat, Feat, ...]
    prereq_class: Tuple(Class.name, level required). Format: ('warrior',4)
    prereq_bab: Int of required Base Attack Bonus
    """
    def __str__(self):
        return self.name

    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=50)
    detail = models.TextField()
    prereq_abil = models.CharField(max_length=24, blank=True)
    prereq_skill = models.CharField(max_length=50, blank=True)
    prereq_feat = models.ForeignKey('self', blank=True, null=True)
    prereq_class = models.CharField(max_length=25, blank=True)
    prereq_bab = models.SmallIntegerField(blank=True, default=0)


class Character(models.Model):
    GENDER_OPTIONS = [('m','Male'), ('f','Female'), ('n','None'), ('o','Other')]

    id = models.CharField(max_length=16, primary_key=True)
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
    hair = models.CharField(max_length=20, blank=True)
    eyes = models.CharField(max_length=20, blank=True)
    vision = models.OneToOneField(VisionStats)
    ability_scores = models.OneToOneField(AbilitySet)
    hit_points = models.IntegerField(default=0)
    speed = models.OneToOneField(SpeedStats)
    inventory = models.ManyToManyField(Equipment)
    skills = models.OneToOneField(SkillSet)
    feats = models.ManyToManyField(Feat)
    languages = models.TextField(blank=True)