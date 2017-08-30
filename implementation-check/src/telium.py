"""
	Telium project model
	
"""

import dexml

from dexml import fields


class userInc(dexml.Model):
	value = fields.String()


class config(dexml.Model):
	name = fields.String()
	binaryName=fields.String()
	hardware=fields.String()
	userIncs= fields.List(userInc, tagname="userIncs")

class projectDescription(dexml.Model):
	activeConfig=fields.String()
	enableUsingCpp=fields.Boolean()
	projectType=fields.String()
	configs = fields.List(config, tagname="configs")
	

