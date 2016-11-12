#!groovy                                                                           
                                                                                   
properties(                                                                        
    [                                                                              
        [                                                                          
            $class: 'jenkins.model.BuildDiscarderProperty', strategy: [$class: 'LogRotator', numToKeepStr: '10', artifactNumToKeepStr: '10'],
            $class: 'CopyArtifactPermissionProperty', projectNames: '*'            
        ]                                                                          
    ]                                                                              
)                                                                                  
                                                                                   
def buildRpm(dist) {                                                               
    deleteDir()                                                                    
                                                                                   
    unstash 'binaries'                                                             
                                                                                   
    env.WORKSPACE = pwd()                                                          
                                                                                   
    sh "find ${env.WORKSPACE}"                                                     
                                                                                   
    sh 'mkdir -p SPECS SOURCES'                                                    
    sh "cp build/distributions/*.zip SOURCES/upsilon-reactor.zip"                      
                                                                                   
    sh 'unzip -jo SOURCES/upsilon-reactor.zip "upsilon-reactor-*/setup/upsilon-reactor.spec" "upsilon-reactor-*/.upsilon-reactor.rpmmacro" -d SPECS/'
    sh "find ${env.WORKSPACE}"                                                     
                                                                                   
    sh "rpmbuild -ba SPECS/upsilon-reactor.spec --define '_topdir ${env.WORKSPACE}' --define 'dist ${dist}'"
                                                                                   
    archive 'RPMS/noarch/*.rpm'                                                    
}                                                                                  
                                                                                   
node {                                                                             
    stage ("Compile") {
		deleteDir()                                                                    
		checkout scm                                                                   
																					   
		sh "./make.sh" 
																					   
		stash includes:"build/distributions/*.zip", name: "binaries"                   
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
}
