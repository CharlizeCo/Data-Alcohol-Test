import streamlit as st
import pandas as pd
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
import matplotlib.pyplot as plt

st.title("Alcohol Consumption Project")
st.write("Made by: Charlize Corriette")
st.markdown('---')

urlexport = ('https://raw.githubusercontent.com/CharlizeCo/Data-Alcohol-Test/main/export.csv')
df1 = pd.read_csv(urlexport)


#Top 20 Countries with the Most Alcohol Consum----------------------------------------------------------------------------------------------------------------------


year_2019_df = df1[df1['date_of_information'] >= 2019]
top_20_co = year_2019_df.nlargest(20, 'value')
top_20_co = top_20_co[top_20_co['name'] != 'Cook Islands']
fig = plt.figure()
fig, ax = plt.subplots(figsize = (15, 7))

bar_color='#CE5A67'
st.subheader("Top 20 Countries with the Most Overall Alcohol Consumption in 2019")

bars1 = ax.bar(top_20_co['name'], top_20_co['value'], color=bar_color)
ax.set_xlabel('Country')
ax.set_ylabel('Overall Alcohol Consumption on Average \n(in liters)')
ax.set_title('\nCountries with the Most Overall Alcohol Consumption on Average in 2019\n')
plt.xticks(rotation = 45, ha='right')

for bar in bars1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', color='black', fontsize=8)

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
st.pyplot(plt)

st.write("This first graph shows the nations with the highest levels of alcohol consumption with Lavita being the highest. Analyzing this graph lets us determine"
         " the countries with increased alcohol consumption and whether they are close geographically. We can see the graph underlines multiple European nations"
         " with a prominent density of alcohol consumption. This pattern suggests a possible connection with the general drinking cultures that are a part of these"
         " countries, which sets them apart from other countries.")


#Top 20 Countries with the Least Alcohol Consum--------------------------------------------------------------------------------------------------------------------


low_20_co = year_2019_df.nsmallest(20, 'value')
fig, ax = plt.subplots(figsize = (15, 7))

st.subheader("Top 20 Countries with the Least Overall Alcohol Consumption in 2019")

bars2 = ax.bar(low_20_co['name'], low_20_co['value'], color=bar_color)
ax.set_xlabel('Country')
ax.set_ylabel('Overall Alcohol Consumption on Average \n(in liters)')
ax.set_title('\nCountries with the Least Overall Alcohol Consumption on Average in 2019\n')
plt.xticks(rotation = 45, ha='right')

for bar in bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom', color='black', fontsize=8)

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
st.pyplot(plt)

st.write("The following graph is designed to display nations characterized by minimal alcohol consumption. It allows a comparison with the previously mentioned"
         " graph based on numerical values and specific countries that exhibit different behaviors. Notably, Saudi Arabia, Mauritania, Bangladesh, Somalia, and"
         " Kuwait appear to have the lowest alcohol consumption. This makes sense when considering the most practiced religions in these nations are Islam and"
         " Hinduism, which strictly prohibit the use of alcohol. However, this extends beyond religious constraints as a significant pattern shows that most of"
         " these countries are in the Middle East and Northern Africa, showcasing these regions' influence.")


#Line Chart Data User input based on country-----------------------------------------------------------------------------------------------------------------------


urlpurealcohol = ('https://raw.githubusercontent.com/CharlizeCo/Data-Alcohol-Test/main/total-alcohol-consumption-per-capita-litres-of-pure-alcohol.csv')
df2 = pd.read_csv(urlpurealcohol)

st.subheader("\nCountry Alcohol Consumption Over Time (2000 - 2018)")
st.write("Please enter the name of the country for which you'd like to observe the changes in alcohol consumption over time. Try 'United States' as a start!")
user = st.text_input("Enter a country's name:")
country_data = df2[df2['Entity'] == user]

line_color='#F4BF96'

if not country_data.empty:    

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(country_data['Year'], country_data['Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)'], marker='o', color=line_color)
    ax.set_xlabel('Year')
    ax.set_ylabel('Overall Alcohol Consumption of Alcohol on Average \n(in liters)')
    ax.set_title(f'Overall Alcohol Consumption in {user} Over Time')
    
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')
    st.pyplot(fig)
else:
    st.warning(f"You have yet to or not entered a valid country name or there is no data for the country you've inputed. Please try again.")

st.write("This line graph was created to provide a more focused analysis of specific countries within a broader timeline of alcohol use. This approach allows us"
         " to determine the course of alcohol consumption in the selected country, allowing us to identify any significant shifts between years or the continuation"
         " of a consistent trend.")

st.write("A similar method was applied to the line graph below, offering a more expansive yet still focused examination of the overall"
         " timeline of alcohol consumption. This approach allows for a better look at trends and variations in alcohol use over time within a larger context, such"
         " as income level.")

st.write("These two line graphs show a clear connection between the two, which is that higher-income countries tend to exhibit higher levels of alcohol consumption."
         " In contrast, lower-income countries lean towards lower alcohol consumption. This trend may stem from financial differences, where individuals in"
         " higher-income countries have greater means to afford alcohol compared to lower-income countries.")

st.write("Nevertheless, some exceptions depict a different picture of this economic trend. Some countries exhibit lower alcohol consumption despite being"
         " considerably wealthy. In these instances, factors such as religion and culture are a significant influence on alcohol consumption. This highlights"
         " the difference between the economic and cultural factors shaping these nations' drinking habits.")


#Income Level Line Chart-------------------------------------------------------------------------------------------------------------------------------------------


income_level = st.radio('Select an income level:',
                        ('High-income countries','Upper-middle-income countries','Middle-income countries','Lower-middle-income countries','Low-income countries'))

fig, ax = plt.subplots(figsize=(12, 7))

if income_level != 'Select an income level:':
    filtered_df = df2[df2['Entity'] == income_level]
    
    if not filtered_df.empty:
        
        ax.plot(filtered_df['Year'], filtered_df['Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)'],
                label = income_level, color = line_color, marker = 'o')
        
        ax.set_xlabel('Year')
        ax.set_ylabel('Overall Alcohol Consumption on Average (in liters)')
        ax.set_title(f'Overall Alcohol Consumption in {income_level} Over Time')
                

        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

        fig.patch.set_facecolor('none')
        ax.set_facecolor('none')

        st.pyplot(fig)
    else:
        st.warning(f"No data available for {income_level}.")
else:
    st.warning("You have not selected an income level.")

st.markdown('---')


#Premature Deaths Due to Alcohol Top------------------------------------------------------------------------------------------------------------------------------


st.subheader("Top 20 Countries with the Highest Numbers of Premature Deaths Linked to Alcohol")

urlpremature = ('https://raw.githubusercontent.com/CharlizeCo/Data-Alcohol-Test/main/rate-of-premature-deaths-due-to-alcohol.csv')
df3 = pd.read_csv(urlpremature)

fig = plt.figure()
fig, ax = plt.subplots(figsize=(12, 7))

deaths2019_df = df3[df3['Year'] >= 2019]
top_20_count = deaths2019_df.nlargest(21, 'Deaths that are from all causes attributed to alcohol use per 100,000 people, in both sexes aged age-standardized')
top_20_count = top_20_count[top_20_count['Entity'] != 'Central African Republic']

bars3 = ax.bar(top_20_count['Entity'], top_20_count['Deaths that are from all causes attributed to alcohol use per 100,000 people, in both sexes aged age-standardized'], color = bar_color)
ax.set_xlabel('Country')
ax.set_ylabel('All Deaths Caused By Any Attributation to Alcohol Use \n(per 100,000 people, both sexes)')
ax.set_title('\nTop 20 Countries with the Most Attributed Alcohol Deaths in 2019\n')
plt.xticks(rotation = 45, ha='right')

for bar in bars3:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', color='black', fontsize=8)

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
st.pyplot(plt)

st.write("These graphs highlight the top 20 countries with the highest and lowest alcohol-attributed deaths. The main goal was to distinguish any connection"
         " between alcohol consumption and the fatalities attached to it. Upon examining the top 20 countries with the highest alcohol-attributed deaths, it"
         " becomes apparent that the connection between alcohol consumption and alcohol fatalities is not straightforward. Mongolia tops the list, and the"
         " remaining countries are mainly African, suggesting a distinct difference from the first bar graph.")

st.write("However, the second graph reveals a closer correlation. The top 20 countries with the least alcohol-attributed deaths align closely with those"
         " showing the lowest alcohol consumption. This suggests that the lower use of alcohol consumption in these countries may indeed contribute to a"
         " reduced death count related to alcohol, offering a more direct connection between alcohol intake and associated fatalities.")


#Premature Deaths Due to Alcohol Low-----------------------------------------------------------------------------------------------------------------------------


st.subheader("Top 20 Countries with the Lowest Numbers of Premature Deaths Linked to Alcohol")

fig = plt.figure()
fig, ax = plt.subplots(figsize=(12, 7))

deaths2019low_df = df3[df3['Year'] >= 2019]
low_20_count = deaths2019_df.nsmallest(21, 'Deaths that are from all causes attributed to alcohol use per 100,000 people, in both sexes aged age-standardized')
low_20_count = low_20_count[low_20_count['Entity'] != 'Middle East & North Africa (WB)']

bars4 = ax.bar(low_20_count['Entity'], low_20_count['Deaths that are from all causes attributed to alcohol use per 100,000 people, in both sexes aged age-standardized'], color = bar_color)
ax.set_xlabel('Country')
ax.set_ylabel('All Deaths Caused By Any Attributation to Alcohol Use \n(per 100,000 people, both sexes)')
ax.set_title('\nTop 20 Countries with the Least Attributed Alcohol Deaths in 2019\n')
plt.xticks(rotation = 45, ha='right')

for bar in bars4:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', color='black', fontsize=8)

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
st.pyplot(plt)


#Alcohol Disorder-----------------------------------------------------------------------------------------------------------------------------------------------

st.markdown('---')

urldis = ('https://raw.githubusercontent.com/CharlizeCo/Data-Alcohol-Test/main/share-with-alcohol-use-disorders.csv')
df4 = pd.read_csv(urldis)

st.subheader('Alcohol Disorder Cases Based On Country')

st.write("Lastly, I aimed to explore the potential correlation between high alcohol consumption and alcohol disorders. Here, we have a timeline illustrating"
         " recorded alcohol disorders based on country. Additionally, a pie chart was created to show the relationship between alcohol disorders and the"
         " overall population of the selected country.")

st.write("The results of this analysis were to shed light on whether countries with high alcohol consumption also exhibit a higher amount of alcohol disorders."
         " By analyzing both the timeline and pie chart, we can determine patterns that may indicate a connection between the level of alcohol consumption and"
         " the level of alcohol disorders.")

st.write('Write which country you would like to see on their cases of alcohol disorders.')
user2 = st.text_input("Enter a country's name here:")

country_data2 = df4[df4['Entity'] == user2]

if not country_data2.empty:

    fig, ax = plt.subplots(figsize = (10,6))
    ax.plot(country_data2['Year'], country_data2['Current number of cases of alcohol use disorders per 100 people, in both sexes aged age-standardized'], color = line_color, marker = 'o')
    ax.set_xlabel('Country')
    ax.set_ylabel('Cases of Alcohol Use Disorders \n(100,000 people, both sexes)')
    ax.set_title(f'Cases of Alcohol Use Disorders in {user2} (1990 - 2019)')

    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')
    st.pyplot(fig)

else:
    st.warning(f"You have yet to or not entered a valid country name or there is no data for the country you've inputed. Please try again.")


urldis2 = ('https://raw.githubusercontent.com/CharlizeCo/Data-Alcohol-Test/main/share-with-alcohol-use-disorder-vs-alcohol-consumption.csv')
df5 = pd.read_csv(urldis2)

country_data3 = df5[df5['Entity'] == user2]
year2019_data = country_data3[country_data3['Year'] >= 2019]


if not year2019_data.empty:

    disorder_multi = year2019_data['Current number of cases of alcohol use disorders per 100 people, in both sexes aged age-standardized'].values * 1000000
    percentage1 = disorder_multi / year2019_data['Population (historical estimates)'].values * 100  # decimal form
    percentage2 = 100 - percentage1

    fig, ax = plt.subplots(figsize=(10, 6))

    labels = ['Cases of Alcohol Use Disorders', 'Population Without Alcohol Use Disorders']
    sizes = [percentage1[0], percentage2[0]]

    colors = ['#F4BF96', '#CE5A67']

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(edgecolor='black'))

    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')
    ax.axis('equal')

    ax.set_title(f'Cases of Alcohol Use Disorders as a Percentage of Population in {user2} (2019)')

    st.pyplot(fig)

else:
    st.warning(f"You have yet to enter a valid country name or there is no data for the country you've inputted. Please try again.")


