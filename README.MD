# endpoints

> note : for POST, PUT, DELETE methods, authentication needed  

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
* get all posts :
        method => GET
        endpoint => http://127.0.0.1:8000/api/v1/posts/

        data type => json

        how to search => http://127.0.0.1:8000/api/v1/posts/?search=ورودی

        how to filter => http://127.0.0.1:8000/api/v1/posts/?category=آیدی کتگوری

        how to paginate using page number => http://127.0.0.1:8000/api/v1/posts/?page=2

        how to paginate to the last page => http://127.0.0.1:8000/api/v1/posts/?page=last

        how to paginate to the first page => http://127.0.0.1:8000/api/v1/posts/?page=first

* retrieve a post :
        method => GET
        endpoint => http://127.0.0.1:8000/api/v1/posts/id/
        data type => json
        input data => <int:id>

* get all categories and sub categories :
        method => GET
        endpoint => http://127.0.0.1:8000/api/v1/categories/
        data type => json


#### videos

