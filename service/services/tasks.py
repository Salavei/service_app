from celery import shared_task


@shared_task
def set_price(subscription_id):
    # кросс иморт
    from services.models import Subscription

    subscription = Subscription.objects.get(id=subscription_id)
    new_price = subscription.service.full_price - \
                subscription.service.full_price * (subscription.plan.discount_percent / 100)
    subscription.price = new_price
    # save_model=False - не даст создать рекурсию
    subscription.save()