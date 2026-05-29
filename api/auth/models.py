from dataclasses import dataclass, field


@dataclass
class AuthUser:
    id: str

@dataclass
class LoginRequest:
    email: str
    password: str


@dataclass
class RegisterRequest:
    email: str
    password: str

@dataclass
class AnonRegisterRequest:
    id: str

@dataclass
class RefreshRequest:
    refresh_token: str


@dataclass
class LogoutRequest:
    refresh_token: str


@dataclass
class TokenResponse:
    access_token: str
    refresh_token: str
    token_type: str = field(default="bearer")

@dataclass
class AnonRegisterResponse:
    device_token: str
    friend_request_token: str
