# Getting started

This template provides a minimal working example of a deployment-ready Streamlit app. This app is designed to be deployed via Google's App Engine.

### Project structure

So what's in this project? You'll see the following four directories:

* `data` - This is where any data artifacts your app needs can live. Note that if you're using large datasets, you should look at storing them with a cloud storage provider of your choice.
* `docs` - You are here! Store any relevant documentation your users might find helpful in here.
* `src` - It's a good idea to try and separate out your 'frontend' code from your 'backend' code -- it can really help with debugging your app and can make the app easier to extend too. Try and keep useful 'backend' code (e.g. standard data transformations) in here.
* `tests` - Put the tests for your app in here. Test are good, try and get some written!

How about the files in the top-level directory? Well, funny you should ask:

* `app.py` - This is your Streamlit App code and acts as an _entrypoint_ for your app. You can build other bits and pieces elsewhere if you're working on a complex app, but just make sure this is where your app is 'knitted together'.
* `requirements.txt` - This file contains your app's requirements -- the packages you need to get it all running. Makes sure to keep this up-to-date.
* `Dockerfile` - This file defines the image used to build the container your app is going to deploy into. By default, it runs with Python 3.7.8, and will install the packages you provide in `requirements.txt` too. When your container is running locally, it'll expose your app at `http://localhost:8080`.
* `Makefile` - This is a little utility file that provides a few handy commands to get you up and running quickly. More on this later.
* `README.md` - This file describes your app. Make sure to update this if you're using this template for your own projects.
 
 There's also one conspicuous file in here that is tied to deploying your app to Google Cloud, that's this one:
 
* `app.yaml` - This file tells Google's App Engine what it needs to do to deploy app.

You'll also see a couple more files in here. For completeness:

* `.gitignore` - This file simply tells `git` to, well, ignore certain files. This one is configured for Python. 
* `LICENSE` - Well, it is what it says it is -- the template's license. **Make sure to update this if you'd like to not use the MIT license.**

### Create your app

Create your app! Head over to `app.py`, you can have anything in here. You'll see one of Streamlit's [demo apps](https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/app.py) in here (with some small changes).

Don't feel limited to the style and structure in here (though you might find it helpful to work with `black` and `flake8`!), so go wild.

### Local testing

You can build and test your app locally with:

```bash
make run-container
```

You'll see your app launch on `http://localhost:8080` (by default). Navigate to it and have a play!

### Deploying to Google Cloud

Ready to deploy your app for other's to use? Great, you'll need to [get your GCP set up](https://cloud.google.com/appengine/docs/flexible/custom-runtimes/quickstart) first.

When you're set up, run:

```bash
make gcloud-deploy
```

This build your app, and deploy it through App Engine. You'll need to select your app's name and the region you'd like to deploy the app into.

You'll see a URL in your console (or navigate to the GCP Console's App Engine dashboard and grab the URL from there).

You're done! 
