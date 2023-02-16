from django.urls import path
from accelerators.views import AcceleratorView

urlpatterns=[
    path("accelerator/",AcceleratorView.as_view()),
    path("accelerator/<uuid:uid>", AcceleratorView.as_view())
]