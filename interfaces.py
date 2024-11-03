import collections.abc
from collections.abc import *
from typing import Literal, Protocol, Union, Any, runtime_checkable
@runtime_checkable
class Oauth4(Protocol):
    def delete(self, arg0: str):
        ...
@runtime_checkable
class Keywords1(Protocol):
    def __iter__(self):
        ...
@runtime_checkable
class Oauth2(Protocol):
    def post(self, arg0: str, json: Any):
        ...
@runtime_checkable
class Oauth1(Protocol):
    def get(self, arg0: str, params: dict[str, str]):
        ...
@runtime_checkable
class R1(Protocol):
    headers: Any
