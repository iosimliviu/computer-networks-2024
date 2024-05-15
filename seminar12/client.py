import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.pow(2,3))  # returns 2**3 = 8
print(s.add(2,3))  # returns 5
print(s.mul(5,2))  # returns 5*2 = 10

# print list of available methods -> one of the introspection methods exposed
print(s.system.listMethods())