from dataclasses import dataclass


@dataclass
class Airplane:
    number: int
    company_code: str
    company_name: str
    capacity: int
    model: str
