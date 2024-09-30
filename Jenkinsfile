// scripted Pipeline groovy script
node {
    stage('Build') {
        echo 'Building...'
    }

    stage('Test') {
        echo 'Testing...'
    }

    stage('Deploy') {
        echo 'Deploying...'
    }

    if (currentBuild.result == 'SUCCESS') {
        echo 'Build succeeded!'
    } else {
        echo 'Build failed!'
    }
}

// Declarative pipeline groovy script
// pipeline {
//     agent any

//     stages {
//         stage('Checkout') {
//             steps {
//                 echo "checkout"
//             }
//         }
//         stage('Build'){
//             steps{
//                 echo "built"
//                 }
//         }
//         stage('Test'){
//             steps{
//                 echo "Job is tested"
//             }
//         }
//     }
// }
