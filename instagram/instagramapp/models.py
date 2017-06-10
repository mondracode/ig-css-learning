from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class MiUsuario( models.Model ):
    usuario = models.OneToOneField( User, on_delete=models.CASCADE )
    foto = models.CharField( max_length = 600, null = True )

class Follow( models.Model ):
    followers = models.ForeignKey( MiUsuario, related_name='%(class)s_username_sigue' )
    following = models.ForeignKey ( MiUsuario, related_name='%(class)s_username_sigo' )

class Post( models.Model ):
    foto = models.CharField( max_length = 600 )
    descripcion = models.CharField( max_length = 600, null = True )
    fecha = models.DateTimeField( default=datetime.now )
    creador = models.ForeignKey( MiUsuario )

class Like( models.Model ):
    creador = models.ForeignKey ( MiUsuario )
    post = models.ForeignKey ( Post )

class Comentario( models.Model ):
    creador = models.ForeignKey ( MiUsuario )
    contenido = models.CharField ( max_length = 600 )
    fecha = models.DateTimeField ( default=datetime.now )
    post = models.ForeignKey( Post )
# Create your models here.
