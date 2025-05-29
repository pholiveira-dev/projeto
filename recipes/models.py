from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=65)


class Recipe(models.Model):
    title = models.CharField(max_length=65) # Vai ser o equivalente a um varchar na base de dados
    description = models.CharField(max_length=165)
    slug = models.SlugField()# Aqui, todo espaço vai virar hífen, por exemplo: curso-de-django-para-iniciantes
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.CharField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField() # Aqui é uma área livre pro usuário poder digitar
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add vai gerar exatamente a data e o horário quando o usuário enviar a receita para o sistema
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )


# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)