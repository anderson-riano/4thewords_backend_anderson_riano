from pydantic import BaseModel, Field
from typing import Generic, TypeVar, Optional

T = TypeVar("T")

class RequestModel(BaseModel, Generic[T]):
    data: T

class ResponseModel(BaseModel, Generic[T]):
    success: bool = Field(...)
    message: Optional[str] = Field(None)
    data: Optional[T] = Field(None)
