from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Optional

class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class TodoForm(FlaskForm):
    
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    done = BooleanField('Done', default = False, false_values=(False,'False'), validators=[Optional()])
    submit = SubmitField('Create')
    
class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Delete')
    
class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Complete Task')