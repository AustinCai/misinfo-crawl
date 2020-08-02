import cdx_toolkit

cdx = cdx_toolkit.CDXFetcher(source='cc')
url = 'commoncrawl.org/*'

print(url, 'size_estimate', cdx.get_size_estimate(url))

for obj in cdx.iter(url, limit=1, filter='=status:200'):
    print(obj.content)



