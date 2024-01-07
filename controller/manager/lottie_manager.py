from model import JsonHandler

class LottieManager:
    WAKEUP_LOGO = JsonHandler.load_json(json_file_path="./data/wakeup_lottie.json")
    LOGIN_SUCCESS_LOGO = JsonHandler.load_json(json_file_path="./data/login_success_lottie.json")