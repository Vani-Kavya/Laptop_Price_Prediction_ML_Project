{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f9e5ce77-0a19-4fd6-93cb-56e0494fdf61",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "309ecf61-ba99-4913-b038-e93c8003ca97",
   "metadata": {},
   "outputs": [],
   "source": [
    "loaded_model = pickle.load(open('trained_model_Latptop_Price_Prediction.sav', 'rb'))\n",
    "df = pickle.load(open('df.sav','rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ab70e324-ea62-4c4e-b802-09122d223606",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Laptop_Price_Prediction_function(input_data):\n",
    "    \n",
    "\n",
    "# changing the input_data to numpy array\n",
    "    input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "# reshape the array as we are predicting for one instance\n",
    "    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "    prediction = loaded_model.predict(input_data_reshaped)\n",
    "    return round(np.exp(prediction[0]),2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "2ca0a260-6710-4e0e-b218-741f450ee672",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-16 16:59:54.049 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Vanita\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "def main():\n",
    "    st.title(\"Laptop Price Prediction Web App\")\n",
    "\n",
    "\n",
    "    Company = st.selectbox('Brand',df['Company'].unique())\n",
    "    TypeName = st.selectbox('Type',df['TypeName'].unique())\n",
    "    Ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])\n",
    "    Weight = st.number_input('Weight of the Laptop')\n",
    "    Touchscreen = st.selectbox('Touchscreen',['No','Yes'])\n",
    "    Ips = st.selectbox('IPS',['No','Yes'])\n",
    "    Screen_size = st.slider('Scrensize in inches', 10.0, 18.0, 13.0)\n",
    "    Resolution = st.selectbox('Screen Resolution',\n",
    "                              ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])\n",
    "    CPU = st.selectbox('CPU',df['Cpu brand'].unique())\n",
    "    HDD = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])\n",
    "    SSD = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])\n",
    "    GPU = st.selectbox('GPU',df['Gpu brand'].unique())\n",
    "    OS = st.selectbox('OS',df['os'].unique())\n",
    "\n",
    "\n",
    "    Prediction=\"\"\n",
    "    if st.button(\"Predict Price\"):\n",
    "        \n",
    "        if Touchscreen == 'Yes':\n",
    "            Touchscreen = 1\n",
    "        else:\n",
    "            Touchscreen = 0\n",
    "\n",
    "        if Ips == 'Yes':\n",
    "            Ips = 1\n",
    "        else:\n",
    "            Ips = 0\n",
    "\n",
    "        X_res = int(Resolution.split('x')[0])\n",
    "        Y_res = int(Resolution.split('x')[1])\n",
    "        ppi = ((X_res**2 + Y_res**2)**0.5) /Screen_size\n",
    "        \n",
    "        input_data = [Company, TypeName, Ram, Weight, Touchscreen, Ips, ppi, CPU, HDD, SSD, GPU, OS]\n",
    "        Prediction= Laptop_Price_Prediction_function(input_data)\n",
    "        \n",
    "\n",
    "    if Prediction:\n",
    "        st.success(f\"Predicted Laptop Price: ₹{Prediction}\")\n",
    "\n",
    "if __name__=='__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "00343c98-bafe-43af-b971-3f2b14ef5b4f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "ed515e76-219a-41fb-b49b-9b4f4f00641d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "23ce6d4d-bfb2-453e-82d4-e7f4c9d63dc1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "60f79623-8e07-4425-9c3a-f05adbf7ad16",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "295daba0-89af-44e6-9a89-285c6f6f43a9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "91fe6eb2-cb80-4074-8371-979b80cc81ec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "b89a5d92-b918-4dcb-a135-c50490a39ddb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "f0960f0c-2533-4a89-b89f-7b45f12f04f2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "d46b92b3-8d85-49b5-8ac2-34aaf37d0abc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "9cbf586c-b506-49f2-a0c3-d9f3ea7cd909",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "f3da4760-a99c-4012-bbcc-c3dd037c6b4d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "13820c06-d889-4408-b15a-9016ee91f88f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "8ed1d0a6-60e1-463d-bd2b-74c5486cf50d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "24353957-f975-4bb8-a5f3-6531dfb19165",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "3ad2d330-1cb4-4e7e-a1c7-e489e85d6b86",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "67f14595-12d2-497b-88bf-a82432a1f1c0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "af266df5-ca5c-4c34-8f64-388dee898b8a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "940a8452-5bc6-42f1-8d5c-5c8936ef9878",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
