from wtforms import Form, SearchField, TextAreaField

class PostForm(Form):
    title = SearchField('Title')
    body = TextAreaField('Body')