# Deploy Pytorch Model with Flask as Web App 

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![](https://img.shields.io/badge/python-3.5%2B-green.svg)]()
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

A pretty and customizable web app to deploy your DL model with ease

<a href="https://www.buymeacoffee.com/fing" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png" alt="Buy Me A Coffee"></a>

## Getting Started in 10 Minutes

- Clone this repo 
- Install requirements
- Run the script
- Go to http://localhost:5000  or ip address
- Done! :tada:


------------------

## Run with flask 

we used azure server ,but don't worry you can run it locally

```shell
# 1. First, clone the repo
$ git clone https://github.com/azzaelnaggar/defect_inspection.git
$ cd pytorch-flask-deploy

# 2. run python app
$ python app.py .

```
Open http://localhost:5000 and wait till the webpage is loaded.

## Local Installation

It's easy to install and run it on your computer.

```shell
# 1. First, clone the repo
$ git clone https://github.com/azzaelnaggar/defect_inspection
$ cd keras-flask-deploy-webapp

# 2. Install Python packages
$ pip install -r requirements.txt

# 3. Run!
$ python app.py
```
Open http://localhost:5000 and have fun. :smiley:

------------------

## Customization

It's also easy to customize and include your models in this app.

<details>
 <summary>Details</summary>

### Use your own model

Place your trained `.pt` file saved by `model.save()` under models directory.

Check the [commented code](https://github.com/azzaelnaggar/defect_inspection) in app.py.

### Use other pre-trained model

Check [this section](https://github.com/azzaelnaggar/defect_inspection) in app.py.

### UI Modification

Modify files in `templates` and `static` directory.

`index.html` for the UI and `main.js` for all the behaviors.

</details>


## Deployment

To deploy it for public use, you need to have a public **linux server**.

<details>
 <summary>Details</summary>
  
### Run the app

Run the script and hide it in background with `tmux` or `screen`.
```
$ python app.py
```

You can also use gunicorn instead of gevent
```
$ gunicorn -b 127.0.0.1:5000 app:app
```

More deployment options, check [here](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/)

