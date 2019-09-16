# API

![API](https://4.bp.blogspot.com/-wVSij9rfStg/XG7iQvHUqpI/AAAAAAAAGwI/Eol6oonV49k6QgizI6nquU373QVBhxGigCLcBGAs/s1600/image1.png)

[api](https://medium.com/@perrysetgo/what-exactly-is-an-api-69f36968a41f)

---

In basic terms, APIs just allow applications to communicate with one another.

When people speak of “an API”, they sometimes generalize and actually mean “a publicly available web-based API that returns data, likely in JSON or XML”. The API is not the database or even the server, it is the code that governs the  _access point(s)_  for the server.

## But why would we need an API?

Imagine the following scenario: You (as in, your application, or your client, this could be a web browser) wants to access another app’s data or functionality. For example, perhaps you want to access all Twitter tweets that mention the  _#epicodus_  hashtag.

You could email Twitter and ask for a spreadsheet of all these tweets. But then you’d have to find a way to import that spreadsheet into your application; and, even if you stored them in a database, as we have been, the data would become outdated  _very_  quickly. It would be impossible to keep it up to date.

It would be better and simpler for Twitter to provide you a way to query their application to get that data, so that you can view or use it in your own application. It would stay up to date automatically that way.

An API brokers access to a different application to provide functionality or access to data, so data can be included in different applications.

## Who Creates Public, Web-Based APIs?

Large tech companies, especially social media companies frequently make their aggregate data available to the public, but APIs are also maintained by government organizations, conferences, publishing houses, software startups, fan groups, eSports leagues and even individuals, in order to share anything from social media content to trivia questions, rankings, maps, song lyrics, recipes, parts lists and more.

In short, any person or organization that collects data might have an interest in making that data available for use by a different app. Maybe you have an API you’d like to build and make available?

## APIs Make Life Easier for Developers 

Let’s say you want to develop an app for an iPhone. Apple’s iOS operating system provides a large number of APIs—as every other operating system does—to make this easier on you. If you want to embed a web browser to show one or more web pages, for example, you don’t have to program your own web browser from scratch just for your application. You use the WKWebView API to embed a WebKit (Safari) browser object in your application. If you want to capture photos or video from the iPhone’s camera, you don’t have to write your own camera interface. You use the camera API to embed the iPhone’s built-in camera in your app. If APIs didn’t exist to make this easy, app developers would have to create their own camera software and interpret the camera hardware’s inputs. But Apple’s operating system developers have done all this hard work so the developers can just use the camera API to embed a camera, and then get on with building their app. And, when Apple improves the camera API, all the apps that rely on it will take advantage of that improvement automatically. This applies to every platform. For example, do you want to create a dialog box on Windows? There’s an API for that. Want to support fingerprint authentication on Android? There’s an API for that, too, so you don’t have to test every different Android manufacturer’s fingerprint sensor. Developers don’t have to reinvent the wheel over and over.

----