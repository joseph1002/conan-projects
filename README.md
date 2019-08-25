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

#### add remote server
```
conan remote add myconan https://api.bintray.com/conan/wallestar/conan
```

#### local conan server
```
sudo apt install docker-ce
sudo docker pull docker.bintray.io/jfrog/artifactory-cpp-ce
sudo docker run -d -p 8081:8081 docker.bintray.io/jfrog/artifactory-cpp-ce
```

### build quazip
```
conan create . wallestar/conan
conan upload quazip/0.8.1@wallestar/conan --all -r=myconan
```

### build libQtShadowsocks
```
conan create . wallestar/conan
conan upload quazip/0.8.1@wallestar/conan --all -r=myconan
# conan export-pkg . quazip/0.8.1@wallestar/conan  --package-folder=./build/package
```

# 创建
```
conan create . HelloConan/0.1.0@conan/teting
```
# 使用
```
conan install HelloConan/0.1.0@conan/teting
```
conan alias HelloConan/0.1@conan/testing HelloConan/0.1.5@conan/testing

conan install . --install-folder=./build
conan build . --source-folder=./ --build-folder=./build
conan export-pkg . HelloConan/0.1.0@conan/testing --package-folder=./build/package
conan user -p APcwSGCR7qgJ6KC -r myconan wallestar
conan user -p <PASSWORD> -r <REMOTE> <USERNAME>
