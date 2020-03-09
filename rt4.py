#!/usr/bin/env python


class RTTicket(object):

    def __init__(self, ticketstr):
        self.ticket_status = ['new', 'open', 'stalled', 'resolved', 'rejected', 'deleted']
        ticket_dict = dict([map(lambda x: x.strip(), i.split(':'))
                            for i in
                            filter(lambda x: len(x.split(':'))==2, ticketstr.split('\n'))])
        self.__dict__.update(ticket_dict)
        if self.Status not in self.ticket_status:
            raise Exception('RTTicket creation error:','Status is not a valid state')

    def __repr__(self):
        return reduce(
            lambda h,i: "{}\n{}".format(h,i),
            map(lambda i:
                reduce(lambda x,y: "{}: {}".format(x,y),
                    i),
                rt.__dict__.items()))

a = "RT/3.4.5 200 Ok\nid: ticket/101123\nQueue: <...>\nOwner: <...>\nCreator: <...>\nSubject: <...>\nStatus: open\nPriority: <...>\nInitialPriority: <...>\nFinalPriority: <...>\nRequestors: <...>\nCc: <...>\nAdminCc: <...>\nCreated: <...>\nStarts: <...>\nStarted: <...>\nDue: <...>\nResolved: <...>\nTold: <...>\nTimeEstimated: <...>\nTimeWorked: <...>\nTimeLeft: <...>"

rt = RTTicket(a)
print(rt)
rt.Status='opened'
print(rt)
