from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="frontend/index.html"), name='main_page'),
    path('about/', TemplateView.as_view(template_name="frontend/about.html"), name='about'),
    path('account/', TemplateView.as_view(template_name="frontend/account.html"), name='account'),
    path('cart/', TemplateView.as_view(template_name="frontend/cart.html"), name='cart'),
    path('catalog/', TemplateView.as_view(template_name="frontend/catalog.html"), name='catalog'),
    path('catalog/<int:id>/', TemplateView.as_view(template_name="frontend/catalog.html"), name='catalog_id'),
    path('history-order/', TemplateView.as_view(template_name="frontend/historyorder.html"), name='historyorder'),
    path('order-detail/<int:id>/', TemplateView.as_view(template_name="frontend/oneorder.html"), name='oneorder'),
    path('orders/<int:id>/', TemplateView.as_view(template_name="frontend/order.html"), name='order'),
    path('payment/<int:id>/', TemplateView.as_view(template_name="frontend/payment.html"), name='payment'),
    path('payment-someone/', TemplateView.as_view(template_name="frontend/paymentsomeone.html"), name='paymentsomeone'),
    path('product/<int:id>/', TemplateView.as_view(template_name="frontend/product.html"), name='product'),
    path('profile/', TemplateView.as_view(template_name="frontend/profile.html"), name='profile'),
    path('progress-payment/', TemplateView.as_view(template_name="frontend/progressPayment.html"), name='progressPayment'),
    path('sale/', TemplateView.as_view(template_name="frontend/sale.html"), name='sale'),
    path('sign-in/', TemplateView.as_view(template_name="frontend/signIn.html"), name='signIn'),
    path('sign-up/', TemplateView.as_view(template_name="frontend/signUp.html"), name='signUp'),
]
