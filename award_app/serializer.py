from rest_framework import serializers
from .models import Project,Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_name', 'image', 'demo', 'project_description', 'project_url', 'technologies_used')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','first_name','last_name','bio','profile_pic','pub_date_created']