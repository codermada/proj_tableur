from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired


class CellForm(FlaskForm):
    value = FloatField('', validators=[DataRequired('data required')])
    def __init__(self, placeholder):
        super().__init__()
        self.value.render_kw ={'placeholder': placeholder}


class AddForm(FlaskForm):
    A = FloatField('A', validators=[DataRequired('data required')], render_kw={'placeholder': 0.0})
    B = FloatField('B', validators=[DataRequired('data required')], render_kw={'placeholder': 0.0})