from django.contrib import admin
from Quicksilver import models

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,            {'fields': ['name', 'player']}),
        ('General Info',  {'fields': ['class1', 'class1_lvl', 'class2', 'class2_lvl', 'class3', 'class3_lvl',
                                     'race', 'alignment', 'deity', 'home']}),
        ('Physical Info', {'fields': ['gender', 'age', 'height', 'weight', 'hair_color', 'hair_style', 'hair_length', 'skin_tone', 'eyes']}),
        ('Stats',         {'fields': ['ability_scores', 'hit_points', 'vision', 'speed',
                                      'inventory', 'skills', 'feats', 'languages']})
    ]
    list_display = ('player', 'name', 'class1', 'race', 'alignment')
    list_filter = ['player', 'class1', 'race', 'alignment']
    search_fields = ['player', 'name']


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail')


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail')


class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail')


class FeatAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,            {'fields': ['name', 'detail']}),
        ('Prerequisites', {'fields': ['prereq_abil', 'prereq_skill', 'prereq_feat', 'prereq_class', 'prereq_bab']})
    ]
    list_display = ('name', 'prereq_feat', 'detail')
    list_filter = ('name', 'prereq_feat', 'prereq_abil', 'prereq_skill', 'prereq_class', 'prereq_bab')


admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.Class, ClassAdmin)
admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.Feat, FeatAdmin)
admin.site.register(models.Race, RaceAdmin)