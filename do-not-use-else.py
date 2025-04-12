def login(request):
    username = "username"
    password = "password"

    if request.username == username and request.password == password:
        redirect("homepage")
    else:
        add_flash("error", "Bad credentials")
        redirect("login")


def login(request):
    username = "username"
    password = "password"

    if request.username == username and request.password == password:
        return redirect("homepage")

    add_flash("error", "Bad credentials")
    return redirect("login")