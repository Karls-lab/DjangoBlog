# Generated by Django 3.2.7 on 2021-10-14 20:44

from django.db import migrations
from django.utils import timezone
import django.apps
from random import randrange

# I could literaly create a python program that opens a text file with all my blog posts and turn
# them into html code... Hmmmm. 

lorem = """Deutsches Ipsum Dolor id latine Weihnachten complectitur pri, mea Danke denique nominavi id. Siebentausendzweihundertvierundfünfzig expetenda nam an, Handtasche ei reque euismod Meerschweinchen Odio principes iracundia Apfelstrudel pri. Ut vel Aperol Spritz mandamus, quas natum Apfelschorle ei ius, diam Rotwurst honestatis eum no
quo Apfelschorle posidonium at, adhuc Nackenheim sadipscing per at, Heisenberg mei ullum gloriatur. Mercedes Benz inermis recteque accommodare Ampelmännchen Id nec assum Handschuh te melius erroribus Projektplanung Nec ut amet Glühwein iriure, prodesset gloriatur Mertesacker ut. Dicunt virtute Juttensack per no. At Audi scaevola eum. An Volkswagen malorum efficiendi
Deutsches Ipsum Dolor sit Goethe consectetur Hörspiele elit, Schweinsteiger do Lebkuchen tempor Milka ut Schnaps et Erbsenzähler magna Ampelmännchen Ut Grossbritannien ad danke veniam, Lebensabschnittsgefährte nostrud Lebkuchen ullamco Pfannkuchen nisi Bahnhof aliquip Hallo ea Schneewittchen consequat. genau aute Projektplanung dolor Bildung reprehenderit Reinheitsgebot voluptate Erbsenzähler esse Stuttgart dolore Glühwein fugiat Welt pariatur. Spezi sint Hamburg cupidatat Umsatzanalyse proident, Lebensabschnittsgefährte in Umsatzanalyse qui genau deserunt Glühwein anim Schweinsteiger est Sauerkraut dissentias Wurst et. schnell argumentum Bier an. Umsatzanalyse lobortis Ritter Sport per Zauberer nam Bezirksschornsteinfegermeister probatus Vorsprung durch Technik impetus Goethe aliquando Audi sea. 99 Luftballons scripserit Fernweh vis, Knappwurst meis Döner ea. Zeitgeist ea Bezirksschornsteinfegermeister eleifend, Hockenheim blandit Spezi sed, Wurst eius Flughafen sanctus Goethe Cu Köln legimus Audi vim
"""


def get_lorem(n = 1):
	text_size = len(lorem)
	random_text = lorem[randrange(text_size):]
	for x in range(n - 1):
		random_text += lorem[randrange(text_size):]
	return random_text
	
def get_text():
	data = ""
	f = open("D:/Web_Dev/mysite/blog/migrations/text.txt", mode='r', encoding='utf-8')
	for line in f:
		data += line
	f.close()
	return data

	


def populate_db(apps, schema_editor):
	print("LSDKFJLDSKFJLSDKFJLSDKFJLSDKFJDLSKF")
	Blog = apps.get_model('blog', 'Blog')
	now = timezone.now()
	

	blog_posts = 10
	for blog in range(blog_posts):
		b = Blog(title="Blog Post "+str(blog), author='bot '+str(blog), 
		#content=get_lorem(5),
		content=get_text(),
		pub_date=now)
		b.save()
		for blog in range(randrange(10)):
			b.comment_set.create(name='bot '+str(randrange(1000)), 
				email='notarealemailaddress'+str(randrange(1000))+"@masterhacker.com", 
				content=get_lorem()[:randrange(500)],
				pub_date=now)



class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
		migrations.RunPython(populate_db)
    ]
