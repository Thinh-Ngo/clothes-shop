from django.urls import path
from .views import (
    HomeView,
    CheckoutView,
    ItemDetailView,
    StripeIntentView,
    LandingPage,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_item_from_cart,
    add_single_item_to_cart,
    WebHook,
)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("landing/", LandingPage.as_view(), name="landing"),
    path("webhook/", WebHook.as_view(), name="webhook"),
    path(
        "create-payment-intent/<username>/",
        StripeIntentView.as_view(),
        name="create-payment-intent",
    ),
    path("order-summary/", OrderSummaryView.as_view(), name="order-summary"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product"),
    path("add-to-cart/<slug>/", add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<slug>/", remove_from_cart, name="remove-from-cart"),
    path(
        "remove-single-item-from-cart/<slug>/",
        remove_single_item_from_cart,
        name="remove-single-item-from-cart",
    ),
    path(
        "add-single-item-to-cart/<slug>",
        add_single_item_to_cart,
        name="add-single-item-to-cart",
    ),
]