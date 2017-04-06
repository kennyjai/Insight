# Feature 1

"""List in descending order the top 10 most active hosts/IP
write to a file named hosts.txt
10 most active hosts/ip addresses and how many times they have accessed any part of the site

e.g. example.host.com,1000000

code

read the data in python
make a counter for each unique ip/hosts appears
make a dictionary with the ip and the hit
sort through the counter to pick the top 10 most active
output a file name host.txt that lists descencding order of top 10 name and occurrence

"""
input_file = open("log.txt", "r")
host_file = open("host.txt", "w")

# Dictionary for host/ips with a counter
hits = {}
# Repeat for each line in the text file
for line in input_file:
	# Split the line into an array called "hosts" using the separator "- -"
	hosts = line.split(" - -")
	# Extract the data so that the first array of each line is the ip/hosts
	host = hosts[0]
	# if the ip/host not in dictionary, append to list and start counter at 1
	if host not in hits:
		hits[host] = 1
	# if the ip/host is in dictionary, just add to the counter
	else:
		hits[host] += 1

# sort the dictionary by the counter values and print the top 10 {host, count} pairs
for count in sorted(hits, key=hits.get, reverse=True)[:10]:
	host_file.write("%s, %i" % (count, hits[count]))
	host_file.write('\n')

host_file.close()
input_file.close()

