# endpoints
### users
* register user : 
            endpoint => api/v1/register-user/
            input data => full_name, email, password, password2
            data type => json 

* login and get tokens : 
            endpoint => api/v1/token/
            input data => email, password
            output data => refresh token, access token
            data type => json

* get new token via entering refresh token : 
            endpoint => api/v1/token/refresh/
            input data => refresh token
            output data => access token
            data type => json


### posts and categories
