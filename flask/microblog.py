from app import create_app, cli

app = create_app()
cli.register(app)

#from app.models import User

@app.shell_context_processor
def make_shell_context():
	return {
		#'User':User
	}