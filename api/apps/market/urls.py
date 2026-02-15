from rest_framework.routers import DefaultRouter
from .views import StoreViewSet, CategoryViewSet, ProductViewSet, SaleViewSet

router = DefaultRouter()

router.register(r"store", StoreViewSet, basename="store")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"sales", SaleViewSet, basename="sales")

urlpatterns = router.urls
