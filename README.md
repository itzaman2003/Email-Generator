# 📧 Cold Mail Generator
Students often struggle with crafting personalized emails when applying for internships or jobs. This tool helps by automating the process of generating tailored emails based on job postings. By analyzing the skills required for a position, it creates a relevant message that highlights the student's experience and capabilities. This saves time and improves the chances of making a strong impression on potential employers.

![img.png](imgs/img.png)

## Architecture Diagram
![img.png](![image](https://github.com/user-attachments/assets/46314c21-25de-4a33-80a7-f1f626cef610)
)

## Set-up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```
   



