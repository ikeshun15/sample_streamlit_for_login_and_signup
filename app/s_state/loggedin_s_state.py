from .base_s_state import BaseSState


class LoggedinSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return "loggedin"
    
    @staticmethod
    def get_default() -> str:
        return False