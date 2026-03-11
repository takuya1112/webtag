from uuid import UUID

from ..exceptions import InvalidUuidError


class AppUuid:
    """AppUuid value objects

    Raises:
        InvalidUuidError: if not UUID objects
    """

    __slots__ = ("_value",)

    def __init__(self, value: UUID | str):
        if isinstance(value, UUID):
            uuid = value
        elif isinstance(value, str):
            try:
                uuid = UUID(value)
            except (ValueError, AttributeError):
                raise InvalidUuidError() from None
        else:
            raise InvalidUuidError()

        object.__setattr__(self, "_value", uuid)

    @property
    def value(self) -> UUID:
        return self._value

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self._value}')"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, UUID):
            return self._value == other
        if isinstance(other, AppUuid):
            return type(self) is type(other) and self._value == other._value
        return NotImplemented

    def __hash__(self) -> int:
        return hash(type(self), self._value)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError(
            f"'{self.__class__.__name__}' is immutable",
        )

    def __delattr__(self, name: str) -> None:
        raise AttributeError(
            f"'{self.__class__.__name__}' is immutable",
        )
