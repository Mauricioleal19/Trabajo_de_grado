#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
    	           listenPort=6633,
                   build=False
                   )

    info( '* Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      protocol='tcp',
                      protocols='OpenFlow13',
                      ip='192.168.1.7')

    info( '* Add switches\n')

    s10 = net.addSwitch('s10', protocols='OpenFlow13') 
    s9 = net.addSwitch('s9', protocols='OpenFlow13')
    s4 = net.addSwitch('s4', protocols='OpenFlow13')
    s7 = net.addSwitch('s7', protocols='OpenFlow13')
    s1 = net.addSwitch('s1', protocols='OpenFlow13') 
    s8 = net.addSwitch('s8', protocols='OpenFlow13')
    s5 = net.addSwitch('s5', protocols='OpenFlow13')
    s3 = net.addSwitch('s3', protocols='OpenFlow13')
    s2 = net.addSwitch('s2', protocols='OpenFlow13')
    s11 = net.addSwitch('s11', protocols='OpenFlow13')
    s6 = net.addSwitch('s6', protocols='OpenFlow13')

    info( '* Add hosts\n')
    h3 = net.addHost('h3', cls=Host, ip='192.168.152.3',defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='192.168.32.2',defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='192.168.96.2',defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='192.168.136.2',defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='192.168.156.3',defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='192.168.64.3',defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='192.168.144.3',defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='192.168.128.3',defaultRoute=None)
    h18 = net.addHost('h18', cls=Host, ip='192.168.0.2',defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='192.168.152.2',defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='192.168.64.2',defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='192.168.128.2',defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='192.168.144.2',defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='192.168.32.3',defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='192.168.156.2',defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='192.168.0.3',defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='192.168.96.3',defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='192.168.136.3',defaultRoute=None)

    info( '* Add links\n')
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s2, h3)
    net.addLink(s2, h4)
    net.addLink(s3, h5)
    net.addLink(s3, h6)
    net.addLink(s4, h7)
    net.addLink(s4, h8)
    net.addLink(s5, h9)
    net.addLink(s5, h10)
    net.addLink(s6, h12)
    net.addLink(h11, s6)
    net.addLink(s7, h14)
    net.addLink(s7, h13)
    net.addLink(s8, h15)
    net.addLink(s8, h16)
    net.addLink(s9, h17)
    net.addLink(s9, h18)
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s4)
    net.addLink(s4, s5)
    net.addLink(s5, s6)
    net.addLink(s6, s7)
    net.addLink(s7, s8)
    net.addLink(s8, s9)
    net.addLink(s10, s4)
    net.addLink(s10, s3)
    net.addLink(s10, s2)
    net.addLink(s10, s1)
    net.addLink(s11, s7)
    net.addLink(s11, s8)
    net.addLink(s11, s9)
    net.addLink(s11, s6)
    net.addLink(s11, s10)
    net.addLink(s10, s5)

    info( '* Starting network\n')
    net.start()
    
    info( '* Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
