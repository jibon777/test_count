pipeline {
environment {
imagename = "jibon/testcount"
registryCredential = 'jibon'
dockerImage = ''
}
agent any
stages {
stage('Cloning Git') {
steps {
git([url: 'https://github.com/jibon777/test_count.git', branch: 'test', credentialsId: 'jenkins-test'])
}
}
stage('Building image') {
steps{
script {
dockerImage = docker.build imagename
}
}
}
stage('Deploy Image') {
steps{
script {
docker.withRegistry( '', registryCredential ) {
dockerImage.push("$BUILD_NUMBER")
dockerImage.push('latest')
}
}
}
}
stage('Remove Unused docker image') {
steps{
sh "docker rmi $imagename:$BUILD_NUMBER"
sh "docker rmi $imagename:latest"
}
}
}
}