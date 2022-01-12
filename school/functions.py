def handle_uploaded_file(f):
    with open('school/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)