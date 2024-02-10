from aiogram.fsm.state import StatesGroup, State


class ReportUser(StatesGroup):
    """
    Состояние - Репорта
    """

    message_text: str = State()
    tg_id: int = State()
    photo_user: bytes = State()
    street_data: str = State()
    latitude: int = State()
    longitude: int = State()