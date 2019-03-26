settings = {
    "manage_ip_addresses": ["127.0.0.1"],
    "database_file": "polls.db",
    "time_format": "%m/%d/%Y %I:%M:%S %p",
    "ran_locally": True, # True = only devices on same wifi network can access it, False = otherwise,
    "base_domain": False, # Set this to a string, e.g. "xyz.com" only if you are using a domain, otherwise let the app determine it automatically by leaving it False
    "secret_key": "e8bc7a0b-c329-44a0-8fa3-d8bbfccf4670", # Used by flask for sessions, change this
}