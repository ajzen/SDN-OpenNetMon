#!/usr/bin/env python
"""Custom topology example
This example create a topology with 6 switches and 2 hosts.

     h1 --- s1 --- s2 --- s3 --- s6 --- h2
             \            /
              \          /
               s4 --- s5

"""

from mininet.topo import Topo  
from mininet.net import Mininet  
from mininet.cli import CLI  
from mininet.log import setLogLevel, info  
class Type1( Topo ):  
    switchList = []
    def __init__( self):
        #Initialize topology
        Topo.__init__( self )
        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        for i in range(1,7):
            self.switchList.append( self.addSwitch( 's' + str(i) ))
        # Add Links
        self.addLink( h1, self.switchList[0] )
        self.addLink( self.switchList[0], self.switchList[1] )
        self.addLink( self.switchList[0], self.switchList[3] )
        self.addLink( self.switchList[3], self.switchList[4] )
        self.addLink( self.switchList[4], self.switchList[2] )
        self.addLink( self.switchList[1], self.switchList[2] )
        self.addLink( self.switchList[2], self.switchList[5] )
        self.addLink( h2, self.switchList[5] )

def createTopo():  
    topo = Type1()
    net = Mininet( topo = topo )
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':  
    setLogLevel('info')
    createTopo()
