from django.shortcuts import redirect

class AdminAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/SRAB/Admin/Menu'):
            if not request.session.get('admin_auth'):
                return redirect('/SRAB/Admin')
        
        response = self.get_response(request)
        return response
