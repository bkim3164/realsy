from bs4 import BeautifulSoup
import requests
from collections import namedtuple

#setup
def main(city: str, state: str) -> dict:

    city = city.replace(',','')
    city = city.replace(' ', '_')
    source = requests.get(f'https://www.realtor.com/realestateagents/{city}_{state}')

    
    if source.status_code // 100 != 2:
        print("Error Retrieving Page, Code: " + source.status_code)
        return

    soup = BeautifulSoup(source.content, 'html.parser')

    agents_only = soup.find_all("div", class_="jsx-1526930885")

    all_agent_data = dict()

    for agent in agents_only:
        agent_name = agent.find("div", class_="jsx-2987058905 agent-name text-bold")
        agent_agency = agent.find("div", class_="jsx-2987058905 agent-group text-semibold ellipsis")
        agent_phone = agent.find("div", class_="jsx-2987058905 agent-phone hidden-xs hidden-xxs")
        agent_sold = agent.find("span", class_="jsx-2987058905 sale-sold-count")
        agent_experience = agent.find("span", class_="jsx-2987058905 bold-text")

        if __name__ == '__main__':

            if agent_experience != None:
                if agent_experience.text[0] != '$':
                    print("Experience: " + agent_experience.text)
                else:
                    print("Experience: Not Reported")
            
            if agent_sold != None:
                print("Sold: " + agent_sold.text)

            if agent_phone != None:
                print(agent_phone.text)

            if agent_agency != None:
                print(agent_agency.text)

            if agent_name != None:
                print(agent_name.text)

            print('\n')


        if agent_name != None and agent_experience != None and agent_agency != None and agent_phone != None and agent_sold != None:
            all_agent_data[agent_name.text] = agent_name.text,agent_agency.text,agent_phone.text,int(agent_sold.text),agent_experience.text,f'{city},{state}'
    
    print("Scraped data from: 'realtor.com'")
    return all_agent_data



if __name__ == '__main__':
    pass
