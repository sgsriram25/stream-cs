import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import chart_studio.plotly as py
from plotly import offline as pyoff
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout = "wide")
st.title("Insights Spark Shop Dashboard")

side = st.sidebar.selectbox('Select page',
  ['Monthly Customer Status','New vs Existing Customers','Segmentation based on UK','Product Clustering','RFM Clustering'])
first = pd.read_csv('first.csv')
if side == 'Monthly Customer Status':
    
    
    #st.set_page_config(layout = "wide")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""Monthly Revenue Line graph""")
        first = pd.read_csv('first.csv')
        plot_data = [
            go.Scatter(
                x=first['InvoiceYearMonth'],
                y=first['Revenue'],
            )
        ]
        
        plot_layout = go.Layout(
                xaxis={"type": "category"},
                title='Montly Revenue'
            )
        
        fig = go.Figure(data=plot_data, layout=plot_layout)
        
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("""Monthly Revenue Growth Rate""")
        plot_data10 = [
          go.Scatter(
            x=first['InvoiceYearMonth'],
            y=first['MonthlyGrowth'],
          )
        ]
    
        plot_layout = go.Layout(
             xaxis={"type": "category"},
             title='Montly Growth Rate'
        )
    
        fig10 = go.Figure(data=plot_data10, layout=plot_layout)        
        st.plotly_chart(fig10, use_container_width=True)
    
    st.markdown("""Monthly Order Status""")
    page = st.selectbox('Select page',['Monthly Active Customers','Monthly Total Order','Monthly Average Order'])
    
    if page == 'Monthly Active Customers':
        plot_data11 = [
            go.Bar(
                x=first['InvoiceYearMonth'],
                y=first['CustomerID'],
                )
            ]

        plot_layout = go.Layout(
            xaxis={"type": "category"},
            title='Monthly Active Customers'
            )

        fig11 = go.Figure(data=plot_data11, layout=plot_layout)
        st.plotly_chart(fig11, use_container_width=True)
    
    elif page == 'Monthly Total Order':
         plot_data12 = [
             go.Bar(
                 x=first['InvoiceYearMonth'],
                 y=first['Quantity'],
         )
        ]

         plot_layout = go.Layout(
                    xaxis={"type": "category"},
                    title='Monthly Total # of Order'
                )

         fig12 = go.Figure(data=plot_data12, layout=plot_layout) 
         st.plotly_chart(fig12, use_container_width=True)
         
    else:
         plot_data13 = [
             go.Bar(
                 x=first['InvoiceYearMonth'],
                 y=first['Avgrevenue'],
                 )
             ]

         plot_layout = go.Layout(
             xaxis={"type": "category"},
             title='Monthly Order Average Revenue'
          )
         fig13 = go.Figure(data=plot_data13, layout=plot_layout)
         st.plotly_chart(fig13, use_container_width=True)
         

elif side == 'New vs Existing Customers':
    st.markdown("""New vs Existing """)
    comp = pd.read_csv('comp.csv')
    plot_data14 = [
    go.Scatter(
        x=comp.query("UserType == 'Existing'")['InvoiceYearMonth'],
        y=comp.query("UserType == 'Existing'")['Revenue'],
        name = 'Existing'
    ),
    go.Scatter(
        x=comp.query("UserType == 'New'")['InvoiceYearMonth'],
        y=comp.query("UserType == 'New'")['Revenue'],
        name = 'New'
    )
    ]

    plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='New vs Existing'
    )
    fig14 = go.Figure(data=plot_data14, layout=plot_layout)
    st.plotly_chart(fig14, use_container_width=True)
    
    st.markdown("""Retention Rate""")
    ret = pd.read_csv('ret.csv')
    plot_data15 = [
    go.Scatter(
        x=ret.query("InvoiceYearMonth<201112")['InvoiceYearMonth'],
        y=ret.query("InvoiceYearMonth<201112")['RetentionRate'],
        name="organic"
    )
    
    ]

    plot_layout = go.Layout(
        xaxis={"type": "category"},
        title='Monthly Retention Rate'
    )
    fig15 = go.Figure(data=plot_data15, layout=plot_layout)
    st.plotly_chart(fig15, use_container_width=True)
    
elif side == 'Segmentation based on UK': 
    st.markdown("""Segmentation Based on UK Data""")
    page = st.selectbox('Select page',['Recency Histogram','Frequency Histogram','Monetary Histogram'])
    fin = pd.read_csv('final.csv')
    if page == 'Recency Histogram':
        plot_data16 = [
            go.Histogram(
                x=fin['Recency']
                )
            ]
    
        plot_layout = go.Layout(
                title='Recency'
                )
        fig16 = go.Figure(data=plot_data16, layout=plot_layout)
        st.plotly_chart(fig16, use_container_width=True)
    elif page == 'Frequency Histogram':
        plot_data17 = [
            go.Histogram(
                x=fin.query('Frequency < 1000')['Frequency']
                )
            ]
        plot_layout = go.Layout(
                   title='Frequency'
                   )
        fig17 = go.Figure(data=plot_data17, layout=plot_layout)  
        st.plotly_chart(fig17, use_container_width=True)
    else:
        plot_data18 = [
            go.Histogram(
            x=fin.query('Revenue < 10000')['Revenue']
            )
        ]

        plot_layout = go.Layout(
            title='Monetary Value'
        )
        fig18 = go.Figure(data=plot_data18, layout=plot_layout)
        st.plotly_chart(fig18, use_container_width=True)
        
    page = st.selectbox('Select page',['Recency Vs Frequncy','Frequency vs Monetary','Monetary vs Recency'])
    if page == 'Frequency vs Monetary':
       tx_graph = fin.query("Revenue < 50000 and Frequency < 2000")
        
       plot_data19 = [
            go.Scatter(
                x=tx_graph.query("Segment == 'Low-Value'")['Frequency'],
                y=tx_graph.query("Segment == 'Low-Value'")['Revenue'],
                mode='markers',
                name='Low',
                marker= dict(size= 7,
                    line= dict(width=1),
                    color= 'blue',
                    opacity= 0.8
                   )
            ),
                go.Scatter(
                x=tx_graph.query("Segment == 'Mid-Value'")['Frequency'],
                y=tx_graph.query("Segment == 'Mid-Value'")['Revenue'],
                mode='markers',
                name='Mid',
                marker= dict(size= 9,
                    line= dict(width=1),
                    color= 'green',
                    opacity= 0.5
                   )
            ),
                go.Scatter(
                x=tx_graph.query("Segment == 'High-Value'")['Frequency'],
                y=tx_graph.query("Segment == 'High-Value'")['Revenue'],
                mode='markers',
                name='High',
                marker= dict(size= 11,
                    line= dict(width=1),
                    color= 'red',
                    opacity= 0.9
                   )
            ),
        ]
        
       plot_layout = go.Layout(
                yaxis= {'title': "Revenue"},
                xaxis= {'title': "Frequency"},
                title='Segments'
            )
       fig19 = go.Figure(data=plot_data19, layout=plot_layout)
       st.plotly_chart(fig19, use_container_width=True)
       
    elif page == 'Monetary vs Recency':
        tx_graph = fin.query("Revenue < 50000 and Frequency < 2000")       
        plot_data20 = [
            go.Scatter(
                x=tx_graph.query("Segment == 'Low-Value'")['Recency'],
                y=tx_graph.query("Segment == 'Low-Value'")['Revenue'],
                mode='markers',
                name='Low',
                marker= dict(size= 7,
                    line= dict(width=1),
                    color= 'blue',
                    opacity= 0.8
                   )
            ),
                go.Scatter(
                x=tx_graph.query("Segment == 'Mid-Value'")['Recency'],
                y=tx_graph.query("Segment == 'Mid-Value'")['Revenue'],
                mode='markers',
                name='Mid',
                marker= dict(size= 9,
                    line= dict(width=1),
                    color= 'green',
                    opacity= 0.5
                   )
            ),
                go.Scatter(
                x=tx_graph.query("Segment == 'High-Value'")['Recency'],
                y=tx_graph.query("Segment == 'High-Value'")['Revenue'],
                mode='markers',
                name='High',
                marker= dict(size= 11,
                    line= dict(width=1),
                    color= 'red',
                    opacity= 0.9
                   )
            ),
        ]
        
        plot_layout = go.Layout(
                yaxis= {'title': "Revenue"},
                xaxis= {'title': "Recency"},
                title='Segments'
            )
        fig20 = go.Figure(data=plot_data20, layout=plot_layout)
        st.plotly_chart(fig20, use_container_width=True)
    
    else:
        tx_graph = fin.query("Revenue < 50000 and Frequency < 2000")
        plot_data21 = [
            go.Scatter(
                x=tx_graph.query("Segment == 'Low-Value'")['Recency'],
                y=tx_graph.query("Segment == 'Low-Value'")['Frequency'],
                mode='markers',
                name='Low',
                marker= dict(size= 7,
                    line= dict(width=1),
                    color= 'blue',
                    opacity= 0.8
                   )
            ),
                go.Scatter(
                x=tx_graph.query("Segment == 'Mid-Value'")['Recency'],
                y=tx_graph.query("Segment == 'Mid-Value'")['Frequency'],
                mode='markers',
                name='Mid',
                marker= dict(size= 9,
                    line= dict(width=1),
                    color= 'green',
                    opacity= 0.5
                   )
            ),
                go.Scatter(
                x=tx_graph.query("Segment == 'High-Value'")['Recency'],
                y=tx_graph.query("Segment == 'High-Value'")['Frequency'],
                mode='markers',
                name='High',
                marker= dict(size= 11,
                    line= dict(width=1),
                    color= 'red',
                    opacity= 0.9
                   )
            ),
        ]
        
        plot_layout = go.Layout(
                yaxis= {'title': "Frequency"},
                xaxis= {'title': "Recency"},
                title='Segments'
            )
        fig21 = go.Figure(data=plot_data21, layout=plot_layout)
        st.plotly_chart(fig21, use_container_width=True)
    
elif side == 'Product Clustering':
    col1, col2 = st.columns(2)
    with col1:
        cat1 = Image.open('dashimage/dash1.png')
        st.image(cat1, caption='Category 1 Products')
        st.markdown('This category has general products like mug, flowers, jewellery etc')
    with col2:
        cat2 = Image.open('dashimage/dash2.png')
        st.image(cat2, caption='Category 2 Products')
        st.markdown('This category has bag products like shopper bag,gift bag, jumbo bag etc')
    
    col3, col4 = st.columns(2)
    with col3:
        cat3 = Image.open('dashimage/dash3.png')
        st.image(cat3, caption='Category 3 Products')
        st.markdown('This category has chirstmas decorative products like star, christmas tree, hangings etc')
    with col4:
        cat4 = Image.open('dashimage/dash4.png')
        st.image(cat4, caption='Category 4 Products')
        st.markdown('This category has general decorative products like crystal, mirror, antique etc')
        
    st.text("")
    
    col5, col6 = st.columns(2)
    
    with col5:
        gra1 = Image.open('dashimage/graph.jpeg')
        st.image(gra1, caption='Graph for Amount spent on each category')
        st.markdown('All category 1 ,2, 3 has sharp increase in sales in the months November and december indicating the **chirstmas season**')
    
    with col6:
        heat = pd.read_csv('heat.csv')
        fig, ax = plt.subplots()
        sns.heatmap(heat,
                        annot=True,                
                        #cmap='rocket_r',
                        #linewidths=.5,
                        ax=ax)
        plt.xlabel('Spending', fontsize = 15) 
        plt.ylabel('Cluster', fontsize = 15)
        st.write(fig)
                                 
elif side == 'RFM Clustering':    
    col1, col2 = st.columns(2)
    with col1:
        def cluster_profile_RFM_country(customer_clustering,cut_off=0):
              ''' profile clusters '''
            
              customer_clusters=customer_clustering.reset_index().groupby(['cluster']).agg({'Customer ID':['count'], 
                                                                     'recency':'median',
                                                                     'frequency':'median',
                                                                     'monetary_value':'median',
                                                                     'weighted GDP':'median'})
              idx= customer_clusters['Customer ID']>=cut_off
              idx=idx['count'].to_list()
              customer_clusters=customer_clusters[idx]
              print(customer_clusters)
              print('\n')
              customer_clusters_sum=customer_clusters.sum(axis=0)
              #print(customer_clusters_sum)
              customer_clusters['monetary_value']=100*customer_clusters['monetary_value']/customer_clusters_sum['monetary_value']
              customer_clusters['frequency']=100*customer_clusters['frequency']/customer_clusters_sum['frequency']
              customer_clusters['recency']=100*customer_clusters['recency']/customer_clusters_sum['recency']
              customer_clusters['weighted GDP']=100*customer_clusters['weighted GDP']/customer_clusters_sum['weighted GDP']
              print(customer_clusters)
              print('\n')
              
              st.subheader("HEAT map - Numbers are column percentages")
              fig, ax = plt.subplots()
              sns.heatmap(customer_clusters.drop(['Customer ID'],axis=1), annot=True,  linewidths=.5,ax=ax)
              st.write(fig)
        
        rfm1 = pd.read_csv('rfm1.csv')
        cluster_profile_RFM_country(rfm1,cut_off=100)
        
    with col2:
        cross = pd.read_csv('cross.csv')
        st.subheader("HEAT map - Numbers are column percentages")
        fig, ax = plt.subplots()
        sns.heatmap(cross/100,
                        annot=True,
                        fmt='.2%',
                        #cmap='rocket_r',
                        #linewidths=.5,
                        ax=ax)
        plt.xlabel('Item Category Cluster', fontsize = 15) 
        plt.ylabel('RFM Country Cluster', fontsize = 15)
        st.write(fig)
        #plt.show()
    
    
    col1, col2 = st.columns(2)
   
    with col1:
        st.header('Cluster 1 (0)')
        st.markdown('Cluster 1 has low recency and frequency but high monetary value - classified as one time high amount buyers')
        st.header('Cluster 2 (1)')
        st.markdown('Cluster 2 has medium recency and frequency and has the highest monetary value among all')
        st.header('Cluster 3 (3)')
        st.markdown('Cluster 3 has decent recency, frequency and monetary value - They are medium regular buyers')
        st.header('Cluster 4 (5)')
        st.markdown('Cluster 4 has highest frequency and recency value but medium monetary value - Classfied as best regular Medium Money spenders')
        
   
    with col2:
        page = st.selectbox('Select page',['RFM cluster 1','RFM cluster 2','RFM cluster 3','RFM cluster 4'])
        if page == 'RFM cluster 1':
            plot_data12 = [
                go.Bar(
                    x=['General Category','Bags Category','Christmas decoration category','Other Decoration Category'],
                    y=[2588,234,95,628],
            )
           ]
        
            plot_layout = go.Layout(
                       xaxis={"type": "category"},
                       title='Cluster 1 Each Category Buyers'
                   )
            
            fig12 = go.Figure(data=plot_data12, layout=plot_layout) 
            st.plotly_chart(fig12, use_container_width=True)
            st.markdown('The RFM first cluster has high value General category customers')
            st.markdown('The RFM first cluster has high value chirstmas category customers')
            st.markdown('The RFM first cluster has high value General Decoration category customers')
        
        if page == 'RFM cluster 2':
            plot_data12 = [
                go.Bar(
                    x=['General Category','Bags Category','Christmas decoration category','Other Decoration Category'],
                    y=[1126,95,35,291],
            )
           ]
        
            plot_layout = go.Layout(
                       xaxis={"type": "category"},
                       title='Cluster 2 Each Category Buyers'
                   )
            
            fig12 = go.Figure(data=plot_data12, layout=plot_layout) 
            st.plotly_chart(fig12, use_container_width=True)
            st.markdown('The RFM Second cluster has high value General decoration category customers')
            st.markdown('The RFM Second cluster has low value General bag and christmas decoration category customers')
            st.markdown('The RFM second cluster has regular but medium spenders')
            
        
        if page == 'RFM cluster 3':
            plot_data12 = [
                go.Bar(
                    x=['General Category','Bags Category','Christmas decoration category','Other Decoration Category'],
                    y=[467,12,17,81],
            )
           ]
        
            plot_layout = go.Layout(
                       xaxis={"type": "category"},
                       title='Cluster 3 Each Category Buyers'
                   )
            
            fig12 = go.Figure(data=plot_data12, layout=plot_layout) 
            st.plotly_chart(fig12, use_container_width=True)
            st.markdown('The RFM third cluster has low value but does have some contribution so can gain their attraction by giving offers')
        
        if page == 'RFM cluster 4':
            plot_data12 = [
                go.Bar(
                    x=['General Category','Bags Category','Christmas decoration category','Other Decoration Category'],
                    y=[1126,95,35,291],
            )
           ]
        
            plot_layout = go.Layout(
                       xaxis={"type": "category"},
                       title='Cluster 4 Each Category Buyers'
                   )
            
            fig12 = go.Figure(data=plot_data12, layout=plot_layout) 
            st.plotly_chart(fig12, use_container_width=True)
            st.markdown('The RFM fourth cluster has very little value so can ignore them')
       
