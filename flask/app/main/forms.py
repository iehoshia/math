from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from flask_babel import _, lazy_gettext as _l

class SearchForm(FlaskForm):
	value = StringField('',
		validators=[DataRequired()],
		render_kw={'placeholder':'Ingrese palabra a buscar *'
	})
	submit = SubmitField('BUSCAR',
        render_kw={"class":"call-to-us"},
        )