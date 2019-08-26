### pre-requisite
#### install conan
```
sudo apt install python3-pip
sudo pip3 install conan
```

#### conan profile
```
conan profile new default --detect
conan profile update settings.compiler.libcxx=libstdc++11 default

cat ~/.conan/profiles/default
```

#### local conan server
```
sudo apt install docker-ce
sudo docker pull docker.bintray.io/jfrog/artifactory-cpp-ce
sudo docker run -d -p 8081:8081 docker.bintray.io/jfrog/artifactory-cpp-ce
```

#### add remote server (optional)
```
conan remote add myconan https://api.bintray.com/conan/${username}/${repo_name}
conan remote add myconan https://localhost:8081/conan/${username}/${repo_name}
```

### build quazip
```
# Replace wallestar with your username
conan create . wallestar/testing
conan upload quazip/0.8.1@wallestar/testing --all -r=myconan
```

### build libQtShadowsocks
```
# Replace wallestar with your username
conan create . wallestar/testing
conan upload libQtShadowsocks/2.1.0@wallestar/testing --all -r=myconan
```

### notes
```
# -p option is api key, not password in bintray 
conan user -p ${api_key} -r {remote_name} ${username}

# To save time, create package manually after first time:
conan install . --install-folder=./build
conan build . --source-folder=./ --build-folder=./build
conan export-pkg . quazip/0.8.1@wallestar/testing --package-folder=./build/package
```

### usage
```
# To install the dependencies defined in your project's conanfile.txt, user the following command:
conan install quazip/0.8.1@wallestar/testing
```
