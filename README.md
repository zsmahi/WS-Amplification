WS-Amplification
================

Tool to explore the WS-Amplification DoS threat. Part of the OWASP WS-Amplification DoS Project.
Tool consists of 3 parts:

- Webservice crawler
    - Finds webservices and their corresponding WSDLs
- Webservice client generator
    - Generates a client from a WSDl and sends a empty request with a WS-Addressing header, with a ReplyTo that points to the next part;
- Public reply logger
    - Google App that listens to incoming requests and logs them.
