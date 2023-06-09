from django.contrib.auth.backends import ModelBackend
import re
from .models import User


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }


def get_mobile_username(account):
    # 获取前端传来的数据，判断是否手机号还是用户名
    try:
        if re.match(r'1[3-9]\d{9}$', account):
            user = User.objects.get(mobile=account)
        else:
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user


class UsernameMobileAuthBackend(ModelBackend):
    # 判断密码是否正确
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_mobile_username(username)
        if user and user.check_password(password):
            return user
