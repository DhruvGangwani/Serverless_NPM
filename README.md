### Serverless Architecture: Deployed Salary Extractor to AWS Lambda using Serverless NPM
### Salary Extractor is developed using Custom Spacy NER

### File system:
	--data
		--data_gathering.py: Creates content.json by combination of multiple scenarios and test cases. Makes data gathering 		reproducible.  
		--content.json: Contains data in a format which is expected by Spacy Custom NER
		
	--model: Contains trained custom NER model
	
	--performance
		--result.csv: Contains result produced by model on test dataset
		
	--preprocessing
		--preprocessing.py: contains method to preprocess the inpout text before passed to inference 
		
	--training
		--Spacy_NER.ipynb: Training script to create a Custom NER model
		
	--handler.py: Contains method to produce inference from trained model. In the format supported by AWS Lambda.
	
	--requirements.txt: Dependencies for the app
	
	--serverless.yml: Config needed by Serverless NPM
	
	
### Configure AWS:
Use command "aws configure" and enter details such as :
1. AWS Access Key ID
2. AWS Secret Access Key
3. Region

### Serverless NPM: 
To deploy function to AWS Lambda 

### Install : 
```bash
npm install -g serverless
```

Step 1: "serverless" command to create repository depending on the choice of app. For this app, we chosed python starter package.

```bash
serverless
```

Step 2: To add requirements.txt to package, add plugin using command 

```bash
sls plugin install -n serverless-python-requirements
```

Step 3: To Deploy

```bash
serverless deploy function -f salary_extraction
```

Step 4: To Invoke

```bash
serverless invoke -f salary_extraction -l
```

Step 5: To Invoke locally

```bash
serverless invoke local -f salary_extraction -l
```




