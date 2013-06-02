import sys
import suds
from suds.sax.element import Element
from suds.client import Client
import logging


def testWSDL(wsdlURL):
  replyURL = 'http://wsamplification.appspot.com/?webservice=' + wsdlURL
  try:
    client = Client(wsdlURL)    
    wsans = ('wsa', 'http://schemas.xmlsoap.org/ws/2004/08/addressing')
    wsaReply = Element('ReplyTo', ns=wsans)
    wsaAddress = Element('Address', ns=wsans).setText(replyURL)
    wsaReply.insert(wsaAddress)
  except:
    print 'Moving on...'
    return
  try:
    client.set_options(soapheaders=wsaReply) 
    #impl = getattr(client.service, 'submitOrderNoAck')
    #print impl()
    for method in client.wsdl.services[0].ports[0].methods.values():
      print method.name
      result = getattr(client.service, method.name)()
      #print result()
  except suds.WebFault as detail:
    print 'Invoking method failed'
    print client
  except:
    print 'Derping...'
    print client

from google import search   
if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  logging.getLogger('suds.client').setLevel(logging.DEBUG)
  logging.getLogger('suds.transport').setLevel(logging.DEBUG)
  logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
  logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
  if(len(sys.argv) > 1):
    print('testing given URL...')
    testWSDL(sys.argv[1])
  else:
    for url in search('axis2 filetype:wsdl -svn -github -git -repo -repository -trunk -branch', start=50, stop=100): 
      #('\"xmlns:wsdl=\" \"http://schemas.xmlsoap.org/wsdl/\" inurl:wsdl -wso2 -stackoverflow -github', stop=50):
      if(url.endswith('wsdl') or url.endswith('WSDL')):
        print('trying to parse WSDL:')
        print(url)
        testWSDL(url)
      else:
        print('Not a WSDL file. Next!')

'''
import GoogleScraper
import urllib.parse

if __name__ == '__main__':


  
	urls = GoogleScraper.scrape('\"xmlns:wsdl=\" \"http://schemas.xmlsoap.org/wsdl/\" inurl:wsdl -wso2 -stackoverflow -github', number_pages=2)
	for url in urls:
		# You can access all parts of the search results like that
		# url.scheme => URL scheme specifier (Ex: 'http')
		# url.netloc => Network location part (Ex: 'www.python.org')
		# url.path => URL scheme specifier (Ex: ''help/Python.html'')
		# url.params => Parameters for last path element
		# url.query => Query component
		resurl = urllib.parse.unquote(url.geturl())
		print 'Starting test on: ' + resurl
        if(resurl.endswith('wsdl') or resurl.endswith('WSDL')):
          print('trying to parse WSDL:')
          print(resurl)
          testWSDL(resurl)
        else:
          print('Not a WSDL file. Next!')

	print('#################################################################')	
	print('[!] Received %d results by asking %d pages with %d results per page' %
				(len(urls), 2, 100))
'''
