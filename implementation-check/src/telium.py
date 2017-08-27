"""
	Telium project model
	
"""

import dexml

from dexml import fields


class userInc(dexml.Model):
	path = fields.String()


class configuration(dexml.Model):
	name = fields.String()
	userIncludes = fields.List(userInc, tagname="userIncludes")

class teliumProject(dexml.Model):
	configurations = fields.List(configuration)
	

