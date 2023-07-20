from django.shortcuts import redirect

NOT_ALLOWED_URLS = ["/categories/", "/all_companies/", "/staff/task/", "/", "/home/"]


class ConfirmUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path in NOT_ALLOWED_URLS:
                return redirect("/login/")
        response = self.get_response(request)
        return response
