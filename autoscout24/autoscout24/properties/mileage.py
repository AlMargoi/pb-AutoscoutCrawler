from enum import Enum

class MileageTo(Enum):
    ALL = ""
    TO_2500 = "2500"
    TO_5000 = "5000"
    TO_50000 = "50000"
    TO_100000 = "100000"
    TO_125000 = "125000"
    TO_150000 = "150000"

class MileageFrom(Enum):
    ALL = ""
    FROM_2500 = "2500"
    FROM_5000 = "5000"
    FROM_50000 = "50000"