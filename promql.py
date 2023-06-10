from prometheus_api_client import PrometheusConnect
import time
# create a PrometheusConnect instance
prom = PrometheusConnect(url="http://192.168.56.11:32216")



def make_true(filename, tf):
  with open(filename, 'w') as f:
    f.write(tf)

# define the query
query = '100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[2m])) * 100)'

while True:
    # retrieve the query result
    result = prom.custom_query(query)

    # print the result
    #print(result)

    # group 1
    avg1 = 0
    for item in result:
        if item['metric']['instance'] == '192.168.56.31:9100':
            avg1 += float(item['value'][1])
        elif item['metric']['instance'] == '192.168.56.32:9100':
            avg1 += float(item['value'][1])
        elif item['metric']['instance'] == '192.168.56.33:9100':
            avg1 += float(item['value'][1])
        elif item['metric']['instance'] == '192.168.56.34:9100':
            avg1 += float(item['value'][1])
    avg1 = avg1/4
    
    if avg1 > 80:
        make_true("g1_overcommitted.txt", "true")
        print('g1 overcommitted')
    else:
        make_true("g1_overcommitted.txt", "false")

    avg2 = 0
    for item in result:
        if item['metric']['instance'] == '192.168.56.41:9100':
            avg2 += float(item['value'][1])
        elif item['metric']['instance'] == '192.168.56.42:9100':
            avg2 += float(item['value'][1])
        elif item['metric']['instance'] == '192.168.56.43:9100':
            avg2 += float(item['value'][1])
        elif item['metric']['instance'] == '192.168.56.44:9100':
            avg2 += float(item['value'][1])
    avg2 = avg2/4

    if avg2 > 80:
        make_true("g2_overcommitted.txt", "true")
        print('g2 overcommitted')
    else:
        make_true("g2_overcommitted.txt", "false")
    #print(avg2/4)

    avg3 = 0
    for item in result:
        if item['metric']['instance'] == '192.168.56.21:9100':
            avg3 += float(item['value'][1])
        elif item['metric']['instance'] == '192.168.56.22:9100':
            avg3 += float(item['value'][1])
        elif item['metric']['instance'] == '192.168.56.23:9100':
            avg3 += float(item['value'][1])
        elif item['metric']['instance'] == '192.168.56.24:9100':
            avg3 += float(item['value'][1])
    avg3 = avg3/4

    if avg3 > 80:
        make_true("g3_overcommitted.txt", "true")
        print('g3 overcommitted')
    else:
        make_true("g3_overcommitted.txt", "false")
    #print(avg3/4)

    timestamp = str(int(time.time()))

    # Format the output string
    output_str = f"{timestamp}, {avg1}, {avg2}, {avg3}"

    # Print the output to the console
    print(output_str)
    # Append the output to a file
    with open("usage.csv", "a") as f:
        f.write(output_str + "\n")

    time.sleep(1)

    
