import time
import xml.etree.ElementTree as ET

TAG_PREFIX = "{http://www.ebay.com/marketplace/search/v1/services}"

class Item:
    def __init__(self, itemId, title, url, currentPrice, endTime):
        self.itemId = itemId
        self.title = title
        self.url = url
        self.currentPrice = currentPrice
        self.endTime = endTime

    def __str__(self):
        return self.title+" ("+str(self.itemId)+") - €"+str(self.currentPrice)+" - "+str(self.endTime)+"\n"+self.url

    def endsAtGoodTime(self):
        endTimestamp = time.strptime(self.endTime, '%Y-%m-%dT%H:%M:%S.000Z')
        wday = endTimestamp.tm_wday
        hour = endTimestamp.tm_hour + 1 + time.daylight     # calculate localtime (for Germany)
        if hour > 24:
            hour %= 24
            wday += 1
            wday %= 7
        return (1 <= wday <= 5) and (0 <= hour < 13)    # we want offers with endTime on workdays between 12am and 1pm

def parseResults(xmldoc):
    """ parses xmldoc (findItemsAdvancedResponse) to array of matched items """
    tree = ET.fromstring(xmldoc)
    items = []
    for itemElement in tree.findall('.//'+TAG_PREFIX+'item'):
        itemId = itemElement.find('./'+TAG_PREFIX+'itemId').text
        title = itemElement.find('./'+TAG_PREFIX+'title').text
        url = itemElement.find('./'+TAG_PREFIX+'viewItemURL').text
        currentPrice = itemElement.find('./'+TAG_PREFIX+'sellingStatus'+'/'+TAG_PREFIX+'currentPrice').text
        endTime = itemElement.find('./'+TAG_PREFIX+'listingInfo'+'/'+TAG_PREFIX+'endTime').text
        items.append(Item(itemId, title, url, currentPrice, endTime))
    return items

def findGoodOffers(xmldoc):
    """ parses xmldoc (findItemsAdvancedResponse) to array of matched items with good endTime """
    items = parseResults(xmldoc)
    return list(filter(lambda i: i.endsAtGoodTime(), items))

