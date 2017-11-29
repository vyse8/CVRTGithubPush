#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wap

server = 'http://api.wolframalpha.com/v2/query.jsp'
appid = '28W43H-6P86G7XK79'
input = 'What is Alzheimers?'

waeo = wap.WolframAlphaEngine(appid, server)

queryStr = waeo.CreateQuery(input)
wap.WolframAlphaQuery(queryStr, appid)
result = waeo.PerformQuery(queryStr)
result = wap.WolframAlphaQueryResult(result)
x = 0
print(result)
for pod in result.Pods():
	#if x < 2:
		waPod = wap.Pod(pod)
		for subpod in waPod.Subpods():
			waSubpod = wap.Subpod(subpod)
			plaintext = waSubpod.Plaintext()[0]
			img = waSubpod.Img()
			alt = wap.scanbranches(img[0], 'alt')[0]
			print (alt)
			x = x + 1