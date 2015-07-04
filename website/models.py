# coding=utf-8
from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    status = models.BooleanField(verbose_name="Ativo", default=True)
    created_at = models.DateTimeField(verbose_name='Data do Cadastro', blank=True, default=datetime.now,
                                      help_text="Data em que este filme foi cadastrado")

    class Meta:
        abstract = True


class Country(models.Model):
    name = models.CharField('Nome', max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __unicode__(self):
        return self.name


class Star(BaseModel):
    photo = models.ImageField('Foto', upload_to='uploads/star/%Y/%m/')
    country = models.ForeignKey(Country, verbose_name='País', blank=True, null=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'star_detail', [self.slug]

    def admin_photo(self):
        if self.photo:
            im = self.photo
            return '<img src="{0}" />'.format(im.url)
        else:
            return 'Sem Imagem'

    admin_photo.allow_tags = True
    admin_photo.short_description = u'Foto'

class Gender(BaseModel):
    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    title = models.CharField('Título', max_length=100, help_text='Titulo do filme, no maximo 100 caracteres.')
    gender = models.ManyToManyField(Gender, verbose_name='Genero do filme')
    photo = models.ImageField('Foto', upload_to='uploads/movie/%Y/%m/')
    trailer = models.CharField(max_length=200, help_text='Endereço do Youtube', blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, )
    synopsis = models.TextField('Sinopse')
    stars = models.ManyToManyField(Star, max_length=300, help_text='Elenco do filme')
    created_at = models.DateTimeField(verbose_name='Data do Cadastro', blank=True, default=datetime.now,
                                      help_text="Data em que este filme foi cadastrado")
    status = models.BooleanField(verbose_name="Cartaz", default=True, help_text="Se está em cartaz ou não.")

    @models.permalink
    def get_absolute_url(self):
        return 'movie_detail', [self.gender.last().slug, self.slug]

    def __unicode__(self):
        return self.title

    def admin_photo(self):
        if self.photo:
            im = self.photo
            return '<img src="{0}" />'.format(im.url)
        else:
            return 'Sem Imagem'

    admin_photo.allow_tags = True
    admin_photo.short_description = u'Foto'

    def get_trailer(self):
        return "http://www.youtube.com/embed/" + self.trailer.split('/v/')[-1]