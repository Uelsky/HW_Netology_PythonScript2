import nmap3
import sys

target = sys.argv[1]

scan = nmap3.Nmap()
result = scan.nmap_version_detection(target)

for i in result[target]['ports']:
    answer = list()

    try:
        answer.append(f"{i['service']['name']}({i['service']['product']})")
    except:
        answer.append(i['service']['name'])

    try:
        answer.append(f"version: {i['service']['version']}")
    except:
        pass

    answer.append(f"port: {i['portid']}")

    print(' ==== '.join(answer))
