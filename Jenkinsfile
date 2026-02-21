pipeline { 
    agent any 

    stages { 
        stage('Setup') { 
            steps { 
                echo 'Installing dependencies...' 
                bat 'python -m pip install -r requirements.txt' 
            } 
        } 

        stage('Run Flask App') { 
            steps { 
                echo 'Starting Flask application...' 
                bat 'python app.py' 
            } 
        } 
    } 

    post { 
        success { 
            echo 'Pipeline SUCCESS - Flask app started' 
        } 
        failure { 
            echo 'Pipeline FAILED - Check logs' 
        } 
    } 
}