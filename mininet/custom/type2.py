from mininet.topo import Topo  
class MyTopo( Topo ):  
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Switch1 = self.addSwitch('s1')
        Switch2 = self.addSwitch('s2')
	Switch3 = self.addSwitch('s3')
        Switch4 = self.addSwitch('s4')
	Switch5 = self.addSwitch('s5')
        Switch6 = self.addSwitch('s6')
        # Add links
        self.addLink( Host1, Switch1 )
        self.addLink( Host2, Switch6 )
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch1, Switch4 )
        self.addLink( Switch2, Switch3)
	self.addLink( Switch4, Switch5)
        self.addLink( Switch3, Switch5 )
        self.addLink( Switch3, Switch6)
topos = { 'mytopo': ( lambda: MyTopo() ) }  