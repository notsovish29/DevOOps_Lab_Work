# app.py
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

# Step 1: Configure Django
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="abc123",
    ALLOWED_HOSTS=["*"],
)

# Step 2: Create a simple view
def home(request):
    return HttpResponse("<center><h1>Django Project is running!</h1></center>")

# Step 3: Define URL pattern
urlpatterns = [
    path("", home),
]

# Step 4: Run server if executed directly
if __name__ == "__main__":
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
