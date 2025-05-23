pipeline {
    agent  {label "First" }

    parameters {
        string( name: 'USERNAME', defaultlValue: "Parth", description: "Enter your username" )
        string( name: "EMAIL", defaultvalue: "parth@example.com", description: "Enter your email" )
    }

    stages {
        stage("Run Python with Params") {
            steps {
                echo "Username: ${params.USERNAME}"
                echo "Email: ${params.EMAIL}"

                sh """
                    python3 user_logger.py ${params.USERNAME} ${params.EMAIL}
                """
            }
        }
    }
}