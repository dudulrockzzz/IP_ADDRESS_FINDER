
import socket as a 

my_host_name = a.gethostname()
# Display my hostname
print("Your Hostname is: " + my_host_name)

# Get my IP
my_ip_addr = a.gethostbyname(my_host_name)
# Display my IP 
print("Your Ip Address is: " + my_ip_addr)

host = "github.com"
# Fetch the IP
ip = a.gethostbyname(host)

# Display the IP
print("The IP Address of " + host + " is: "  + ip)