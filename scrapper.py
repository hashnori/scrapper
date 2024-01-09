import requests
import json

def extract_and_write_s_values(links, output_file):
    with open(output_file, 'w') as f:
        for link in links:
            try:
                response = requests.get(link)
                
                # Check if the response is successful (status code 200)
                if response.status_code == 200:
                    try:
                        json_data = json.loads(response.text)
                        
                        # Check if the response has the expected structure
                        if 'data' in json_data and 'data' in json_data['data']:
                            # Navigate through both levels of 'data'
                            data_objects = json_data['data']['data']
                            
                            for data_object in data_objects:
                                # Assuming 's' is a key in each object
                                s_value = data_object.get('s')
                                
                                if s_value is not None:
                                    f.write(f'"{s_value}",\n')
                                else:
                                    print(f'Warning: No "s" key found in an object from {link}')
                        else:
                            print(f'Error: Unexpected response format from {link}')
                    except json.JSONDecodeError:
                        print(f'Error decoding JSON from {link}')
                else:
                    print(f'Error: Non-successful response from {link} - Status Code: {response.status_code}')
            except Exception as e:
                print(f'Error processing {link}: {e}')

# Example usage
links = ['https://stockanalysis.com/api/screener/s/f?m=marketCap&s=desc&c=no,s,n,marketCap,price,change,revenue&cn=1000&f=exchange-is-NASDAQ&p=1&i=allstocks',
         'https://stockanalysis.com/api/screener/s/f?m=marketCap&s=desc&c=no,s,n,marketCap,price,change,revenue&cn=1000&f=exchange-is-NASDAQ&p=2&i=allstocks',
         'https://stockanalysis.com/api/screener/s/f?m=marketCap&s=desc&c=no,s,n,marketCap,price,change,revenue&cn=1000&f=exchange-is-NASDAQ&p=3&i=allstocks',
         'https://stockanalysis.com/api/screener/s/f?m=marketCap&s=desc&c=no,s,n,marketCap,price,change,revenue&cn=1000&f=exchange-is-NASDAQ&p=4&i=allstocks',

         ]
output_file = 'output_nasdaq-stocks.txt'

extract_and_write_s_values(links, output_file)
