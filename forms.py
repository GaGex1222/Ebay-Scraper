from wtforms import StringField, SelectField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class FindProductForm(FlaskForm):
    product = StringField('Product Name:', validators=[DataRequired()], render_kw={"class": "custom-width"})
    site = SelectField('Site To Search Product In', choices=[('https://www.ebay.com/', 'Ebay')], render_kw={"class": "custom-width"})
    submit = SubmitField('Search')