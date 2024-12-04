from collections.abc import *
from typing import *
from typing import Any
from typing import Protocol as ProtocolistProtocol
from typing import runtime_checkable
from typing import Union


@runtime_checkable
class Oauth(ProtocolistProtocol):
	
	def delete(self, arg0: str):
		...
	def post(self, arg0: str, json: Any):
		...
	def get(self, arg0: str, params: dict[str, str]):
		...
@runtime_checkable
class Keywords(ProtocolistProtocol):
	
	def __iter__(self):
		...
@runtime_checkable
class KeywordsSubscript(ProtocolistProtocol):
	
	def lower(self):
		...
@runtime_checkable
class Headers(ProtocolistProtocol):
	
	def __setitem__(self, key, value):
		...
@runtime_checkable
class R(ProtocolistProtocol):
	headers: Union[Headers, MutableMapping]
