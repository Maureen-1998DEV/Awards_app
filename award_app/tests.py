from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Profile

# Create your tests here.


class ProjectTestClass(TestCase): 
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="test_user", first_name="maureen", last_name="ougo"
        )

        self.project = Project(
            title="Test Project",
            description="Test Description",
            image="image.jpg",
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.project.save_project()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)


class ProfileTestClass(TestCase):  
    def setUp(self):
        
        user = User.objects.create(
            username="test_user", first_name="maureen", last_name="ougo"
        )

        self.profile = Profile(
            bio="Test Bio",
            user=user,
            contact="Test Contact",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)