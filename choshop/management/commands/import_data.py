from django.core.management.base import BaseCommand
from collections import Counter
import csv
import os.path
from django.core.files.images import ImageFile
from django.template.defaultfilters import slugify
from shop import models as shop_models

class Command(BaseCommand):
	help = 'Import products in BookTime'

	def add_arguments(self, parser):
		parser.add_argument('csvfile', type=open)
		parser.add_argument('image_basedir', type=str)
		

	def handle(self, *args, **options):
		self.stdout.write(' Importing Data')
		c = Counter()
		reader = csv.DictReader(options.pop('csvfile'))
		for row in reader:
			product, created = shop_models.Product.objects.get_or_create(
				name = row['name'], price = row['price']
			)

			product.description = row['description']
			product.slug = slugify(row['name'])
			# for loop for the tags 
			for import_tag in row['tags'].split('|'):
				tag, tag_created = shop_models.Category.objects.get_or_create(
					name = import_tag
				)
				product.tags.add(tag)
				c['tags'] += 1
				if tag_created:
					c['tags_created'] += 1 
					for import_sub_tag in row['sub_tags'].split('|'):
						sub_tag, sub_tag_created = shop_models.SubCategory.objects.get_or_create(
							name = sub_tag,
							cat = import_tag,
						)
						product.sub_tags.add(sub_tag)
						if sub_tag_created:
							c['sub_tags_created'] += 1

				with open(os.path.join(
					options['image_basedir'],
					row['image_filename'],
				), 'rb') as f:
					image = shop_models.ProductImage(
						product = product, 
						image = ImageFile(
							f, name=row['image_filename']
						),
					)
					image.save()
					c['images'] += 1 
				
				product.save()
				c['products'] += 1
				if created:
					c['products_created'] +=1



		
			self.stdout.write(f"Products processed={created} {c['products']}, {c['products_created']}")
		self.stdout.write(f"Tags processed= {created} {c['tags']} ,{c['tags_created']}")
		self.stdout.write(f"Sub Tags processed= {created} {c['sub_tags']} ,{c['sub_tags_created']}")
		self.stdout.write(f"Images processed={c['images']}")
