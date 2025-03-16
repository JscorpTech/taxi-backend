from django.core.management.base import BaseCommand
import jwt
from config.env import env
from datetime import datetime, timedelta


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--type", default="user", required=False)

    def handle(self, *args, **options):
        jwt_type = options.get("type", "user")
        if jwt_type == "user":
            payload = {
                "exp": datetime.now() + timedelta(minutes=10),
                "tg_id": 1,
            }
        else:
            payload = {
                "exp": datetime.now() + timedelta(minutes=10),
                "bot_id": 1,
            }
        token = jwt.encode(payload, env.str("DJANGO_SECRET_KEY"), "HS256")
        print("%s: %s" % (jwt_type, token))
