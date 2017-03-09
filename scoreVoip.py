from most.voip.api import VoipLib
import sys

my_voip = VoipLib()

voip_params = {
        'username': 'scoringEngine',
        'sip_server_address': '10.0.2.99',
        'sip_server_user': '2699',
        'sip_server_pwd': 'Sc0reTh@tV0IP',
        'sip_server_transport': 'udp',
        'log_level': 0,
        'debug': True
}

status = {'status': "failure"}

def notify_events(voip_event_type, voip_event, params):
        if voip_event == "VOIP_EVENT__CALL_ACTIVE":
                status['status'] = "success"
#       print "Received Event Type:%s -> Event: %s Params: %s" % (voip_event_type, voip_event, params)

my_voip.init_lib(voip_params, notify_events)

my_voip.register_account()

my_extension = sys.argv[1] + "99"
my_voip.make_call(my_extension)

import time

time.sleep(5)

print(status['status'])
if status['status'] == "success":
        sys.exit(0)
else:
        sys.exit(1)
