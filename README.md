# Introduction

CogHome is an ongoing project devoted to the development of an open-source smart home platform with cognitive capabilities including perception, knowledge, common sense, and reasoning. OpenCog (https://github.com/singnet/atomspace and https://github.com/singnet/ure) provides the cognitive core on top of which the smart home platform is implemented. It interacts with IoT devices via Home Assistant (hass, https://www.home-assistant.io/) local server. `coghome` module includes an OpenCog/hass adapter. Extending the platform by using SingularityNET AI services is planned.

## Setting up
First, you need to configure your local Home Assistant server and get URI and access token (Long-Lived Access Tokens). You will need to replace URI and token in `examples/config.cfg` with your values. Then, you either need to install OpenCog (https://github.com/singnet/atomspace#building-and-installing) or run the examples in the docker container.

## coghome module
`hass_communicator.py` implements `HassCommunicator` class for communication with Home Assistant server. It exchanges information with the rest of the code via `quest_send` and `queue_recv` (because we run it in a separate thread). When it receives a message from Home Assistant, it puts it in `queue_recv` (and `reactive_loop` in `launcher.py` waits for this massage). Simillary, when someone needs to send a message to Home Assistant, this message should be put to `queue_send` and `hass_communicator` gets it from this queue and sends it. It should be noted that in the current prototype we send messages in `entity.py` in the functions `send_simple_command` and `send_command`, and this function is called from `GroundingObjectNode` by OpenCog.

`entity.py` implements `Entity` class, which represents some entity in our smart house (buttons, motion sensors, lamps, etc.). This class keeps the state of the devices and also can send commands to this device. In OpenCog, each device is represented via `GroundedObjectNode`, which wraps an instance of the `Entity` class.

`home_state.py` implements `HomeState` class, which collects entities from Home Assistant and tracks their changes.

`event.py` implements `Event` class, which represents an event accessible by OpenCog via `GroundedObjectNode`.

