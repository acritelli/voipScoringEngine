Quick and dirty scoring check for ISTS blue team voice servers. This check connects to the white team Asterisk server with credentials (provided in the code) and initiates a call to the blue team's server on extension 99 (i.e. 0199 for team 1). If the call succeeds, it is assumed that the peering relationship between the blue and white team is functional, and their server is accepting calls.

# Requirements

* Requires the most-voip library installed. This may also require installing a dummy sound interface on the scoring engine.
* Requires dummy extension 99 on each blue team server. This extension must simply answer the call, wait a few seconds, and hang up. The scoring check is only looking for call success.
* Requires an end endpoint configured on the white team server so that the scoring engine can authenticate and place calls.

# Setup
Change the following in the config before running:

* username - change to the username for the scoring engine extension on the white team server.
* sip_server_address - change to the IP of the white team VoIP server
* sip_server_user - change to the username for the scoring engine extension on the white team server.
* sip_server_pwd - change to the password of the scoring engine extension on the white team server

# Running

python scoreVoip.py <TEAMNUM>

Example: python scoreVoip.py 01

Note: single digit team names must be prefaced by a 0 (i.e. 01, 02, etc.) because I'm lazy.
