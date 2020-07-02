# WebApp

## Define REST API

We used https://app.swaggerhub.com to define the REST API as you can find in RESTful_API_Definition folder.



## Frontend:

### Used Technologie:

- Vue.js: JavaScript framework for building user interfaces and single-page applications.
		https://vuejs.org/
- Bootstrap 4: Build responsive, mobile-first projects on the web with the world’s most popular front-end component library.
		https://getbootstrap.com/
- vue-axios: http client library.
		https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html

### Working Environments: 
- Visual Studio Code
- nodejs/npm: https://www.npmjs.com/get-npm
- vue module: https://github.com/creativetimofficial/vue-white-dashboard

### prerequisites

To install the dependencies of the frontend, open a commandline-prompt in the ```Frontend/``` folder. In there run

```npm install```

This will install all dependencies listed in the package.json file.

### usage

To run the frontend, start a commandline-prompt in the ```Frontend/``` folder. To start your local http-server, run

```npm run serve``` ( OR ```npm run dev```)

and open the displayed URL in your browser.

> The frontend is dynamic. To get the data you should run the backend first.



## Backend 

We are using python-flask as backend framework.

### prerequisites

Prior to the use of this backend, several dependencies have to be installed. You can do this via ```pip install -r requirements.txt```.

### configuration

The model should be placed into ```ml/``` in ```<modelname>.h5``` format. The ```<modelnam>``` should then be set in the ```controller.py```.

### usage

To run this backend, run ```py server.py```. Depending on how you access python on your machine you have to replace ```py```.

