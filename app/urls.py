from . import views
from . import app

app.add_url_rule('/', view_func=views.index, methods=['GET'], endpoint='index')

#urls for user

app.add_url_rule('/register', view_func=views.register, methods=['GET', 'POST'], endpoint='register')
app.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'], endpoint='login')
app.add_url_rule('/logout', view_func=views.logout, methods=['GET', 'POST'], endpoint='logout')
app.add_url_rule('/add/post', view_func=views.post_add, methods=['GET', 'POST'], endpoint='post_add')
app.add_url_rule('/post/<int:post_id>', view_func=views.post_detail, methods=['GET', 'POST'], endpoint='post_detail')
app.add_url_rule('/post/<int:post_id>/delete', view_func=views.post_delete, methods=['GET', 'POST'], endpoint='post_delete')
app.add_url_rule('/post/<int:post_id>/edit', view_func=views.post_edit, methods=['GET', 'POST'], endpoint='post_edit')
