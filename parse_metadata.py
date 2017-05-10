#!/usr/bin/python
import json, urllib

u = urllib.urlopen('http://169.254.169.254/latest/meta-data/iam/security-credentials/AllowS3_Download')
j = json.load(u)
print "export AWS_ACCESS_KEY=%s" % j['AccessKeyId']
print "export AWS_SECRET_KEY=%s" % j['SecretAccessKey']
print "export TOKEN=%s" % j['Token']

