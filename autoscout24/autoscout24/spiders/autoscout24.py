# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import Request
from scrapy.loader.processors import Join, MapCompose, Compose, TakeFirst, Identity

from autoscout24.items import CarsItem
from autoscout24.properties.properties import Make, Model, SortCriteria, SortDirection, VehicleCondition, Gear, RegistrationYear, BodyType
from autoscout24.properties.location import Country, City, LocationRadius
from autoscout24.properties.equipment import Equipment
from autoscout24.properties.price import PriceFrom, PriceTo
from autoscout24.properties.mileage import MileageTo, MileageFrom

from urllib.parse import urljoin
from w3lib.html import remove_tags, replace_escape_chars
import datetime
import socket
import uuid


class Autoscout24Spider2(scrapy.Spider):
    MAX_PAGES = 20
    name = 'autoscout24v2'
    allowed_domains = ['autoscout24.com']
    start_urls = ['https://www.autoscout24.com/']

    def start_requests(self):
        page_count = 20
        # Get the next index URLs and yield Requests
        for make in Make:
            for model in Model:
                for sortcrit in SortCriteria:
                    for desc in SortDirection:
                        for idx in range(1, page_count+1):                    
                            yield scrapy.Request(
                                'https://www.autoscout24.com/lst'
                                + make.value
                                + model.value
                                + "?fregfrom="
                                + RegistrationYear.Year2010.value
                                + "&fregto="
                                + RegistrationYear.Year2020.value
                                + "&kmfrom="
                                + MileageFrom.FROM_50000.value
                                + '&kmto='
                                + MileageTo.TO_150000.value
                                + "&body="
                                + BodyType.STATIONWAGON.value
                                + '?&sort='
                                + sortcrit.value
                                + '&'
                                + desc.value
                                + '&offer='
                                + VehicleCondition.USED.value
                                + '&eq='
                                + Equipment.ALL.value
                                + '&gear='
                                + Gear.MANUAL.value
                                + '&ustate=N%2CU&size=20&cy='
                                + Country.GERMANY.value
                                + '&priceto='
                                + PriceTo.TO_17500.value
                                + '&pricefrom='
                                + PriceFrom.FROM_8000.value
                                + '&atype=C&page='
                                + str(idx)
                            , callback=self.parse)
        
    def parse(self, response):
        for index, car in enumerate(response.xpath("//main[@class='ListPage_main__L0gsf']/article")):
            yield {
                'Index': index,
                'Model': car.xpath(".//*[@class='ListItem_title__znV2I Link_link__pjU1l']/h2/text()").get(),
                'Details': car.xpath(".//*[@class='ListItem_title__znV2I Link_link__pjU1l']/span[@class='ListItem_version__jNjur']/text()").get(),
                'Price': ((car.xpath(".//p[@class='Price_price__WZayw']/text()").get()).replace("€ ", "")).replace(".-",""),
                'Km' : (car.xpath(".//span[contains(text(), 'km')]/text()").get()).replace(" km", ""),
                'FirstReg' : car.xpath(".//span[contains(text(), '/20')]/text()").get(),
                'Power' : car.xpath(".//span[contains(text(), 'hp')]/text()").get(),
                'Owners' : (car.xpath(".//span[contains(@class, 'VehicleDetailTable_item__koEV4')][5]/text()").get()).replace("- (Previous Owners)", "0 Previous Owners"),
                'Transmission' : car.xpath(".//span[contains(@class, 'VehicleDetailTable_item__koEV4')][6]/text()").get(),
                'Fuel' : car.xpath(".//span[contains(@class, 'VehicleDetailTable_item__koEV4')][7]/text()").get(),
                'FuelConsumption' : car.xpath(".//span[contains(@class, 'VehicleDetailTable_item__koEV4')][8]/text()").get(),
            }
            
