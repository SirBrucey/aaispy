# Andrews & Arnold API wrapper for Python 3.5+

This package will allow you to access the (work-in-progress) [Chaos API](https://web.archive.org/web/20150908020506/http://aa.net.uk/support-chaos.html). Use cases could include scripts to monitor your data, VoIP or SIP2SIM usage.

# Requirements

Python 3.5 or later
Python-Requests (will be installed automatically using `pip`)

# Installation

    pip install aaispy

# Usage

    import aaispy

    aa = aaispy.Chaos("username", "password") # use your normal credentials for control.aa.net.uk

Methods correspond to "commands" as defined in the API documentation, and any arguments are passed as JSON to the API. The method name is passed as the "command" parameter of the JSON object, and it will override any "command" argument set manually.

    aa.info() # lists all the services associated to your account
    aa.usage(sim={"ID": "1234"}) # displays call/SMS records for a particular SIM based in its ICCID
    aa.usage(voip={"ID": "+44..."}) # same but for a VoIP line based on its phone number

# License

MIT.