max_network_bandwidth = 1000
num_current_users = 200
app_a = 0.2
app_b = 0.1
new_app = 0.35
mbps_to_bps = 10**6

current_usage_mbps = (app_a + app_b)* num_current_users
current_available_mbps = max_network_bandwidth - current_usage_mbps
bandwidth_available = current_available_mbps - new_app * num_current_users

network_capacity_bps = max_network_bandwidth * mbps_to_bps
current_available_bps = current_available_mbps * mbps_to_bps
current_usage_bps = current_usage_mbps * mbps_to_bps
new_app_bps = new_app * mbps_to_bps

print('The network capacity is: ' + str(round(network_capacity_bps)) , 'bps')
print('The current usage is: ' + str(round(current_usage_bps)) , 'bps')
print('The current availability is: ' + str(round(current_available_bps)) , 'bps')
print('The new application required is: ' + str(round(new_app_bps))  , 'bps')
print('The bandwidth available if the new application is installed: ' + str(round(bandwidth_available)), 'mbps')
