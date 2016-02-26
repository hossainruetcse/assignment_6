import json
import urllib
url="https://graph.facebook.com/1002329293113152_1131871366825610/comments?access_token=CAACEdEose0cBANreZBKmZBMzfVHvv5IJo2dugrYKyEzgwtF7MbrPOd9xX1Tz95XcIpWGmPYdD6wbcZBSvMQxeXAiw1fJGCEsFXJOA8KQ7zNgKKZBkIuwW4BN9e0jqdkWqb91wYBbB8z1129XlU2rs2jn0Mc4x49ZBAGQAyLNRdZAxNs90WMd0ZAHmid1H7EdzuXJioNsDFKvgZDZD"
response = urllib.urlopen(url)
dat = json.loads(response.read())
for d in dat['data']:
	print d['message'],"\n"
