from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

    def validate_title(self, value):
        filter_list = ["php","laravel"]
        
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("stop it, get some help! dont use {}".format(i))

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"