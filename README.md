WS-Amplification
================

Tool to explore the WS-Amplification DoS threat. Part of the OWASP WS-Amplification DoS Project.

This tool contains 3 parts:

- Webservice crawler
    - Finds webservices and their corresponding WSDLs
- Webservice client generator
    - Generates a client from the WSDl and sends an empty request with a WS-Addressing header, with a ReplyTo that points to the Google App
- Public reply logger (Google App)
    - Public reachable web application that listens to incoming requests and logs them.
