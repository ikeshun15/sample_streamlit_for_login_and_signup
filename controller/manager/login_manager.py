import hashlib

from model import UserInfoManager, UserInfoEntity

class LoginManager:
    @staticmethod
    def hash_password(password: str) -> str:
        # パスワードをバイト列に変換する
        password_bytes = password.encode('utf-8')

        # ハッシュ化アルゴリズムを選択する
        hash_algorithm = hashlib.sha256()

        # パスワードをハッシュ化する
        hash_algorithm.update(password_bytes)

        # ハッシュ化されたパスワードを返す
        return hash_algorithm.hexdigest()

    @classmethod
    def login(cls, username: str, password: str) -> tuple[bool, str, UserInfoEntity]:
        hashed_password = cls.hash_password(password=password)
        registered_users = UserInfoManager.get_registered_users_dict()
        user_info_instance = UserInfoEntity(username=username, hashed_password=hashed_password)

        if user_info_instance.username not in registered_users:
            return False, "このユーザは登録されていません。", None
        if registered_users[user_info_instance.username] != user_info_instance.hashed_password:
            return False, "パスワードが誤っています。", None
        
        return True, "ログイン成功", user_info_instance