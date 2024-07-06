# Generated by Django 5.0.6 on 2024-07-06 05:43

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0053_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'This username already exists.Input other username'}, help_text='', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('country', models.CharField(choices=[('Uzbekistan', 'Uzbekistan'), ('afghanistan', 'Afghanistan'), ('albania', 'Albania'), ('algeria', 'Algeria'), ('american samoa', 'American Samoa'), ('andorra', 'Andorra'), ('angola', 'Angola'), ('anguilla', 'Anguilla'), ('anonymous numbers', 'Anonymous Numbers'), ('antigua & barbuda', 'Antigua & Barbuda'), ('argentina', 'Argentina'), ('armenia', 'Armenia'), ('aruba', 'Aruba'), ('australia', 'Australia'), ('austria', 'Autria'), ('azerbaijan', 'Azerbaijan'), ('bahamas', 'Bahamas'), ('bahrain', 'Bahrain'), ('bangladesh', 'Bangladesh'), ('barbados', 'Barbados'), ('belarus', 'Belarus'), ('belgium', 'Belgium'), ('belize', 'Belize'), ('benin', 'Benin'), ('bermuda', 'Bermuda'), ('bhutan', 'Bhutan'), ('bolivia', 'Bolivia'), ('bonaire, sint eustatius & saba', 'Bonaire, Bint Eustatius & Saba'), ('bosnia & herzegovina', 'Bosnia & Herzegovina'), ('botswana', 'Botswana'), ('brazil', 'Brazil'), ('british virgin islands', 'British Virgin Islands'), ('brunei darussalam', 'Brunei Darussalam'), ('bulgaria', 'Bulgaria'), ('burkina faso', 'Burkina Faso'), ('burundi', 'Burundi'), ('cambodia', 'Cambodia'), ('cameroon', 'Cameroon'), ('canada', 'Canada'), ('cape verde', 'Cape Verde'), ('cayman islands', 'Cayman Islands'), ('central african rep.', 'Central African Rep.'), ('chad', 'Chad'), ('chile', 'Chile'), ('china', 'China'), ('colombia', 'Colombia'), ('comoros', 'Comoros'), ('congo (dem. rep.)', 'Congo (Dem. Rep.)'), ('congo (rep.)', 'Congo (Rep.)'), ('cook islands', 'Cook Islands'), ('costa rica', 'Costa Rica'), ('côte d"ivoire', 'Côte d"ivoire'), ('croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Curaçao', 'Curaçao'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Diego Garcia', 'Diego Garcia'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Rep.', 'Dominican Rep.'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'), ('Falkland Islands', 'Falkland Islands'), ('Faroe Islands', 'Faroe Islands'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('French Polynesia', 'French Polynesia'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macau', 'Macau'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Micronesia', 'Micronesia'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Caledonia', 'New Caledonia'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Norfolk Island', 'Norfolk Island'), ('North Korea', 'North Korea'), ('North Macedonia', 'North Macedonia'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Palestine', 'Palestine'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Réunion', 'Réunion'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Helena', 'Saint Helena'), ('Saint Kitts & Nevis', 'Saint Kitts & Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Pierre & Miquelon', 'Saint Pierre & Miquelon'), ('Saint Vincent & the GrenadinesSamoa', 'Saint Vincent & the GrenadinesSamoa'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('São Tomé & Príncipe', 'São Tomé & Príncipe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Switzerland', 'Switzerland'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor-Leste', 'Timor-Leste'), ('Togo', 'Togo'), ('Trinidad & Tobago', 'Trinidad & Tobago'), ('Turkmenistan', 'Turkmenistan'), ('Turks & Caicos Islands', 'Turks & Caicos Islands'), ('Tuvalu', 'Tuvalu'), ('Uzbekistan', 'Uzbekistan'), ('USA', 'USA'), ('US Virgin Islands', 'US Virgin Islands'), ('Uruguay', 'Uruguay'), ('United Kingdom', 'United Kingdom'), ('United Arab Emirates', 'United Arab Emirates'), ('Vanuatu', 'Vanuatu'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Wallis & Futuna', 'Wallis & Futuna'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default='Uzbekistan', max_length=35)),
                ('address', models.CharField(max_length=128)),
                ('age', models.CharField(choices=[('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('1994', '1994'), ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'), ('1989', '1989'), ('1988', '1988'), ('1987', '1987'), ('1986', '1986'), ('1985', '1985')], default='2010', max_length=6)),
                ('active', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.PositiveIntegerField(default='+998')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='Input Description')),
                ('name', models.CharField(max_length=50, null=True)),
                ('tur', models.CharField(choices=[('channel', 'CHANNEL'), ('group', 'GROUP'), ('chatting', 'CHATTING')], default='chatting', max_length=25)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='chat/images/')),
                ('Admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Admin', to=settings.AUTH_USER_MODEL)),
                ('Admins', models.ManyToManyField(related_name='Admins', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='chat_members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('chat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chat_url', to='king.chat')),
            ],
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(null=True)),
                ('expired_time', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('amalda', 'Amalda'), ('checked', 'Checked'), ('expired', 'Expired')], default='amalda', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_codes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(choices=[('text', 'Text'), ('rasm', 'Rasm')], default='text', max_length=30)),
                ('sms', models.TextField()),
                ('created', models.TimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='king.chat')),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('birthday', models.CharField(blank=True, max_length=90, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('bio', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='telegram/user/')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_images', to='king.profile')),
            ],
        ),
    ]
