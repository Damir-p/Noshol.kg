from django.db.models import TextChoices


class UserType(TextChoices):
    PRODUCER = 'PRODUCER'
    CONSUMER = 'CONSUMER'

    


# PRODUCER = 'PRODUCER'
# CONSUMER = 'CONSUMER'

    # USER_TYPE = (
    #     (PRODUCER, PRODUCER),
    #     (CONSUMER, CONSUMER)
    # )