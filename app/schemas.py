from pydantic import BaseModel
from enum import Enum
from datetime import date
from typing import Dict, List


class CargoType(str, Enum):
    glass = 'Glass'
    other = 'Other'


class TariffItem(BaseModel):
    cargo_type: CargoType
    rate: float


class TariffCreate(BaseModel):
    tariffs: Dict[date, List[TariffItem]]

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "tariffs": {
                        "2020-06-01": [
                            {"cargo_type": "Glass",
                             "rate": 0.04},

                            {"cargo_type": "Other",
                             "rate": 0.01}
                        ],
                        "2020-07-01": [
                            {"cargo_type": "Glass",
                             "rate": 0.035},

                            {"cargo_type": "Other",
                             "rate": 0.015}
                        ]
                    }
                }
            ]
        }


class Tariff(TariffItem):
    tariff_date: date


class InsuranceData(BaseModel):
    cargo_type: CargoType
    tariff_date: date
    cost: float
