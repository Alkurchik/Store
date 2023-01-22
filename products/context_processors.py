from products.models import Basket


def baskets(requst):
    user = requst.user
    return {'baskets': Basket.objects.filter(user=user) if user.is_authenticated else []}
