from fastapi import APIRouter, Request, Response, HTTPException, Cookie
from uuid import uuid4
from typing import Optional

router = APIRouter()

sessions = {}
SESSION_TIMEOUT = 3600


@router.post(
    "/create-session",
    summary="Создать сессию",
    description="Создает новую сессию и возвращает session_id в cookies.",
    tags=["Сессии"],
)
async def create_session(response: Response):
    """
    Создает сессию для пользователя, возвращая session_id через cookies.
    """
    session_id = str(uuid4())
    sessions[session_id] = {"data": {}, "expires_at": None}
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    return {"message": "Session created", "session_id": session_id}


@router.get(
    "/get-session",
    summary="Получить данные сессии",
    description="Возвращает данные текущей сессии по session_id из cookies.",
    tags=["Сессии"],
)
async def get_session(session_id: Optional[str] = Cookie(None)):
    """
    Получение данных сессии. session_id извлекается из cookies.
    """
    if not session_id or session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    session = sessions[session_id]
    return {"session_id": session_id, "data": session["data"]}


@router.post(
    "/update-session",
    summary="Обновить данные сессии",
    description="Обновляет данные в текущей сессии.",
    tags=["Сессии"],
)
async def update_session(data: dict, session_id: Optional[str] = Cookie(None)):
    """
    Обновление данных в текущей сессии. Данные передаются в теле запроса.
    """
    if not session_id or session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    sessions[session_id]["data"].update(data)
    return {"message": "Session updated", "data": sessions[session_id]["data"]}


@router.post(
    "/delete-session",
    summary="Удалить сессию",
    description="Удаляет текущую сессию, удаляя session_id из cookies.",
    tags=["Сессии"],
)
async def delete_session(response: Response, session_id: Optional[str] = Cookie(None)):
    """
    Удаляет сессию пользователя и session_id из cookies.
    """
    if not session_id or session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    del sessions[session_id]
    response.delete_cookie("session_id")
    return {"message": "Session deleted"}
