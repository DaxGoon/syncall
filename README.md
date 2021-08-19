
# Syncall

# A restful API that calls synthesia API for signing messages.

_What is this?_

This is a Flask based RESTful API application designed according to the specification document.

_Endpoints_

```
1. /crypto/sign
:accepts - GET
:query string param - message: str
:headers - 'Authorization': API_KEY
:returns - API response from Sythensia API or a message as following in case the call was unsuccessful:
{
  "message": "First API call did not succeed, persistent calling in the background in progress.",
  "next": "Call /delayed_response later to get the valid response (when available) of this call."
}

2. /delayed_response
:accepts - GET
:query string param - message: str
:returns - API response signed message on available result or info string oninforming unavailability of result.
:socketio - broadcasts in realtime when signed msg is available. The client-side application can use any of the SocketIO
 client libraries or compatible client to establish a permanent connection to listen the msg


```

_How is it written?_
* API resources are defined in resources.py.
* API resources are registered in app.py.
* uses WSGIServer with greenlet (gevent is also installed and can be switched to), serves the api on port 5000
* uses SocketIO for broadcasting msg (notification)

_How to build and run?_

1Create a Config.py file in the application directory paste the following:
```
class Config:
    """
    Configuration parameters for the application.
    """

    synthesia_api_endpoint = "https://hiring.api.synthesia.io/crypto/sign"
    synthesia_api_sign_query_param_key = "?message="
    synthesia_api_key = ""

```

2. Do not forget to add proper synthesia_api_key in string format eg. "798798797"


3. Deploying locally in a dockerized environment:
    - Start building the application by running:
         
         `sh start.sh`
          This will start doing the following things:
            
            0. Downloading required base image and dependencies.
            
            1. Building an image called syncall.
            
            2. Creating the container, binding port 5000 with the host.
            
            3. Running the API inside the container.
      
      Then the API can be reached on the following URL:
      
         `http://127.0.0.1:5000` or `http://localhost:5000`
   

4. Running locally without deployment:
   - Check if the requirements are met as before.
   - Check if the port is available as before.
   - From the application directory initialize python virtual environment with:
      
      `virtualenv venv`
   - Install application library requirements with:
      
      `pip install --no-cache-dir -r requirements.txt`
   - start the application with:
      
      `python app.py`  or `python3 app.py`
     
   - Then the API can be reached on the following URL:
      
         `http://127.0.0.1:5000` or `http://localhost:5000`
   
5. Tests:
    - Tests are written using unittest module from python standard library. To run tests do the following:
      - Start the server
      - Start a new terminal session and go to the application directory
      - run ```python test_app.py```


## Links
1. Virtualenv installation
https://virtualenv.pypa.io/en/latest/installation.html
   
2. Docker installation
https://docs.docker.com/engine/install/

