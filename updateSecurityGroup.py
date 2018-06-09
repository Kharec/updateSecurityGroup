#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit
from requests import get
import boto3, botocore
import argparse

__version__ = '0.1'
__author__ = 'Sandro CAZZANIGA'
__license__ = "GPLv3+"
__maintainer__ = "Sandro CAZZANIGA"
__email__ = "sandro@cazzaniga.fr"
__status__ = "Production"


def getIp():
	'''Simple function to get your ip, using ipinfo.io
	API and JSON. We're modifying it to match AWS SG
	requirements'''

	return(get(('https://ipinfo.io')).json()['ip']+"/32")

parser = argparse.ArgumentParser(description="Update your AWS security group with your new IP address")
parser.add_argument('-v', '--version', action='store_true', help='Print version and exit')
parser.add_argument('-i', '--id', help='Security group\'s id you want to update')

args = vars(parser.parse_args())

if not args['id']:
	parser.print_help()
	exit(1)

ec2 = boto3.client('ec2')
sgGroupId = args['id']

# check if the given id is correct
try:
	sg = ec2.describe_security_groups(
		GroupIds=[sgGroupId],
	)

except botocore.exceptions.ClientError:
	print("Security group id", sgGroupId, "seems wrong...")
	exit(1)

# get old and current IP
oldIp = sg['SecurityGroups'][0]['IpPermissions'][1]['IpRanges'][0]['CidrIp']
currentIp = getIp()

if oldIp != currentIp:

	# Revoke old rule
	deleteOldRule = ec2.revoke_security_group_ingress(
    	GroupId=sgGroupId,
    	IpPermissions=[
        	{
            	'IpProtocol': '-1',
            	'IpRanges': [
                	{
                    	'CidrIp': oldIp,
                	},
            	],
        	},
    	],
	)

	# Create our new rule with our new IP
	try:
		createNewRule = ec2.authorize_security_group_ingress(
			GroupId=sgGroupId,
    		IpPermissions=[
        		{
        			'IpProtocol': '-1',
            		'IpRanges': [
                		{
                    		'CidrIp': currentIp,
                		},
            		],
        		},
    		],
		)

	except botocore.exceptions.ClientError:
		print("Malformed IP:", currentIp)
		exit(1)
		
	print("Security group updated with new IP:", currentIp)

exit(0)