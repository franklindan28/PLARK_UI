#!/usr/bin/python

from PyQt5 import QtCore, QtGui, QtNetwork
import sys
      
      
class Example:
  
    def __init__(self):    
        
        self.doRequest()
        
        
    def doRequest(self):   
    
        url = "https://api.github.com/users"
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)    
             
      
    def handleResponse(self, reply):

        er = reply.error()
        
        if er == QtNetwork.QNetworkReply.NoError:
    
            bytes_string = reply.readAll()
            print(str(bytes_string, 'utf-8'))
            
        else:
            print("Error occured: ", er)
            print(reply.errorString())
            
        QtCore.QCoreApplication.quit()    
        
        
if __name__ == '__main__':       
           
    app = QtCore.QCoreApplication([])
    ex = Example()
    sys.exit(app.exec_())