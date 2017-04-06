"""
Feature 2

Identify the top 10 resources on the site that consume the most bandwidth (bytes)
write to a file named resources.txt

e.g. /images/USA-logosmall.gif
	 /shuttle/resources/orbiters/discovery.html

psuedo-code

read the data
create a dictionary for each resource
make key for the amount of bandwidth each resource consumes
sort through the counter to pick the top 10 bandwidth-intensive resources

"""

input_file = open("log.txt", "r")
resource_file = open("resources.txt", "w")

# Dictionary for resource and bytes
most_bytes = {}
websites = {}
# Repeat for each line in the text file
for line in input_file:
	# Split the line into an array
	resources = line.split()
	# last array of each line represents the bytes/bandwidth
	if resources[-1] == '-':
		byte = 0
	else:
		byte = resources[-1]
	host = resources[0]
	resource = resources[-4]
	if host not in websites:
		websites[host] = resource
		if resource not in most_bytes:
			most_bytes[resource] = int(byte)
		if resource in most_bytes:
			most_bytes[resource] += int(byte)

for count in sorted(most_bytes, key=most_bytes.get, reverse=True)[:10]:
	resource_file.write("%s" % count)
	resource_file.write('\n')

resource_file.close()
input_file.close()