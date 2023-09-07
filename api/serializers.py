from .models import UserProfile
from rest_framework import serializers

REPO_URL = "github.com/50-Course/hngx"

class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    current_day = serializers.SerializerMethodField()
    utc_time = serializers.SerializerMethodField()
    github_file_url = serializers.SerializerMethodField()
    github_repo_url = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            "slack_name",
            "current_day",
            "utc_time",
            "track",
            "github_file_url",
            "github_repo_url",
        ]

    @property
    def get_current_day(self, obj):
        return datetime.datetime.now().strftime("%A")
    
    @property
    def get_utc_time(self, obj):
        return timezone.now()

    def get_github_file_url(self, obj):
        return f"https://{REPO_URL}/blob/main/{README}.md"

    def get_github_repo_url(self, obj):
        return f"https://{REPO_URL}/"
