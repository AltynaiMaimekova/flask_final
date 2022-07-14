from flask_wtf import FlaskForm
# from wtforms import validators
import wtforms as wf


class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('Ok')
    #
    # def validate(self):
    #     if not super().validate():
    #         return False
    #     needed_symbols = '!@#$%'
    #     check = 0
    #     for i in needed_symbols:
    #         if i in self.password.data:
    #             check = 1
    #
    #     if check == 0:
    #         self.password.errors.append('Пароль должен содержать символы  !@#$%')
    #         return False
    #
    #     if not self.password.data.isdigit():
    #         check = 1
    #
    #     if check == 0:
    #         self.password.errors.append('Пароль не может состоять только из цифр')
    #         return False
    #
    #     if not self.password.data.isalpha():
    #         check = 1
    #
    #     if check == 0:
    #         self.password.errors.append('Пароль не может состоять только из букв')
    #         return False
    #     return True


class PostForm(FlaskForm):
    title = wf.StringField('Заголовок', validators=[wf.validators.DataRequired()])
    content = wf.TextAreaField('Текст', validators=[wf.validators.DataRequired()])
    date_post = wf.DateField('Дата', validators=[wf.validators.DataRequired()])
    is_boom_news = wf.BooleanField('Супер новость')
    submit = wf.SubmitField('Ok')


