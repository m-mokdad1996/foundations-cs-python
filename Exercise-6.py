def is_valid_ipv4_address(ip):
    
    # Split the IP address into its components
    parts = ip.split('.')
    
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return "invalid IPv4 addresses"
    
    for part in parts:
        # Check if the part is a digit and does not start with '0' unless it is '0'
        if not part.isdigit() or (part[0] == '0' and len(part) > 1):
            return "invalid IPv4 address"
        
        # Convert part to an integer
        num = int(part)
         # Check if the number is in the valid range
        if num < 0 or num > 255:
            return "invalid IPv4 address"
    
    return "valid IPv4 address"
ipAddresses = input("please enter an IP address")
print(is_valid_ipv4_address(ipAddresses))