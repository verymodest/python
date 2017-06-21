#!/usr/bin/python
def listComps():
	f=open('tmp/test.log')
	allLineLens = [len(x.strip()) for x in f]
	f.close()
	return max(allLineLens) 

def generatorExpression():
	return max(len(x.strip()) for x in open('tmp/test.log')) 

print listComps()
print generatorExpression()
