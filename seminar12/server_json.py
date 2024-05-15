from jsonrpcserver import Success, method, serve, InvalidParams, Result, Error
import re

@method
def validEmail(email) -> Result:    
    if email == "":
        return Error(code=123, message="Empty email provided")
    if re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", email):    
        return Success(True)
    else:
        return Success(False)

@method
def validZipCode(zip) -> Result: 
    if zip == "":
        return InvalidParams("Null value")
    if re.match("^[0-9]{5}(?:-[0-9]{4})?$", zip):
        result = { "zip": zip, "result" : "Valid Zipcode" }
    else:
        result = { "zip": zip, "result" : "Invalid Zipcode" }
    return Success(result)

if __name__ == "__main__":
    serve('localhost', 5001)