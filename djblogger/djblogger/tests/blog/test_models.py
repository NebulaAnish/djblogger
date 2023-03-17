import pytest
pytestmark = pytest.mark.django_db

class TestPostModel:
   def test_str_return(self,post_factory):
      post = post_factory(title="test_post")
      assert post.__str__() == "test_post"