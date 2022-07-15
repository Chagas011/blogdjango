from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django.contrib import messages
from posts.forms import RegisterForm
from django.urls import reverse


class RegisterView(FormView):
    template_name = 'posts/register_view.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.contexto = {
            'form': RegisterForm(request.POST)
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, self.contexto)

        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuario criado com sucesso')
        return redirect(reverse('login_form'))
