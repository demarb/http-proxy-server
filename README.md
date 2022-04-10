# http-proxy-server

This is a simple http proxy server capable of handling http traffic.

## Implemented Features Features
1. Handling HTTP Traffic
2. Handling multiple transactions simultaneously (i.e. several requests and
responses) to improve its performance. (Multithreaded)
3. Logging of requests in logs folder inside server
4. Runtime check for how long server is running.
5. Automatically locating logs on the click of a button

## Features that could be implemnted in the future
1. Blacklisting Domains for greater security. Ex. blocking a specific ip address or a
website
2. Content monitoring: Blocking certain websites based on patterns in url or html found on page.
3.  Proxy  only Forwarding requests that are authorized to access a
service
4. Handling https traffic

## Running Proxy Server
1. Configure your port to 4444 or change configuration setup to port of your choice.
2. Run main.py
3. 3. Start, stop and navigate to logs as desired using GUI.
