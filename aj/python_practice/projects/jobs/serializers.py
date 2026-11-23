from rest_framework import serializers
from .models import Job
from candidates.models import Skill
from candidates.serializers import SkillSerializer
from recruiters.models import CompanyProfile

# Company Details Serializer (Job Output me dikhane ke liye)
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = ('id', 'name', 'website', 'logo')

# Job Read & Write Serializer
class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    required_skills = SkillSerializer(many=True, read_only=True)
    required_skill_ids = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        write_only=True,
        source='required_skills'
    )

    class Meta:
        model = Job
        fields = (
            'id', 
            'title', 
            'description', 
            'location', 
            'company', 
            'required_skills', 
            'required_skill_ids', 
            'is_active', 
            'created_at'
        )
        read_only_fields = ('company', 'posted_by', 'created_at')