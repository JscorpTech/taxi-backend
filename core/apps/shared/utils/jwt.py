from typing import Dict, Optional
from config.env import env
import jwt
from datetime import datetime, timedelta


def get_claim(token: str) -> Optional[Dict]:
    if token is not None:
        try:
            claim = jwt.decode(token, env.str("DJANGO_SECRET_KEY"), ["HS256"])
            return claim
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    return None


def get_pk(request) -> Optional[int]:
    token = request.headers.get("token", None)
    if token is None:
        return None
    claim = get_claim(token)
    if claim is None:
        return None
    pk = claim.get("bot_id", None)
    return pk


def make_bot_jwt():
    payload = {
        "exp": datetime.now() + timedelta(minutes=10),
        "bot_id": 1,
    }
    return jwt.encode(payload, env.str("DJANGO_SECRET_KEY"), "HS256")


def make_user_jwt():
    payload = {
        "exp": datetime.now() + timedelta(minutes=10),
        "tg_id": 1,
    }
    return jwt.encode(payload, env.str("DJANGO_SECRET_KEY"), "HS256")
