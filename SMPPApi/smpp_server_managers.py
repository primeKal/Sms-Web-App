from random import randint

import smpplib
import logging
import sys

from threading import Thread

import smpplib.gsm
import smpplib.client
import smpplib.consts

import sqlconnector as sql
import service

client = smpplib.client.Client('0.0.0.0', 2775)



def send_to_jasmin_smpp_server(sender, reciver, message):
    logging.basicConfig(level='DEBUG')

    parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(message * 10)

    client = smpplib.client.Client('0.0.0.0', 2775)

    client.set_message_sent_handler(
        lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))

    client.set_message_received_handler(
        lambda pdu: sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id)))

    client.connect()
    client.bind_transceiver(system_id='kk', password='kk')

    for part in parts:
        pdu = client.send_message(
            source_addr_ton=smpplib.consts.SMPP_TON_INTL,
            # source_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
            # Make sure it is a byte string, not unicode:
            source_addr=sender,

            dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
            # dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
            # Make sure thease two params are byte strings, not unicode:
            destination_addr=reciver,
            short_message=part,

            data_coding=encoding_flag,
            esm_class=msg_type_flag,
            registered_delivery=True,
        )
        print(pdu.sequence)
        t = Thread(target=client.listen())
        t.start()


def bind_client():
    logging.basicConfig(level='DEBUG')
    client = smpplib.client.Client('10.99.101.246', 2775)

    def getPdu(pdu):
        print(pdu.short_message.decode('utf-8'))
        print(type(pdu))
        sql.save_des(randint(1, 1000000), "orginnn", pdu.short_message.decode('utf-8'),pdu.receipted_message_id)
        sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id))

    client.set_message_received_handler(
        lambda pdu: getPdu(pdu))
    client.set_message_sent_handler(
        lambda pdu: sys.stdout.write('sent {}\n'.format(pdu.receipted_message_id)))

    client.connect()
    client.bind_transceiver(system_id='trial', password='trial')
    client.listen()
    t = Thread(target=client.listen, args=())
    t.daemon = True
    t.start()
    t.join()
    return


def send_mssg(message, sender, reciver):
    parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(message * 10)

    for part in parts:
        pdu = client.send_message(
            source_addr_ton=smpplib.consts.SMPP_TON_INTL,
            # source_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
            # Make sure it is a byte string, not unicode:
            source_addr=sender,

            dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
            # dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
            # Make sure thease two params are byte strings, not unicode:
            destination_addr=reciver,
            short_message=part,

            data_coding=encoding_flag,
            esm_class=msg_type_flag,
            registered_delivery=True,
        )
