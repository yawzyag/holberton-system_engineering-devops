# Application server

![class](https://process.filestackapi.com/cache=expiry:max/resize=width:1050/rJf1U9MTraWZDCJWjQoE)

[guinicorn](https://gunicorn.org/)

---

In this guide, you will build a Python application using the Flask microframework on Ubuntu 18.04. The bulk of this article will be about how to set up the  Gunicorn application server and how to launch the application and configure Nginx to act as a front-end reverse proxy.


## A production stack dream team

The unix approach is to have small tools which do one thing, and do it well.

Imagine if you had to do everything yourself with every new web application you build:

-   Host static files
-   Handle https connections
-   Recover from crashes
-   Make sure your application can scale up (via framework or your own code)

That sounds like a lot of work. And a lot of work which is the same across most web applications you might come up with.

This is good news! Because those problems are so common, you can build tools which take care of them. You don’t even need to put that functionality into your web framework of choice.

Three common building blocks when deploying a Python web application to production are:

-   A web server (like nginx)
-   A WSGI application server (like Gunicorn)
-   Your actual application (written using a developer-friendly framework like Django)

The web server accepts requests, takes care of general domain logic and takes care of handling https connections. Only requests which are meant to arrive at the application are passed on toward the application server and the application itself. The application code does not care about anything except being able to process single requests.

The application server is what we’re talking about here. Let’s look into what it does.


## Gunicorn is a WSGI server

Gunicorn is built so many different web servers can interact with it. It also does not really care what you used to build your web application - as long as it can be interacted with using the WSGI interface.

Gunicorn takes care of everything which happens in-between the web server and your web application. This way, when coding up your a Django application you don’t need to find your own solutions for:

-   communicating with multiple web servers
-   reacting to lots of web requests at once and distributing the load
-   keepiung multiple processes of the web application running

## Web Server Gateway Interface

As described in  PEP3333, the Python Web Server Gateway Interface (WSGI) is a way to make sure that web servers and python web applications can talk to each other. To be more precise:

> The server side invokes a callable object that is provided by the application side

So somewhere inside your application (usually a wsgi.py file) an object is defined which can be invoked by Gunicorn. This object is used to pass request data to your application, and to receive response data.

Gunicorns takes care of running multiple instances of your web application, making sure they are healthy and restart them as needed, distributing incoming requests across those instances and communicate with the web server. In addition to that, Gunicorn is pretty darn fast about it. A lot of effort has gone into optimizing it.

## In Conclusion

If you’re planning on running your Python web application in production, you’ll want to make use of a WSGI server. This way, you deployment will be more stable, be able to handle more requests at once and be fast about it.

You can choose any WSGI server you want, and change your time anytime you want without having to change your project in a big way.

Gunicorn is a great choice! If you’re unsure about what WSGI server to use, it’s perfectly fine to go along and use it. In case something’s not working out, you can always switch to another WSGI server easily. That’s one more thing the WSGI standard makes possible :)

---
