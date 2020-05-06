import requests as rq
import os
import json
"""
Countyfile = os.path.join(os.path.dirname(__file__), "counties.json")
Zonefile = os.path.join(os.path.dirname(__file__), "zone.json")
SAMEfile = os.path.join(os.path.dirname(__file__), "SAME.json")
"""

with open("counties.json") as file:
    countydict = json.load(file)
with open("zone.json") as file:
    zonedict = json.load(file)
class API:
    def __init__(self, userAgent):
        self.ua = userAgent
    def countyUGC(self, County, State):
        if State.upper() not in countydict:
            raise Exception("Incorrect State Name")
        if County.lower() not in countydict[State.upper()]:
            raise Exception("Incorrect County Name")
        UGC = countydict[State.upper()][County.lower()]
        return UGC
    def zoneUGC(self, County, State):
        if State.upper() not in zonedict:
            raise Exception("Incorrect State Name")
        if County.title() not in zonedict[State.upper()]:
            raise Exception("Incorrect County Name")
        UGC = zonedict[State.upper()][County.title()]
        return UGC
    def forecast(self, County, State):
        zone = self.zoneUGC(County, State)
        UGC = zone["UGC"]
        url = f"https://api.weather.gov/zones/ForecastArea/{UGC}/forecast"
        req = rq.get(url, headers={
            "Accept":"application/ld+json",
            "user-agent": self.ua
            })
        response = req.json()
        returnObj = {
            "county": zone["CountyName"],
            "office": zone["Office"],
            "forecast": response["periods"]
        }
        return returnObj
    def alerts(self, County, State):
        events = []
        county = self.countyUGC(County, State)
        url = f"https://api.weather.gov/alerts/active/zone/{county}"
        req = rq.get(url, headers={
            "Accept":"application/ld+json",
            "user-agent": self.ua
            })
        response = req.json()
        alerts = response["@graph"]
        for alert in alerts:
            alertDictionary = {
                "name": alert["event"],
                "severity": alert["severity"],
                "effective": alert["effective"],
                "expires": alert["expires"],
                "senderName": alert["senderName"],
                "headline": alert["headline"]
            }
            events.append(alertDictionary)
        return events
