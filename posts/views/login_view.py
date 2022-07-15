from django.views.generic.edit import FormView
from posts.forms import LoginForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse


class LoginView(FormView):
    template_name = 'posts/login.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'form': LoginForm(request.POST)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Dados invalidos')

        authenticated_user = authenticate(
            request,
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Logado com sucesso')
            login(request, authenticated_user)
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Usuario ou senha invalidos')

        return render(request, self.template_name, self.contexto)
