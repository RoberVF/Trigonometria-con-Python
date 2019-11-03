#!/usr/bin/env python
#_*_ coding: utf-8 _*_

from scapy.all import *
from colorama import Fore, init
import argparse
import sys

#Parametros para escribir en la consola a la hora de iniciar el programa
parse= argparse.ArgumentParser()
parse.add_argument("-r", "--range", help= "Rango a spoofear")
parse.add_argument("-g", "--gateway", help= "Gateway")
parse= parse.parse_args()

def get_mac(gateway): #Obtener direccion MAC del gateway
	arp_layer= ARP(pdst=gateway) #pdts-> Recibe la direccion a la que queremos enviarle el paquete ARP Request. Gateway es la direccion IP del router
	broadcast= Ether(dst="ff:ff:ff:ff:ff:ff")
	final_packet= broadcast/arp_layer
	mac= srp(final_packet, timeout=2, verbose= False)[0] #Verbose-> Mensaje en pantalla 
	mac= mac[0][1].hwsrc
	return mac

def scanner_red(rango, gateway):
	lista_hosts= dict() #Crea un diccionario
	arp_layer= ARP(pdst=rango) 
	broadcast= Ether(dst="ff:ff:ff:ff:ff:ff")
	final_packet= broadcast/arp_layer
	answers= srp(final_packet, timeout=2, verbose=False)[0]
	print("\n")
	for a in answers:
		print(a)

def restore_arp(destip, sourceip, hwsrc, hwdst): #Restaurar las tablas ARP para que los dispositivos no se queden sin internet
	pass

def arp_spoofing(hwdst, pdst, psrc): 
	pass

def main():
	if parse.range and parse.gateway: #Estas dos opciones tuvieron que se establecidas arriba
		mac_gateway= get_mac(parse.gateway) #Direccion MAC del router
		print(mac_gateway)
		scanner_red(parse.range, parse.gateway)

	else:
		print("Necesito opciones :(")

if __name__ == '__main__':
	main()