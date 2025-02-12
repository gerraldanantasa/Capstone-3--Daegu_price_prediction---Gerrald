import pandas as pd
import streamlit as st
import pickle


# Set page configuration
st.set_page_config(
    page_title="Daegu House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# Custom CSS for improved styling
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    color: #333;
}
.highlight {
    background-color: #f0f2f6;
    padding: 10px;
    border-radius: 5px;
}
.stNumberInput>div>div>input {
    font-size: 16px !important;
}
.stSelectbox>div>div>select {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# Function to format currency
def format_currency(amount):
    """Format amount in Korean Won with comma separators"""
    return f"{int(amount):,} ₩"

# Main function to collect user input features
def user_input_feature():
    """Collect user input features for house price prediction"""
    # Sidebar for input features with improved layout
    st.sidebar.header("🏘️ House Features Input", divider='rainbow')
    
    # Input features with improved descriptions and ranges
    size = st.sidebar.number_input(
        label="🔲 Total Area (sq ft)", 
        min_value=135, 
        max_value=2337, 
        value=500,
        help="Enter the total area of the apartment in square feet"
    )

    numofuni = st.sidebar.selectbox(
        label="🎓 Nearby Universities", 
        options=(0,1,2,3,4,5),
        help="Number of universities near the apartment"
    )

    numofpuboffice = st.sidebar.selectbox(
        label="🏢 Nearby Public Offices", 
        options=(0,1,2,3,4,5,7),
        help="Number of public offices in the vicinity"
    )

    numofarking = st.sidebar.selectbox(
        label="🚗 Parking Spaces", 
        options=(0, 18, 56, 76, 79, 108, 181, 184, 203, 218, 400, 475, 524, 536, 605, 798, 930, 1174, 1270, 1321),
        help="Number of parking spaces available"
    )

    timetosubway = st.sidebar.selectbox(
        label="🚇 Distance to Subway", 
        options=('0-5min', '5min~10min', '10min~15min', '15min~20min', 'no_bus_stop_nearby'),
        help="Walking time to the nearest subway station"
    )

    subwaystation = st.sidebar.selectbox(
        label="🚉 Nearest Subway Station", 
        options=(
            'Bangoge', 'Banwoldang', 'Chil-sung-market', 'Daegu', 
            'Kyungbuk_uni_hospital', 'Myung-duk', 'Sin-nam', 'no_subway_nearby'
        ),
        help="Closest subway station to the apartment"
    )

    yearbuilt = st.sidebar.selectbox(
        label="🏗️ Year Built", 
        options=(1978, 1980, 1985, 1986, 1992, 1993, 1997, 2003, 2005, 2006, 
                2007, 2008, 2009, 2013, 2014, 2015),
        help="The year the apartment building was constructed"
    )
        
        # Create DataFrame with input features
    df = pd.DataFrame({
        'TimeToSubway': [timetosubway],
        'SubwayStation': [subwaystation],
        'N_FacilitiesNearBy(PublicOffice)': [numofpuboffice],
        'N_SchoolNearBy(University)': [numofuni],
        'N_Parkinglot(Basement)': [numofarking],
        'YearBuilt': [yearbuilt],
        'Size(sqf)': [size]
    })
    
    return df

def main():
    """Main function to run the Streamlit app"""
    # Title and description
    st.title("🏘️ Daegu House Price Predictor")
    st.markdown("""
    ### Predict Apartment Prices in Daegu with Machine Learning
    Use the sidebar to input apartment features and get an estimated price.
    """)
    
    # Collect user input
    df_customer = user_input_feature()
    
    # Prediction section
    st.header("Price Prediction", divider='blue')
    
    # Load pre-trained model
    try:
        model_loaded = pickle.load(open('final_model.sav', 'rb'))
        
        # Make prediction
        predicted_price = model_loaded.predict(df_customer)[0]
        
        # Create columns for better layout
        col1, col2 = st.columns(2)
        
        # Display input features
        with col1:
            st.subheader("🔍 Apartment Features")
            features_display = df_customer.transpose()
            features_display.columns = ['Value']
            st.dataframe(features_display, use_container_width=True)
        
        # Display prediction and model performance
        with col2:
            st.subheader("💰 Price Estimation")
            
            # Highlight predicted price
            st.markdown(f"""
            <div class='highlight'>
            <h3 style='color:#007bff;text-align:center;'>
            Predicted Price: {format_currency(predicted_price)}
            </h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Model performance metrics
            st.markdown("""
            ### Model Performance
            - **MAPE**: 18.3%
            - **MAE**: 36,959 ₩
            """)
        
        # Add some explanatory text
        st.info("""
        💡 **Note**: 
        - This is an estimated price based on machine learning model
        - Actual prices may vary due to market conditions
        - Consult with a local real estate expert for precise valuations
        """)
    
    except FileNotFoundError:
        st.error("❌ Model file not found. Please ensure 'final_model.sav' is in the correct directory.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Run the app
if __name__ == '__main__':
    main()