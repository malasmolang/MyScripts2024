from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from rich import print as rprint
import getpass
import sys
from lxml import etree
import xmltodict
from pprint import pprint
device = Device(host='172.25.11.1', user='lab', passwd='lab123', port=22)

try:
    device.open()
except ConnectError as err:
    print("Connection to Device failed", err)
    sys.exit(1)
except Exception as err:
    print(err)
    sys.exit(1)

#### This portion will collect facts from the Junos device


# response = device.facts
# rprint(response.keys())
# print(response['serialnumber'])
# print(response['version'])
# print(response['junos_info']['re0']['object'])

# info = {'junos_info': {'re0': {'object': "junos.version_info(major=(21, 4), type=R, minor=3, build=15)",
#                         'text': '21.4R3.15'}}}
# print(info['junos_info']['re0']['text'])

# response = device.rpc.get_interface_information()
# response = device.rpc.get_source_nat_rule_sets_information
# print(etree.tostring(response))
# rprint(dict_result.keys())
# rprint(dict_result['interface-information']['physical-interface'][2]['name'])




# Execute the RPC and get the response
def get_source_nat_rule_sets_information():
    list_of_rules=['RULE1',
               'RULE2'
            ]
    for i in list_of_rules:
        response = device.rpc.get_source_nat_rule_sets_information(rule_name=i)
        dict_result = xmltodict.parse(etree.tostring(response, pretty_print=True).decode())
        result = dict_result['source-nat-rule-detail-information']['source-nat-rule-entry']['source-nat-rule-hits-entry']['concurrent-hits']
        print(f"The number of translations for {i} is {result}")

def get_source_nat_rule_sets_information_all():
    response = device.rpc.get_source_nat_rule_sets_information(all=True)
    dict_result = xmltodict.parse(etree.tostring(response, pretty_print=True).decode())
    # rprint(dict_result)
    # result = dict_result['source-nat-rule-detail-information']['source-nat-rule-entry']['source-nat-rule-hits-entry']['concurrent-hits']
    # print(f"The number of translations for is {result}")
    # print(result)
    result = dict_result['source-nat-rule-detail-information']['source-nat-rule-entry']
    # rprint(result)
    for i in result:
        if i['source-nat-rule-action-entry']['source-nat-rule-action'] == 'POOL1':
            print(i['rule-name'], i['source-nat-rule-hits-entry']['concurrent-hits'])


# Define main python function

def main():
    if __name__ == "__main__":
        get_source_nat_rule_sets_information_all()
    # print the duration of program execution completion
    
main()

# # Close the connection
# device.close()