from conans import ConanFile, CMake, tools


class LibqtshadowsocksConan(ConanFile):
    name = "libQtShadowsocks"
    version = "v2.1.0"
    license = "MIT"
    url = "https://github.com/shadowsocks/libQtShadowsocks.git"
    description = "libQtShadowsocks conan file"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/shadowsocks/libQtShadowsocks.git")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="libQtShadowsocks")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    # def package(self):
    #     self.copy("*.h", dst="include", src="libQtShadowsocks")
    #     self.copy("*libQtShadowsocks.lib", dst="lib", keep_path=False)
    #     self.copy("*.dll", dst="bin", keep_path=False)
    #     self.copy("*.so", dst="lib", keep_path=False)
    #     self.copy("*.dylib", dst="lib", keep_path=False)
    #     self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["QtShadowsocks"]