# This is a sample Python script.
from scrapy import Request
from scrapy.http.response import Response
from scrapy.spiders import Spider
from scrapy.http import FormRequest
import lxml.etree
import lxml.html



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class getWolf(Spider):
    name = "wolf-bot"

    def start_request(self):
        return [FormRequest(self.args1,
                                   formdata={'user':'hondaaussie@hotmail.com', 'pass':'rukidding'}, callback=log_parse)]

    def __init__(self, sNewWebsite="https://wolf.live/my+gams"):
        self.args1 = sNewWebsite
        if __name__ == '__main__':
            print("[+] Running getWolf")
            response = self.start_request()
            print(response)

    def log_parse(self, response):
        print("test1")
        print("[+] Logged visit to %s" % self.args1)


    def getWebsiteRequest(self, response):
        print("[+] argument type %s" % self.args1)
        response = lxml.html.fromstring(self.start_request())
        lxml.etree.strip_elements(response, lxml.etree.Comment, "script", "head")
        return lxml.html.tostring(response, method="text", encoding=unicode)


class typingGame:
    def __init__(self, args1="<--| trashcan | -->"):
        self.args1 = args1


    def invoke(self):
        return print("!print")

    def sanitize(self):
        sOutput = self.args1
        sOutput = sOutput.replace('<', '')
        sOutput = sOutput.replace('-', '')
        sOutput = sOutput.replace('|', '')
        sOutput = sOutput.replace(' ', '')
        sOutput = sOutput.replace('>', '')
        return sOutput


class matheleticsBot:

    def __init__(self, args1="2x4 + 21"):
        self.args1 = args1

    def orderOfOperations(self):
        sOutput = self
        sOutput = sOutput.replace('x', '*')
        sOutput = sOutput.replace(' ', '')
        sOutput = sOutput.replace('"', '')
        dOutput = eval(sOutput)
        return dOutput

    def invoke(self):
        return print("!math")


class countDownBot:

    def check_sums(array, k): #TODO REDO THIS FUNCTION
        potential_solutions = set()
        for num in array:
            if num in potential_solutions:
                return True
            potential_solutions.add(k - num)
        return False


    def __init__(self, args1=[2, 9, 25, 10, 3], args2=309):
        self.args1 = args1
        self.args2 = args2


class readBackwards:
    def __init__(self, args1="racecar"):
        self.args1 = args1

    def readStringBackwards(self, backWord):
        '''backWord is now reversed'''
        return backWord[::-1]

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

# adding
'''games to run'''

#ReadBackwards
object = readBackwards()  # initialize with regular arguments racecar
print(object.runRead())

#getWolf connection helpa
sp=Spider
print(sp.name)
object=getWolf(Spider)
#typing game
object=typingGame()
print(object.sanitize())
#math game
print(matheleticsBot.orderOfOperations("2x2 + 23"))
#wcd
object = countDownBot()