from bs4 import BeautifulSoup
import requests
from collections import namedtuple

#setup
def main():

    #TODO figure inputs later
    city = 'irvine' #default 
    state = 'CA' #default

    city = city.replace(',','')
    city = city.replace(' ', '_')
    source = requests.get(f'https://www.realtor.com/realestateagents/{city}_{state}')

    
    if source.status_code // 100 != 2:
        print("Error Retrieving Page, Code: " + source.status_code)
        return

    soup = BeautifulSoup(source.content, 'html.parser')

    agents_only = soup.find_all("div", class_="jsx-1526930885")

    agent_info = namedtuple("agent_info", ['name','agency','phone','sold','experience'])

    all_agent_data = []

    for agent in agents_only:
        agent_name = agent.find("div", class_="jsx-2987058905 agent-name text-bold")
        agent_agency = agent.find("div", class_="jsx-2987058905 agent-group text-semibold ellipsis")
        agent_phone = agent.find("div", class_="jsx-2987058905 agent-phone hidden-xs hidden-xxs")
        agent_sold = agent.find("span", class_="jsx-2987058905 sale-sold-count")
        agent_experience = agent.find("span", class_="jsx-2987058905 bold-text")

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



    #all_people = set()

    #for x in all_info:
    #    all_people.add(x.text)


    #for person in all_people:
       #print(person)




if __name__ == '__main__':
    main()