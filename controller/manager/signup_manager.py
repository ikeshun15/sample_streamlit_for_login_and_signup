from ..handler import HashHandler
from model import UserInfoManager

class SignupManager:
    @staticmethod
    def signup(username: str, password: str, retype_password: str) -> tuple[bool, str]:
        hashed_password = HashHandler.hash_password(password=password)
        registered_users = UserInfoManager.get_registered_users_dict()

        if username in registered_users:
            return False, "このユーザはすでに登録されています。"
        if password != retype_password:
            return False, "パスワードが誤っています。パスワード入力欄を確認してください。"
        
        UserInfoManager.save_signup_user_info(data=registered_users, new_data={username: hashed_password})
        return True, "登録完了"
        