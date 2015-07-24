# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbilitySet',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('str_score', models.IntegerField()),
                ('dex_score', models.IntegerField()),
                ('con_score', models.IntegerField()),
                ('int_score', models.IntegerField()),
                ('wis_score', models.IntegerField()),
                ('cha_score', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('name', models.CharField(max_length=50)),
                ('alignment', models.CharField(max_length=40, choices=[(b'LG', b'Lawful Good'), (b'LN', b'Lawful Neutral'), (b'LE', b'Lawful Evil'), (b'NG', b'Neutral Good'), (b'TN', b'True Neutral'), (b'NE', b'Neutral Evil'), (b'CG', b'Chaotic Good'), (b'CN', b'Chaotic Neutral'), (b'CE', b'Chaotic Evil')])),
                ('class1_lvl', models.PositiveSmallIntegerField()),
                ('class2_lvl', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('class3_lvl', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('deity', models.CharField(max_length=50, blank=True)),
                ('home', models.CharField(max_length=50, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'n', b'None'), (b'o', b'Other')])),
                ('age', models.IntegerField(default=0, blank=True)),
                ('height', models.IntegerField(default=0, blank=True)),
                ('weight', models.IntegerField(default=0, blank=True)),
                ('hair_color', models.CharField(max_length=20, null=True, blank=True)),
                ('hair_style', models.CharField(max_length=20, null=True, blank=True)),
                ('hair_length', models.CharField(max_length=20, null=True, blank=True)),
                ('skin_tone', models.CharField(max_length=20, null=True, blank=True)),
                ('eyes', models.CharField(max_length=20, blank=True)),
                ('hit_points', models.IntegerField(default=0)),
                ('languages', models.TextField(blank=True)),
                ('ability_scores', models.OneToOneField(to='Quicksilver.AbilitySet')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('name', models.CharField(max_length=24)),
                ('detail', models.TextField()),
                ('alignment', models.CharField(max_length=40, choices=[(b'LG,NG,CG,LN,TN,CN,LE,NE,CE', b'Any'), (b'LG,NG,CG', b'Good'), (b'NG,TN,NE,LN,CN', b'Neutral'), (b'LE,NE,CE', b'Evil'), (b'LG,LN,LE', b'Lawful'), (b'CG,CN,CE', b'Chaotic')])),
                ('hit_die', models.CharField(max_length=8, choices=[(b'4', b'd4'), (b'6', b'd6'), (b'8', b'd8'), (b'10', b'd10'), (b'12', b'd12')])),
                ('skill_ranks', models.PositiveSmallIntegerField(default=0)),
                ('caster', models.CharField(blank=True, max_length=10, choices=[(b'', b'Non-caster'), (b'arcane', b'Arcane'), (b'divine', b'Divine')])),
                ('weapon_prof', models.CharField(blank=True, max_length=50, choices=[(b'', b'None'), (b'simple', b'Simple'), (b'martial', b'Martial'), (b'exotic', b'Exotic'), (b'simple,martial', b'Simple + Martial'), (b'simple,exotic', b'Simple + Exotic'), (b'martial,exotic', b'Martial + Exotic'), (b'simple,martial,exotic', b'All')])),
                ('armor_prof', models.CharField(blank=True, max_length=50, choices=[(b'', b'None'), (b'light', b'Light'), (b'medium,light', b'Medium'), (b'heavy,medium,light', b'Heavy')])),
                ('shield_prof', models.CharField(blank=True, max_length=50, choices=[(b'', b'None'), (b'shield', b'Shield'), (b'shield,tower', b'Tower Shield')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassStats',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('bab', models.CharField(max_length=4, choices=[(b'slow', b'Slow (*.5)'), (b'med', b'Normal (*.75)'), (b'fast', b'Fast (*1.0)')])),
                ('fort', models.CharField(max_length=4, choices=[(b'slow', b'Slow'), (b'fast', b'Fast')])),
                ('ref', models.CharField(max_length=4, choices=[(b'slow', b'Slow'), (b'fast', b'Fast')])),
                ('will', models.CharField(max_length=4, choices=[(b'slow', b'Slow'), (b'fast', b'Fast')])),
                ('skill_training', models.TextField()),
                ('prereqs', models.TextField()),
                ('spell_abil', models.CharField(max_length=3, choices=[(b'str', b'STRength'), (b'dex', b'DEXterity'), (b'con', b'CONstitution'), (b'int', b'INTelligence'), (b'wis', b'WISdom'), (b'cha', b'CHArisma')])),
                ('name', models.OneToOneField(to='Quicksilver.Class')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('name', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('use_effect', models.TextField()),
                ('damage', models.CharField(max_length=24)),
                ('armor', models.IntegerField()),
                ('placement', models.CharField(max_length=24)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feat',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('name', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('prereq_abil', models.CharField(max_length=24, blank=True)),
                ('prereq_skill', models.CharField(max_length=50, blank=True)),
                ('prereq_class', models.CharField(max_length=25, blank=True)),
                ('prereq_bab', models.SmallIntegerField(default=0, blank=True)),
                ('prereq_feat', models.ForeignKey(blank=True, to='Quicksilver.Feat', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KnowledgeSet',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('arcana_ranks', models.IntegerField(default=0, blank=True)),
                ('arcana_mods', models.IntegerField(default=0, blank=True)),
                ('dungeon_ranks', models.IntegerField(default=0, blank=True)),
                ('dungeon_mods', models.IntegerField(default=0, blank=True)),
                ('engineer_ranks', models.IntegerField(default=0, blank=True)),
                ('engineer_mods', models.IntegerField(default=0, blank=True)),
                ('geo_ranks', models.IntegerField(default=0, blank=True)),
                ('geo_mods', models.IntegerField(default=0, blank=True)),
                ('history_ranks', models.IntegerField(default=0, blank=True)),
                ('history_mods', models.IntegerField(default=0, blank=True)),
                ('local_ranks', models.IntegerField(default=0, blank=True)),
                ('local_mods', models.IntegerField(default=0, blank=True)),
                ('nature_ranks', models.IntegerField(default=0, blank=True)),
                ('nature_mods', models.IntegerField(default=0, blank=True)),
                ('noble_ranks', models.IntegerField(default=0, blank=True)),
                ('noble_mods', models.IntegerField(default=0, blank=True)),
                ('planes_ranks', models.IntegerField(default=0, blank=True)),
                ('planes_mods', models.IntegerField(default=0, blank=True)),
                ('religion_ranks', models.IntegerField(default=0, blank=True)),
                ('religion_mods', models.IntegerField(default=0, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('name', models.CharField(max_length=24)),
                ('detail', models.TextField()),
                ('size', models.CharField(max_length=1, choices=[(b'f', b'Fine'), (b'd', b'Diminutive'), (b't', b'Tiny'), (b's', b'Small'), (b'm', b'Medium'), (b'l', b'Large'), (b'h', b'Huge'), (b'g', b'Gargantuan'), (b'c', b'Colossal')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('acro_ranks', models.IntegerField(default=0, blank=True)),
                ('acro_mods', models.IntegerField(default=0, blank=True)),
                ('appr_ranks', models.IntegerField(default=0, blank=True)),
                ('appr_mods', models.IntegerField(default=0, blank=True)),
                ('bluff_ranks', models.IntegerField(default=0, blank=True)),
                ('bluff_mods', models.IntegerField(default=0, blank=True)),
                ('craft1_name', models.CharField(max_length=24, blank=True)),
                ('craft1_ranks', models.IntegerField(default=0, blank=True)),
                ('craft1_mods', models.IntegerField(default=0, blank=True)),
                ('craft2_name', models.CharField(max_length=24, blank=True)),
                ('craft2_ranks', models.IntegerField(default=0, blank=True)),
                ('craft2_mods', models.IntegerField(default=0, blank=True)),
                ('craft3_name', models.CharField(max_length=24, blank=True)),
                ('craft3_ranks', models.IntegerField(default=0, blank=True)),
                ('craft3_mods', models.IntegerField(default=0, blank=True)),
                ('diplo_ranks', models.IntegerField(default=0, blank=True)),
                ('diplo_mods', models.IntegerField(default=0, blank=True)),
                ('disable_ranks', models.IntegerField(default=0, blank=True)),
                ('disable_mods', models.IntegerField(default=0, blank=True)),
                ('disguise_ranks', models.IntegerField(default=0, blank=True)),
                ('disguise_mods', models.IntegerField(default=0, blank=True)),
                ('escape_ranks', models.IntegerField(default=0, blank=True)),
                ('escape_mods', models.IntegerField(default=0, blank=True)),
                ('fly_ranks', models.IntegerField(default=0, blank=True)),
                ('fly_mods', models.IntegerField(default=0, blank=True)),
                ('handle_ranks', models.IntegerField(default=0, blank=True)),
                ('handle_mods', models.IntegerField(default=0, blank=True)),
                ('heal_ranks', models.IntegerField(default=0, blank=True)),
                ('heal_mods', models.IntegerField(default=0, blank=True)),
                ('intimidate_ranks', models.IntegerField(default=0, blank=True)),
                ('intimidate_mods', models.IntegerField(default=0, blank=True)),
                ('linguist_ranks', models.IntegerField(default=0, blank=True)),
                ('linguist_mods', models.IntegerField(default=0, blank=True)),
                ('percep_ranks', models.IntegerField(default=0, blank=True)),
                ('percep_mods', models.IntegerField(default=0, blank=True)),
                ('perform1_name', models.CharField(max_length=24, blank=True)),
                ('perform1_ranks', models.IntegerField(default=0, blank=True)),
                ('perform1_mods', models.IntegerField(default=0, blank=True)),
                ('perform2_name', models.CharField(max_length=24, blank=True)),
                ('perform2_ranks', models.IntegerField(default=0, blank=True)),
                ('perform2_mods', models.IntegerField(default=0, blank=True)),
                ('profes1_name', models.CharField(max_length=24, blank=True)),
                ('profes1_ranks', models.IntegerField(default=0, blank=True)),
                ('profes1_mods', models.IntegerField(default=0, blank=True)),
                ('profes2_name', models.CharField(max_length=24, blank=True)),
                ('profes2_ranks', models.IntegerField(default=0, blank=True)),
                ('profes2_mods', models.IntegerField(default=0, blank=True)),
                ('ride_ranks', models.IntegerField(default=0, blank=True)),
                ('ride_mods', models.IntegerField(default=0, blank=True)),
                ('motive_ranks', models.IntegerField(default=0, blank=True)),
                ('motive_mods', models.IntegerField(default=0, blank=True)),
                ('sleight_ranks', models.IntegerField(default=0, blank=True)),
                ('sleight_mods', models.IntegerField(default=0, blank=True)),
                ('spellcraft_ranks', models.IntegerField(default=0, blank=True)),
                ('spellcraft_mods', models.IntegerField(default=0, blank=True)),
                ('stealth_ranks', models.IntegerField(default=0, blank=True)),
                ('stealth_mods', models.IntegerField(default=0, blank=True)),
                ('survival_ranks', models.IntegerField(default=0, blank=True)),
                ('survival_mods', models.IntegerField(default=0, blank=True)),
                ('swim_ranks', models.IntegerField(default=0, blank=True)),
                ('swim_mods', models.IntegerField(default=0, blank=True)),
                ('magic_device_ranks', models.IntegerField(default=0, blank=True)),
                ('magic_device_mods', models.IntegerField(default=0, blank=True)),
                ('knowledges', models.OneToOneField(to='Quicksilver.KnowledgeSet')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpeedStats',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('base', models.IntegerField(default=0)),
                ('run', models.IntegerField(default=0)),
                ('charge', models.IntegerField(default=0)),
                ('fly', models.IntegerField(default=0)),
                ('climb', models.IntegerField(default=0)),
                ('swim', models.IntegerField(default=0)),
                ('burrow', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpellsPerDay',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('lvl1', models.TextField(null=True)),
                ('lvl2', models.TextField(null=True)),
                ('lvl3', models.TextField(null=True)),
                ('lvl4', models.TextField(null=True)),
                ('lvl5', models.TextField(null=True)),
                ('lvl6', models.TextField(null=True)),
                ('lvl7', models.TextField(null=True)),
                ('lvl8', models.TextField(null=True)),
                ('lvl9', models.TextField(null=True)),
                ('lvl10', models.TextField(null=True)),
                ('lvl11', models.TextField(null=True)),
                ('lvl12', models.TextField(null=True)),
                ('lvl13', models.TextField(null=True)),
                ('lvl14', models.TextField(null=True)),
                ('lvl15', models.TextField(null=True)),
                ('lvl16', models.TextField(null=True)),
                ('lvl17', models.TextField(null=True)),
                ('lvl18', models.TextField(null=True)),
                ('lvl19', models.TextField(null=True)),
                ('lvl20', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisionStats',
            fields=[
                ('id', models.CharField(max_length=17, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('dark', models.IntegerField(default=0)),
                ('dark_color', models.BooleanField(default=False)),
                ('sense', models.IntegerField(default=0)),
                ('special', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='classstats',
            name='spells_per_day',
            field=models.OneToOneField(to='Quicksilver.SpellsPerDay'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='class1',
            field=models.ForeignKey(related_name='player_class1', to='Quicksilver.Class'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='class2',
            field=models.ForeignKey(related_name='player_class2', blank=True, to='Quicksilver.Class', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='class3',
            field=models.ForeignKey(related_name='player_class3', blank=True, to='Quicksilver.Class', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='feats',
            field=models.ManyToManyField(to='Quicksilver.Feat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='inventory',
            field=models.ManyToManyField(to='Quicksilver.Equipment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(to='Quicksilver.Race'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.OneToOneField(to='Quicksilver.SkillSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='speed',
            field=models.OneToOneField(to='Quicksilver.SpeedStats'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='vision',
            field=models.OneToOneField(to='Quicksilver.VisionStats'),
            preserve_default=True,
        ),
    ]
