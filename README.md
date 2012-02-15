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
 - [Kenneth Knowles](https://github.com/kennknowles) ([@KennKnowles](https://twitter.com/KennKnowles))

Copyright & License
-------------------
Copyright 2007-2012 Kenneth Knowles

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
