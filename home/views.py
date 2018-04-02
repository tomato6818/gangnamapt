from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['data'] = 'hello world'
        return context

