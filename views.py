from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Pyramid Scaffold'}

@view_config(route_name='color', renderer='templates/mytemplate.jinja2')

def my_view_color(request):

	mydict = request.matchdict
	print mydict['query']

return {'color': mydict['query']}