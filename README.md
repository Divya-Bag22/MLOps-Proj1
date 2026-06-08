# Vehicle Insurance Prediction - End-to-End MLOps

## 📌 Project Overview
This is an end-to-end Machine Learning pipeline (MLOps) project that predicts whether a customer will be interested in buying vehicle insurance based on their demographics and vehicle details. The project implements a complete CI/CD pipeline, taking the ML model from a raw dataset to a fully deployed live web application using Docker and AWS.

## 🚀 Tech Stack
- **Language**: Python 3.10
- **Machine Learning**: Scikit-Learn (Random Forest Classifier), Pandas, NumPy, Imbalanced-Learn (SMOTEENN)
- **Web Framework**: FastAPI, Uvicorn, HTML/CSS (Jinja2 Templates)
- **Database**: MongoDB Atlas (Cloud Database)
- **Cloud & Deployment**: AWS EC2, AWS S3, AWS ECR, Docker, GitHub Actions (CI/CD)

## 🏗️ Architecture & Pipeline Flow
The project follows a modular programming approach with the following pipeline steps:
1. **Data Ingestion**: Extracts raw data securely from MongoDB Atlas and splits it into Train/Test datasets.
2. **Data Validation**: Validates the extracted dataset against a predefined schema to ensure consistency and prevent data drift.
3. **Data Transformation**: Cleans data, encodes categorical variables, scales numerical features, and handles imbalanced data using SMOTEENN.
4. **Model Training**: Trains the machine learning model (Random Forest) and validates it against a base accuracy threshold.
5. **Model Evaluation**: Downloads the production model from AWS S3 (if it exists) and compares its performance with the newly trained model.
6. **Model Pusher**: If the new model performs better, it is securely pushed to the AWS S3 Bucket.
7. **Deployment**: A CI/CD pipeline triggers on every push to `main`. It builds a Docker image, pushes it to AWS ECR, and deploys the container live on an AWS EC2 instance.

## ⚙️ How to Run Locally

### Prerequisites
- Python 3.10
- MongoDB Atlas Account (with a Database & Collection created)
- AWS Account (IAM User with S3 access)

### Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd MLOps-Proj1
   ```

2. Create and activate a virtual environment:
   ```bash
   conda create -n projenv python=3.10 -y
   conda activate projenv
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Environment Variables:
   Create a `.env` file in the root directory and add your MongoDB URL:
   ```env
   MONGODB_URL_KEY="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
   ```

### Start the Application
To run the web app and pipeline locally:
```bash
python app.py
```
- Visit `http://localhost:5000` to interact with the application and make predictions.
- To trigger the entire machine learning training pipeline manually, visit `http://localhost:5000/train`.

## ☁️ Cloud Deployment (AWS CI/CD)
This project is configured with GitHub Actions for automated CI/CD deployment to AWS.

### Setup Steps:
1. Create an **IAM User** in AWS with `AmazonEC2FullAccess`, `AmazonECRFullAccess`, and `AmazonS3FullAccess` policies.
2. Create an **S3 Bucket** (for model storage) and an **ECR Repository** (for Docker images).
3. Launch an **EC2 Instance (Ubuntu)**, install Docker, and configure it as a **Self-Hosted Runner** in GitHub.
4. Add the following secrets in your repository under **GitHub -> Settings -> Secrets and variables -> Actions**:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_DEFAULT_REGION`
   - `ECR_REPO` (Your ECR Repository Name)
   - `MONGODB_URL_KEY` (Your MongoDB Connection String)

Once configured, simply push your code to the `main` branch. GitHub Actions will automatically build the image and deploy it to your live EC2 instance!

## 📝 License
This project is licensed under the MIT License.