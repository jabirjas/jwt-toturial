from rest_framework import serializers
from snippets.models import Snippet


# class SnippetSerializer(serializers.Serializer):
# 	title = serializers.CharField(required=False)
# 	code = serializers.CharField(required=False)

# 	def create(self, validated_data):
# 		return Snippet.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		instance.title = validated_data.get("title",instance.title)
# 		instance.code = validated_data.get("code",instance.code)
# 		instance.save()
# 		return instance


class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ['id', 'title', 'code']



