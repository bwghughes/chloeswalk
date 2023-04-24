from django.urls import path

from .views import (
    HomePageView,
    CancelView,
    SuccessView,
    CreateCheckoutSessionView,
    ProductLandingPageView,
    stripe_webhook
)

urlpatterns = [
    # path("about/", AboutPageView.as_view(), name="about"),  # new
    path("", HomePageView.as_view(), name="home"),
    path("cancel/", CancelView.as_view(), name="cancel"),
    path("success/", SuccessView.as_view(), name="success"),
    path(
        "create-checkout-session/<pk>/",
        CreateCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path('landing', ProductLandingPageView.as_view(), name='landing'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
]
