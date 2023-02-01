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


class Autoscout24Spider(scrapy.Spider):
    MAX_PAGES = 20
    name = 'autoscout24'
    allowed_domains = ['web', 'autoscout24.com']
    start_urls = ['https://www.autoscout24.com/lst?&sort=age&desc=1&ustate=N%2CU&size=20&cy=D&atype=C&page=1']

    def parse(self, response):
        page_count = 20
        # Get the next index URLs and yield Requests
        for make in Make:
            for model in Model:
                for sortcrit in SortCriteria:
                    for desc in SortDirection:
                        for idx in range(1, page_count+1):                    
                            yield Request(
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
                            )

        # Get item URLs and yield Requests
        item_selector = response.xpath('//*[@class="cldt-summary-titles"]/a/@href')
        for url in item_selector.extract():
            yield Request(urljoin(response.url, url), callback=self.parse_item)

    def parse_item(self, response):
        """ This function parses a car page.
        @url https://www.autoscout24.com/offers/ferrari-monza-sp2-ready-now-export-worldwide-gasoline-red-662f3a46-7168-46e5-b284-6636e5276303?cldtidx=1&cldtsrc=listPage
        @returns items 1
        @scrapes make model version registration price_euro driven_km power_kW
        @scrapes url project spider server date
        """

        self.log("Visited %s" % response.url)
        for car in response.selector.xpath("//main[@class='ListPage_main__L0gsf']/article").get():
            yield {
                'Model' : car.selector.xpath("/div[@class='ListItem_header__uPzec']//h2/text()").get(), 
            }