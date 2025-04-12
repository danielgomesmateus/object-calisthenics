def login(request):
    username = "username"
    password = "password"

    if request.username == username and request.password == password:
        redirect("homepage")
    else:
        redirect("login")


def login(request):
    username = "username"
    password = "password"

    if request.username == username and request.password == password:
        return redirect("homepage")
    return redirect("login")