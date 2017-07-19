#!groovy                                                                           
                                                                                   
properties(                                                                        
    [                                                                              
        [                                                                          
            $class: 'jenkins.model.BuildDiscarderProperty', strategy: [$class: 'LogRotator', numToKeepStr: '10', artifactNumToKeepStr: '10'],
            $class: 'CopyArtifactPermissionProperty', projectNames: '*'            
        ]                                                                          
    ]                                                                              
)                                                                                  

def prepareEnv() {
    deleteDir()                                                                    
                                                                                   
    unstash 'binaries'
                                                                                   
    env.WORKSPACE = pwd()                                                          
                                                                                   
    sh "find ${env.WORKSPACE}"                                                     

	sh 'mkdir -p SPECS SOURCES'                                                    
    sh "cp build/distributions/*.zip SOURCES/upsilon-reactor.zip"                      
}

def buildDockerContainer() {
	prepareEnv();
	unstash 'el7'
	
	sh 'mv RPMS/noarch/*.rpm RPMS/noarch/upsilon-reactor.rpm'

    sh 'unzip -jo SOURCES/upsilon-reactor.zip "upsilon-reactor-*/var/pkg/Dockerfile" "upsilon-reactor-*/.buildid" -d . '

    tag = sh script: 'buildid -pk tag', returnStdout: true

    println "tag: ${tag}"

    sh "docker build -t 'upsilonproject/reactor:${tag}' ."
    sh "docker tag 'upsilonproject/reactor:${tag}' 'upsilonproject/reactor:latest' "
    sh "docker save upsilonproject/reactor:${tag} > upsilon-reactor-docker-${tag}.tgz"

	archive "upsilon-reactor-docker-${tag}.tgz"
}
                                                                                   
def buildRpm(dist) {                                                               
	prepareEnv()
       
	sh 'unzip -l SOURCES/upsilon-reactor.zip'                                                                               
    sh 'unzip -jo SOURCES/upsilon-reactor.zip "upsilon-reactor-*/var/pkg/upsilon-reactor.spec" "upsilon-reactor-*/.buildid.rpmmacro" -d SPECS/'
    sh "find ${env.WORKSPACE}"                                                     
                                                                                   
    sh "rpmbuild -ba SPECS/upsilon-reactor.spec --define '_topdir ${env.WORKSPACE}' --define 'dist ${dist}'"
                                                                                   
    archive 'RPMS/noarch/*.rpm'
	stash includes: "RPMS/noarch/*.rpm", name: dist
}                                                                                  
                                                                                   
node {                                                                             
    stage ("Compile") {
		deleteDir()                                                                    
		checkout scm                                                                   
																					   
		sh "./make.sh" 
																					   
		stash includes:"build/distributions/*.zip", name: "binaries"                   
		archive 'build/distributions/*.zip'
	}
}                                                                                  
                                                                                   
node {                                                                             
    stage ("Smoke") {
	    echo "Smokin' :)"                                                              
	}
}                                                                                  
                                                                                   
stage ("Package") {
	node {                                                                             
		buildRpm("el7")                                                                
	}                                                                                  
																					   
	node {                                                                             
		buildRpm("el6")                                                                
	}                                                                                  
																					   
	node {                                                                             
		buildRpm("fc24")                                 
	} 

	node {
		buildDockerContainer()
	}
}
