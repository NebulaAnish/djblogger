# factory creates data for us to perform tests on
import factory 
from django.contrib.auth.models import User
from djblogger.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
   class Meta:
      model = User

   username = "test"
   password = "test"
   is_superuser = True
   is_staff = True
   
   
class PostFactory(factory.django.DjangoModelFactory):
   class Meta:
      model = Post
   title = "Anish"
   subtitle = "anish"
   slug = "x"
   author = factory.SubFactory(UserFactory)
   content = "anish neupane"
   status = "published"