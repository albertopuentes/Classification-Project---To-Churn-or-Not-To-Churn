# Classification Project - Telco Churn
Project Description: develop a machine learning model that will predict churn using teclo dataset


### Project Objectives

- Data Pipeline: Acquire data from SQL database and convert into a panda dataframe, prepare the data for exploration, explore the data and document key takeaways, visualize feature attributes and incorporate into machine learning model.

- Document progress and present results in Jupyter Notebook

- Create modules (acquire.py, prepare.py) that make process repeateable for 3rd party

- Present thought process and modeling results to cohort utilizing Jupyter Notebook as presentation material

- Be prepared to handle questions about code, process, findings, key takeaways, and model.

### Project Goals

- Find drivers for customer churn in the telco data that can be utilized to construct predictive model
- Construct a machine learning classification model that accurately predicts churn while maximizing for recall
- Document the process so that 3rd party can read like a report and easily follow along/replicate


### Audience
- Target audience for my notebook walkthrough is the Codeup Data Science Florence Cohort and instructors

### Deliverables
-  Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn. This notebook should be commented and documented well enough to be read like a report or walked through as a presentation.

- README.md file containing the project description with goals, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), key findings, recommendations, and takeaways from your project.

- CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn). Predictions from best performing model ran on X_test. 

- individual modules, .py files, that hold functions to acquire and prepare data.

- Jupyter notebook walkthrough presentation with a high-level overview of your project (5 minutes max). Follow-up questions about your code, process, tests, model, and findings.


### Pipeline Stages Breakdown ==> Plan

-Create README.md with data dictionary, project and business goals, come up with initial hypotheses.

- Set project goals and define deliverables

### Pipeline Stages Breakdown ==> Acquire

- Write function that establish connectivity to SQL Ace, run an SQL query on the telco_churn database and merge all tables

- Convert imported data into dataframe

- Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).

- store functions in acquire.py

### Pipeline Stages Breakdown ==> Prepare

- prepare.py module

    - Store functions that are needed to prepare your data; make sure module contains the necessary imports to run your code. Final function should do the following:

        - Split your data into train/validate/test.

        -  Handle Missing Values.

        - Handle erroneous data and/or outliers you wish to address.

        - Encode variables as needed.

        - Create any new features, if you decided to make any for this project.

-  Notebook

    -  Explore missing values and document takeaways/action plans for handling them.

    - Is 'missing' equivalent to 0 (or some other constant value) in the specific case of this variable?

    - Replace the missing values with a value it is most likely to represent, like mean/median/mode?

    - Remove the variable (column) altogether because of the percentage of missing data?

    - Remove individual observations (rows) with a missing value for that variable?

    - Explore data types and adapt types or data values as needed to have numeric represenations of each attribute.

### Pipeline Stages Breakdown ==> Explore
- Notebook

    - Answer key questions, formulate hypotheses, and figure out the drivers of churn. Run at least 2 statistical tests in data exploration. 

    - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). Goal is to identify features that are related to churn (your target), identify any data integrity issues, and understand 'how the data works'. 

    - Summarize conclusions, provide clear answers to specific questions, and summarize any takeaways/action plan from the work above.

### Pipeline Stages Breakdown ==> Modeling and Evaluation

- Notebook

    - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document steps.

    -  Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.

    - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.

    - Feature Selection: Are there any variables that seem to provide limited to no additional information? 

    - Based on the evaluation of your models using the train and validate datasets, choose best model that you will try with your test data, once.

    - Test the final model on your out-of-sample data (the testing dataset), summarize the performance, interpret and document your results.

### Initial thoughts and Hypothesis

- Having worked with the telco data briefly in the past, I anticipate churn to be largely driven by: contract type and monthly fees.  Tenure was highly correlated with Churn in previous exercises, but I view this as more of a correlation and not causation.  Still, there are various sub-groupings whose impact will be overweighted on the overall feature and will be worth diving into further should to potentially fine tune my preliminary model.

- It's too early to formulate a full hypothesis but I expect several features to have enough predictive significance enabling for a model that will outperform the baseline.

### Repeating processes and results
- the final notebook provides a detailed step by step process that should easily be followed once the data is imported.  
- The data acquire functions and data prepare functions will do the heavy lifting but anyone looking to recreate the study will need to write their own env.py file containing their SQL access data.  
- Key Takeaways are provided at each important step to guide the reader in the though process and enable them to act on their own thoughts and interact with the process. 


## Data Dictionary

|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
| customer_id | object   | unique customer identifier    |
| gender   | object | Female or Male|
| senior_citizen   | int64 | {0:No, 1:Yes}|
| partner  | object | Yes or No|
| dependents  | object| Yes or No|
| tenure  | float64 | length of subscription in monnths|
| phone_service   | object| Yes or No|
| multiple_lines   | object | Yes, No, No phone service|
| internet_service_type_id   | int64 | {1:DSL, 2:Fiber optic, 3:None}|
| online_security  | object | Yes, No, No internet service|
| online_backup   | object | Yes, No, No internet service|
| device_protection  | object | Yes, No, No internet service|
| tech_support  | object | Yes, No, No internet service|
| streaming_tv | object | Yes, No, No internet service|
| streaming_movies | object | Yes, No, No internet service|
| contract_type_id  | int64 | {1:Month-to-mont, 2:One year, 3:Two year} |
| paperless_billing   | object | Yes or No|
| payment_type_id   | int64 | {1:Electronic check, 2:Mailed check, 3:Bank transfer (automatic), 4:Credit card (automatic) |
| monthly_charges   | float64 | monthly billing rate|
| total_charges   | float64 | cumulative charges across tenure|
| churn   | object | Yes or No|

