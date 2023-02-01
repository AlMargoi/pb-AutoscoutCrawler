from enum import Enum

class Make(Enum):
    # ALL = ""
    # BMW = "/bmw"
    AUDI = "/audi"
    # FORD = "/ford"
    # MERCEDES_BENZ = "/mercedes-benz"
    # OPEL = "/opel"
    # VOLKSWAGEN = "/volkswagen"
    # RENAULT = "/renault"
    # TOYOTA = "/toyota"
    # PEUGEOT = "/peugeot"
    # NISSAN = "/nissan"
    # MINI = "/mini"
    # KIA = "/kia"
    # JAGUAR = "/jaguar"
    # HYNDAI = "/hyundai"
    # HONDA = "/honda"
    # FIAT = "/fiat"
    # DAIMLER = "/daimler"
    # CITROEN = "/citroen"
    # CHRYSLER = "/chrysler"
    # CHEVROLET = "/chevrolet"
    # NINEFF = "/9ff"
    # ABARTH = "/abarth"
    # AC = "/ac"
    # ACM = "/acm"
    # ACURA = "/acura"
    # AIXAM = "/aixam"
    # ALFA_ROMEO = "/alfa-romeo"
    # ALPINA = "/alpina"
    # ALPINE = "/alpine"
    # AMPHICAR = "/amphicar"
    # ARIEL_MOTOR = "/ariel-motor"
    # ARTEGA = "/artega"
    # ASPID = "/aspid"
    # ASTON_MARTIN = "/aston-martin"
    # AUSTIN = "/austin"
    # AUTOBIANCHI = "/autobianch"
    # AUVERLAND = "/auverland"
    # BAIC = "/baic"
    # BEDFORD = "/bedford"
    # BELLIER = "/bellier"
    # BENTLEY = "/bentley"
    # BOLLORE = "/bolloré"
    # BORGWARD = "/borgward"
    # BRILLIANCE = "/brilliance"
    # BUGATTI = "/bugatti"
    # BUICK = "/buick"
    # BYD = "/byd"
    # CADILLAC = "/cadillac"
    # CARAVANS_WOHNM = "/caravans-wohnm"
    # CASALINI = "/casalini"
    # TESLA = "/tesla"


class Model(Enum):
    A4 = "/a4"
    # A4_AllRoad = "/a4-allroad"

class Variant(Enum):
    pass

class FuelType(Enum):
    ALL = ""
    GASOLINE = "B"
    DIESEL = "D"
    ETHANOL = "M"
    ELECTRIC = "E"
    HYDROGEN = "H"
    LPG = "L"
    CNG = "C"
    ELECTRIC_GASOLINE = "2"
    OTHER = "O"
    ELECTRIC_DIESEL = "3"

class BodyType(Enum):
    #ALL = ""
    #COMPACT = "1"
    #CONVERTIBLE = "2"
    #COUPE = "3"
    #OFFROAD = "4"
    SEDANS = "5"
    STATIONWAGON = "6"
    #TRANSPORTER = "7"
    #VAN = "8"
    #OTHER = "9"

class Gear(Enum):
    AUTOMATIC = "A"
    MANUAL = "M"
    SEMI_AUTOMATIC = "S"

class VehicleCondition(Enum):
    #ALL = ""
    #NEW = "N"
    USED = "U"
    #EMPLOYEE_CAR = "J"
    #CLASSIC = "O"
    #DEMONSTRATION = "D"
    #PRE_REGISTERED = "S"

class Seller(Enum):
    ALL = ""
    #DEALER = "D"
    #PRIVATE = "P"

class SortCriteria(Enum):
    #AGE = "age"
    PRICE = "price"
    #MILEAGE = "mileage"
    #POWER = "power"
    #YEAR = "year"

class SortDirection(Enum):
    #DESCENDING = "desc=1"
    ASCENDING = "desc=0"

class RegistrationYear(Enum):
    Year2010 = "2010"
    Year2011 = "2011"
    Year2012 = "2012"
    Year2013 = "2013"
    Year2014 = "2014"
    Year2015 = "2015"
    Year2016 = "2016"
    Year2017 = "2017"
    Year2018 = "2018"
    Year2019 = "2019"
    Year2020 = "2020"
    Year2021 = "2021"
    Year2022 = "2022"
