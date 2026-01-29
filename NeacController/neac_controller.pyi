from typing import Final as __Final


PAGE_NOACCESS: __Final[int] = 0x01
PAGE_READONLY: __Final[int] = 0x02
PAGE_READWRITE: __Final[int] = 0x04
PAGE_WRITECOPY: __Final[int] = 0x08
PAGE_EXECUTE: __Final[int] = 0x10
PAGE_EXECUTE_READ: __Final[int] = 0x20
PAGE_EXECUTE_READWRITE: __Final[int] = 0x40
PAGE_EXECUTE_WRITECOPY: __Final[int] = 0x80
PAGE_GUARD: __Final[int] = 0x100
PAGE_NOCACHE: __Final[int] = 0x200
PAGE_WRITECOMBINE: __Final[int] = 0x400


class NeacDriverManager:
    def __init__(self): ...
    @staticmethod
    def start_driver() -> bool: ...

    @staticmethod
    def stop_driver() -> bool: ...

    @staticmethod
    def connect() -> bool: ...

    @staticmethod
    def disconnect() -> None: ...

    @staticmethod
    def is_connected() -> bool: ...

    @staticmethod
    def get_process_base(pid: int) -> int: ...

    @staticmethod
    def read_process_memory(pid: int, address: int, size: int) -> bytes: ...

    @staticmethod
    def write_process_memory(pid: int, address: int, data: bytes) -> bool: ...

    @staticmethod
    def read_int8(pid: int, address: int) -> int: ...

    @staticmethod
    def read_uint8(pid: int, address: int, data: bytes): ...

    @staticmethod
    def read_int16(pid: int, address: int) -> int: ...

    @staticmethod
    def read_uint16(pid: int, address: int) -> int: ...

    @staticmethod
    def read_int32(pid: int, address: int) -> int: ...

    @staticmethod
    def read_uint32(pid: int, address: int) -> int: ...

    @staticmethod
    def read_int64(pid: int, address: int) -> int: ...

    @staticmethod
    def read_uint64(pid: int, address: int) -> int: ...

    @staticmethod
    def read_float(pid: int, address: int) -> float: ...

    @staticmethod
    def read_double(pid: int, address: int) -> float: ...

    @staticmethod
    def write_int8(pid: int, address: int, value: int) -> bool: ...

    @staticmethod
    def write_uint8(pid: int, address: int, value: int) -> bool: ...

    @staticmethod
    def write_int16(pid: int, address: int, value: int) -> bool: ...

    @staticmethod
    def write_uint16(pid: int, address: int, value: int) -> bool: ...

    @staticmethod
    def write_int32(pid: int, address: int, value: int) -> bool: ...

    @staticmethod
    def write_uint32(pid: int, address: int, value: int) -> bool: ...

    @staticmethod
    def write_int64(pid: int, address: int, value: int) -> bool: ...

    @staticmethod
    def write_uint64(pid: int, address: int, value: int) -> bool: ...

    @staticmethod
    def write_float(pid: int, address: int, value: float) -> bool: ...

    @staticmethod
    def write_double(pid: int, address: int, value: float) -> bool: ...

    @staticmethod
    def protect_process_memory(pid: int, address: int, size: int, new_protect: int) -> bool: ...

    @staticmethod
    def update_driver_state(function_id: int, state: int) -> bool: ...

    @staticmethod
    def kill_process_by_pid(pid: int) -> bool: ...

    @staticmethod
    def read_kernel_memory(address: int, size: int) -> bytes: ...

    @staticmethod
    def write_kernel_memory(address: int, data: bytes) -> bool: ...

    @staticmethod
    def get_ssdt_table() -> list[int]: ...

