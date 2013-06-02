WS-Amplification
================

Tool to explore the WS-Amplification DoS threat. Part of the OWASP WS-Amplification DoS Project (https://www.owasp.org/index.php/OWASP_WS_Amplification_DoS_Project).

This tool contains 3 parts:

- Webservice crawler (WSA_spoof.py)
    - Finds webservices and their corresponding WSDLs
- Webservice client generator (WSA_spoof.py)
    - Generates a client from the WSDl and sends an empty request with a WS-Addressing header, with a ReplyTo that points to the Google App
- Public reply logger (GoogleApp_code.py - Google App)
    - Public reachable web application that listens to incoming requests and logs them.









