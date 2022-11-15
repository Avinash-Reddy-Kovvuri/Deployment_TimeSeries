import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import datetime
import streamlit as st
import streamlit.components.v1 as com
st.set_page_config(page_title="prediction water level",layout='wide')
# --------------------

with open('demo.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
# st.markdown("""
# <style>
# [data-baseweb="base-input"]{
# background:linear-gradient(to bottom, #3399ff 0%,#00ffff 100%);
# border: 2px;
# border-radius: 3px;
# }
# </style>
# """, unsafe_allow_html=True)
# ------------------------
# a1,a2 = st.columns([1,9])
# with a2:
#     st.title('CHENNAI DRINKING WATER LEVEL PREDICTION')
remo = '<h1 style="font-family: Times New Roman;color:rgb(255,120,71,1);padding-left:15px;margin-bottom:25px;">CHENNAI DRINKING WATER LEVEL PREDICTION</h1>'
st.markdown(remo,unsafe_allow_html=True)
#ML

def parser(x):
  return pd.to_datetime(x)
different_chennai_reservoir_water_levels = pd.read_csv("chennai_reservoir_levels.csv.csv",)
total_water_levels = pd.read_csv('final_Reservior.csv', index_col = 0, parse_dates=[0], date_parser = parser)

total_water_levels = pd.DataFrame(total_water_levels['Total'].resample('MS').sum())
different_chennai_reservoir_water_levels = pd.read_csv("chennai_reservoir_levels.csv.csv",)
poondi = pd.Series(different_chennai_reservoir_water_levels["POONDI"])
cholavaram = pd.Series(different_chennai_reservoir_water_levels["CHOLAVARAM"])
redhills = pd.Series(different_chennai_reservoir_water_levels["REDHILLS"])
chembarakkam = pd.Series(different_chennai_reservoir_water_levels["CHEMBARAMBAKKAM"])
labels=["POONDI", "CHOLAVARAM", "REDHILLS", "CHEMBARAMBAKKAM"]
dat = [poondi[:].mean(),cholavaram[:].mean(),redhills[:].mean(),chembarakkam[:].mean()]
fig,plt = plt.subplots()
plt.pie(dat,labels=labels,autopct='%1.1f%%',shadow=True,startangle=100,explode=(0.018, 0.018, 0.1, 0.018),colors=["red","green","pink","orange"])
from joblib import Parallel, delayed 

import joblib 

result= joblib.load('SARIMAX.pkl') 
 
from datetime import datetime
from dateutil import relativedelta
# -------------------------------------------
col1,col2= st.columns([5,4])



# ----------------------------------------------
d1 = str('01/09/2019')
# ---------------------------
with col2:
    st.subheader("Enter Date (YYYY/MM/DD)")
with col2:
    d2=str(st.date_input(' '))
# -----------------------------
d2 = d2[8:]+"/"+d2[5:7]+"/"+d2[0:4]
start_date = datetime.strptime(d1, "%d/%m/%Y")
end_date = datetime.strptime(d2, "%d/%m/%Y")
delta = relativedelta.relativedelta(end_date, start_date)
res_months = delta.months + (delta.years * 12)
start = len(total_water_levels)
end = (len(total_water_levels)) + res_months
forecast_1 = result.predict(start = start, 
                          end = end, 
                          typ = 'linear').rename('Forecast')
yyy = pd.concat([total_water_levels['Total'],forecast_1])

# ----------------------------------------------
def main():
    with col2:
        if st.button('Predict'):
            i=1
            while(forecast_1[-i]<0):
                i+=1
            st.write(str(forecast_1[-i]) + " Million Cubic Feet (MCF)")
            st.line_chart(yyy)

if __name__=='__main__':
    main()
# -----------------------------------------------
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-color:black;
             padding:12%;
             background-attachment: fixed;
             background-size: cover
         }}
         .stTitle{{
             background-color:yellow;
         }}
         
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


with col1:
    with st.expander('FLOODS'):
        st.write('''A flood is an overflow of water (or rarely other fluids) that submerges land that is usually dry.Floods: Do’s & Don’ts

What to do before a flood

To prepare for a flood, you should:

    Avoid building in flood prone areas unless you elevate and reinforce your home.
    Elevate the furnace, water heater, and electric panel if susceptible to flooding.
    Install "Check Valves" in sewer traps to prevent floodwater from backing up into the drains of your home.
    Contact community officials to find out if they are planning to construct barriers (levees, beams and floodwalls) to stop floodwater from entering the homes in your area.
    Seal the walls in your basement with waterproofing compounds to avoid seepage.

If a flood is likely to hit  your area, you should:

    Listen to the radio or television for information.
    Be aware that flash flooding can occur. If there is any possibility of a flash flood, move immediately to higher ground. Do not wait for instructions to move.
    Be aware of streams, drainage channels, canyons, and other areas known to flood suddenly. Flash floods can occur in these areas with or without such typical warnings as rain clouds or heavy rain.

If you must prepare to evacuate, you should:

    Secure your home. If you have time, bring in outdoor furniture. Move essential items to an upper floor.
    Turn off utilities at the main switches or valves if instructed to do so. Disconnect electrical appliances. Do not touch electrical equipment if you are wet or standing in water.

If you have to leave your home, remember these evacuation tips:

    Do not walk through moving water. Six inches of moving water can make you fall. If you have to walk in water, walk where the water is not moving. Use a stick to check the firmness of the ground in front of you.
    Do not drive into flooded areas. If floodwaters rise around your car, abandon the car and move to higher ground if you can do so safely. You and the vehicle can be quickly swept away.
        ''')
    with st.expander('DROUGTS'):
        st.write('''Save Water: The Do's and Don'ts of Water Conservation

	Water is one of the essential resources needed for the existence of life. But due to some factors, many countries in the world suffer from water scarcity. Saving water helps to reduce water scarcity and its related problems in the future. Continue reading this article to know more about how to save water and follow the effective ways to conserve water.

Water-Universal Liquid
	Save Water: The Do's and Don'ts of Water Conservation
	Water is one of the essential resources needed for the existence of life. But due to some factors, many countries in the world suffer from water scarcity. Saving water helps to reduce water scarcity and its related problems in the future. Continue reading this article to know more about how to save water and follow the effective ways to conserve water.

Water-Universal Liquid
	Water is the primary ingredient which plays a major role in assuring the quality of life on the Earth. Humans, trees, plants, birds, animals and all such living forms need water to lead their life. Like food and oxygen, water is also an important source needed much for the humans to perform the daily activities such as drinking, cooking, bathing, cleaning, vessels washing and gardening. On the other hand, water is also needed for agriculture and industrial activities.

Is water sufficient for use in the Earth?
	The entire planet is covered with 97% of salt water and only 3% of fresh water. But unfortunately, out of 3% of fresh water, glaciers and ice caps cover 2% and the remaining 1% is left in the form of drinking water. The balance of clean water on the earth is managed by rainfall and evaporation process. During summer season and at the time of lack of rainfall, the level of groundwater gets reduced, the land gets dried and the human population faces drought and water scarcity.

	Only a meager percentage of water is present in the earth for the entire population. Many countries in the world face water scarcity which is one of the major problems where people need to suffer a lot to get clean water to perform their daily activities. Apart from water scarcity, the planet also suffers from water pollution. Lack of water also affects the growth of population, industry, agriculture, etc.

	Water wastage is one of the mistakes being done by the humans who have adequate water. Huge usage of water above the daily needs in homes, factories, industries, construction work and agriculture lands leads to the shortage of water and creates a serious threat.

save water

Effects of the shortage of water
	Can you imagine your life without water? It is highly impossible to continue living on the earth without water. Already the world is facing problems such as water scarcity and water pollution at a high level. In the olden days, adequate water was present in rivers, wells, ponds, and dams. At present, we are in a situation to buy mineral water and packaged drinking water from shops. The present situation clearly reveals the shortage of water in the world and it may even get worse in the future. To avoid the below-mentioned effects of the shortage of water, it is the responsibility of the humans to conserve water for the future use.

	The shortage of water would convert agriculture lands into barren lands and will lead to drought.
	If there is no water, then it is difficult to cook and the mankind would be forced to face starvation.
	No plants and trees would survive without water.
	Animals and Birds would be on the verge of extinction.
	Lack of water causes a lot of diseases and malnutrition in the children.
	Difficult for humans to stay hygienic as it would be impossible to take bath, clean clothes and vessels without water.


conserve water

How to save water?
	The demand for water is getting higher due to increased population, industrialization and agricultural usage. Over usage of water beyond the limits and polluting the water with the domestic wastes and industrial wastes are the major causes for the lack of clean water. On the other hand, dumping of plastics in the rivers and oceans also leads to plastic pollution and water pollution. So, it is the responsibility of the humans to conserve water and avoid pollution.

Listed below are some of the water conservation tips which can be followed to save water in our daily life.

Water conservation at home
	Since water is used extensively for domestic purpose, special attention must be given while using the water at home very particularly in the kitchen, bathroom, and the lawn. Also, teach your kids about water conservation and make it as a habit to implement it in life. Saving a drop of water adds value to your contribution to the mission of water conservation.

Kitchen

	Close the tap tightly and avoid water leakage in the taps.
	Run the dishwasher when it is full.
	Do not turn the tap fully on. A large amount of water will get wasted if the tap is fully on.
	Do not waste the water while washing the vessels. Fill a bucket or a basin with water and rinse the vessels.	
	Throw the food scraps into the garbage before rinsing the vessels because the scraps of food may block the sink and it may lead to the excess usage of water.
	Use paper cups, paper plates or banyan leaves if you host a huge family function or a party at your home.
	Instead of dumping down the liquid used to cook pasta or boil eggs, re-use it effectively by pouring that water to your plants after the liquid gets cooled.
	Do not use running water to clean vegetables or meat.
	Use efficient water doctor or other drinking water appliances. Fill a bottle with water instead of opening the tap every time you drink a glass of water.


tap waterdrop

	Bathroom and Laundry
	Close the tap while brushing your teeth. Do not waste the water by letting it go down the drain while you brush, instead open the tap only when it is time to rinse your mouth.
	Take short showers.
	Fill the tub or bucket halfway while bathing. Do not let the water to overflow from the bucket.
	Avoid flushing the toilet unnecessarily. It is advisable to use small capacity flush in toilets.
	Install shower heads, water saving toilets, and faucet aerators to control the flow of water.
	Save water while shaving, washing your face or hands. Do not let the water to run while you scrub your face or hands with soap, face wash or hand wash.
	Run the washing machine when it is loaded fully.
	Buy water efficient appliances such as dishwashers, washing machines, bathtubs, etc.
	Instead of using water to clean the bathrooms, use brooms or dusters for cleaning.
	Check for the leaks regularly and fix the faucet immediately when you spot a leak in the faucet. Temporarily insulate the faucet using a tape or a cloth to avoid water wastage and hire a plumber as soon as possible to fix the tap permanently.
	Limit the usage of water while washing the clothes. Do not wash the clothes with the tap open. Fill the buckets with water and use it for washing and rinsing the clothes.


Lawn and Outdoor
	Fix a nozzle on the hose to control the flow of water. Do not leave the hoses unattended.
	Water the plants in the garden only when needed. Do not over water your lawn. Use a hand sprinkler while watering the plants.
	Use a bucket of water to wash your car, instead of washing the car at home using a hose. It is also advisable to take yours to the car wash where the water gets recycled.
	Re-use the water from the kitchen and bathroom for watering a plant. Just take a note that the soap you are washing should not harm the plants and trees in the garden.
	Switch off the motor before it overflows. Excess water will get wasted if the motor gets overflowed. Try to use that water for some other purpose.
	It is better to water your plants in the morning than in the evening because in the morning time the temperature and the speed of the air will be low and the evaporation will not happen.
	Do not clean the pavement or driveway with water instead use a broom to clean the leaves or debris.
	Shut off the water system when the tap gets broken or if you can't control the water leakage.
	Use self-serve pet washing system to wash your dogs or take your pet to the grooming center.
	Install rainwater harvesting systems in the house to store rainwater. Also during the rainy season, collect rainwater in large tubs and use it to water the plants in the house.

save water

Effects of the shortage of water
Can you imagine your life without water? It is highly impossible to continue living on the earth without water. Already the world is facing problems such as water scarcity and water pollution at a high level. In the olden days, adequate water was present in rivers, wells, ponds, and dams. At present, we are in a situation to buy mineral water and packaged drinking water from shops. The present situation clearly reveals the shortage of water in the world and it may even get worse in the future. To avoid the below-mentioned effects of the shortage of water, it is the responsibility of the humans to conserve water for the future use.

The shortage of water would convert agriculture lands into barren lands and will lead to drought.
If there is no water, then it is difficult to cook and the mankind would be forced to face starvation.
No plants and trees would survive without water.
Animals and Birds would be on the verge of extinction.
Lack of water causes a lot of diseases and malnutrition in the children.
Difficult for humans to stay hygienic as it would be impossible to take bath, clean clothes and vessels without water.


conserve water

How to save water?
The demand for water is getting higher due to increased population, industrialization and agricultural usage. Over usage of water beyond the limits and polluting the water with the domestic wastes and industrial wastes are the major causes for the lack of clean water. On the other hand, dumping of plastics in the rivers and oceans also leads to plastic pollution and water pollution. So, it is the responsibility of the humans to conserve water and avoid pollution.

Listed below are some of the water conservation tips which can be followed to save water in our daily life.

Water conservation at home
Since water is used extensively for domestic purpose, special attention must be given while using the water at home very particularly in the kitchen, bathroom, and the lawn. Also, teach your kids about water conservation and make it as a habit to implement it in life. Saving a drop of water adds value to your contribution to the mission of water conservation.

Kitchen

Close the tap tightly and avoid water leakage in the taps.
Run the dishwasher when it is full.
Do not turn the tap fully on. A large amount of water will get wasted if the tap is fully on.
Do not waste the water while washing the vessels. Fill a bucket or a basin with water and rinse the vessels.
Throw the food scraps into the garbage before rinsing the vessels because the scraps of food may block the sink and it may lead to the excess usage of water.
Use paper cups, paper plates or banyan leaves if you host a huge family function or a party at your home.
Instead of dumping down the liquid used to cook pasta or boil eggs, re-use it effectively by pouring that water to your plants after the liquid gets cooled.
Do not use running water to clean vegetables or meat.
Use efficient water doctor or other drinking water appliances. Fill a bottle with water instead of opening the tap every time you drink a glass of water.


tap waterdrop

Bathroom and Laundry
Close the tap while brushing your teeth. Do not waste the water by letting it go down the drain while you brush, instead open the tap only when it is time to rinse your mouth.
Take short showers.
Fill the tub or bucket halfway while bathing. Do not let the water to overflow from the bucket.
Avoid flushing the toilet unnecessarily. It is advisable to use small capacity flush in toilets.
Install shower heads, water saving toilets, and faucet aerators to control the flow of water.
Save water while shaving, washing your face or hands. Do not let the water to run while you scrub your face or hands with soap, face wash or hand wash.
Run the washing machine when it is loaded fully.
Buy water efficient appliances such as dishwashers, washing machines, bathtubs, etc.
Instead of using water to clean the bathrooms, use brooms or dusters for cleaning.
Check for the leaks regularly and fix the faucet immediately when you spot a leak in the faucet. Temporarily insulate the faucet using a tape or a cloth to avoid water wastage and hire a plumber as soon as possible to fix the tap permanently.
Limit the usage of water while washing the clothes. Do not wash the clothes with the tap open. Fill the buckets with water and use it for washing and rinsing the clothes.


Lawn and Outdoor
	Fix a nozzle on the hose to control the flow of water. Do not leave the hoses unattended.	
	Water the plants in the garden only when needed. Do not over water your lawn. Use a hand sprinkler while watering the plants.
	Use a bucket of water to wash your car, instead of washing the car at home using a hose. It is also advisable to take yours to the car wash where the water gets recycled.
	Re-use the water from the kitchen and bathroom for watering a plant. Just take a note that the soap you are washing should not harm the plants and trees in the garden.	
	Switch off the motor before it overflows. Excess water will get wasted if the motor gets overflowed. Try to use that water for some other purpose.
	It is better to water your plants in the morning than in the evening because in the morning time the temperature and the speed of the air will be low and the evaporation will not happen.
Do not clean the pavement or driveway with water instead use a broom to clean the leaves or debris.
Shut off the water system when the tap gets broken or if you can't control the water leakage.
Use self-serve pet washing system to wash your dogs or take your pet to the grooming center.
Install rainwater harvesting systems in the house to store rainwater. Also during the rainy season, collect rainwater in large tubs and use it to water the plants in the house.''')
    with st.expander('PIE CHART'):
        st.pyplot(fig)