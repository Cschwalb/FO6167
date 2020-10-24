# This is a sample Python script.
import scrapy
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class getWolf:
    def __init__(self, sNewWebsite="https://wolf.live/my+gams"):
        self.args1 = sNewWebsite

        if __name__ == '__main__':
            print("Here argument %s " % self.args1)
            rReq = self.getWebsiteRequest()
            print("request is %s" % rReq.body)

    def log_parse(self, response):
        self.logger.info("Visited %s", response.url)

    def getWebsiteRequest(self):
        return scrapy.Request(self.args1, callback=self.log_parse)




class readBackwards:
    def __init__(self, args1="racecar"):
        self.args1 = args1



    def readStringBackwards(self, backWord):
        '''backWord is now reversed'''
        return backWord[::-1]

    def curlWebsiteWithCookies(self):
        return None

    def sanitizeString(self, frontWord):
        frontWord = frontWord.replace('|', '')
        frontWord = frontWord.replace('-', '')
        frontWord = frontWord.replace('<', '')
        frontWord = frontWord.replace('>', '')
        frontWord = frontWord.replace(' ', '')
        return frontWord

    def runRead(self):
        sOutput = readBackwards.sanitizeString(self, readBackwards.readStringBackwards(self, self.args1))
        print('output is %s' % sOutput)
        return sOutput



if __name__ == "__main__":
    # execute only if run as a script
    print("[+] Running wordSwitch")


#adding
object=readBackwards()# initialize with regular arguments racecar

print(object.runRead())
object = getWolf()
resp = object.getWebsiteRequest()
print(resp)

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
