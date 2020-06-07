import os
import click

def register(app):
	@app.cli.group()
	def translate():

		pass

	@translate.command()
	@click.argument('lang')
	def init(lang):
		if os.system('pybabel extrac -F babel.cfg -k -l -o messages.pot .'):
			raise RuntimEError('init command failed')

		if os.system(
				'pybabel init -i messages.pot -d app/translations -l '+lang):
			raise RuntimEError('init command failed')
		os.remove('messages.pot')

	@translate.command()
	def update():
		if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
			raise RuntimEError('extract command failed')
		if os.system('pybabel update -i message.pot -d app/translations'):
			raise RuntimEError('update command failed')
		os.remove('messages.pot')

	@translate.command()
	def compile():

		if os.system('pybabel compile -d app/translations'):
			raise RuntimEError('compile command failed')