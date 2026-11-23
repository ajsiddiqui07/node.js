from rest_framework import serializers
from django.contrib.auth import get_user_model
from candidates.models import CandidateProfile
from recruiters.models import RecruiterProfile, CompanyProfile

User = get_user_model()

# User Details Serializer (Token Response ke liye)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'phone')

# Register Serializer for Candidate & Recruiter
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    company_name = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'phone', 'company_name')

    def validate(self, attrs):
        role = attrs.get('role')
        company_name = attrs.get('company_name')

        # Recruiter validation: Company Name zaroori hai
        if role == 'recruiter' and not company_name:
            raise serializers.ValidationError({"company_name": "Company name is required for Recruiter registration."})
        return attrs

    def create(self, validated_data):
        role = validated_data.get('role', 'candidate')
        company_name = validated_data.pop('company_name', None)
        password = validated_data.pop('password')

        # Create Custom User
        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        # Automatic Profile Creation based on Role
        if role == 'candidate':
            CandidateProfile.objects.create(user=user)
        elif role == 'recruiter':
            # Check or Create Company Profile
            company, _ = CompanyProfile.objects.get_or_create(name=company_name)
            RecruiterProfile.objects.create(user=user, company=company)

        return user