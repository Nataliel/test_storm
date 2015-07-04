from django.views.generic import ListView, DetailView, TemplateView
from website.models import Movie, Star


class HomePageTemplateView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageTemplateView, self).get_context_data(**kwargs)
        order = self.request.GET.get('ordering', '')
        if order:
            if order == 'a-z':
                context['movies'] = Movie.objects.all().order_by('title')
            else:
                context['movies'] = Movie.objects.all().order_by('-title')
        else:
            context['movies'] = Movie.objects.all()
        return context


class MovieDetailView(DetailView):
    model = Movie

    def get_queryset(self):
        return self.model.objects.filter(status=True, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        gender_id = [gen.id for gen in context['object'].gender.all()]
        star_id = [gen.id for gen in context['object'].stars.all()]
        context['related_movies'] = Movie.objects.filter(status=True, gender__pk__in=gender_id, stars__pk__in=star_id).\
                                        exclude(slug=context['object'].slug).distinct()[:10]
        return context


class StarDetailView(DetailView):
    model = Star
    template_name = 'website/star_detail.html'

    def get_queryset(self):
        return self.model.objects.filter(status=True, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(StarDetailView, self).get_context_data(**kwargs)
        context['related_movies'] = Movie.objects.filter(status=True, stars__slug=self.kwargs['slug'])[:20]
        return context


class GenderListView(ListView):
    template_name = 'website/gender_list.html'
    model = Movie

    def get_queryset(self):
        return self.model.objects.filter(status=True, gender__slug=self.kwargs['gender'])

    def get_context_data(self, **kwargs):
        context = super(GenderListView, self).get_context_data(**kwargs)
        order = self.request.GET.get('ordering', '')
        if order:
            if order == 'a-z':
                context['movie_list'] = context['movie_list'].order_by('title')
            else:
                context['movie_list'] = context['movie_list'].order_by('-title')

        return context
