import streamlit as st
from streamlit_lottie import st_lottie
from time import sleep

from controller import LoginManager, LottieManager
from ..s_state import LoggedinUserInfoSState, WakeupLottieSState, FinishedLoginLottieSState, LoggedinSState

class HomeAppComponents:
    @staticmethod
    def init_page() -> None:
        st.set_page_config(
            page_title="Home",
            page_icon="🏠",
        )

    @staticmethod
    def init_session_state() -> None:
        LoggedinSState.init()
        WakeupLottieSState.init()
        FinishedLoginLottieSState.init()
        LoggedinUserInfoSState.init()

    @staticmethod
    def wakeup_lottie() -> None:
        if not WakeupLottieSState.get():
            st_lottie(animation_source=LottieManager.WAKEUP_LOGO, key="WAKEUP_LOTTIE", speed=0.6, reverse=False, loop=False)
            sleep(1.3)
            WakeupLottieSState.set(value=True)
            st.rerun()
    
    @staticmethod
    def login_success_lottie() -> None:
        if not FinishedLoginLottieSState.get():
            st_lottie(animation_source=LottieManager.LOGIN_SUCCESS_LOGO, key="LOGIN_SUCCESS_LOTTIE", speed=1.7, reverse=False, loop=False)
            sleep(1.3)
            FinishedLoginLottieSState.set(value=True)
            st.rerun()
    
    @staticmethod
    def main_page() -> None:
        st.header(body="😊 メインページ", divider='rainbow')

        st.markdown(
            """
            ### 食べたいいちご
            - 越後姫
            - とちおとめ
            - あまおう
            
            This streamlit was made by Shunichi Ikezu🍓
            """
        )

        st.write(f"ユーザ名: :rainbow[**{st.session_state.loggedin_user_info.username}**]でログイン中")
    
    # @staticmethod
    # def signup_page() -> None:
    #     pass

    @classmethod
    def login_page(cls) -> None:
        st.header(body="🔑 ログイン", divider='rainbow')
        login_form = st.form(key="login_form")
        with login_form:
            username = st.text_input(label="ユーザ名", placeholder="ユーザ名を入力")
            password = st.text_input(label="パスワード", type="password", placeholder="パスワードを入力")
            submit_button = st.form_submit_button(label="Submit", type="primary")

        if submit_button:
            is_success, message, user_info_instance = LoginManager.login(username=username, password=password)
            LoggedinSState.set(value=is_success)

            with login_form:
                if is_success:
                    st.success(icon="🙆", body=message)
                    LoggedinUserInfoSState.set(value=user_info_instance)
                    cls.login_success_lottie()
                else:
                    st.warning(icon="🙅", body=message)

            # st.rerun()

    # @classmethod
    # def select_signup_or_login_page(cls):
    #     signup_or_login =  st.radio(label="ログインまたは新規登録", options=["**ログイン**", "**新規登録**"], horizontal=True)
    #     if signup_or_login == "**ログイン**":
    #         cls.login_page()
    #     else:
    #         cls.signup_page()

    @classmethod
    def set_page(cls) -> None:
        cls.init_page()
        cls.init_session_state()
        cls.wakeup_lottie()
        
        if LoggedinSState.get():
            cls.main_page()
        else:
            # cls.select_signup_or_login_page()
            cls.login_page()