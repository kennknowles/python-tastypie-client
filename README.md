Django Tastypie Client
======================

This is a client library for fluidly working with a Django Tastypie REST API.

Key Features:
 - From the root URL of the API, downloads the schema and discovers all resources.
 - From any resource, discovers and can seamlessly follow fields that are references to other objects.

In other words, it is a "web crawler" but instead of HTML and hrefs, it handles the much-simpler case 
of JSON with pointers implemented as URLs.

Contributors
------------
 - [Kenneth Knowles](https://github.com/kennknowles) (@KennKnowles)

Copyright and License
---------------------
(apache 2)
