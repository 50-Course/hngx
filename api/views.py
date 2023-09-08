from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timezone


class SlackUserView(APIView):
    def get(self, request: Request) -> Response:
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

        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')

        if slack_name is None or track is None:
            return Response({"error": "slack_name and track are required query parameters"}, status=status.HTTP_400_BAD_REQUEST)


        current_day = datetime.now().astimezone(timezone.utc).strftime('%A')


        # Validate UTC time (+/-2 hours)
        utc_time = datetime.now(timezone.utc).replace(microsecond=0).isoformat() + 'Z'

        github_repo_url = 'https://github.com/50-Course/hngx'
        github_file_url = f'{github_repo_url}/blob/main/api/view.py'

        return Response(
            data = {
                "slack_name": slack_name,
                "current_day": current_day,
                "utc_time": utc_time,
                "track": track,
                "github_file_url": github_file_url,
                "github_repo_url": github_repo_url,
                "status_code": status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )
