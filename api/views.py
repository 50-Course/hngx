from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer


class SlackUserView(APIView):
    def get(request: Request, slack_name: str, track: str) -> Response:
        """
        Retrieve a user by their slack_name and track
        
        Usage:
            GET /api/v1/users?q=slack_name=<slack_name>&track=<track>
        
        Example:
            {
              "slack_name": "example_name",
              "current_day": "Monday",
              "utc_time": "2023-08-21T15:04:05Z",
              "track": "backend",
              "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
              "github_repo_url": "https://github.com/username/repo",
              “status_code”: 200
            }

        """

        try:
            user = UserProfile.objects.get(slack_name=slack_name, track=track)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


