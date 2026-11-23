from rest_framework import serializers
from .models import CandidateProfile, Skill, Project
from jobPortal.serializers import UserSerializer

# Skill Serializer
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name')

# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'github_link', 'live_link')
        read_only_fields = ('candidate',)

# Candidate Profile Serializer
class CandidateProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    skill_ids = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), 
        many=True, 
        write_only=True, 
        source='skills'
    )
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = CandidateProfile
        fields = ('id', 'user', 'title', 'bio', 'resume', 'skills', 'skill_ids', 'projects')

# File Upload Serializer for Resume
class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = ('resume',)