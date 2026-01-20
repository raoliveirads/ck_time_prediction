# Chekin Time Prediction

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

<font color='#415a77'>


# <center>Airport Check-in Queue Wait Time Prediction</center>

## <center>Transforming Data into Operational Efficiency</center>



### <center>The Check-in Queue Challenge</center>

The check-in operation at airports is one of the main friction points in the passenger experience. Long lines and unpredictable service times negatively impact customer satisfaction, operational efficiency, and costs for airlines and airport administrators. This project proposes the use of Machine Learning techniques to estimate waiting time in line and service time, based on operational variables collected in near real-time.



### <center>Impact on Operators and Airports</center>

For airport operators, poorly managed queues represent significant financial losses. Long wait times result in lower customer satisfaction (reduced NPS), formal complaints, additional costs with relocating passengers who miss connections, and underutilization or overload of human resources. Airports with poor reputations in queue management face loss of competitiveness, impacting commercial agreements with airlines and concessionaires. Furthermore, inefficient allocation of counters and agents generates waste of resources that could be optimized with accurate predictions.



### <center>Key Benefits of Optimization</center>

The ability to predict and optimize check-in queue time offers tangible and measurable benefits:

- **Dynamic resource allocation**: sizing teams and counters according to predicted demand, reducing operational costs by up to 30%

- **Improved passenger experience**: increases satisfaction and loyalty, with direct impact on NPS and airport reputation

- **Strategic planning**: based on historical data and seasonal patterns enables more assertive decisions about infrastructure and investments

- **Reduction of operational bottlenecks**: improves overall terminal flow, increasing effective capacity without costly physical expansions



### <center>Why This Project?</center>

This project stems from the real need to apply data science to a complex and multidimensional problem. Using machine learning techniques and predictive analytics, I demonstrate how to transform operational data into actionable insights that generate real business value. The choice of this theme reflects my ability to identify optimization opportunities in critical environments, where precision and reliability are essential. More than a technical exercise, this project evidences my strategic vision: understanding that behind each predictive model there are people seeking to reach their destination with peace of mind, and organizations pursuing operational excellence.


### <center>Functional Requirements</center>

- **Reading and consolidation of historical and operational data**
- **Treatment of missing data and inconsistencies**
- **Training of Machine Learning models for regression**
- **Evaluation of performance metrics**
- **Automatic selection of the best model**
- **Versioning and traceability of experiments**
- **Implementation of Logs**
- **Web interface for data input and visualization of predictions**



### <center>Objective</center>

Develop a robust predictive model capable of estimating wait time in check-in queues based on operational, temporal, and seasonal variables, providing support for real-time decision-making.

</font>

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         chekin_time_prediction and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── chekin_time_prediction   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes chekin_time_prediction a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

