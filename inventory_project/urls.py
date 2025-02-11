from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from inventory.views import ProductViewSet, InvoiceViewSet, SupplierViewSet, PurchaseOrderViewSet, low_stock_alert

# Create a router for ViewSets
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'purchase-orders', PurchaseOrderViewSet)

# Define URL patterns
urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # API authentication (Login, Logout, Password Reset, Registration)
    path('api/auth/', include('dj_rest_auth.urls')),  
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  
    
    # Social authentication (Google, etc.)
    path('api/auth/social/', include('allauth.socialaccount.urls')),  

    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Inventory API routes
    path('api/', include(router.urls)),

    # Low-stock alert endpoint
    path('api/low-stock/', low_stock_alert, name='low-stock-alert'),
]
