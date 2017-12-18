from .models import Book
from rest_framework import  serializers
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')# usename
	class Meta:
		model = Book
		fields = ('name','title','author','owner')

	# def restore_object(self,attrs,instance=None):
	# 	if instance:
	# 		instance.name = attrs['name']
	# 		instance.title = attrs['title']
	# 		instance.author = attrs['author']
	# 		return instance
	# 	return Book(**attrs)
class UserSerializer(serializers.ModelSerializer):
	book = serializers.PrimaryKeyRelatedField(many=True,queryset=Book.objects.all())
	class Meta:
		model = User
		fields = ('id', 'username', 'book')