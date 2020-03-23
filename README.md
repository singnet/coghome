# Introduction

CogHome is an ongoing project devoted to the development of an open-source smart home platform with cognitive capabilities including perception, knowledge, common sense, and reasoning. OpenCog (https://github.com/singnet/atomspace and https://github.com/singnet/ure) provides the cognitive core on top of which the smart home platform is implemented. It interacts with IoT devices via Home Assistant (hass, https://www.home-assistant.io/) local server. `coghome` module includes an OpenCog/hass adapter. Extending the platform by using SingularityNET AI services is planned.

## Setting up
First, you need to configure your local Home Assistant server and get URI and access token (Long-Lived Access Tokens). You will need to replace URI and token in `examples/config.cfg` with your values. Then, you either need to install OpenCog (https://github.com/singnet/atomspace#building-and-installing) or run the examples in the docker container.
