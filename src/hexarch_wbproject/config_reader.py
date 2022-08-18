from dataclasses import dataclass

from environs import Env


@dataclass
class DjangoConfig:
    sekret_key: str
    debug_options: bool
    allowed_hosts: str


@dataclass
class Config:
    django: DjangoConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        django=DjangoConfig(
            sekret_key=env.str('SECRET_KEY'),
            allowed_hosts=env.str('ALLOWED_HOSTS'),
            debug_options=env.bool('DEBUG_OPTIONS')
        )
    )
