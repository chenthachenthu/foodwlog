def names(request):
    if 'username' in request.session:
        for KEY in request.session.keys():
            name = request.session[KEY]
            print(name)
        return {'name':name}
    return {}

